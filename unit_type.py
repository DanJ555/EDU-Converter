class TooManyOfficersError(Exception):
	"""Is raised if more than 3 officer lines are read for a given unit."""
	pass


class Unit:

	def __init__(self) -> None:
		self.type: str = None
		self.dictionary: dict[str: str] = {
			"name_0": None,
			"name_1": None
		}
		self.category: str = None
		self.unit_class: str = None
		self.voice_type: str = None
		self.accent: str = None
		self.banner_faction: str = None
		self.banner_holy: str = None
		self.banner_unit: str = None
		self.soldier: dict[str, str | int | float] = {
			"model": "Peasants",
			"men": 30,
			"extras": 0,
			"mass": 1,
			"radius": None,
			"height": None
		}
		self.ship: str = None
		self.officer_0: str = None
		self.officer_1: str = None
		self.officer_2: str = None
		self.engine: str = None
		self.animal: str = None
		self.mounted_engine: str = None
		self.mount: str = None
		self.mount_effect: dict[str, str] = {}
		self.attributes: list[str] = []
		self.move_speed_mod: float = None
		self.formation: [str, str | float | int] = {
			"close_x": 1.2,
			"close_y": 1.2,
			"loose_x": 2.4,
			"loose_y": 2.4,
			"ranks": 8,
			"shape": "square",
			"ability": None
		}
		self.stat_health: list[int] = [1, 0]
		self.stat_primary: dict[str, str | int | float] = {
			"attack": 0,
			"charge_bonus": 0,
			"missile": None,
			"range": 0,
			"ammunition": 0,
			"weapon_type": None,
			"tech_type": "melee_simple",
			"damage_type": "blunt",
			"sound": "none",
			"musket_shot_set": None,
			"attack_delay": 25,
			"scfim": 1
		}
		self.stat_primary_attribute: list[str] = []
		self.stat_secondary: dict[str, str | int | float] = {
			"attack": 0,
			"charge_bonus": 0,
			"missile": None,
			"range": 0,
			"ammunition": 0,
			"weapon_type": None,
			"tech_type": "melee_simple",
			"damage_type": "blunt",
			"sound": "none",
			"musket_shot_set": None,
			"attack_delay": 25,
			"scfim": 1
		}
		self.stat_secondary_attribute: list[str] = []
		self.stat_tertiary: dict[str, str | int | float] = {
			"attack": None,
			"charge_bonus": 0,
			"missile": None,
			"range": 0,
			"ammunition": 0,
			"weapon_type": None,
			"tech_type": "melee_simple",
			"damage_type": "blunt",
			"sound": "none",
			"musket_shot_set": None,
			"attack_delay": 25,
			"scfim": 1
		}
		self.stat_tertiary_attribute: list[str] = []
		self.stat_primary_armour: dict[str, int | str] = {
			"armour": 0,
			"defense_skill": 0,
			"shield": 0,
			"sound": "flesh"
		}
		self.stat_secondary_armour: dict[str, str | int] = {
			"armour": 0,
			"defense_skill": 0,
			"sound": "flesh"
		}
		self.stat_heat: int = 0
		self.stat_ground: dict[str, int] = {
			"scrub": 0,
			"sand": 0,
			"forest": 0,
			"snow": 0
		}
		self.stat_mental: dict[str, str | int] = {
			"morale": 0,
			"discipline": "normal",
			"training": "trained",
			"lock_morale": None
		}
		self.stat_charge_dist: int = 0
		self.stat_fire_delay: int = 0
		self.stat_cost: dict[str, int] = {
			"turns": 0,
			"construct": 0,
			"upkeep": 0,
			"weapon_ug": 0,
			"armour_ug": 0,
			"custom": 0,
			"custom_softcap": 0,
			"custom_penalty": 0
		}
		self.stat_stl: int = None
		self.armour_ug_levels: dict[str, int] = {
			"level_0": 0,
			"level_1": None,
			"level_2": None,
			"level_3": None
		}
		self.armour_ug_models: dict[str, str] = {
			"level_0": "Peasant",
			"level_1": None,
			"level_2": None,
			"level_3": None
		}
		self.ownership: list[str] = []
		self.eras: dict[str, list[str]] = {
			"era 0": None,
			"era 1": None,
			"era 2": None
		}
		self.recruit_priority_offset: float = None
		self.raw = None

	def __repr__(self) -> str:
		return f"Unit {self.type}"

	def __str__(self) -> str:
		lines = [f"type{" "*13}{self.type}"]
		if self.dictionary["name_1"] is None:
			name = ""
		else:
			name = self.dictionary["name_1"]
		lines.append(f"dictionary{" "*7}{self.dictionary["name_0"]}{" "*6}; {name}")
		lines.append(f"category{" "*9}{self.category}")
		lines.append(f"class{" "*12}{self.unit_class}")
		lines.append(f"voice_type{" "*7}{self.voice_type}")
		if self.accent is not None:
			lines.append(f"accent{" "*11}{self.accent}")
		if self.banner_faction is not None:
			lines.append(f"banner faction   {self.banner_faction}")
		if self.banner_unit is not None:
			lines.append(f"banner unit      {self.banner_unit}")
		if self.banner_holy is not None:
			lines.append(f"banner holy      {self.banner_holy}")
		soldier_stat = f"soldier{" "*10}{self.soldier["model"]}, {self.soldier["men"]}, {self.soldier["extras"]}, {self.soldier["mass"]}"
		if self.soldier["radius"]:
			soldier_stat += f", {self.soldier["radius"]}"
		if self.soldier["height"]:
			soldier_stat += f", {self.soldier["height"]}"
		lines.append(soldier_stat)
		if self.ship is not None:
			lines.append(f"ship{" "*13}{self.ship}")
		if self.officer_0 is not None:
			lines.append(f"officer{" "*10}{self.officer_0}")
		if self.officer_1 is not None:
			lines.append(f"officer{" "*10}{self.officer_1}")
		if self.officer_2 is not None:
			lines.append(f"officer{" "*10}{self.officer_2}")
		if self.engine is not None:
			lines.append(f"engine{" "*11}{self.engine}")
		if self.animal is not None:
			lines.append(f"animal{" "*11}{self.animal}")
		if self.mounted_engine is not None:
			lines.append(f"mounted_engine   {self.mounted_engine}")
		if self.mount is not None:
			lines.append(f"mount{" "*12}{self.mount}")
		mount_effect = ""
		for key in self.mount_effect.keys():
			if self.mount_effect != {}:
				mount_effect += f"{key} {self.mount_effect[key]}, "
		if mount_effect != "":
			lines.append(f"mount_effect     {mount_effect[:-2]}")
		at = ", ".join(self.attributes)
		lines.append(f"attributes       {at}")
		if self.move_speed_mod:
			lines.append(f"move_speed_mod   {self.move_speed_mod}")
		formation = ""
		for value in self.formation.values():
			if value is not None:
				formation += f"{value}, "
		lines.append(f"formation{" "*8}{formation[:-2]}")
		lines.append(f"stat_health      {self.stat_health[0]}, {self.stat_health[1]}")
		i = 0
		pre = ("pri", "sec", "ter")
		for stat in (
				(self.stat_primary, self.stat_primary_attribute),
				(self.stat_secondary, self.stat_secondary_attribute),
				(self.stat_tertiary, self.stat_tertiary_attribute)):
			if stat[0]["attack"] is None:
				break
			stat_pst = ""
			for key in stat[0].keys():
				if stat[0][key] is None:
					stat_pst += "no, "
					if key == "musket_shot_set":
						stat_pst = stat_pst[:-4]
				else:
					stat_pst += f"{stat[0][key]}, "
			lines.append(f"stat_{pre[i]}{" "*9}{stat_pst[:-2]}")
			attributes = ", ".join(stat[1])
			lines.append(f"stat_{pre[i]}_attr    {attributes}")
			i += 1
		primary_armour = ""
		for v in self.stat_primary_armour.values():
			primary_armour += f"{v}, "
		lines.append(f"stat_pri_armour  {primary_armour[:-2]}")
		secondary_armour = ""
		for v in self.stat_secondary_armour.values():
			secondary_armour += f"{v}, "
		lines.append(f"stat_sec_armour  {secondary_armour[:-2]}")
		lines.append(f"stat_heat{" "*8}{self.stat_heat}")
		stat_ground = ""
		for value in self.stat_ground.values():
			stat_ground += f"{value}, "
		lines.append(f"stat_ground      {stat_ground[:-2]}")
		stat_mental = ""
		for key in self.stat_mental.keys():
			stat_mental += f"{self.stat_mental[key]}, "
			if key == "lock_morale" and self.stat_mental[key] is None:
				stat_mental = stat_mental[:-6]
		lines.append(f"stat_mental      {stat_mental[:-2]}")
		lines.append(f"stat_charge_dist {self.stat_charge_dist}")
		lines.append(f"stat_fire_delay  {self.stat_fire_delay}")
		lines.append(f"stat_food        60, 300")  # Does nothing but will crash the game if it's missing.
		stat_cost = ""
		for value in self.stat_cost.values():
			stat_cost += f"{value}, "
		lines.append(f"stat_cost{" "*8}{stat_cost[:-2]}")
		if self.stat_stl:
			lines.append(f"stat_stl{" "*9}{self.stat_stl}")
		upgrade_level = ""
		for value in self.armour_ug_levels.values():
			if value is not None:
				upgrade_level += f"{value}, "
		lines.append(f"armour_ug_levels {upgrade_level[:-2]}")
		upgrade_model = ""
		for value in self.armour_ug_models.values():
			if value is not None:
				upgrade_model += f"{value}, "
		lines.append(f"armour_ug_models {upgrade_model[:-2]}")
		owner = ""
		for value in self.ownership:
			owner += f"{value}, "
		lines.append(f"ownership{" "*8}{owner[:-2]}")
		for era in self.eras.items():
			if era[1] is not None:
				era_line = ""
				for value in era[1]:
					era_line += f"{value}, "
				lines.append(f"{era[0]}{" "*12}{era_line[:-2]}")
		if self.recruit_priority_offset is not None:
			lines.append(f"recruit_priority_offset    {self.recruit_priority_offset}")
		final = ""
		for line in lines:
			final += (line + "\n")
		return final

	def fill_from_list(self, stat_list) -> None:
		self.raw = stat_list
		for line in stat_list:
			match line:
				case ["type", *unit_type]:
					name = ""
					for word in unit_type:
						name += f"{word} "
					self.type = name[:-1]
				case (["dictionary", *dictionary]):
					self.dictionary["name_0"] = dictionary[0]
					try:
						name = ""
						for word in dictionary[2:]:
							name += f"{word} "
						self.dictionary["name_1"] = name[:-1]
					except KeyError:
						pass
				case ["category", category]:
					self.category = category
				case ["class", unit_class]:
					self.unit_class = unit_class
				case ["voice_type", voice_type]:
					self.voice_type = voice_type
				case ["accent", accent]:
					self.accent = accent
				case ["banner", "faction", banner]:
					self.banner_faction = banner
				case ["banner", "unit", banner]:
					self.banner_unit = banner
				case ["banner", "holy", banner]:
					self.banner_holy = banner
				case ["soldier", *soldier_stat]:
					self.soldier["model"] = soldier_stat[0]
					self.soldier["men"] = soldier_stat[1]
					self.soldier["extras"] = soldier_stat[2]
					try:
						self.soldier["mass"] = soldier_stat[3]
					except IndexError:
						self.soldier["mass"] = 1
					try:
						if ";" not in soldier_stat[4]:
							self.soldier["radius"] = soldier_stat[4]
						else:
							soldier_stat = []
					except IndexError:
						pass
					try:
						self.soldier["height"] = soldier_stat[5]
					except IndexError:
						pass
				case ["engine", engine]:
					self.engine = engine
				case ["ship", *ship]:
					self.ship = f"{ship[0]} {ship[1]}"
				case ["officer", officer]:
					if self.officer_0 is None:
						self.officer_0 = officer
					elif self.officer_1 is None:
						self.officer_1 = officer
					elif self.officer_2 is None:
						self.officer_2 = officer
					else:
						raise TooManyOfficersError("A unit can only have 3 officers maximum")
				case ["mounted_engine", mounted_engine]:
					self.mounted_engine = mounted_engine
				case ["mount", *mount]:
					mount_string = ""
					for string in mount:
						mount_string += f"{string} "
					self.mount = mount_string[:-1]
				case ["mount_effect", *effects]:
					for index, effect in enumerate(effects):
						if ";" in effect:
							break
						if index % 2 == 0:
							self.mount_effect[effect] = effects[index + 1]
				case ["attributes", *attributes]:
					for attribute in attributes:
						self.attributes.append(attribute)
				case ["move_speed_mod", mod]:
					self.move_speed_mod = mod
				case ["formation", *formation_stats]:
					self.formation["close_x"] = formation_stats[0]
					self.formation["close_y"] = formation_stats[1]
					self.formation["loose_x"] = formation_stats[2]
					self.formation["loose_y"] = formation_stats[3]
					self.formation["ranks"] = formation_stats[4]
					self.formation["shape"] = formation_stats[5]
					try:
						self.formation["ability"] = formation_stats[6]
					except IndexError:
						pass
				case ["stat_health", *health]:
					self.stat_health = health
				case ["stat_pri", *stat_primary]:
					if "musket_shot_set" in stat_primary:
						self.stat_primary["musket_shot_set"] = "musket_shot_set"
						stat_primary.pop(9)
					self.stat_primary["attack"] = stat_primary[0]
					self.stat_primary["charge_bonus"] = stat_primary[1]
					self.stat_primary["missile"] = stat_primary[2]
					self.stat_primary["range"] = stat_primary[3]
					self.stat_primary["ammunition"] = stat_primary[4]
					self.stat_primary["weapon_type"] = stat_primary[5]
					self.stat_primary["tech_type"] = stat_primary[6]
					self.stat_primary["damage_type"] = stat_primary[7]
					self.stat_primary["sound"] = stat_primary[8]
					self.stat_primary["attack_delay"] = stat_primary[9]
					self.stat_primary["scfim"] = stat_primary[10]
				case ["stat_pri_attr", *stat_primary_attribute]:
					for attribute in stat_primary_attribute:
						self.stat_primary_attribute.append(attribute)
				case ["stat_sec", *stat_secondary]:
					if "musket_shot_set" in stat_secondary:
						self.stat_secondary["musket_shot_set"] = "musket_shot_set"
						stat_secondary.pop(9)
					self.stat_secondary["attack"] = stat_secondary[0]
					self.stat_secondary["charge_bonus"] = stat_secondary[1]
					self.stat_secondary["missile"] = stat_secondary[2]
					self.stat_secondary["range"] = stat_secondary[3]
					self.stat_secondary["ammunition"] = stat_secondary[4]
					self.stat_secondary["weapon_type"] = stat_secondary[5]
					self.stat_secondary["tech_type"] = stat_secondary[6]
					self.stat_secondary["damage_type"] = stat_secondary[7]
					self.stat_secondary["sound"] = stat_secondary[8]
					self.stat_secondary["attack_delay"] = stat_secondary[9]
					self.stat_secondary["scfim"] = stat_secondary[10]
				case ["stat_sec_attr", *stat_secondary_attribute]:
					for attribute in stat_secondary_attribute:
						self.stat_secondary_attribute.append(attribute)
				case ["stat_ter", *stat_tertiary]:
					if "musket_shot_set" in stat_tertiary:
						self.stat_tertiary["musket_shot_set"] = "musket_shot_set"
						stat_tertiary.pop(9)
					self.stat_tertiary["attack"] = stat_tertiary[0]
					self.stat_tertiary["charge_bonus"] = stat_tertiary[1]
					self.stat_tertiary["missile"] = stat_tertiary[2]
					self.stat_tertiary["range"] = stat_tertiary[3]
					self.stat_tertiary["ammunition"] = stat_tertiary[4]
					self.stat_tertiary["weapon_type"] = stat_tertiary[5]
					self.stat_tertiary["tech_type"] = stat_tertiary[6]
					self.stat_tertiary["damage_type"] = stat_tertiary[7]
					self.stat_tertiary["sound"] = stat_tertiary[8]
					self.stat_tertiary["attack_delay"] = stat_tertiary[9]
					self.stat_tertiary["scfim"] = stat_tertiary[10]
				case ["stat_ter_attr", *stat_tertiary_attribute]:
					for attribute in stat_tertiary_attribute:
						self.stat_tertiary_attribute.append(attribute)
				case ["stat_pri_armour", *stat_primary_armour]:
					self.stat_primary_armour["armour"] = stat_primary_armour[0]
					self.stat_primary_armour["defense_skill"] = stat_primary_armour[1]
					self.stat_primary_armour["shield"] = stat_primary_armour[2]
					self.stat_primary_armour["sound"] = stat_primary_armour[3]
				case ["stat_sec_armour", *ssa]:
					self.stat_secondary_armour["armour"] = ssa[0]
					self.stat_secondary_armour["defense_skill"] = ssa[1]
					self.stat_secondary_armour["sound"] = ssa[2]
				case ["stat_heat", sa]:
					self.stat_heat = sa
				case ["stat_ground", *stat_ground]:
					self.stat_ground["scrub"] = stat_ground[0]
					self.stat_ground["sand"] = stat_ground[1]
					self.stat_ground["forest"] = stat_ground[2]
					self.stat_ground["snow"] = stat_ground[3]
				case ["stat_mental", *stat_mental]:
					self.stat_mental["morale"] = stat_mental[0]
					self.stat_mental["discipline"] = stat_mental[1]
					self.stat_mental["training"] = stat_mental[2]
					try:
						self.stat_mental[stat_mental[3]] = stat_mental[3]
					except IndexError:
						pass
				case ["stat_charge_dist", distance]:
					self.stat_charge_dist = distance
				case ["stat_fire_delay", delay]:
					self.stat_fire_delay = delay
				case ["stat_cost", *stat_cost]:
					self.stat_cost["turns"] = stat_cost[0]
					self.stat_cost["construct"] = stat_cost[1]
					self.stat_cost["upkeep"] = stat_cost[2]
					self.stat_cost["weapon_ug"] = stat_cost[3]
					self.stat_cost["armour_ug"] = stat_cost[4]
					self.stat_cost["custom"] = stat_cost[5]
					self.stat_cost["custom_softcap"] = stat_cost[6]
					self.stat_cost["custom_penalty"] = stat_cost[7]
				case ["stat_stl", s]:
					self.stat_stl = s
				case ["armour_ug_levels", *aul]:
					for i, s in enumerate(aul):
						if ";" in s:
							break
						self.armour_ug_levels[f"level_{i}"] = s
				case ["armour_ug_models", *aum]:
					for i, s in enumerate(aum):
						self.armour_ug_models[f"level_{i}"] = s
				case ["ownership", *ownership]:
					if "all" in ownership[0]:
						self.ownership.append("all")
					else:
						for faction in ownership:
							self.ownership.append(faction)
				case ["era", num, *o]:
					self.eras[f"era {num}"] = []
					for f in o:
						self.eras[f"era {num}"].append(f)
				case ["recruit_priority_offset", offset]:
					self.recruit_priority_offset = offset


def create_units_from_txt(file="export_descr_unit.txt") -> list[Unit]:
	try:
		edu = open(file)
		lines = edu.readlines()
	except UnicodeDecodeError:
		edu = open(file, encoding="ISO-8859-1")
		lines = edu.readlines()
	finally:
		edu.close()
	# Makes instances of missing spaces between commas separated
	# values not crash the program.
	unit_starts = []
	for line_index, line in enumerate(lines):
		for char_index, char in enumerate(line):
			if char == "," and line[char_index+1] != " ":
				lines[line_index] = f"{line[:char_index+1]} {line[char_index+1:]}"
		if line[:4] == "type":
			unit_starts.append(line_index)
	units = []
	raw_units = []
	for start in range(len(unit_starts)):
		interval = []
		try:
			interval = (unit_starts[start], unit_starts[start + 1])
		except IndexError:
			interval = (unit_starts[start], None)
		finally:
			unit = []
			for line in lines[interval[0]:interval[1]]:
				line = line.split()
				for index, word in enumerate(line):
					if word[-1] == ",":
						line[index] = word[:-1]
				unit.append(line)
			raw_units.append(unit)
	for raw_unit in raw_units:
		unit = Unit()
		unit.fill_from_list(raw_unit)
		units.append(unit)
	return units


def create_edu_file(unit_list, file_name="Modified_EDU.txt") -> None:
	with open(file_name, "w") as mod_edu:
		for unit in unit_list:
			mod_edu.write(str(unit))
			mod_edu.write(" \n \n")


def main() -> None:
	unit_list = create_units_from_txt()
	create_edu_file(unit_list)


if __name__ == "__main__":
	main()
