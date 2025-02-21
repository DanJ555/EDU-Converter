import sqlite3

import uniteditor
from uniteditor import *


# Function to initialize the SQLite database
def initialize_database(db_name="export_descr_unit.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create the tables
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS units (
        unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
        dictionary TEXT UNIQUE NOT NULL,
        type TEXT,
        name TEXT,
        category TEXT,
        class TEXT,
        voice_type TEXT,
        accent TEXT,
        banner_faction TEXT,
        banner_holy TEXT,
        banner_unit TEXT,
        attributes TEXT,
        stat_cost_turns INTEGER,
        stat_cost_construct INTEGER,
        stat_cost_upkeep INTEGER,
        stat_cost_weapon_upgrade INTEGER,
        stat_cost_armour_upgrade INTEGER,
        stat_cost_custom INTEGER,
        stat_cost_custom_softcap INTEGER,
        stat_cost_custom_penalty INTEGER,
        stat_stl INTEGER,
        ownership TEXT,
        era_0 TEXT,
        era_1 TEXT,
        era_2 TEXT,
        recruit_priority_offset INTEGER
    );

    CREATE TABLE IF NOT EXISTS formations (
        unit_id INTEGER PRIMARY KEY,
        dictionary TEXT UNIQUE NOT NULL,
        soldier_model TEXT,
        soldier_count INTEGER,
        soldier_extras REAL,
        soldier_collision_mass REAL,
        soldier_radius REAL,
        soldier_height REAL,
        officer_0 TEXT,
        officer_1 TEXT,
        officer_2 TEXT,
        ship TEXT,
        engine TEXT,
        animal TEXT,
        mounted_engine TEXT,
        mount TEXT,
        mount_effect_0 TEXT,
        mount_effect_1 TEXT,
        mount_effect_2 TEXT,
        close_x REAL,
        close_y REAL,
        loose_x REAL,
        loose_y REAL,
        ranks INTEGER,
        shape TEXT,
        ability TEXT,
        stat_health_0 INTEGER,
        stat_health_1 INTEGER,
        stat_heat INTEGER,
        stat_ground_scrub INTEGER,
        stat_ground_sand INTEGER,
        stat_ground_forest INTEGER,
        stat_ground_snow INTEGER,
        stat_mental_morale INTEGER,
        stat_mental_discipline TEXT,
        stat_mental_training TEXT,
        stat_mental_lock_morale TEXT,
        stat_charge_distance INTEGER,
        stat_fire_delay INTEGER,
        move_speed_mod REAL,
        FOREIGN KEY (unit_id) REFERENCES units (unit_id)
    );

    CREATE TABLE IF NOT EXISTS weapons (
        weapon_id INTEGER PRIMARY KEY AUTOINCREMENT,
        unit_id INTEGER,
        dictionary TEXT,
        weapon_category TEXT,
        attack INTEGER,
        charge_bonus INTEGER,
        missile TEXT,
        range INTEGER,
        ammunition INTEGER,
        weapon_type TEXT,
        tech_type TEXT,
        damage_type TEXT,
        sound TEXT,
        musket_shot_set TEXT,
        attack_delay INTEGER,
        scfim REAL,
        attribute TEXT,
        FOREIGN KEY (unit_id) REFERENCES units (unit_id)
    );

    CREATE TABLE IF NOT EXISTS armour (
        unit_id INTEGER PRIMARY KEY,
        dictionary TEXT,
        primary_armour INTEGER,
        primary_defense_skill INTEGER,
        primary_shield INTEGER,
        primary_material TEXT,
        secondary_armour INTEGER,
        secondary_defense_skill INTEGER,
        secondary_material TEXT,
        upgrade_levels TEXT,
        upgrade_models TEXT,
        FOREIGN KEY (unit_id) REFERENCES units (unit_id)
    );
    """)

    conn.commit()
    conn.close()


def str_join(collection: list) -> str | None:
    try:
        return ", ".join(collection)
    except TypeError:
        return None


def dict_pair(dictionary: dict, index: int) -> str | None:
    item = tuple(dictionary.items())
    try:
        return f"{item[index][0]} {item[index][1]}"
    except IndexError:
        return None


# Function to insert unit data into the database
def insert_unit(conn, unit):
    cursor = conn.cursor()

    # Insert into units table
    cursor.execute("""
        INSERT INTO units (
            dictionary, type, name, category, class, voice_type, accent, banner_faction, 
            banner_holy, banner_unit, attributes, stat_cost_turns, stat_cost_construct,
            stat_cost_upkeep, stat_cost_weapon_upgrade, stat_cost_armour_upgrade,
            stat_cost_custom, stat_cost_custom_softcap, stat_cost_custom_penalty,
            stat_stl, ownership, era_0, era_1, era_2, recruit_priority_offset
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        unit.dictionary["name0"],
        unit.type,
        unit.dictionary["name1"],
        unit.category,
        unit.unit_class,
        unit.voice_type,
        unit.accent,
        unit.banner_faction,
        unit.banner_holy,
        unit.banner_unit,
        ", ".join(unit.attributes.keys()),  # Convert attributes dictionary to a comma-separated string
        unit.stat_cost["turns"],
        unit.stat_cost["construct"],
        unit.stat_cost["upkeep"],
        unit.stat_cost["weapon_ug"],
        unit.stat_cost["armour_ug"],
        unit.stat_cost["custom"],
        unit.stat_cost["custom_softcap"],
        unit.stat_cost["custom_penalty"],
        ", ".join(unit.ownership),  # Convert ownership list to a comma-separated string
        unit.stat_stl,
        str_join(unit.eras["era 0"]),
        str_join(unit.eras["era 1"]),
        str_join(unit.eras["era 2"]),
        unit.recruit_priority_offset
    ))

    unit_id = cursor.lastrowid  # Get the ID of the inserted unit

    # Insert into formations table
    cursor.execute("""
        INSERT INTO formations (
            unit_id, dictionary, soldier_model, soldier_count, soldier_extras,
            soldier_collision_mass, soldier_radius, soldier_height, officer_0, officer_1, officer_2, ship, engine,
            animal, mounted_engine, mount, mount_effect_0, mount_effect_1, mount_effect_2,
            close_x, close_y, loose_x, loose_y, ranks, shape, ability, stat_health_0,
            stat_health_1, stat_heat, stat_ground_scrub, stat_ground_sand,
            stat_ground_forest, stat_ground_snow, stat_mental_morale, stat_mental_discipline,
            stat_mental_training, stat_mental_lock_morale, stat_charge_distance, stat_fire_delay,
            move_speed_mod
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
         ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        unit_id,
        unit.dictionary["name0"],
        unit.soldier["model"],
        unit.soldier["men"],
        unit.soldier["extras"],
        unit.soldier["mass"],
        unit.soldier["radius"],
        unit.soldier["height"],
        unit.officer0,
        unit.officer1,
        unit.officer2,
        unit.ship,
        unit.engine,
        unit.animal,
        unit.mounted_engine,
        unit.mount,
        dict_pair(unit.mount_effect, 0),
        dict_pair(unit.mount_effect, 1),
        dict_pair(unit.mount_effect, 2),
        unit.formation["close_x"],
        unit.formation["close_y"],
        unit.formation["loose_x"],
        unit.formation["loose_y"],
        unit.formation["ranks"],
        unit.formation["shape"],
        unit.formation["ability"],
        unit.stat_health[0],
        unit.stat_health[1],
        unit.stat_heat,
        unit.stat_ground["scrub"],
        unit.stat_ground["sand"],
        unit.stat_ground["forest"],
        unit.stat_ground["snow"],
        unit.stat_mental["morale"],
        unit.stat_mental["discipline"],
        unit.stat_mental["training"],
        unit.stat_mental["lock_morale"],
        unit.stat_charge_dist,
        unit.stat_fire_delay,
        unit.move_speed_mod
    ))

    # Insert primary, secondary, and tertiary weapons
    for weapon_category, stat in [
        ("primary", unit.stat_primary),
        ("secondary", unit.stat_secondary),
        ("tertiary", unit.stat_tertiary)
    ]:
        if stat["attack"] is not None:  # Only insert if the weapon exists
            cursor.execute("""
                INSERT INTO weapons (
                    unit_id, dictionary, weapon_category, attack, charge_bonus, missile,
                    range, ammunition, weapon_type, tech_type, damage_type, sound, 
                    musket_shot_set, attack_delay, scfim, attribute
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                unit_id,
                unit.dictionary["name0"],
                weapon_category,
                stat["attack"],
                stat["charge_bonus"],
                stat["missile"],
                stat["range"],
                stat["ammunition"],
                stat["weapon_type"],
                stat["tech_type"],
                stat["damage_type"],
                stat["sound"],
                stat["musket_shot_set"],
                stat["attack_delay"],
                stat["scfim"],
                ", ".join(unit.stat_primary_attribute.keys())  # Convert dict to string for now
            ))

    # Insert armour data
    cursor.execute("""
        INSERT INTO armour (
            unit_id, dictionary, primary_armour, primary_defense_skill, primary_shield, primary_material, 
            secondary_armour, secondary_defense_skill, secondary_material, upgrade_levels,
            upgrade_models
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        unit_id,
        unit.dictionary["name0"],
        unit.stat_primary_armour["armour"],
        unit.stat_primary_armour["defense_skill"],
        unit.stat_primary_armour["shield"],
        unit.stat_primary_armour["sound"],
        unit.stat_secondary_armour["armour"],
        unit.stat_secondary_armour["defense_skill"],
        unit.stat_secondary_armour["sound"],
        str(unit.armour_ug_levels),
        str(unit.armour_ug_models)
    ))

    conn.commit()


def extract_units(conn) -> list[Unit]:
    cursor = conn.cursor()
    cursor.execute("""
    SELECT
        *
    FROM
        units
    """)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    initialize_database()

    units: list[Unit] = uniteditor.create_unit_list(file="export_descr_unit.txt")  # Replace with real data
    conn = sqlite3.connect("export_descr_unit.db")

    for unit in units:
        insert_unit(conn, unit)

    extract_units(conn)

    conn.close()
    print("Database populated successfully!")
