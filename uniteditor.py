class Unit:

	def __init__(self):
		self.type: str = None
		self.dictionary: dict[str: str] = {
			"name0": None,
			"name1": None}
		self.category: str = None
		self.unit_class: str = None
		self.voice_type: str = None
		self.accent: str = None
		self.banner_faction: str = None
		self.banner_holy: str = None
		self.banner_unit: str = None
		self.soldier: dict[str | int | float] = {
			"model": "Peasants",
			"men": 30,
			"extras": 0,
			"mass": 1}
		self.ship: str = None
		self.officer0: str = None
		self.officer1: str = None
		self.officer2: str = None
		self.engine: str = None
		self.animal: str = None
		self.mounted_engine: str = None
		self.mount: str = None
		self.mount_effect: dict[str, int] = {}
		self.attributes: dict[str, str] = {}
		self.move_speed_mod: float = None
		self.formation: [str, str | float | int] = {
			"close_x": 1.2,
			"close_y": 1.2,
			"loose_x": 2.4,
			"loose_y": 2.4,
			"ranks": 8,
			"shape": "square",
			"ability": None}
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
			"musket_shot_set": 0,
			"atk_delay": 25,
			"scfim": 1}
		self.stat_primary_attribute: dict[str, str] = {}
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
			"musket_shot_set": 0,
			"atk_delay": 25,
			"scfim": 1}
		self.stat_secondary_attribute: dict[str, str] = {}
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
			"musket_shot_set": 0,
			"atk_delay": 25,
			"scfim": 1}
		self.stat_tertiary_attribute: dict[str, str] = {}
		self.stat_primary_armour: dict[str, int | str] = {
			"armour": 0,
			"defense_skill": 0,
			"shield": 0,
			"sound": "flesh"}
		self.stat_armour_ex = {
			"armour": 0,
			"b_armour": 0,
			"s_armour": 0,
			"g_armour": 0,
			"defense_skill": 0,
			"shield_melee": 0,
			"shield_missile": 0,
			"sound": "flesh"}
		self.stat_secondary_armour: dict[str, str | int] = {
			"armour": 0,
			"defense_skill": 0,
			"sound": "flesh"}
		self.stat_heat: int = 0
		self.stat_ground: dict[str, int] = {
			"scrub": 0,
			"sand": 0,
			"forest": 0,
			"snow": 0}
		self.stat_mental: dict[str, str | int] = {
			"morale": 0,
			"discipline": "normal",
			"training": "trained"}
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
			"custom_penalty": 0}
		self.stat_stl: int = None
		self.armour_ug_levels: dict[str, int] = {
			"level_0": 0,
			"level_1": None,
			"level_2": None,
			"level_3": None}
		self.armour_ug_models: dict[str, str] = {
			"level_0": "Peasant",
			"level_1": None,
			"level_2": None,
			"level_3": None}
		self.ownership: list[str] = []
		self.eras: dict[str, list[str]] = {
			"era 0": None,
			"era 1": None,
			"era 2": None}
		self.recruit_priority_offset: float = None
		# self.commented_out = []
		self.raw = None

	def __repr__(self):
		return f"Unit {self.type}"

	def __str__(self):
		lines = [f"type{' '*13}{self.type}"]
		if self.dictionary["name1"] is None:
			n = ''
		else:
			n = self.dictionary["name1"]
		lines.append(f"dictionary{' '*7}{self.dictionary['name0']}{' '*6}; {n}")
		lines.append(f"category{' '*9}{self.category}")
		lines.append(f"class{' '*12}{self.unit_class}")
		lines.append(f"voice_type{' '*7}{self.voice_type}")
		if self.accent is not None:
			lines.append(f"accent{' '*11}{self.accent}")
		if self.banner_faction is not None:
			lines.append(f"banner faction   {self.banner_faction}")
		if self.banner_unit is not None:
			lines.append(f"banner unit      {self.banner_unit}")
		if self.banner_holy is not None:
			lines.append(f"banner holy      {self.banner_holy}")
		lines.append(
			f"soldier{' '*10}{self.soldier['model']}, {self.soldier['men']}, {self.soldier['extras']}, {self.soldier['mass']}")
		if self.ship is not None:
			lines.append(f"ship{' '*13}{self.ship}")
		if self.officer0 is not None:
			lines.append(f"officer{' '*10}{self.officer0}")
		if self.officer1 is not None:
			lines.append(f"officer{' '*10}{self.officer1}")
		if self.officer2 is not None:
			lines.append(f"officer{' '*10}{self.officer2}")
		if self.engine is not None:
			lines.append(f"engine{' '*11}{self.engine}")
		if self.animal is not None:
			lines.append(f"animal{' '*11}{self.animal}")
		if self.mounted_engine is not None:
			lines.append(f"mounted_engine   {self.mounted_engine}")
		if self.mount is not None:
			lines.append(f"mount{' '*12}{self.mount}")
		me = ''
		for k in self.mount_effect.keys():
			if self.mount_effect != {}:
				me += f"{k} {self.mount_effect[k]}, "
		if me != '':
			lines.append(f"mount_effect     {me[:-2]}")
		at = ''
		for k in self.attributes.keys():
			if self.attributes[k] > 0:
				if k == "stakes":
					at += f"{k}, "*2
				else:
					at += f"{k}, "
		if at[-2:] == ", ":
			at = at[:-2]
		elif at == '':
			at = "no"
		lines.append(f"attributes       {at}")
		if self.move_speed_mod:
			lines.append(f"move_speed_mod   {self.move_speed_mod}")
		fo = ''
		for v in self.formation.values():
			if v is not None:
				fo += f"{v}, "
		lines.append(f"formation{' '*8}{fo[:-2]}")
		lines.append(f"stat_health      {self.stat_health[0]}, {self.stat_health[1]}")
		i = 0
		pre = ("pri", "sec", "ter")
		for stat in (
				(self.stat_primary, self.stat_primary_attribute),
				(self.stat_secondary, self.stat_secondary_attribute),
				(self.stat_tertiary, self.stat_tertiary_attribute)):
			if stat[0]["attack"] is None:
				break
			sp = ''
			for k in stat[0].keys():
				if stat[0][k] is None:
					sp += "no, "
				elif k == "musket_shot_set":
					if stat[0][k]:
						sp += f"{k}, "
				else:
					sp += f"{stat[0][k]}, "
			lines.append(f"stat_{pre[i]}{' '*9}{sp[:-2]}")
			sp = ''
			for k in stat[1].keys():
				if stat[1][k]:
					if stat[1][k] == 1:
						sp += f"{k}, "
			lines.append(f"stat_{pre[i]}_attr    {sp[:-2]}")
			i += 1
		pa = ''
		for v in self.stat_primary_armour.values():
			pa += f"{v}, "
		lines.append(f"stat_pri_armour  {pa[:-2]}")
		ae = ''
		for v in self.stat_armour_ex.values():
			ae += f"{v}, "
		lines.append(f"stat_armour_ex   {ae[:-2]}")
		sa = ''
		for v in self.stat_secondary_armour.values():
			sa += f"{v}, "
		lines.append(f"stat_sec_armour  {sa[:-2]}")
		lines.append(f"stat_heat{' '*8}{self.stat_heat}")
		sg = ''
		for v in self.stat_ground.values():
			sg += f"{v}, "
		lines.append(f"stat_ground      {sg[:-2]}")
		sm = ''
		for k in self.stat_mental.keys():
			if k == "lock_morale" and self.stat_mental[k] == 1:
				sm += f"{k}, "
			else:
				sm += f"{self.stat_mental[k]}, "
		lines.append(f"stat_mental      {sm[:-2]}")
		lines.append(f"stat_charge_dist {self.stat_charge_dist}")
		lines.append(f"stat_fire_delay  {self.stat_fire_delay}")
		sc = ''
		for v in self.stat_cost.values():
			sc += f"{v}, "
		lines.append(f"stat_cost{' '*8}{sc[:-2]}")
		if self.stat_stl:
			lines.append(f"stat_stl{' '*9}{self.stat_stl}")
		ul = ''
		for v in self.armour_ug_levels.values():
			if v is not None:
				ul += f"{v}, "
		lines.append(f"armour_ug_levels {ul[:-2]}")
		um = ''
		for v in self.armour_ug_models.values():
			if v is not None:
				um += f"{v}, "
		lines.append(f"armour_ug_models {um[:-2]}")
		o = ''
		for v in self.ownership:
			o += f"{v}, "
		lines.append(f"ownership{' '*8}{o[:-2]}")
		for era in self.eras.items():
			if era[1] is not None:
				e = ''
				for v in era[1]:
					e += f"{v}, "
				lines.append(f"{era[0]}{' '*12}{e[:-2]}")
		# No longer supporting commenting out lines of unit stats.
		# Was mostly just lines that don't do anything even uncommented
		# since they no longer had a function in the game. And if you don't
		# want it to affect your unit, just leave it out.
		'''if self.commented_out is not None: 
			print(self.commented_out)
			print(self.dictionary)
			for i in self.commented_out:
				lines[i] = f";{lines[i]}"'''
		r = ''
		for line in lines:
			r += (line + "\n")
		return r

	def disable_secondary_weapon(self):
		self.stat_secondary["attack"] = 0
		self.stat_secondary["charge_bonus"] = 0
		self.stat_secondary["missile"] = None
		self.stat_secondary["range"] = 0
		self.stat_secondary["ammunition"] = 0
		self.stat_secondary["weapon_type"] = None

	def fill_from_list(self, stat_list):
		self.raw = stat_list
		'''for index, line in enumerate(stat_list):
			try:
				if ';' in line[0]:
					self.commented_out.append(index)
					stat_list[index][0] = line[0][1:]
			except IndexError:
				pass'''
		for line in stat_list:
			match line:
				case ["type", *unit_type]:
					name = ''
					for word in unit_type:
						name += f"{word} "
					self.type = name[:-1]
				case (["dictionary", *dictionary]):
					self.dictionary["name0"] = dictionary[0]
					try:
						name = ''
						for word in dictionary[2:]:
							name += f"{word} "
						self.dictionary["name1"] = name[:-1]
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
					# print(soldier_stat)
					self.soldier["model"] = soldier_stat[0]
					self.soldier["men"] = soldier_stat[1]
					self.soldier["extras"] = soldier_stat[2]
					try:
						self.soldier["mass"] = soldier_stat[3]
					except IndexError:
						self.soldier["mass"] = 1
				case ["engine", engine]:
					self.engine = engine
				case ["ship", *ship]:
					self.ship = f"{ship[0]} {ship[1]}"
				case ["officer", officer]:
					if self.officer0 is None:
						self.officer0 = officer
					elif self.officer1 is None:
						self.officer1 = officer
					elif self.officer2 is None:
						self.officer2 = officer
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
						if index % 2 == 0:
							self.mount_effect[effect] = effects[index + 1]
				case ["attributes", *attributes]:
					for attribute in attributes:
						self.attributes[attribute] = 1
				case ["move_speed_mod", mod]:
					self.move_speed_mod = mod
				case ["formation", *formation_stats]:
					# print(self.type)
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
						self.stat_primary["musket_shot_set"] = 1
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
					self.stat_primary["atk_delay"] = stat_primary[9]
					self.stat_primary["scfim"] = stat_primary[10]
				case ["stat_pri_attr", *stat_primary_attribute]:
					for a in stat_primary_attribute:
						self.stat_primary_attribute[a] = 1
				case ["stat_sec", *sp]:
					if "musket_shot_set" in sp:
						self.stat_secondary["musket_shot_set"] = 1
						sp.pop(9)
					self.stat_secondary["attack"] = sp[0]
					self.stat_secondary["charge_bonus"] = sp[1]
					self.stat_secondary["missile"] = sp[2]
					self.stat_secondary["range"] = sp[3]
					self.stat_secondary["ammunition"] = sp[4]
					self.stat_secondary["weapon_type"] = sp[5]
					self.stat_secondary["tech_type"] = sp[6]
					self.stat_secondary["damage_type"] = sp[7]
					self.stat_secondary["sound"] = sp[8]
					self.stat_secondary["atk_delay"] = sp[9]
					self.stat_secondary["scfim"] = sp[10]
				case ["stat_sec_attr", *stat_secondary_attribute]:
					for a in stat_secondary_attribute:
						self.stat_secondary_attribute[a] = 1
				case ["stat_ter", *sp]:
					if "musket_shot_set" in sp:
						self.stat_tertiary["musket_shot_set"] = 1
						sp.pop(9)
					self.stat_tertiary["attack"] = sp[0]
					self.stat_tertiary["charge_bonus"] = sp[1]
					self.stat_tertiary["missile"] = sp[2]
					self.stat_tertiary["range"] = sp[3]
					self.stat_tertiary["ammunition"] = sp[4]
					self.stat_tertiary["weapon_type"] = sp[5]
					self.stat_tertiary["tech_type"] = sp[6]
					self.stat_tertiary["damage_type"] = sp[7]
					self.stat_tertiary["sound"] = sp[8]
					self.stat_tertiary["atk_delay"] = sp[9]
					self.stat_tertiary["scfim"] = sp[10]
				case ["stat_ter_attr", *stat_tertiary_attribute]:
					for a in stat_tertiary_attribute:
						self.stat_tertiary_attribute[a] = 1
				case ["stat_pri_armour", *stat_primary_armor]:
					self.stat_primary_armour["armour"] = stat_primary_armor[0]
					self.stat_primary_armour["defense_skill"] = stat_primary_armor[1]
					self.stat_primary_armour["shield"] = stat_primary_armor[2]
					self.stat_primary_armour["sound"] = stat_primary_armor[3]
				case ["stat_armour_ex", *sae]:  # Unused by game, needs to be removed
					self.stat_armour_ex["armour"] = sae[0]
					self.stat_armour_ex["b_armour"] = sae[1]
					self.stat_armour_ex["s_armour"] = sae[2]
					self.stat_armour_ex["g_armour"] = sae[3]
					self.stat_armour_ex["defense_skill"] = sae[4]
					self.stat_armour_ex["shield_melee"] = sae[5]
					self.stat_armour_ex["shield_missile"] = sae[6]
					self.stat_armour_ex["sound"] = sae[7]
				case ["stat_sec_armour", *ssa]:
					self.stat_secondary_armour["armour"] = ssa[0]
					self.stat_secondary_armour["defense_skill"] = ssa[1]
					self.stat_secondary_armour["sound"] = ssa[2]
				case ["stat_heat", sa]:
					self.stat_heat = sa
				case ["stat_ground", *sg]:
					self.stat_ground["scrub"] = sg[0]
					self.stat_ground["sand"] = sg[1]
					self.stat_ground["forest"] = sg[2]

					self.stat_ground["snow"] = sg[3]
				case ["stat_mental", *sm]:
					self.stat_mental["morale"] = sm[0]
					self.stat_mental["discipline"] = sm[1]
					self.stat_mental["training"] = sm[2]
					try:
						self.stat_mental[sm[3]] = 1
					except IndexError:
						pass
				case ["stat_charge_dist", d]:
					self.stat_charge_dist = d
				case ["stat_fire_delay", d]:
					self.stat_fire_delay = d
				case ["stat_cost", *sc]:
					self.stat_cost["turns"] = sc[0]
					self.stat_cost["construct"] = sc[1]
					self.stat_cost["upkeep"] = sc[2]
					self.stat_cost["weapon_ug"] = sc[3]
					self.stat_cost["armour_ug"] = sc[4]
					self.stat_cost["custom"] = sc[5]
					self.stat_cost["custom_softcap"] = sc[6]
					self.stat_cost["custom_penalty"] = sc[7]
				case ["stat_stl", s]:
					self.stat_stl = s
				case ["armour_ug_levels", *aul]:
					for i, s in enumerate(aul):
						self.armour_ug_levels[f"level_{i}"] = s
				case ["armour_ug_models", *aum]:
					for i, s in enumerate(aum):
						self.armour_ug_models[f"level_{i}"] = s
				case ["ownership", *o]:
					for f in o:
						self.ownership.append(f)
				case ["era", num, *o]:
					self.eras[f"era {num}"] = []
					for f in o:
						self.eras[f"era {num}"].append(f)
				case ["recruit_priority_offset", o]:
					self.recruit_priority_offset = o


class TooManyOfficersError(Exception):
	"""Is raised if more than 3 officer lines are read for a given unit."""
	pass


def main():
	edu = open("export_descr_unit(SS6.4).txt", encoding="ISO-8859-1")
	lines = edu.readlines()
	# Makes instances of missing spaces between commas separated
	# values not crash the program.
	for line_index, line in enumerate(lines):
		for char_index, char in enumerate(line):
			if char == "," and line[char_index+1] != " ":
				lines[line_index] = f"{line[:char_index+1]} {line[char_index+1:]}"
	edu.close()
	unit_starts = []
	for i, line in enumerate(lines):
		if line[:4] == "type":
			unit_starts.append(i)
	units = []
	raw_units = []
	for start in range(len(unit_starts)):
		interval = []
		try:
			interval = (unit_starts[start], unit_starts[start + 1])
		except IndexError:
			interval = (unit_starts[start], None)
		finally:
			u = []
			for i, l in enumerate(lines[interval[0]:interval[1]]):
				line = l.split()
				for c, word in enumerate(line):
					if word[-1] == ',':
						line[c] = word[:-1]
				u.append(line)
			raw_units.append(u)
	for raw_unit in raw_units:
		unit = Unit()
		unit.fill_from_list(raw_unit)
		units.append(unit)
	with open("Modified_EDU", "w") as mod:
		for unit in units:
			mod.write(str(unit))
			mod.write(" \n \n")


if __name__ == "__main__":
	main()
