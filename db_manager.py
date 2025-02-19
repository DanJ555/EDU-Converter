import sqlite3

import uniteditor
from uniteditor import *


# Function to initialize the SQLite database
def initialize_database(db_name="export_descr_units.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create the tables
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS units (
        unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
        unit_dictionary TEXT UNIQUE NOT NULL,
        name TEXT,
        category TEXT,
        class TEXT,
        voice_type TEXT,
        accent TEXT,
        banner_faction TEXT,
        banner_holy TEXT,
        banner_unit TEXT,
        ship TEXT,
        engine TEXT,
        animal TEXT,
        mounted_engine TEXT,
        mount TEXT,
        attributes TEXT,
        move_speed_mod REAL,
        ownership TEXT,
        recruit_priority_offset INTEGER
    );

    CREATE TABLE IF NOT EXISTS formations (
        unit_id INTEGER PRIMARY KEY,
        close_x REAL,
        close_y REAL,
        loose_x REAL,
        loose_y REAL,
        ranks INTEGER,
        shape TEXT,
        ability TEXT,
        stat_health TEXT,
        stat_heat INTEGER,
        stat_ground TEXT,
        stat_mental TEXT,
        stat_charge_dist INTEGER,
        FOREIGN KEY (unit_id) REFERENCES units (unit_id)
    );

    CREATE TABLE IF NOT EXISTS weapons (
        weapon_id INTEGER PRIMARY KEY AUTOINCREMENT,
        unit_id INTEGER,
        weapon_type TEXT,
        attack INTEGER,
        charge_bonus INTEGER,
        missile TEXT,
        range INTEGER,
        ammunition INTEGER,
        weapon_class TEXT,
        tech_type TEXT,
        damage_type TEXT,
        sound TEXT,
        attack_delay INTEGER,
        scfim INTEGER,
        stat_ex TEXT,
        stat_attr TEXT,
        FOREIGN KEY (unit_id) REFERENCES units (unit_id)
    );

    CREATE TABLE IF NOT EXISTS armor (
        unit_id INTEGER PRIMARY KEY,
        primary_armor INTEGER,
        defense_skill INTEGER,
        shield INTEGER,
        armor_material TEXT,
        upgrade_levels TEXT,
        upgrade_models TEXT,
        FOREIGN KEY (unit_id) REFERENCES units (unit_id)
    );

    CREATE TABLE IF NOT EXISTS cost (
        unit_id INTEGER PRIMARY KEY,
        turns INTEGER,
        construct INTEGER,
        upkeep INTEGER,
        weapon_upgrade INTEGER,
        armor_upgrade INTEGER,
        custom INTEGER,
        custom_softcap INTEGER,
        custom_penalty INTEGER,
        FOREIGN KEY (unit_id) REFERENCES units (unit_id)
    );
    """)

    conn.commit()
    conn.close()


# Function to insert unit data into the database
def insert_unit(conn, unit):
    cursor = conn.cursor()

    # Insert into units table
    cursor.execute("""
        INSERT INTO units (
            unit_dictionary, name, category, class, voice_type, accent, banner_faction, 
            banner_holy, banner_unit, ship, engine, animal, mounted_engine, mount, 
            attributes, move_speed_mod, ownership, recruit_priority_offset
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        unit.dictionary["name0"],
        unit.dictionary["name1"],
        unit.category,
        unit.unit_class,
        unit.voice_type,
        unit.accent,
        unit.banner_faction,
        unit.banner_holy,
        unit.banner_unit,
        unit.ship,
        unit.engine,
        unit.animal,
        unit.mounted_engine,
        unit.mount,
        ", ".join(unit.attributes.keys()),  # Convert attributes dictionary to a comma-separated string
        unit.move_speed_mod,
        ", ".join(unit.ownership),  # Convert ownership list to a comma-separated string
        unit.recruit_priority_offset
    ))

    unit_id = cursor.lastrowid  # Get the ID of the inserted unit

    # Insert into formations table
    cursor.execute("""
        INSERT INTO formations (
            unit_id, close_x, close_y, loose_x, loose_y, ranks, shape, ability, 
            stat_health, stat_heat, stat_ground, stat_mental, stat_charge_dist
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        unit_id,
        unit.formation["close_x"],
        unit.formation["close_y"],
        unit.formation["loose_x"],
        unit.formation["loose_y"],
        unit.formation["ranks"],
        unit.formation["shape"],
        unit.formation["ability"],
        f"{unit.stat_health[0]}, {unit.stat_health[1]}",
        unit.stat_heat,
        str(unit.stat_ground),  # Convert dict to string for now
        str(unit.stat_mental),  # Convert dict to string for now
        unit.stat_charge_dist
    ))

    # Insert primary, secondary, and tertiary weapons
    for weapon_type, stat in [
        ("primary", unit.stat_primary),
        ("secondary", unit.stat_secondary),
        ("tertiary", unit.stat_tertiary)
    ]:
        if stat["attack"] is not None:  # Only insert if the weapon exists
            cursor.execute("""
                INSERT INTO weapons (
                    unit_id, weapon_type, attack, charge_bonus, missile, range, 
                    ammunition, weapon_class, tech_type, damage_type, sound, 
                    attack_delay, scfim, stat_attr
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                unit_id,
                weapon_type,
                stat["attack"],
                stat["charge_bonus"],
                stat["missile"],
                stat["range"],
                stat["ammunition"],
                stat["weapon_type"],
                stat["tech_type"],
                stat["damage_type"],
                stat["sound"],
                stat["atk_delay"],
                stat["scfim"],
                str(unit.stat_primary_attribute)  # Convert dict to string for now
            ))

    # Insert armor data
    cursor.execute("""
        INSERT INTO armor (
            unit_id, primary_armor, defense_skill, shield, armor_material, 
            upgrade_levels, upgrade_models
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        unit_id,
        unit.stat_primary_armour["armour"],
        unit.stat_primary_armour["defense_skill"],
        unit.stat_primary_armour["shield"],
        unit.stat_primary_armour["sound"],
        str(unit.armour_ug_levels),  # Convert dict to string for now
        str(unit.armour_ug_models)  # Convert dict to string for now
    ))

    # Insert cost data
    cursor.execute("""
        INSERT INTO cost (
            unit_id, turns, construct, upkeep, weapon_upgrade, armor_upgrade, 
            custom, custom_softcap, custom_penalty
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        unit_id,
        unit.stat_cost["turns"],
        unit.stat_cost["construct"],
        unit.stat_cost["upkeep"],
        unit.stat_cost["weapon_ug"],
        unit.stat_cost["armour_ug"],
        unit.stat_cost["custom"],
        unit.stat_cost["custom_softcap"],
        unit.stat_cost["custom_penalty"]
    ))

    conn.commit()


# Example: Run this to initialize and populate the database
if __name__ == "__main__":
    initialize_database()

    # Assume `units` is a list of `Unit` objects from your parser
    units: list[Unit] = uniteditor.create_unit_list(file="export_descr_unit.txt")  # Replace with real data
    conn = sqlite3.connect("export_descr_units.db")

    for unit in units:
        insert_unit(conn, unit)

    conn.close()
    print("Database populated successfully!")
