class Unit:

	def __init__(self):
		self.type = None
		self.dictionary = {
			"name0": None,
			"name1": None}
		self.category = None
		self.cls = None
		self.voice_type = None
		self.accent = None
		self.banner_faction = None
		self.banner_holy = None
		self.banner_unit = None
		self.soldier = {
			"model": "Peasants",
			"men": 30,
			"extras": 0,
			"mass": 1}
		self.ship = None
		self.officer0 = None
		self.officer1 = None
		self.officer2 = None
		self.engine = None
		self.animal = None
		self.mounted_engine = None
		self.mount = None
		self.mount_effect = {}
		self.attributes = {}
		self.move_speed_mod = None
		self.formation = {
			"close_x": 1.2,
			"close_y": 1.2,
			"loose_x": 2.4,
			"loose_y": 2.4,
			"ranks": 8,
			"shape": "square",
			"ability": None}
		self.stat_health = [1, 0]
		self.stat_pri = {
			"attack": 0,
			"charge_bonus": 0,
			"missile": None,
			"range": 0,
			"ammunition": 0,
			"weapon_type": None,
			"tech_type": "melee_simple",
			"dmg_type": "blunt",
			"sound": "none",
			"musket_shot_set": 0,
			"atk_delay": 25,
			"scfim": 1}
		self.stat_pri_ex = {
			"ab_vs_mount": 0,
			"db_vs_mount": 0,
			"ap": 0}
		self.stat_pri_attr = {}
		self.stat_sec = {
			"attack": 0,
			"charge_bonus": 0,
			"missile": None,
			"range": 0,
			"ammunition": 0,
			"weapon_type": None,
			"tech_type": "melee_simple",
			"dmg_type": "blunt",
			"sound": "none",
			"musket_shot_set": 0,
			"atk_delay": 25,
			"scfim": 1}
		self.stat_sec_ex = {
			"ab_vs_mount": 0,
			"db_vs_mount": 0,
			"ap": 0}
		self.stat_sec_attr = {}
		self.stat_ter = {
			"attack": None,
			"charge_bonus": 0,
			"missile": None,
			"range": 0,
			"ammunition": 0,
			"weapon_type": None,
			"tech_type": "melee_simple",
			"dmg_type": "blunt",
			"sound": "none",
			"musket_shot_set": 0,
			"atk_delay": 25,
			"scfim": 1}
		self.stat_ter_ex = {
			"ab_vs_mount": 0,
			"db_vs_mount": 0,
			"ap": 0}
		self.stat_ter_attr = {}
		self.stat_pri_armour = {
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
		self.stat_sec_armour = {
			"armour": 0,
			"defense_skill": 0,
			"sound": "flesh"}
		self.stat_heat = 0
		self.stat_ground = {
			"scrub": 0,
			"sand": 0,
			"forest": 0,
			"snow": 0}
		self.stat_mental = {
			"morale": 0,
			"discipline": "normal",
			"training": "trained"}
		self.stat_charge_dist = 0
		self.stat_fire_delay = 0
		self.stat_food = [60, 300]
		self.stat_cost = {
			"turns": 0,
			"construct": 0,
			"upkeep": 0,
			"weapon_ug": 0,
			"armour_ug": 0,
			"custom": 0,
			"custom_softcap": 0,
			"custom_penalty": 0}
		self.stat_stl = None
		self.armour_ug_levels = {
			"level_0": 0,
			"level_1": None,
			"level_2": None,
			"level_3": None}
		self.armour_ug_models = {
			"level_0": "Peasant",
			"level_1": None,
			"level_2": None,
			"level_3": None}
		self.ownership = []
		self.eras = {
			"era 0": None,
			"era 1": None,
			"era 2": None}
		self.unit_info = {
			"melee_atk": 0,
			"missile_atk": 0,
			"defense": 0}
		self.recruit_priority_offset = None
		self.commented_out = []
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
		lines.append(f"class{' '*12}{self.cls}")
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
				(self.stat_pri, self.stat_pri_ex, self.stat_pri_attr),
				(self.stat_sec, self.stat_sec_ex, self.stat_sec_attr),
				(self.stat_ter, self.stat_ter_ex, self.stat_ter_attr)):
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
			for v in stat[1].values():
				sp += f"{v}, "
			lines.append(f"stat_{pre[i]}_ex      {sp[:-2]}")
			sp = ''
			for k in stat[2].keys():
				if stat[2][k]:
					if stat[2][k] == 1:
						sp += f"{k}, "
			lines.append(f"stat_{pre[i]}_attr    {sp[:-2]}")
			i += 1
		pa = ''
		for v in self.stat_pri_armour.values():
			pa += f"{v}, "
		lines.append(f"stat_pri_armour  {pa[:-2]}")
		ae = ''
		for v in self.stat_armour_ex.values():
			ae += f"{v}, "
		lines.append(f"stat_armour_ex   {ae[:-2]}")
		sa = ''
		for v in self.stat_sec_armour.values():
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
		lines.append(f"stat_food{' '*8}{self.stat_food[0]}, {self.stat_food[1]}")
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
		if self.unit_info:
			ui = ''
			for v in self.unit_info.values():
				ui += f"{v}, "
			lines.append(f"unit_info{' '*8}{ui[:-2]}")
		if self.commented_out is not None:
			for i in self.commented_out:
				lines[i] = f";{lines[i]}"
		r = ''
		for line in lines:
			r += (line + "\n")
		return r

	def disableSecWeapon(self):
		self.stat_sec["attack"] = 0
		self.stat_sec["charge_bonus"] = 0
		self.stat_sec["missile"] = None
		self.stat_sec["range"] = 0
		self.stat_sec["ammunition"] = 0
		self.stat_sec["weapon_type"] = None

	def fillInFromList(self, stat_list):
		self.raw = stat_list
		for i, line in enumerate(stat_list):
			try:
				if ';' in line[0]:
					self.commented_out.append(i)
					stat_list[i][0] = line[0][1:]
			except IndexError:
				pass
		for line in stat_list:
			match line:
				case ["type", *t]:
					name = ''
					for p in t:
						name += f"{p} "
					self.type = name[:-1]
				case (["dictionary", *dic]):
					self.dictionary["name0"] = dic[0]
					try:
						name = ''
						for p in dic[2:]:
							name += f"{p} "
						self.dictionary["name1"] = name[:-1]
					except KeyError:
						pass
				case ["category", cat]:
					self.category = cat
				case ["class", c]:
					self.cls = c
				case ["voice_type", vt]:
					self.voice_type = vt
				case ["accent", a]:
					self.accent = a
				case ["banner", "faction", bnr]:
					self.banner_faction = bnr
				case ["banner", "unit", bnr]:
					self.banner_unit = bnr
				case ["banner", "holy", bnr]:
					self.banner_holy = bnr
				case ["soldier", *s]:
					self.soldier["model"] = s[0]
					self.soldier["men"] = s[1]
					self.soldier["extras"] = s[2]
					self.soldier["mass"] = s[3]
				case ["engine", e]:
					self.engine = e
				case ["ship", *sp]:
					self.ship = f"{sp[0]} {sp[1]}"
				case ["officer", o]:
					if self.officer0 is None:
						self.officer0 = o
					elif self.officer1 is None:
						self.officer1 = o
					elif self.officer2 is None:
						self.officer2 = o
					else:
						raise TooManyOfficersError("A unit can only have 3 officers maximum")
				case ["mounted_engine", me]:
					self.mounted_engine = me
				case ["mount", *m]:
					r = ''
					for p in m:
						r += f"{p} "
					self.mount = r[:-1]
				case ["mount_effect", *effects]:
					for i, e in enumerate(effects):
						if i % 2 == 0:
							self.mount_effect[e] = effects[i + 1]
				case ["attributes", *attr]:
					for i, a in enumerate(attr):
						self.attributes[a] = 1
				case ["move_speed_mod", m]:
					self.move_speed_mod = m
				case ["formation", *form]:
					print(self.type)
					self.formation["close_x"] = form[0]
					self.formation["close_y"] = form[1]
					self.formation["loose_x"] = form[2]
					self.formation["loose_y"] = form[3]
					self.formation["ranks"] = form[4]
					self.formation["shape"] = form[5]
					try:
						self.formation["ability"] = form[6]
					except IndexError:
						pass
				case ["stat_health", *health]:
					self.stat_health = health
				case ["stat_pri", *sp]:
					if "musket_shot_set" in sp:
						self.stat_pri["musket_shot_set"] = 1
						sp.pop(9)
					self.stat_pri["attack"] = sp[0]
					self.stat_pri["charge_bonus"] = sp[1]
					self.stat_pri["missile"] = sp[2]
					self.stat_pri["range"] = sp[3]
					self.stat_pri["ammunition"] = sp[4]
					self.stat_pri["weapon_type"] = sp[5]
					self.stat_pri["tech_type"] = sp[6]
					self.stat_pri["dmg_type"] = sp[7]
					self.stat_pri["sound"] = sp[8]
					self.stat_pri["atk_delay"] = sp[9]
					self.stat_pri["scfim"] = sp[10]
				case ["stat_pri_ex", *spe]:
					self.stat_pri_ex["ab_vs_mount"] = spe[0]
					self.stat_pri_ex["db_vs_mount"] = spe[1]
					self.stat_pri_ex["ap"] = spe[2]
				case ["stat_pri_attr", *spa]:
					for a in spa:
						self.stat_pri_attr[a] = 1
				case ["stat_sec", *sp]:
					if "musket_shot_set" in sp:
						self.stat_sec["musket_shot_set"] = 1
						sp.pop(9)
					self.stat_sec["attack"] = sp[0]
					self.stat_sec["charge_bonus"] = sp[1]
					self.stat_sec["missile"] = sp[2]
					self.stat_sec["range"] = sp[3]
					self.stat_sec["ammunition"] = sp[4]
					self.stat_sec["weapon_type"] = sp[5]
					self.stat_sec["tech_type"] = sp[6]
					self.stat_sec["dmg_type"] = sp[7]
					self.stat_sec["sound"] = sp[8]
					self.stat_sec["atk_delay"] = sp[9]
					self.stat_sec["scfim"] = sp[10]
				case ["stat_sec_ex", *spe]:
					self.stat_sec_ex["ab_vs_mount"] = spe[0]
					self.stat_sec_ex["db_vs_mount"] = spe[1]
					self.stat_sec_ex["ap"] = spe[2]
				case ["stat_sec_attr", *spa]:
					for a in spa:
						self.stat_sec_attr[a] = 1
				case ["stat_ter", *sp]:
					if "musket_shot_set" in sp:
						self.stat_ter["musket_shot_set"] = 1
						sp.pop(9)
					self.stat_ter["attack"] = sp[0]
					self.stat_ter["charge_bonus"] = sp[1]
					self.stat_ter["missile"] = sp[2]
					self.stat_ter["range"] = sp[3]
					self.stat_ter["ammunition"] = sp[4]
					self.stat_ter["weapon_type"] = sp[5]
					self.stat_ter["tech_type"] = sp[6]
					self.stat_ter["dmg_type"] = sp[7]
					self.stat_ter["sound"] = sp[8]
					self.stat_ter["atk_delay"] = sp[9]
					self.stat_ter["scfim"] = sp[10]
				case ["stat_ter_ex", *spe]:
					self.stat_ter_ex["ab_vs_mount"] = spe[0]
					self.stat_ter_ex["db_vs_mount"] = spe[1]
					self.stat_ter_ex["ap"] = spe[2]
				case ["stat_ter_attr", *spa]:
					for a in spa:
						self.stat_ter_attr[a] = 1
				case ["stat_pri_armour", *spa]:
					self.stat_pri_armour["armour"] = spa[0]
					self.stat_pri_armour["defense_skill"] = spa[1]
					self.stat_pri_armour["shield"] = spa[2]
					self.stat_pri_armour["sound"] = spa[3]
				case ["stat_armour_ex", *sae]:
					self.stat_armour_ex["armour"] = sae[0]
					self.stat_armour_ex["b_armour"] = sae[1]
					self.stat_armour_ex["s_armour"] = sae[2]
					self.stat_armour_ex["g_armour"] = sae[3]
					self.stat_armour_ex["defense_skill"] = sae[4]
					self.stat_armour_ex["shield_melee"] = sae[5]
					self.stat_armour_ex["shield_missile"] = sae[6]
					self.stat_armour_ex["sound"] = sae[7]
				case ["stat_sec_armour", *ssa]:
					self.stat_sec_armour["armour"] = ssa[0]
					self.stat_sec_armour["defense_skill"] = ssa[1]
					self.stat_sec_armour["sound"] = ssa[2]
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
				case ["stat_food", *f]:
					self.stat_food = f
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
				case ["unit_info", *ui]:
					self.unit_info["melee_atk"] = ui[0]
					self.unit_info["missile_atk"] = ui[1]
					self.unit_info["defense"] = ui[2]
				case ["recruit_priority_offset", o]:
					self.recruit_priority_offset = o


class TooManyOfficersError(Exception):
	pass


def main():
	edu = open("export_descr_unit.txt", encoding="ISO-8859-1")
	lines = edu.readlines()
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
	for ru in raw_units:
		u = Unit()
		u.fillInFromList(ru)
		units.append(u)
	with open("Modified_EDU", "w") as mod:
		for u in units:
			mod.write(u.__str__())
			mod.write(" \n \n")


if __name__ == "__main__":
	main()
class Unit:

	def __init__(self):
		self.type = None
		self.dictionary = {
			"name0": None,
			"name1": None}
		self.category = None
		self.cls = None
		self.voice_type = None
		self.accent = None
		self.banner_faction = None
		self.banner_holy = None
		self.banner_unit = None
		self.soldier = {
			"model": "Peasants",
			"men": 30,
			"extras": 0,
			"mass": 1}
		self.ship = None
		self.officer0 = None
		self.officer1 = None
		self.officer2 = None
		self.engine = None
		self.animal = None
		self.mounted_engine = None
		self.mount = None
		self.mount_effect = {}
		self.attributes = {}
		self.move_speed_mod = None
		self.formation = {
			"close_x": 1.2,
			"close_y": 1.2,
			"loose_x": 2.4,
			"loose_y": 2.4,
			"ranks": 8,
			"shape": "square",
			"ability": None}
		self.stat_health = [1, 0]
		self.stat_pri = {
			"attack": 0,
			"charge_bonus": 0,
			"missile": None,
			"range": 0,
			"ammunition": 0,
			"weapon_type": None,
			"tech_type": "melee_simple",
			"dmg_type": "blunt",
			"sound": "none",
			"musket_shot_set": 0,
			"atk_delay": 25,
			"scfim": 1}
		self.stat_pri_ex = {
			"ab_vs_mount": 0,
			"db_vs_mount": 0,
			"ap": 0}
		self.stat_pri_attr = {}
		self.stat_sec = {
			"attack": 0,
			"charge_bonus": 0,
			"missile": None,
			"range": 0,
			"ammunition": 0,
			"weapon_type": None,
			"tech_type": "melee_simple",
			"dmg_type": "blunt",
			"sound": "none",
			"musket_shot_set": 0,
			"atk_delay": 25,
			"scfim": 1}
		self.stat_sec_ex = {
			"ab_vs_mount": 0,
			"db_vs_mount": 0,
			"ap": 0}
		self.stat_sec_attr = {}
		self.stat_ter = {
			"attack": None,
			"charge_bonus": 0,
			"missile": None,
			"range": 0,
			"ammunition": 0,
			"weapon_type": None,
			"tech_type": "melee_simple",
			"dmg_type": "blunt",
			"sound": "none",
			"musket_shot_set": 0,
			"atk_delay": 25,
			"scfim": 1}
		self.stat_ter_ex = {
			"ab_vs_mount": 0,
			"db_vs_mount": 0,
			"ap": 0}
		self.stat_ter_attr = {}
		self.stat_pri_armour = {
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
		self.stat_sec_armour = {
			"armour": 0,
			"defense_skill": 0,
			"sound": "flesh"}
		self.stat_heat = 0
		self.stat_ground = {
			"scrub": 0,
			"sand": 0,
			"forest": 0,
			"snow": 0}
		self.stat_mental = {
			"morale": 0,
			"discipline": "normal",
			"training": "trained"}
		self.stat_charge_dist = 0
		self.stat_fire_delay = 0
		self.stat_food = [60, 300]
		self.stat_cost = {
			"turns": 0,
			"construct": 0,
			"upkeep": 0,
			"weapon_ug": 0,
			"armour_ug": 0,
			"custom": 0,
			"custom_softcap": 0,
			"custom_penalty": 0}
		self.stat_stl = None
		self.armour_ug_levels = {
			"level_0": 0,
			"level_1": None,
			"level_2": None,
			"level_3": None}
		self.armour_ug_models = {
			"level_0": "Peasant",
			"level_1": None,
			"level_2": None,
			"level_3": None}
		self.ownership = []
		self.eras = {
			"era 0": None,
			"era 1": None,
			"era 2": None}
		self.unit_info = {
			"melee_atk": 0,
			"missile_atk": 0,
			"defense": 0}
		self.recruit_priority_offset = None
		self.commented_out = []
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
		lines.append(f"class{' '*12}{self.cls}")
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
				(self.stat_pri, self.stat_pri_ex, self.stat_pri_attr),
				(self.stat_sec, self.stat_sec_ex, self.stat_sec_attr),
				(self.stat_ter, self.stat_ter_ex, self.stat_ter_attr)):
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
			for v in stat[1].values():
				sp += f"{v}, "
			lines.append(f"stat_{pre[i]}_ex      {sp[:-2]}")
			sp = ''
			for k in stat[2].keys():
				if stat[2][k]:
					if stat[2][k] == 1:
						sp += f"{k}, "
			lines.append(f"stat_{pre[i]}_attr    {sp[:-2]}")
			i += 1
		pa = ''
		for v in self.stat_pri_armour.values():
			pa += f"{v}, "
		lines.append(f"stat_pri_armour  {pa[:-2]}")
		ae = ''
		for v in self.stat_armour_ex.values():
			ae += f"{v}, "
		lines.append(f"stat_armour_ex   {ae[:-2]}")
		sa = ''
		for v in self.stat_sec_armour.values():
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
		lines.append(f"stat_food{' '*8}{self.stat_food[0]}, {self.stat_food[1]}")
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
		if self.unit_info:
			ui = ''
			for v in self.unit_info.values():
				ui += f"{v}, "
			lines.append(f"unit_info{' '*8}{ui[:-2]}")
		if self.commented_out is not None:
			for i in self.commented_out:
				lines[i] = f";{lines[i]}"
		r = ''
		for line in lines:
			r += (line + "\n")
		return r

	def disableSecWeapon(self):
		self.stat_sec["attack"] = 0
		self.stat_sec["charge_bonus"] = 0
		self.stat_sec["missile"] = None
		self.stat_sec["range"] = 0
		self.stat_sec["ammunition"] = 0
		self.stat_sec["weapon_type"] = None

	def fillInFromList(self, stat_list):
		self.raw = stat_list
		for i, line in enumerate(stat_list):
			try:
				if ';' in line[0]:
					self.commented_out.append(i)
					stat_list[i][0] = line[0][1:]
			except IndexError:
				pass
		for line in stat_list:
			match line:
				case ["type", *t]:
					name = ''
					for p in t:
						name += f"{p} "
					self.type = name[:-1]
				case (["dictionary", *dic]):
					self.dictionary["name0"] = dic[0]
					try:
						name = ''
						for p in dic[2:]:
							name += f"{p} "
						self.dictionary["name1"] = name[:-1]
					except KeyError:
						pass
				case ["category", cat]:
					self.category = cat
				case ["class", c]:
					self.cls = c
				case ["voice_type", vt]:
					self.voice_type = vt
				case ["accent", a]:
					self.accent = a
				case ["banner", "faction", bnr]:
					self.banner_faction = bnr
				case ["banner", "unit", bnr]:
					self.banner_unit = bnr
				case ["banner", "holy", bnr]:
					self.banner_holy = bnr
				case ["soldier", *s]:
					self.soldier["model"] = s[0]
					self.soldier["men"] = s[1]
					self.soldier["extras"] = s[2]
					self.soldier["mass"] = s[3]
				case ["engine", e]:
					self.engine = e
				case ["ship", *sp]:
					self.ship = f"{sp[0]} {sp[1]}"
				case ["officer", o]:
					if self.officer0 is None:
						self.officer0 = o
					elif self.officer1 is None:
						self.officer1 = o
					elif self.officer2 is None:
						self.officer2 = o
					else:
						raise TooManyOfficersError("A unit can only have 3 officers maximum")
				case ["mounted_engine", me]:
					self.mounted_engine = me
				case ["mount", *m]:
					r = ''
					for p in m:
						r += f"{p} "
					self.mount = r[:-1]
				case ["mount_effect", *effects]:
					for i, e in enumerate(effects):
						if i % 2 == 0:
							self.mount_effect[e] = effects[i + 1]
				case ["attributes", *attr]:
					for i, a in enumerate(attr):
						self.attributes[a] = 1
				case ["move_speed_mod", m]:
					self.move_speed_mod = m
				case ["formation", *form]:
					print(self.type)
					self.formation["close_x"] = form[0]
					self.formation["close_y"] = form[1]
					self.formation["loose_x"] = form[2]
					self.formation["loose_y"] = form[3]
					self.formation["ranks"] = form[4]
					self.formation["shape"] = form[5]
					try:
						self.formation["ability"] = form[6]
					except IndexError:
						pass
				case ["stat_health", *health]:
					self.stat_health = health
				case ["stat_pri", *sp]:
					if "musket_shot_set" in sp:
						self.stat_pri["musket_shot_set"] = 1
						sp.pop(9)
					self.stat_pri["attack"] = sp[0]
					self.stat_pri["charge_bonus"] = sp[1]
					self.stat_pri["missile"] = sp[2]
					self.stat_pri["range"] = sp[3]
					self.stat_pri["ammunition"] = sp[4]
					self.stat_pri["weapon_type"] = sp[5]
					self.stat_pri["tech_type"] = sp[6]
					self.stat_pri["dmg_type"] = sp[7]
					self.stat_pri["sound"] = sp[8]
					self.stat_pri["atk_delay"] = sp[9]
					self.stat_pri["scfim"] = sp[10]
				case ["stat_pri_ex", *spe]:
					self.stat_pri_ex["ab_vs_mount"] = spe[0]
					self.stat_pri_ex["db_vs_mount"] = spe[1]
					self.stat_pri_ex["ap"] = spe[2]
				case ["stat_pri_attr", *spa]:
					for a in spa:
						self.stat_pri_attr[a] = 1
				case ["stat_sec", *sp]:
					if "musket_shot_set" in sp:
						self.stat_sec["musket_shot_set"] = 1
						sp.pop(9)
					self.stat_sec["attack"] = sp[0]
					self.stat_sec["charge_bonus"] = sp[1]
					self.stat_sec["missile"] = sp[2]
					self.stat_sec["range"] = sp[3]
					self.stat_sec["ammunition"] = sp[4]
					self.stat_sec["weapon_type"] = sp[5]
					self.stat_sec["tech_type"] = sp[6]
					self.stat_sec["dmg_type"] = sp[7]
					self.stat_sec["sound"] = sp[8]
					self.stat_sec["atk_delay"] = sp[9]
					self.stat_sec["scfim"] = sp[10]
				case ["stat_sec_ex", *spe]:
					self.stat_sec_ex["ab_vs_mount"] = spe[0]
					self.stat_sec_ex["db_vs_mount"] = spe[1]
					self.stat_sec_ex["ap"] = spe[2]
				case ["stat_sec_attr", *spa]:
					for a in spa:
						self.stat_sec_attr[a] = 1
				case ["stat_ter", *sp]:
					if "musket_shot_set" in sp:
						self.stat_ter["musket_shot_set"] = 1
						sp.pop(9)
					self.stat_ter["attack"] = sp[0]
					self.stat_ter["charge_bonus"] = sp[1]
					self.stat_ter["missile"] = sp[2]
					self.stat_ter["range"] = sp[3]
					self.stat_ter["ammunition"] = sp[4]
					self.stat_ter["weapon_type"] = sp[5]
					self.stat_ter["tech_type"] = sp[6]
					self.stat_ter["dmg_type"] = sp[7]
					self.stat_ter["sound"] = sp[8]
					self.stat_ter["atk_delay"] = sp[9]
					self.stat_ter["scfim"] = sp[10]
				case ["stat_ter_ex", *spe]:
					self.stat_ter_ex["ab_vs_mount"] = spe[0]
					self.stat_ter_ex["db_vs_mount"] = spe[1]
					self.stat_ter_ex["ap"] = spe[2]
				case ["stat_ter_attr", *spa]:
					for a in spa:
						self.stat_ter_attr[a] = 1
				case ["stat_pri_armour", *spa]:
					self.stat_pri_armour["armour"] = spa[0]
					self.stat_pri_armour["defense_skill"] = spa[1]
					self.stat_pri_armour["shield"] = spa[2]
					self.stat_pri_armour["sound"] = spa[3]
				case ["stat_armour_ex", *sae]:
					self.stat_armour_ex["armour"] = sae[0]
					self.stat_armour_ex["b_armour"] = sae[1]
					self.stat_armour_ex["s_armour"] = sae[2]
					self.stat_armour_ex["g_armour"] = sae[3]
					self.stat_armour_ex["defense_skill"] = sae[4]
					self.stat_armour_ex["shield_melee"] = sae[5]
					self.stat_armour_ex["shield_missile"] = sae[6]
					self.stat_armour_ex["sound"] = sae[7]
				case ["stat_sec_armour", *ssa]:
					self.stat_sec_armour["armour"] = ssa[0]
					self.stat_sec_armour["defense_skill"] = ssa[1]
					self.stat_sec_armour["sound"] = ssa[2]
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
				case ["stat_food", *f]:
					self.stat_food = f
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
				case ["unit_info", *ui]:
					self.unit_info["melee_atk"] = ui[0]
					self.unit_info["missile_atk"] = ui[1]
					self.unit_info["defense"] = ui[2]
				case ["recruit_priority_offset", o]:
					self.recruit_priority_offset = o


class TooManyOfficersError(Exception):
	pass


def main():
	edu = open("export_descr_unit.txt", encoding="ISO-8859-1")
	lines = edu.readlines()
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
	for ru in raw_units:
		u = Unit()
		u.fillInFromList(ru)
		units.append(u)
	with open("Modified_EDU", "w") as mod:
		for u in units:
			mod.write(u.__str__())
			mod.write(" \n \n")


if __name__ == "__main__":
	main()
