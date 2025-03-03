import sqlite3

from unit_type import *


def initialize_database(db_name="export_descr_unit.db") -> sqlite3.Connection:
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
        soldier_extras INTEGER,
        soldier_collision_mass INTEGER,
        soldier_radius INTEGER,
        soldier_height INTEGER,
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
        close_x INTEGER,
        close_y INTEGER,
        loose_x INTEGER,
        loose_y INTEGER,
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
        move_speed_mod INTEGER,
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
        scfim INTEGER,
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
    return conn

def open_database(db_name="test.db", unit_list=None) -> sqlite3.Connection:
    try:
        open(db_name)
        return sqlite3.connect(db_name)
    except FileNotFoundError:
        conn = initialize_database(db_name)
        if unit_list:
            for unit in unit_list:
                insert_unit(conn, unit)
        return initialize_database(db_name)


def _str_join(collection: list) -> str | None:
    try:
        return ", ".join(collection)
    except TypeError:
        return None


def _dict_pair(dictionary: dict, index: int) -> str | None:
    item = tuple(dictionary.items())
    try:
        return f"{item[index][0]} {item[index][1]}"
    except IndexError:
        return None


def insert_unit(conn, unit):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO units (
            dictionary, type, name, category, class, voice_type, accent, banner_faction, 
            banner_holy, banner_unit, attributes, stat_cost_turns, stat_cost_construct,
            stat_cost_upkeep, stat_cost_weapon_upgrade, stat_cost_armour_upgrade,
            stat_cost_custom, stat_cost_custom_softcap, stat_cost_custom_penalty,
            stat_stl, ownership, era_0, era_1, era_2, recruit_priority_offset
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        unit.dictionary["name_0"],
        unit.type,
        unit.dictionary["name_1"],
        unit.category,
        unit.unit_class,
        unit.voice_type,
        unit.accent,
        unit.banner_faction,
        unit.banner_holy,
        unit.banner_unit,
        ", ".join(unit.attributes),
        unit.stat_cost["turns"],
        unit.stat_cost["construct"],
        unit.stat_cost["upkeep"],
        unit.stat_cost["weapon_ug"],
        unit.stat_cost["armour_ug"],
        unit.stat_cost["custom"],
        unit.stat_cost["custom_softcap"],
        unit.stat_cost["custom_penalty"],
        unit.stat_stl,
        ", ".join(unit.ownership),
        _str_join(unit.eras["era 0"]),
        _str_join(unit.eras["era 1"]),
        _str_join(unit.eras["era 2"]),
        unit.recruit_priority_offset
    ))

    unit_id = cursor.lastrowid

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
        unit.dictionary["name_0"],
        unit.soldier["model"],
        unit.soldier["men"],
        unit.soldier["extras"],
        unit.soldier["mass"],
        unit.soldier["radius"],
        unit.soldier["height"],
        unit.officer_0,
        unit.officer_1,
        unit.officer_2,
        unit.ship,
        unit.engine,
        unit.animal,
        unit.mounted_engine,
        unit.mount,
        _dict_pair(unit.mount_effect, 0),
        _dict_pair(unit.mount_effect, 1),
        _dict_pair(unit.mount_effect, 2),
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

    for weapon_category, stat in [
        ("primary", unit.stat_primary),
        ("secondary", unit.stat_secondary),
        ("tertiary", unit.stat_tertiary)
    ]:
        if stat["attack"] is not None:
            cursor.execute("""
                INSERT INTO weapons (
                    unit_id, dictionary, weapon_category, attack, charge_bonus, missile,
                    range, ammunition, weapon_type, tech_type, damage_type, sound, 
                    musket_shot_set, attack_delay, scfim, attribute
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                unit_id,
                unit.dictionary["name_0"],
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
                ", ".join(unit.stat_primary_attribute)
            ))

    cursor.execute("""
        INSERT INTO armour (
            unit_id, dictionary, primary_armour, primary_defense_skill, primary_shield, primary_material, 
            secondary_armour, secondary_defense_skill, secondary_material, upgrade_levels,
            upgrade_models
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        unit_id,
        unit.dictionary["name_0"],
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
    rows_units = cursor.fetchall()

    cursor.execute("""
            SELECT
                *
            FROM
                formations
            """)
    rows_formations = cursor.fetchall()

    cursor.execute("""
                SELECT
                    *
                FROM
                    armour
                """)
    rows_armour = cursor.fetchall()

    cursor.execute("""
                    SELECT
                        *
                    FROM
                        weapons
                    """)
    rows_weapons = cursor.fetchall()

    units = [Unit() for _ in range(len(rows_units))]
    for row in rows_units:
        unit = units[row[0] - 1]
        unit.dictionary["name_0"] = row[1]
        unit.type = row[2]
        unit.dictionary["name_1"] = row[3]
        unit.category = row[4]
        unit.unit_class = row[5]
        unit.voice_type = row[6]
        unit.accent = row[7]
        unit.banner_faction = row[8]
        unit.banner_holy = row[9]
        unit.banner_unit = row[10]
        for attribute in row[11].split():
            if "," in attribute:
                attribute = attribute[:-1]
            unit.attributes.append(attribute)
        unit.stat_cost["turns"] = row[12]
        unit.stat_cost["construct"] = row[13]
        unit.stat_cost["upkeep"] = row[14]
        unit.stat_cost["weapon_ug"] = row[15]
        unit.stat_cost["armour_ug"] = row[16]
        unit.stat_cost["custom"] = row[17]
        unit.stat_cost["custom_softcap"] = row[18]
        unit.stat_cost["custom_penalty"] = row[19]
        unit.stat_stl = row[20]
        for owner in row[21].split():
            if "," in owner:
                owner = owner[:-1]
            unit.ownership.append(owner)
        era_index = (
            ("era 0", 22),
            ("era 1", 23),
            ("era 2", 24)
        )
        for era, index in era_index:
            if row[index] is not None:
                unit.eras[era] = []
                for owner in row[index].split():
                    if "," in owner:
                        owner = owner[:-1]
                    unit.eras[era].append(owner)
        unit.recruit_priority_offset = row[25]

    for row in rows_formations:
        unit = units[row[0] - 1]
        unit.soldier["model"] = row[2]
        unit.soldier["men"] = row[3]
        unit.soldier["extras"] = row[4]
        unit.soldier["mass"] = row[5]
        unit.soldier["radius"] = row[6]
        unit.soldier["height"] = row[7]
        unit.officer_0 = row[8]
        unit.officer_1 = row[9]
        unit.officer_2 = row[10]
        unit.ship = row[11]
        unit.engine = row[12]
        unit.animal = row[13]
        unit.mounted_engine = row[14]
        unit.mount = row[15]
        for index in (16, 17, 18):
            if row[index] is not None:
                mount, effect = row[index].split()
                unit.mount_effect[mount] = effect
        unit.formation["close_x"] = row[19]
        unit.formation["close_y"] = row[20]
        unit.formation["loose_x"] = row[21]
        unit.formation["loose_y"] = row[22]
        unit.formation["ranks"] = row[23]
        unit.formation["shape"] = row[24]
        unit.formation["ability"] = row[25]
        unit.stat_health[0] = row[26]
        unit.stat_health[1] = row[27]
        unit.stat_heat = row[28]
        unit.stat_ground["scrub"] = row[29]
        unit.stat_ground["sand"] = row[30]
        unit.stat_ground["forest"] = row[31]
        unit.stat_ground["snow"] = row[32]
        unit.stat_mental["morale"] = row[33]
        unit.stat_mental["discipline"] = row[34]
        unit.stat_mental["training"] = row[35]
        unit.stat_mental["lock_morale"] = row[36]
        unit.stat_charge_dist = row[37]
        unit.stat_fire_delay = row[38]
        unit.move_speed_mod = row[39]

    for row in rows_armour:
        unit = units[row[0]-1]
        unit.stat_primary_armour["armour"] = row[2]
        unit.stat_primary_armour["defense_skill"] = row[3]
        unit.stat_primary_armour["shield"] = row[4]
        unit.stat_primary_armour["sound"] = row[5]
        unit.stat_secondary_armour["armour"] = row[6]
        unit.stat_secondary_armour["defense_skill"] = row[7]
        unit.stat_secondary_armour["sound"] = row[8]
        unit.armour_ug_levels = eval(row[9])
        unit.armour_ug_models = eval(row[10])

    for weapon in rows_weapons:
        unit = units[weapon[1]-1]
        category = weapon[3]
        stat = getattr(unit, f"stat_{category}")
        stat_attribute = getattr(unit, f"stat_{category}_attribute")
        stat["attack"] = weapon[4]
        stat["charge_bonus"] = weapon[5]
        stat["missile"] = weapon[6]
        stat["range"] = weapon[7]
        stat["ammunition"] = weapon[8]
        stat["weapon_type"] = weapon[9]
        stat["tech_type"] = weapon[10]
        stat["damage_type"] = weapon[11]
        stat["sound"] = weapon[12]
        stat["musket_shot_set"] = weapon[13]
        stat["attack_delay"] = weapon[14]
        stat["scfim"] = weapon[15]
        for attribute in weapon[16].split():
            if "," in attribute:
                attribute = attribute[:-1]
            stat_attribute.append(attribute)

    return units


def main() -> None:
    unit_list: list[Unit] = create_units_from_txt(file="export_descr_unit.txt")
    conn = open_database("test.db", unit_list)
    db_unit_list = extract_units(conn)

    for unit in db_unit_list:
        print(str(unit))

    conn.close()


if __name__ == "__main__":
    main()
