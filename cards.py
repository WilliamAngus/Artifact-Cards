"""
Artificer's Mail
Lina
"""



# First in relate for heroes is sig card.

class Card:

    def __init__(self, name, mana, kind, description="", related=[], is_signature=False, is_deck=True):
        self.name = name
        self.mana = mana
        self.kind = kind
        self.description = description
        self.related_cards = related
        self.is_signature = is_signature
        self.is_deck = is_deck


    def get_image_name(self):
        return self.name.replace(",", "").replace("'", "").replace("!", "").replace("-", " ").replace(".", "").replace(" ", "_").lower()


    def __repr__(self):
        return self.name

    def __lt__(self, other):

        return str(self) < str(other)





item_cards = []

blink_scroll = Card("Blink Scroll", 0, "consumable", is_deck=False)
item_cards.append(blink_scroll)

malchanted_mango = Card("Malchanted Mango", 0, "accessory", is_deck=False)
item_cards.append(malchanted_mango)


potion_of_knowledge = Card("Potion of Knowledge", 5, "consumable", is_deck=False)
item_cards.append(potion_of_knowledge)

squirmified_straps = Card("Squirmified-Straps", 0, "armor", is_deck=False)
item_cards.append(squirmified_straps)

transmuted_weapon = Card("Transmuted Weapon", 0, "weapon", is_deck=False)
item_cards.append(transmuted_weapon)


barbed_mail = Card("Barbed Mail", 10, "armor")
item_cards.append(barbed_mail)

bracers_of_sacrifice = Card("Bracers of Sacrifice", 10, "armor")
item_cards.append(bracers_of_sacrifice)

claszureme_hourglass = Card("Claszureme Hourglass", 10, "accessory")
item_cards.append(claszureme_hourglass)

demagicking_maul = Card("Demagicking Maul", 10, "weapon")
item_cards.append(demagicking_maul)

demolishing_warhammer = Card("Demolishing Warhammer", 10, "weapon")
item_cards.append(demolishing_warhammer)

force_staff = Card("Force Staff", 10, "weapon")
item_cards.append(force_staff)

greevil_egg = Card("Greevil Egg", 10, "consumable")
item_cards.append(greevil_egg)

healing_blade = Card("Healing Blade", 10, "weapon")
item_cards.append(healing_blade)

hooked_net = Card("Hooked Net", 10, "weapon")
item_cards.append(hooked_net)

midas_greaves = Card("Midas Greaves", 10, "armor")
item_cards.append(midas_greaves)

phase_boots = Card("Phase Boots", 10, "accessory")
item_cards.append(phase_boots)

revtel_mercenary_contract = Card("Revtel Mercenary Contract", 10, "consumable") # TODO: add Revtel Mercenary
item_cards.append(revtel_mercenary_contract)

ring_of_basilius = Card("Ring of Basilius", 10, "armor")
item_cards.append(ring_of_basilius)

stonehall_cloak = Card("Stonehall Cloak", 10, "accessory")
item_cards.append(stonehall_cloak)


artificers_mail = Card("Artificer's Mail", 15, "armor")
item_cards.append(artificers_mail)

blade_of_the_vigil = Card("Blade of the Vigil", 15, "weapon")
item_cards.append(blade_of_the_vigil)

blink_dagger = Card("Blink Dagger", 15, "weapon")
item_cards.append(blink_dagger)

broadsword = Card("Broadsword", 15, "weapon")
item_cards.append(broadsword)

cloak_of_endless_carnage = Card("Cloak of Endless Carnage", 15, "accessory")
item_cards.append(cloak_of_endless_carnage)

crown_of_the_undying = Card("Crown of the Undying", 15, "armor")            # TODO: add zombie
item_cards.append(crown_of_the_undying)

golden_ticket = Card("Golden Ticket", 15, "consumable")
item_cards.append(golden_ticket)

infernal_amulet = Card("Infernal Amulet", 15, "accessory")
item_cards.append(infernal_amulet)

jasper_daggers = Card("Jasper Daggers", 15, "weapon")
item_cards.append(jasper_daggers)

main_gauche = Card("Main Gauche", 15, "weapon")
item_cards.append(main_gauche)

necronomicon = Card("Necronomicon", 15, "accessory")
item_cards.append(necronomicon)

orchid = Card("Orchid", 15, "weapon")
item_cards.append(orchid)

red_mist_maul = Card("Red Mist Maul", 15, "weapon")
item_cards.append(red_mist_maul)

ring_of_tarrasque = Card("Ring of Tarrasque", 15, "accessory")
item_cards.append(ring_of_tarrasque)

ritsul_emblem = Card("Ritsul Emblem", 15, "armor")
item_cards.append(ritsul_emblem)

warhorn = Card("Warhorn", 15, "accessory")
item_cards.append(warhorn)


claymore = Card("Claymore", 20, "weapon")
item_cards.append(claymore)

gem_of_truesight = Card("Gem of Truesight", 20, "accessory")
item_cards.append(gem_of_truesight)

ghost_scepter = Card("Ghost Scepter", 20, "accessory")
item_cards.append(ghost_scepter)

helm_of_the_dominator = Card("Helm of the Dominator", 20, "armor")
item_cards.append(helm_of_the_dominator)

heros_cape = Card("Hero's Cape", 20, "accessory")
item_cards.append(heros_cape)

mortreds_dagger = Card("Mortred's Dagger", 20, "weapon")
item_cards.append(mortreds_dagger)

nullifier = Card("Nullifier", 20, "armor")
item_cards.append(nullifier)

root_boots = Card("Root Boots", 20, "armor")
item_cards.append(root_boots)

sorla_khans_spear = Card("Sorla Khan's Spear", 20, "weapon")
item_cards.append(sorla_khans_spear)

vanguard = Card("Vanguard", 20, "armor")
item_cards.append(vanguard)

vesture_of_the_tyrant = Card("Vesture of the Tyrant", 20, "armor")
item_cards.append(vesture_of_the_tyrant)

wingfall_hammer = Card("Wingfall Hammer", 20, "weapon")
item_cards.append(wingfall_hammer)


guardian_greaves = Card("Guardian Greaves", 25, "armor")
item_cards.append(guardian_greaves)

holy_locket = Card("Holy Locket", 25, "accessory")
item_cards.append(holy_locket)

horn_of_the_alpha = Card("Horn of the Alpha", 25, "accessory")
item_cards.append(horn_of_the_alpha)

mjolnir = Card("Mjolnir", 25, "weapon")
item_cards.append(mjolnir)

sheep_stick = Card("Sheep Stick", 25, "weapon")
item_cards.append(sheep_stick)

silver_edge = Card("Silver Edge", 25, "weapon")
item_cards.append(silver_edge)

spirit_vessel = Card("Spirit Vessel", 25, "accessory")
item_cards.append(spirit_vessel)

vladmirs_offering = Card("Vladmir's Offering", 25, "armor")
item_cards.append(vladmirs_offering)


apotheosis_blade = Card("Apotheosis Blade", 30, "weapon")
item_cards.append(apotheosis_blade)

dagon = Card("Dagon", 30, "accessory")
item_cards.append(dagon)

darkblight_shield = Card("Darkblight Shield", 30, "armor")
item_cards.append(darkblight_shield)

nyctashas_guard = Card("Nyctasha's Guard", 30, "armor")
item_cards.append(nyctashas_guard)

radiance = Card("Radiance", 30, "weapon")
item_cards.append(radiance)

refresher_orb = Card("Refresher Orb", 30, "accessory")
item_cards.append(refresher_orb)












black_cards = []
green_cards = []
black_signatures = []
green_signatures = []
black_heroes = []
green_heroes = []

hound_of_war = Card("Hound of War", 1, "creep", is_deck=False)
black_cards.append(hound_of_war)

static_remnant = Card("Static Remnant", 2, "creep", is_deck=False)
black_cards.append(static_remnant)





neutral_cards = []

animated_armor = Card("Animated Armor", 5, "creep", related=[artificers_mail], is_deck=False)
neutral_cards.append(animated_armor)
artificers_mail.related_cards = [animated_armor]

courier = Card("Courier", 0, "improvement", is_deck=False)
neutral_cards.append(courier)

demonic_archer = Card("Demonic Archer", 2, "creep", is_deck=False)
neutral_cards.append(demonic_archer)
necronomicon.related_cards = [demonic_archer]

destroyed_from_within = Card("Destroyed from Within", 4, "spell", is_deck=False)
neutral_cards.append(destroyed_from_within)

eidolon = Card("Eidolon", 1, "creep", is_deck=False)
neutral_cards.append(eidolon)

mega_creep = Card("Mega Creep", 2, "creep", is_deck=False)
neutral_cards.append(mega_creep)

melee_creep = Card("Melee Creep", 1, "creep", is_deck=False)
neutral_cards.append(melee_creep)


the_twisted_path = Card("The Twisted Path", 3, "improvement")
neutral_signatures = [the_twisted_path]

rix_oathbound = Card("Rix, Oathbound", 0, "hero", related=[the_twisted_path])
neutral_heroes = [rix_oathbound]

naked_greevil = Card("Naked Greevil", 1, "creep")
neutral_cards.append(naked_greevil)

neutral_cards = neutral_heroes + neutral_signatures + neutral_cards








assassinate = Card("Assassinate", 7, "spell")
black_signatures.append(assassinate)

assault_ladders = Card("Assault Ladders", 2, "improvement")
black_signatures.append(assault_ladders)

ball_lightning = Card("Ball Lightning", 2, "spell")
black_signatures.append(ball_lightning)

chain_frost = Card("Chain Frost", 6, "spell")
black_signatures.append(chain_frost)

coup_de_grace = Card("Coup de Grace", 5, "spell")
black_signatures.append(coup_de_grace)

death_pulse = Card("Death Pulse", 2, "spell")
black_signatures.append(death_pulse)

exorcism = Card("Exorcism", 7, "spell")
black_signatures.append(exorcism)

exsanguinate = Card("Exsanguinate", 4, "spell")
black_signatures.append(exsanguinate)

mana_void = Card("Mana Void", 5, "spell")
black_signatures.append(mana_void)

march_of_the_machines = Card("March of the Machines", 4, "improvement")
black_signatures.append(march_of_the_machines)

no_accident = Card("No Accident", 2, "spell")
black_signatures.append(no_accident)

presence_of_the_dark_lord = Card("Presence of the Dark Lord", 3, "spell")
black_signatures.append(presence_of_the_dark_lord)

sacred_arrow = Card("Sacred Arrow", 4, "spell")
black_signatures.append(sacred_arrow)

shadow_walk = Card("Shadow Walk", 2, "spell")
black_signatures.append(shadow_walk)

winters_curse = Card("Winter's Curse", 5, "spell")
black_signatures.append(winters_curse)



anti_mage = Card("Anti-Mage", 0, "hero", related=[mana_void])
black_heroes.append(anti_mage)

bloodseeker = Card("Bloodseeker", 0, "hero", related=[exsanguinate])
black_heroes.append(bloodseeker)

bounty_hunter = Card("Bounty Hunter", 0, "hero", related=[shadow_walk])
black_heroes.append(bounty_hunter)

death_prophet = Card("Death Prophet", 0, "hero", related=[exorcism])
black_heroes.append(death_prophet)

debbi_the_cunning = Card("Debbi the Cunning", 0, "hero", related=[no_accident])
black_heroes.append(debbi_the_cunning)

lich = Card("Lich", 0, "hero", related=[chain_frost])
black_heroes.append(lich)

mirana = Card("Mirana", 0, "hero", related=[sacred_arrow])
black_heroes.append(mirana)

necrophos = Card("Necrophos", 0, "hero", related=[death_pulse])
black_heroes.append(necrophos)

phantom_assassin = Card("Phantom Assassin", 0, "hero", related=[coup_de_grace])
black_heroes.append(phantom_assassin)

shadow_fiend = Card("Shadow Fiend", 0, "hero", related=[presence_of_the_dark_lord])
black_heroes.append(shadow_fiend)

sniper = Card("Sniper", 0, "hero", related=[assassinate])
black_heroes.append(sniper)

sorla_khan = Card("Sorla Khan", 0, "hero", related=[assault_ladders])
black_heroes.append(sorla_khan)

storm_spirit = Card("Storm Spirit", 0, "hero", related=[ball_lightning, static_remnant])
black_heroes.append(storm_spirit)

tinker = Card("Tinker", 0, "hero", related=[march_of_the_machines])
black_heroes.append(tinker)

winter_wyvern = Card("Winter Wyvern", 0, "hero", related=[winters_curse])
black_heroes.append(winter_wyvern)






bitter_enemies = Card("Bitter Enemies", 1, "improvement")
black_cards.append(bitter_enemies)

escape_route = Card("Escape Route", 1, "improvement")
black_cards.append(escape_route)

gaseous_greevil = Card("Gaseous Greevil", 1, "creep")
black_cards.append(gaseous_greevil)

grazing_shot = Card("Grazing Shot", 1, "spell")
black_cards.append(grazing_shot)

killer_instinct = Card("Killer Instinct", 1, "spell")
black_cards.append(killer_instinct)

ravenous_mass = Card("Ravenous Mass", 1, "creep")
black_cards.append(ravenous_mass)

relentless_pursuit = Card("Relentless Pursuit", 1, "spell")
black_cards.append(relentless_pursuit)

thieving_greevil = Card("Thieving Greevil", 1, "creep")
black_cards.append(thieving_greevil)

trebuchets = Card("Trebuchets", 1, "improvement")
black_cards.append(trebuchets)


arclight_elemental = Card("Arclight Elemental", 2, "creep")     # TODO: add arc remnant
black_cards.append(arclight_elemental)

assassins_apprentice = Card("Assassin's Apprentice", 2, "creep")
black_cards.append(assassins_apprentice)

committed_rebel = Card("Committed Rebel", 2, "creep")
black_cards.append(committed_rebel)

disciple_of_nevermore = Card("Disciple of Nevermore", 2, "creep")
black_cards.append(disciple_of_nevermore)

infernal_ally = Card("Infernal Ally", 2, "creep")
black_cards.append(infernal_ally)

oglodi_catapult = Card("Oglodi Catapult", 2, "creep")
black_cards.append(oglodi_catapult)

path_of_the_cunning = Card("Path of the Cunning", 2, "improvement")
black_cards.append(path_of_the_cunning)

revtel_investments = Card("Revtel Investments", 2, "improvement")
black_cards.append(revtel_investments)

slay = Card("Slay", 2, "spell")
black_cards.append(slay)

the_oath = Card("The Oath", 2, "improvement")
black_cards.append(the_oath)

untested_grunt = Card("Untested Grunt", 2, "creep")
black_cards.append(untested_grunt)


a_thousand_cuts = Card("A Thousand Cuts", 3, "spell")
black_cards.append(a_thousand_cuts)

acolyte_of_the_forbidden_gate = Card("Acolyte of the Forbidden Gate", 3, "creep")
black_cards.append(acolyte_of_the_forbidden_gate)

beyond_the_veil = Card("Beyond the Veil", 3, "spell")
black_cards.append(beyond_the_veil)

burning_pitch = Card("Burning Pitch", 3, "improvement")
black_cards.append(burning_pitch)

gank = Card("Gank", 3, "spell")
black_cards.append(gank)

hip_fire = Card("Hip Fire", 3, "spell")
black_cards.append(hip_fire)

keenfolk_turret = Card("Keenfolk Turret", 3, "improvement")
black_cards.append(keenfolk_turret)

murder_plot = Card("Murder Plot", 3, "spell")
black_cards.append(murder_plot)

pick_off = Card("Pick Off", 3, "spell")
black_cards.append(pick_off)

the_tyler_estate = Card("The Tyler Estate", 3, "improvement")
black_cards.append(the_tyler_estate)


horde_stryder = Card("Horde Stryder", 4, "creep")
black_cards.append(horde_stryder)

insidious_plot = Card("Insidious Plot", 4, "spell", related=[destroyed_from_within])
black_cards.append(insidious_plot)

iron_fog_goldmine = Card("Iron Fog Goldmine", 4, "improvement")
black_cards.append(iron_fog_goldmine)

knives_in_the_dark = Card("Knives in the Dark", 4, "spell")
black_cards.append(knives_in_the_dark)

oglodi_vandal = Card("Oglodi Vandal", 4, "creep")
black_cards.append(oglodi_vandal)

ogre_corpse_tosser = Card("Ogre Corpse Tosser", 4, "creep")
black_cards.append(ogre_corpse_tosser)

pit_fighter_of_quoidge = Card("Pit Fighter of Quoidge", 4, "creep")
black_cards.append(pit_fighter_of_quoidge)

sister_of_the_void = Card("Sister of the Void", 4, "creep", related=[eidolon])
black_cards.append(sister_of_the_void)

tyler_estate_censor = Card("Tyler Estate Censor", 4, "creep")
black_cards.append(tyler_estate_censor)


berserker_of_the_abyssm = Card("Berserker of the Abyssm", 5, "creep")
black_cards.append(berserker_of_the_abyssm)

ravenhook = Card("Ravenhook", 5, "creep")
black_cards.append(ravenhook)

the_cover_of_night = Card("The Cover of Night", 5, "spell")
black_cards.append(the_cover_of_night)

tower_explosion = Card("Tower Explosion", 5, "spell")
black_cards.append(tower_explosion)


abyssm_flesh_render = Card("Abyssm Flesh Render", 6, "creep")
black_cards.append(abyssm_flesh_render)

assassins_shadow = Card("Assassin's Shadow", 6, "creep")
black_cards.append(assassins_shadow)

steam_cannon = Card("Steam Cannon", 6, "improvement")
black_cards.append(steam_cannon)





black_cards = black_heroes + black_signatures + black_cards











corrosive_breath = Card("Corrosive Breath", 4, "improvement", is_deck=False)
green_cards.append(corrosive_breath)

terrapin_greatshell = Card("Terrapin Greatshell", 3, "creep", is_deck=False)
green_cards.append(terrapin_greatshell)



act_of_defiance = Card("Act of Defiance", 2, "spell")
green_signatures.append(act_of_defiance)

astral_imprisonment = Card("Astral Imprisonment", 4, "spell")
green_signatures.append(astral_imprisonment)

atrophy_aura = Card("Atrophy Aura", 3, "spell")
green_signatures.append(atrophy_aura)

dragon_tail = Card("Dragon Tail", 2, "spell")
green_signatures.append(dragon_tail)

enchant = Card("Enchant", 4, "spell")
green_signatures.append(enchant)

gust = Card("Gust", 3, "spell")
green_signatures.append(gust)

hand_of_god = Card("Hand of God", 5, "spell")
green_signatures.append(hand_of_god)

hymn_of_st_crella = Card("Hymn of St. Crella", 3, "spell")
green_signatures.append(hymn_of_st_crella)

ion_shell = Card("Ion Shell", 3, "spell")
green_signatures.append(ion_shell)

prowler_vanguard = Card("Prowler Vanguard", 3, "creep")
green_signatures.append(prowler_vanguard)

repel = Card("Repel", 1, "spell")
green_signatures.append(repel)

roseleaf_druid = Card("Roseleaf Druid", 2, "creep")
green_signatures.append(roseleaf_druid)

sandstorm = Card("Sandstorm", 3, "spell")
green_signatures.append(sandstorm)

savage_wolf = Card("Savage Wolf", 3, "creep")
green_signatures.append(savage_wolf)

weave = Card("Weave", 5, "improvement")
green_signatures.append(weave)

wraithfire_blast = Card("Wraithfire Blast", 4, "spells")
green_signatures.append(wraithfire_blast)





chen = Card("Chen", 0, "hero", related=[hand_of_god])
green_heroes.append(chen)

dark_seer = Card("Dark Seer", 0, "hero", related=[ion_shell])
green_heroes.append(dark_seer)

dazzle = Card("Dazzle", 0, "hero", related=[weave])
green_heroes.append(dazzle)

dragon_knight = Card("Dragon Knight", 0, "hero", related=[dragon_tail])
green_heroes.append(dragon_knight)

drow = Card("Drow Ranger", 0, "hero", related=[gust])
green_heroes.append(drow)

enchantress = Card("Enchantress", 0, "hero", related=[enchant])
green_heroes.append(enchantress)

farvhan_the_dreamer = Card("Farvhan the Dreamer", 0, "hero", related=[prowler_vanguard])
green_heroes.append(farvhan_the_dreamer)

lady_anshu = Card("Lady Anshu", 0, "hero", related=[hymn_of_st_crella])
green_heroes.append(lady_anshu)

lycan = Card("Lycan", 0, "hero", related=[savage_wolf])
green_heroes.append(lycan)

omniknight = Card("Omniknight", 0, "hero", related=[repel])
green_heroes.append(omniknight)

outworld_devourer = Card("Outworld Devourer", 0, "hero", related=[astral_imprisonment])
green_heroes.append(outworld_devourer)

rix = Card("Rix", 0, "hero", related=[act_of_defiance])
green_heroes.append(rix)

sand_king = Card("Sand King", 0, "hero", related=[sandstorm])
green_heroes.append(sand_king)

treant_protector = Card("Treant Protector", 0, "hero", related=[roseleaf_druid])
green_heroes.append(treant_protector)

underlord = Card("Underlord", 0, "hero", related=[atrophy_aura])
green_heroes.append(underlord)

wraith_king = Card("Wraith King", 0, "hero", related=[wraithfire_blast])
green_heroes.append(wraith_king)




bellow = Card("Bellow", 1, "spell")
green_cards.append(bellow)

defend_the_weak = Card("Defend the Weak", 1, "spell")
green_cards.append(defend_the_weak)

juke = Card("Juke", 1, "spell")
green_cards.append(juke)

quicksap_sproutling = Card("Quicksap Sproutling", 1, "creep")
green_cards.append(quicksap_sproutling)

spirited_greevil = Card("Spirited Greevil", 1, "creep")
green_cards.append(spirited_greevil)

stars_align = Card("Stars Align", 1, "spell")
green_cards.append(stars_align)

sticky_greevil = Card("Sticky Greevil", 1, "creep")
green_cards.append(sticky_greevil)


living_armor = Card("Living Armor", 2, "spell")
green_cards.append(living_armor)

path_of_the_dreamer = Card("Path of the Dreamer", 2, "improvement")
green_cards.append(path_of_the_dreamer)

rebel_decoy = Card("Rebel Decoy", 2, "creep")
green_cards.append(rebel_decoy)

rumusque_blessing = Card("Rumusque Blessing", 2, "spell")
green_cards.append(rumusque_blessing)

unearthed_secrets = Card("Unearthed Secrets", 2, "improvement")
green_cards.append(unearthed_secrets)

vhoul_martyr = Card("Vhoul Martyr", 2, "creep")
green_cards.append(vhoul_martyr)


altar_of_the_mad_moon = Card("Altar of the Mad Moon", 3, "improvement")
green_cards.append(altar_of_the_mad_moon)

arm_the_rebellion = Card("Arm the Rebellion", 3, "spell")
green_cards.append(arm_the_rebellion)

caught_unprepared = Card("Caught Unprepared", 3, "spell")
green_cards.append(caught_unprepared)

cheating_death = Card("Cheating Death", 3, "improvement")
green_cards.append(cheating_death)

homefield_advantage = Card("Homefield Advantage", 3, "improvement")
green_cards.append(homefield_advantage)

intimidation = Card("Intimidation", 3, "spell")
green_cards.append(intimidation)

overgrowther = Card("Overgrowther", 3, "creep")
green_cards.append(overgrowther)

rampaging_hellbear = Card("Rampaging Hellbear", 3, "creep")
green_cards.append(rampaging_hellbear)

satyr_duelist = Card("Satyr Duelist", 3, "creep")
green_cards.append(satyr_duelist)

selfish_cleric = Card("Selfish Cleric", 3, "creep")
green_cards.append(selfish_cleric)

shattered_terrapin = Card("Shattered Terrapin", 3, "creep", related=[terrapin_greatshell])
green_cards.append(shattered_terrapin)

smeevil_blacksmith = Card("Smeevil Blacksmith", 3, "creep")
green_cards.append(smeevil_blacksmith)

snarling_harpy = Card("Snarling Harpy", 3, "creep")
green_cards.append(snarling_harpy)

soul_of_spring = Card("Soul of Spring", 3, "spell")
green_cards.append(soul_of_spring)

spriggan_mischief = Card("Spriggan Mischief", 3, "spell")
green_cards.append(spriggan_mischief)

steal_strength = Card("Steal Strength", 3, "spell")
green_cards.append(steal_strength)

summoning_circle = Card("Summoning Circle", 3, "improvement")           # TODO: add Ozkavosh Horror
green_cards.append(summoning_circle)


divine_intervention = Card("Divine Intervention", 4, "spell")
green_cards.append(divine_intervention)

fey_wayfinder = Card("Fey Wayfinder", 4, "creep")
green_cards.append(fey_wayfinder)

ironwood_heart = Card("Ironwood Heart", 4, "spell")
green_cards.append(ironwood_heart)

leech_seed = Card("Leech Seed", 4, "spell")
green_cards.append(leech_seed)

mist_of_avernus = Card("Mist of Avernus", 4, "improvement")
green_cards.append(mist_of_avernus)

moonglade_fusilier = Card("Moonglade Fusilier", 4, "creep")
green_cards.append(moonglade_fusilier)

restoration_effort = Card("Restoration Effort", 4, "spell")
green_cards.append(restoration_effort)

rumusque_redeemer = Card("Rumusque Redeemer", 4, "creep")
green_cards.append(rumusque_redeemer)

shifting_loyalties = Card("Shifting Loyalties", 4, "spell")
green_cards.append(shifting_loyalties)


champion_of_the_ancient = Card("Champion of the Ancient", 5, "creep")
green_cards.append(champion_of_the_ancient)

corrosive_mist = Card("Corrosive Mist", 5, "spell")
green_cards.append(corrosive_mist)

lashvine_creeper = Card("Lashvine Creeper", 5, "creep")
green_cards.append(lashvine_creeper)

roseleaf_rejuvinator = Card("Roseleaf Rejuvenator", 5, "creep")
green_cards.append(roseleaf_rejuvinator)

screeching_harpy = Card("Screeching Harpy", 5, "creep")
green_cards.append(screeching_harpy)


divine_purpose = Card("Divine Purpose", 6, "spell")
green_cards.append(divine_purpose)

emissary_of_the_quorum = Card("Emissary of the Quorum", 6, "creep")
green_cards.append(emissary_of_the_quorum)

revtel_convoy = Card("Revtel Convoy", 6, "creep")
green_cards.append(revtel_convoy)

selemenes_favor = Card("Selemene's Favor", 6, "improvement")
green_cards.append(selemenes_favor)


thunderhide_pack = Card("Thunderhide Pack", 7, "creep")
green_cards.append(thunderhide_pack)
horn_of_the_alpha.related_cards = [thunderhide_pack]


fist_of_the_allseeing_one = Card("Fist of the Allseeing One", 8, "creep")
green_cards.append(fist_of_the_allseeing_one)

thunderhide_alpha = Card("Thunderhide Alpha", 8, "creep")
green_cards.append(thunderhide_alpha)










green_cards = green_heroes + green_signatures + green_cards





red_unplayables = []

# Red Unplayables
# ===============

centaur_poacher = Card("Centaur Poacher", 4, "creep", is_deck=False)
red_unplayables.append(centaur_poacher)

ice_shard = Card("Ice Shard", 1, "creep", is_deck=False)
red_unplayables.append(ice_shard)

loyal_beast = Card("Loyal Beast", 2, "creep", is_deck=False)
red_unplayables.append(loyal_beast)

stonehall_paragon = Card("Stonehall Paragon", 4, "creep", is_deck=False)
red_unplayables.append(stonehall_paragon)




red_signatures = []

# Red Signatures
# ==============

culling_blade = Card("Culling Blade", 2, "spell")
red_signatures.append(culling_blade)

double_edge = Card("Double Edge", 1, "spell")
red_signatures.append(double_edge)

duel = Card("Duel", 2, "spell")
red_signatures.append(duel)

gods_strength = Card("God's Strength", 3, "spell")
red_signatures.append(gods_strength)

gush = Card("Gush", 3, "spell")
red_signatures.append(gush)

ice_shards = Card("Ice Shards", 2, "spell", related=[ice_shard])
red_signatures.append(ice_shards)

lancer_illusion = Card("Lancer Illusion", 3, "creep")
red_signatures.append(lancer_illusion)

life_drain = Card("Life Drain", 3, "spell")
red_signatures.append(life_drain)

overpower = Card("Overpower", 3, "spell")
red_signatures.append(overpower)

primal_roar = Card("Primal Roar", 3, "spell")
red_signatures.append(primal_roar)

reckless_charge = Card("Reckless Charge", 2, "spell")
red_signatures.append(reckless_charge)

toss = Card("Toss", 4, "spell")
red_signatures.append(toss)

viscous_nasal_goo = Card("Viscous Nasal Goo", 3, "spell")
red_signatures.append(viscous_nasal_goo)

whirling_death = Card("Whirling Death", 2, "spell")
red_signatures.append(whirling_death)




red_heroes = []

# Red heroes
# ==========

axe = Card("Axe", 0, "hero", related=[culling_blade])
red_heroes.append(axe)

beastmaster = Card("Beastmaster", 0, "hero", related=[primal_roar, loyal_beast])
red_heroes.append(beastmaster)

bristleback = Card("Bristleback", 0, "hero", related=[viscous_nasal_goo])
red_heroes.append(bristleback)

centaur_warrunner = Card("Centaur Warrunner", 0, "hero", related=[double_edge])
red_heroes.append(centaur_warrunner)

keefe_the_bold = Card("Keefe the Bold", 0, "hero", related=[reckless_charge])
red_heroes.append(keefe_the_bold)

legion_commander = Card("Legion Commander", 0, "hero", related=[duel])
red_heroes.append(legion_commander)

phantom_lancer = Card("Phantom Lancer", 0, "hero", related=[lancer_illusion])
red_heroes.append(phantom_lancer)

pugna = Card("Pugna", 0, "hero", related=[life_drain])
red_heroes.append(pugna)

sven = Card("Sven", 0, "hero", related=[gods_strength])
red_heroes.append(sven)

tidehunter = Card("Tidehunter", 0, "hero", related=[gush])
red_heroes.append(tidehunter)

timbersaw = Card("Timbersaw", 0, "hero", related=[whirling_death])
red_heroes.append(timbersaw)

tiny = Card("Tiny", 0, "hero", related=[toss])
red_heroes.append(tiny)

tusk = Card("Tusk", 0, "hero", related=[ice_shards])
red_heroes.append(tusk)

ursa = Card("Ursa", 0, "hero", related=[overpower])
red_heroes.append(ursa)



red_cards = []

# Red remaining
# =============

burning_oil = Card("Burning Oil", 1, "improvement")
red_cards.append (burning_oil)

fighting_words = Card("Fighting Words", 1, "spell")
red_cards.append(fighting_words)

flesh_of_iron = Card("Flesh of Iron", 1, "spell")
red_cards.append(flesh_of_iron)

greevil_bronco = Card("Greevil Bronco", 1, "creep")
red_cards.append(greevil_bronco)

greevil_eggtender = Card("Greevil Eggtender", 1, "creep")
red_cards.append(greevil_eggtender)

into_the_fray = Card("Into the Fray", 1, "spell")
red_cards.append(into_the_fray)

poised_to_strike = Card("Poised to Strike", 1, "spell")
red_cards.append(poised_to_strike)

bronze_legionnaire = Card("Bronze Legionnaire", 2, "creep")
red_cards.append(bronze_legionnaire)

hellbear_crippler = Card("Hellbear Crippler", 2, "creep")
red_cards.append(hellbear_crippler)

heroic_resolve = Card("Heroic Resolve", 2, "spell")
red_cards.append(heroic_resolve)

nether_ward = Card("Nether Ward", 2, "improvement")
red_cards.append(nether_ward)

no_hesitation = Card("No Hesitation", 2, "spell")
red_cards.append(no_hesitation)

path_of_the_bold = Card("Path of the Bold", 2, "improvement")
red_cards.append(path_of_the_bold)

rend_armor = Card("Rend Armor", 2, "spell")
red_cards.append(rend_armor)

smash_their_defenses = Card("Smash Their Defenses!", 2, "spell")
red_cards.append(smash_their_defenses)

throw_down = Card("Throw Down", 2, "spell")
red_cards.append(throw_down)

unbreakable_column = Card("Unbreakable Column", 2, "spell")
red_cards.append(unbreakable_column)

wild_boar = Card("Wild Boar", 2, "creep")
red_cards.append(wild_boar)


clear_the_deck = Card("Clear the Deck", 3, "spell")
red_cards.append(clear_the_deck)

iron_sharpens_iron = Card("Iron Sharpens Iron", 3, "spell")
red_cards.append(iron_sharpens_iron)

legion_standard_bearer = Card("Legion Standard Bearer", 3, "creep")
red_cards.append(legion_standard_bearer)

smeevil_armsmaster = Card("Smeevil Armsmaster", 3, "creep")
red_cards.append(smeevil_armsmaster)

temple_of_war = Card("Temple of War", 3, "improvement")
red_cards.append(temple_of_war)

the_omexe_arena = Card("The Omexe Arena", 3, "improvement")
red_cards.append(the_omexe_arena)

veterans_insight = Card("Veteran's Insight", 3, "spell")
red_cards.append(veterans_insight)


cursed_satyr = Card("Cursed Satyr", 4, "creep")
red_cards.append(cursed_satyr)

honor_guard = Card("Honor Guard", 4, "creep")
red_cards.append(honor_guard)

punch_it = Card("Punch it!", 4, "spell")
red_cards.append(punch_it)

raze = Card("Raze", 4, "spell")
red_cards.append(raze)

rebel_rabble_rouser = Card("Rebel Rabble Rouser", 4, "creep")                   # TODO: missing Roused Rabble!
red_cards.append(rebel_rabble_rouser)

spirit_swordsman = Card("Spirit Swordsman", 4, "creep")
red_cards.append(spirit_swordsman)

stonehall_elite = Card("Stonehall Elite", 4, "creep", related=[stonehall_paragon])
red_cards.append(stonehall_elite)


back_for_more = Card("Back For More", 5, "spell")
red_cards.append(back_for_more)

marrowfell_brawler = Card("Marrowfell Brawler", 5, "creep")
red_cards.append(marrowfell_brawler)

ogre_conscript = Card("Ogre Conscript", 5, "creep")
red_cards.append(ogre_conscript)

red_mist_pillager = Card("Red Mist Pillager", 5, "creep")
red_cards.append(red_mist_pillager)

stonehall_conscriptor = Card("Stonehall Conscriptor", 5, "creep")
red_cards.append(stonehall_conscriptor)



slumbering_brute = Card("Slumbering Brute", 6, "creep")
red_cards.append(slumbering_brute)

team_fight = Card("Team Fight", 6, "spell")
red_cards.append(team_fight)



hellbear_smasher = Card("Hellbear Smasher", 7, "creep")
red_cards.append(hellbear_smasher)

spring_the_trap = Card("Spring the Trap", 7, "spell", related=[centaur_poacher])
red_cards.append(spring_the_trap)



time_of_triumph = Card("Time of Triumph", 9, "spell")
red_cards.append(time_of_triumph)


red_cards = red_heroes + red_signatures + red_unplayables + red_cards







blue_cards = []
########## BLUE


plague_ward = Card("Plague Ward", 1, "creep", is_deck=False)
blue_cards.append(plague_ward)

rock = Card("Rock", 1, "creep", is_deck=False)
blue_cards.append(rock)

spawn_of_maelrawn = Card("Spawn of Maelrawn", 13, "creep", is_deck=False)
blue_cards.append(spawn_of_maelrawn)

terrapin_channeler = Card("Terrapin Channeler", 2, "creep", is_deck=False)
blue_cards.append(terrapin_channeler)

wildwing = Card("Wildwing", 3, "creep", is_deck=False)
blue_cards.append(wildwing)



blue_signatures = []


barracks = Card("Barracks", 3, "improvement")
blue_signatures.append(barracks)

conspiracy_of_ravens = Card("Conspiracy of Ravens", 1, "creep")
blue_signatures.append(conspiracy_of_ravens)

diabolic_conclusion = Card("Diabolic Conclusion", 1, "spell")
blue_signatures.append(diabolic_conclusion)

divided_we_stand = Card("Divided We Stand", 3, "spell")
blue_signatures.append(divided_we_stand)

dragon_slave = Card("Dragon Slave", 3, "spell")
blue_signatures.append(dragon_slave)

echo_slam = Card("Echo Slam", 6, "spell")
blue_signatures.append(echo_slam)

eclipse = Card("Eclipse", 5, "spell")
blue_signatures.append(eclipse)

frostbite = Card("Frostbite", 2, "spell")
blue_signatures.append(frostbite)

ignite = Card("Ignite", 4, "spell")
blue_signatures.append(ignite)

laguna_blade = Card("Laguna Blade", 4, "spell")
blue_signatures.append(laguna_blade)

light_strike_array = Card("Light Strike Array", 2, "spell")
blue_signatures.append(light_strike_array)

mystic_flare = Card("Mystic Flare", 4, "spell")
blue_signatures.append(mystic_flare)

runic_instigation = Card("Runic Instigation", 2, "spell")
blue_signatures.append(runic_instigation)

sapphire_archon = Card("Sapphire Archon", 6, "creep")
blue_signatures.append(sapphire_archon)

sow_venom = Card("Sow Venom", 4, "spell", related=[plague_ward])
blue_signatures.append(sow_venom)

spark_wraith = Card("Spark Wraith", 2, "creep")
blue_signatures.append(spark_wraith)

spell_steal = Card("Spell Steal", 3, "spell")
blue_signatures.append(spell_steal)

thundergods_wrath = Card("Thundergod's Wrath", 6, "spell")
blue_signatures.append(thundergods_wrath)

void_theft = Card("Void Theft", 3, "spell", related=[eidolon])
blue_signatures.append(void_theft)




blue_heroes = []

arc_warden = Card("Arc Warden", 0, "hero", related=[spark_wraith])
blue_heroes.append(arc_warden)

crystal_maiden = Card("Crystal Maiden", 0, "hero", related=[frostbite])
blue_heroes.append(crystal_maiden)

earthshaker = Card("Earthshaker", 0, "hero", related=[echo_slam, rock])
blue_heroes.append(earthshaker)

imperia = Card("Imperia", 0, "hero", related=[conspiracy_of_ravens])
blue_heroes.append(imperia)

jmuy_the_wise = Card("J'Muy the Wise", 0, "hero", related=[runic_instigation])
blue_heroes.append(jmuy_the_wise)

kanna = Card("Kanna", 0, "hero", related=[diabolic_conclusion, hound_of_war])
blue_heroes.append(kanna)

#lina = Card("Lina", 0, "hero", related=[light_strike_array, dragon_slave, laguna_blade]) # TODO: fix things...
#blue_heroes.append(lina)

luna = Card("Luna", 0, "hero", related=[eclipse])
blue_heroes.append(luna)

meepo = Card("Meepo", 0, "hero", related=[divided_we_stand])
blue_heroes.append(meepo)

ogre_magi = Card("Ogre Magi", 0, "hero", related=[ignite])
blue_heroes.append(ogre_magi)

pierpont = Card("Pierpont", 0, "hero", related=[sapphire_archon])
blue_heroes.append(pierpont)

prellex = Card("Prellex", 0, "hero", related=[barracks, mega_creep])
blue_heroes.append(prellex)

rubick = Card("Rubick", 0, "hero", related=[spell_steal])
blue_heroes.append(rubick)

skywrath_mage = Card("Skywrath Mage", 0, "hero", related=[mystic_flare])
blue_heroes.append(skywrath_mage)

vanessa = Card("Vanessa", 0, "hero", related=[void_theft])
blue_heroes.append(vanessa)

venomancer = Card("Venomancer", 0, "hero", related=[sow_venom, plague_ward])
blue_heroes.append(venomancer)

zeus = Card("Zeus", 0, "hero", related=[thundergods_wrath])
blue_heroes.append(zeus)




arc_bolt = Card("Arc Bolt", 1, "spell")
blue_cards.append(arc_bolt)

cunning_plan = Card("Cunning Plan", 1, "spell")
blue_cards.append(cunning_plan)

determined_greevil = Card("Determined Greevil", 1, "creep")
blue_cards.append(determined_greevil)

fractured_timeline = Card("Fractured Timeline", 1, "improvement")
blue_cards.append(fractured_timeline)

lightning_strike = Card("Lightning Strike", 1, "spell")
blue_cards.append(lightning_strike)

ramp_bolt = Card("Ramp Bolt", 1, "spell")
blue_cards.append(ramp_bolt)

spitting_greevil = Card("Spitting Greevil", 1, "creep")
blue_cards.append(spitting_greevil)

ventriloquy = Card("Ventriloquy", 1, "spell")
blue_cards.append(ventriloquy)


agent_of_claszureme = Card("Agent of Claszureme", 2, "creep")
blue_cards.append(agent_of_claszureme)

better_late_than_never = Card("Better Late Than Never", 2, "spell", related=[terrapin_channeler])
blue_cards.append(better_late_than_never)

claddish_archivist = Card("Claddish Archivist", 2, "creep")
blue_cards.append(claddish_archivist)

compel = Card("Compel", 2, "spell")
blue_cards.append(compel)

doppelganger = Card("Doppelganger", 2, "creep")
blue_cards.append(doppelganger)

howling_mind = Card("Howling Mind", 2, "spell")
blue_cards.append(howling_mind)

leading_from_behind = Card("Leading from Behind", 2, "spell")
blue_cards.append(leading_from_behind)

path_of_the_wise = Card("Path of the Wise", 2, "improvement")
blue_cards.append(path_of_the_wise)

possessed_blade = Card("Possessed Blade", 2, "creep") # TODO: add short sword
blue_cards.append(possessed_blade)

relentless_zombie = Card("Relentless Zombie", 2, "creep") # TODO: add zombie
blue_cards.append(relentless_zombie)

tower_barrage = Card("Tower Barrage", 2, "spell")
blue_cards.append(tower_barrage)

unstable_elemental = Card("Unstable Elemental", 2, "creep")
blue_cards.append(unstable_elemental)

watchtower = Card("Watchtower", 2, "improvement")
blue_cards.append(watchtower)

whispers_of_madness = Card("Whispers of Madness", 2, "spell")
blue_cards.append(whispers_of_madness)


arcane_assault = Card("Arcane Assault", 2, "spell")
blue_cards.append(arcane_assault)

at_any_cost = Card("At Any Cost", 3, "spell")
blue_cards.append(at_any_cost)

body_modifications = Card("Body Modifications", 3, "spell")
blue_cards.append(body_modifications)

fell_spirit = Card("Fell Spirit", 3, "creep")
blue_cards.append(fell_spirit)

fog_of_war = Card("Fog of War", 3, "spell")
blue_cards.append(fog_of_war)

foresight = Card("Foresight", 3, "spell")
blue_cards.append(foresight)

maelrawn_pupate = Card("Maelrawn Pupate", 3, "creep", related=[spawn_of_maelrawn])
blue_cards.append(maelrawn_pupate)

objective_vision = Card("Objective Vision", 3, "spell")
blue_cards.append(objective_vision)

spirit_of_desolation = Card("Spirit of Desolation", 3, "creep")
blue_cards.append(spirit_of_desolation)

wildwing_bait = Card("Wildwing Bait", 3, "creep", related=[wildwing])
blue_cards.append(wildwing_bait)


aghanims_sanctum = Card("Aghanim's Sanctum", 4, "improvement")
blue_cards.append(aghanims_sanctum)

and_one_for_me = Card("...And One For Me", 4, "spell")
blue_cards.append(and_one_for_me)

mana_short = Card("Mana Short", 4, "spell")
blue_cards.append(mana_short)

mimicry = Card("Mimicry", 4, "spell")
blue_cards.append(mimicry)

morphling_whelp = Card("Morphling Whelp", 4, "creep")
blue_cards.append(morphling_whelp)

resonant_construct = Card("Resonant Construct", 4, "creep")
blue_cards.append(resonant_construct)

satyr_magician = Card("Satyr Magician", 4, "creep")
blue_cards.append(satyr_magician)

wall_of_secrets = Card("Wall of Secrets", 4, "creep")
blue_cards.append(wall_of_secrets)


call_the_reserves = Card("Call the Reserves", 5, "spell", related=[melee_creep])
blue_cards.append(call_the_reserves)

conflagration = Card("Conflagration", 5, "improvement")
blue_cards.append(conflagration)

defenstrating_ogre = Card("Defenstrating Ogre", 5, "creep")
blue_cards.append(defenstrating_ogre)

friendly_fire = Card("Friendly Fire", 5, "spell")
blue_cards.append(friendly_fire)

glyph_of_confusion = Card("Glyph of Confusion", 5, "improvement")
blue_cards.append(glyph_of_confusion)

keenfolk_golem = Card("Keenfolk Golem", 5, "creep")
blue_cards.append(keenfolk_golem)

remote_detonation = Card("Remote Detonation", 5, "spell")
blue_cards.append(remote_detonation)

sonic_bubble = Card("Sonic Bubble", 5, "spell")
blue_cards.append(sonic_bubble)

thunderstorm = Card("Thunderstorm", 5, "spell")
blue_cards.append(thunderstorm)

troll_soothsayer = Card("Troll Soothsayer", 5, "creep")
blue_cards.append(troll_soothsayer)

wave_of_madness = Card("Wave of Madness", 5, "spell")
blue_cards.append(wave_of_madness)


annihilation = Card("Annihilation", 6, "spell")
blue_cards.append(annihilation)

essence_font = Card("Essence Font", 6, "spell")
blue_cards.append(essence_font)


incarnation_of_selemene = Card("Incarnation of Selemene", 9, "creep")
blue_cards.append(incarnation_of_selemene)


bolt_of_damocles = Card("Bolt of Damocles", 10, "spell")
blue_cards.append(bolt_of_damocles)







blue_cards = blue_heroes + blue_signatures + blue_cards



signatures = neutral_signatures + red_signatures + blue_signatures + black_signatures + green_signatures




cards = neutral_cards + red_cards + blue_cards + black_cards + green_cards

card_string = ""




# Divide each colour into heroes, mana costs, etc.

max_mana = max(x.mana for x in cards)


ordered_slots = [[] for x in range(max_mana + 2)]


# The following is the ordering of how they will appear!
for colour in [neutral_cards, red_cards, blue_cards, black_cards, green_cards]:
    heroes = [x for x in colour if x.kind == "hero"]
    ordered_slots[0] += heroes
    for i in range(max_mana + 1):
        mana_sorted = [x for x in colour if x.kind != "hero" and x.mana == i]
        mana_sorted.sort()
        ordered_slots[i + 1] += mana_sorted

ordered_cards = [item for sublist in ordered_slots for item in sublist]


# Sort the items....
max_cost = max(x.mana for x in item_cards)
ordered_slots = [[] for x in range(max_cost + 1)]
for i in range(max_cost + 1):
    cost_sorted = [x for x in item_cards if x.mana == i]
    cost_sorted.sort()
    ordered_slots[i] = cost_sorted

ordered_items = [item for sublist in ordered_slots for item in sublist]
ordered_cards += ordered_items



for card in ordered_cards:
    if card.is_deck == False: continue
    if card in signatures: continue

    relateds = []

    if card.related_cards:
        relateds = [card]
        to_search = card.related_cards + [card]

        while set(relateds) != set(to_search):
            for i in range(len(to_search)):
                if to_search[i] not in relateds:
                    card_to_search = to_search[i]
                    relateds.append(to_search[i])
            if card_to_search.related_cards:
                for c in card_to_search.related_cards:
                    if c not in to_search:
                        to_search.append(c)

        relateds = relateds[1:]


    if card in blue_cards:
        colour = "blue"
    elif card in red_cards:
        colour = "red"
    elif card in neutral_cards:
        colour = "neutral"
    elif card in green_cards:
        colour = "green"
    elif card in black_cards:
        colour = "black"
    else:
        colour = "none"

    card_string += "<div class=\"card colour-" + colour + " type-" + card.kind + "\" "
    if len(relateds) == 0:
        card_string += "onclick=\"toggle_card('" + card.get_image_name() + "');\">\n"
    elif len(relateds) == 1:
        card_string += "onclick=\"toggle_card2('" + card.get_image_name() + "', '" + relateds[0].get_image_name() + "');\">\n"
    elif len(relateds) == 2:
        card_string += "onclick=\"toggle_card3('" + card.get_image_name() + "', '" + relateds[0].get_image_name() + "', '" + relateds[1].get_image_name() + "');\">\n"
    else:
        print("Error with card:", card)
        print(relateds)
    card_string += "<div class=\"card-info type\">\n"

    if card.kind == "hero":
        card_string += "<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 250 300\" style=\"enable-background:new 0 0 250 300; width:20px;\" xml:space=\"preserve\">\n"
        card_string += "<g>\n"
        card_string += "<g>\n"
        card_string += "<path d=\"M204,117.2c-22.5,1.2-41.6,7.9-60.8,12.5c-9.2,22.1,10.4,51.3-17.4,68.5c-13.9-6.6-17.9-17-16.8-30.9\n"
        card_string += "c1-11.7,0.2-23.6,0.2-36.5c-20.4-6.6-40.4-11.2-63-14.6c0,13.2,0.5,24.4-0.2,35.4c-0.6,8.7,3.2,14,10.6,16.7\n"
        card_string += "c17.2,6.2,22.5,18.7,23,36.3c0.9,28.8,4,57.4,6.5,89.9c-25.3-18.2-44.5-37.6-64.7-55.9c-5-4.6-3.1-11.2-3.1-16.9\n"
        card_string += "c-0.1-38.2,2.2-76.6-0.6-114.5C14.3,59.7,51.6,20,95,7.6c49.8-14.3,102.8,8.5,128,53.7c5.8,10.5,9.2,21.4,9,33.8\n"
        card_string += "c-0.4,42.1-0.4,84.3,0,126.4c0.1,9.9-2.3,17.2-10.3,23.8c-18.2,15-35.4,31.2-57.3,50.9c2-30.6,4.2-56.3,5.2-81.9\n"
        card_string += "c0.8-21,2.8-40.4,27.2-48.3c11.2-3.6,6.5-14.4,7.1-22.3C204.5,135.3,204,126.8,204,117.2z\"></path>\n"
        card_string += "</g>\n"
        card_string += "</g>\n"
        card_string += "</svg>\n"

    elif card.kind == "creep":
        card_string += "<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 150 150\" style=\"enable-background:new 0 0 150 150; width:20px;\" xml:space=\"preserve\">\n"
        card_string += "<g>\n"
        card_string += "<path d=\"M141.2,42.9c-6.5-16.3-18.4-30.4-33.3-39.7c-6.4,21.5-17.4,40.9-32.7,57.4c-15.2-16.3-26.4-36-32.8-57.4\n"
        card_string += "C27.1,12.8,14.9,27.4,8.6,44.2C3.8,56.5,2.2,69.8,3.5,82.9c13.5,8.9,27,18.4,38.8,29.5c9.6,9.1,15.1,20.9,16.2,34.1\n"
        card_string += "c11.1,0,22.1,0,33.2,0c1.1-13.1,6.6-25,16.2-34.1c11.8-11.1,25.3-20.6,38.8-29.5C148.1,69.3,146.3,55.6,141.2,42.9z M61.6,92.6\n"
        card_string += "c-4.5,5-11.6,6.7-18.1,5c-5.9-1.8-11.3-4.3-15.1-9.3C24.2,83,23,76.2,24.3,69.6c8.5-2.4,17.7-1.9,25.8,1.6\n"
        card_string += "c6.4,2.7,11.8,7.1,16,12.6C65.2,87.1,63.9,90.1,61.6,92.6z M124,84.9c-3.8,7.6-12.7,12.3-20.9,13.3c-9.2,0.7-16.9-5.5-19-14.3\n"
        card_string += "c4.3-5.7,10-10.3,16.6-12.9c8-3.3,16.9-3.6,25.2-1.3C126.9,74.9,126.5,80.2,124,84.9z\"></path>\n"
        card_string += "</g>\n"
        card_string += "</svg>\n"

    elif card.kind == "spell":
        card_string += "<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 150 150\" style=\"enable-background:new 0 0 150 150; height:30px; margin-left: -5px; margin-right: -5px;\" xml:space=\"preserve\">\n"
        card_string += "<g>\n"
        card_string += "<path d=\"m 65.489718,107.42015 -8.00013,-20.175073 -17.08105,-5.044193 c -9.39458,-2.77429 -17.08104,-5.622433 -17.08104,-6.329207 0,-0.706775 7.73079,-3.607538 17.17954,-6.446191 l 17.17954,-5.161175 7.95875,-20.929754 c 4.37733,-11.511387 8.56393,-20.929791 9.30356,-20.929791 0.73963,0 4.99274,9.472263 9.4513,21.049437 l 8.10646,21.049437 17.082922,5.044755 c 9.39564,2.774591 17.08293,5.621532 17.08293,6.326508 0,0.705011 -7.68647,3.551691 -17.08105,6.325981 l -17.081051,5.044193 -8.00013,20.175073 c -4.40009,11.0963 -8.67967,20.17508 -9.51026,20.17508 -0.83058,0 -5.110201,-9.07878 -9.510291,-20.17508 z\"></path>\n"
        card_string += "</g>\n"
        card_string += "</svg>\n"

    elif card.kind == "improvement":
        card_string += "<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 150 150\" style=\"enable-background:new 0 0 150 150; width:20px;\" xml:space=\"preserve\">\n"
        card_string += "<path d=\"M16.7,2.1C26,1.9,35.4,2,44.7,2.1c0.1,8.2-0.1,16.3,0.1,24.4c4.8,0.1,9.7,0.1,14.5,0c0.1-7.8-0.1-15.7,0.1-23.5\n"
        card_string += "c10.3-0.1,20.7-0.1,31,0c0.1,7.8-0.1,15.7,0.1,23.5c4.8,0.1,9.7,0.1,14.5,0c0.1-8.2-0.1-16.3,0.1-24.4c9.3-0.1,18.7-0.1,28.1,0\n"
        card_string += "c0.1,39.9,0,79.8,0.1,119.7c-0.1,1.5,0.2,2.7-1,3.7c-15.1,15-36.5,23.6-58.2,23.5c-18.4-0.5-36.6-7-50.7-18.6\n"
        card_string += "c-2.2-1.9-4.7-3.7-6.4-6.1c-0.2-1.5-0.2-3-0.2-4.5C16.7,80.7,16.5,41.2,16.7,2.1L16.7,2.1z\"></path>\n"
        card_string += "</svg>\n"

    elif card.kind == "consumable":
        card_string += "<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 150 150\" style=\"enable-background:new 0 0 150 150; width:20px;\" xml:space=\"preserve\">\n"
        card_string += "<path d=\"m 75.000002,21.689455 c -9.911331,0 -10.747873,0.158031 -13.044922,2.455078 -1.35,1.35 -2.455078,2.731027 -2.455078,3.070313 0,1.211081 2.883884,3.474609 4.427734,3.474609 1.323811,0 1.572266,1.575758 1.572266,10 v 8.832031 a 40.646027,39.971878 0.00405846 0 0 -4.376953,1.285157 c -0.728257,0.118793 -1.291625,0.319276 -1.509766,0.568359 A 40.646027,39.971878 0.00405846 0 0 41.033205,66.443361 c -0.413295,0.541955 -0.765571,1.106089 -1.060547,1.699219 a 40.646027,39.971878 0.00405846 0 0 -5.61914,20.189453 40.646027,39.971878 0.00405846 0 0 40.640625,39.978507 40.646027,39.971878 0.00405846 0 0 40.652337,-39.966788 40.646027,39.971878 0.00405846 0 0 -5.57617,-20.115235 c -0.23937,-0.49281 -0.51287,-0.967916 -0.83203,-1.423828 A 40.646027,39.971878 0.00405846 0 0 96.859377,54.691408 c -0.275201,-0.177286 -0.550813,-0.346421 -0.826172,-0.5 -0.01425,-0.0079 -0.02873,-0.01751 -0.04297,-0.02539 A 40.646027,39.971878 0.00405846 0 0 90.369143,51.357424 C 90.128919,51.103551 89.539566,50.897709 88.77344,50.785158 a 40.646027,39.971878 0.00405846 0 0 -4.273438,-1.263672 v -8.832031 c 0,-8.424242 0.248456,-10 1.572266,-10 1.54385,0 4.427734,-2.263528 4.427734,-3.474609 0,-0.339286 -1.105075,-1.720313 -2.455078,-3.070313 -2.29705,-2.297047 -3.133583,-2.455078 -13.044922,-2.455078 z\"></path>"
        card_string += "</svg>\n"

    elif card.kind == "weapon":
        card_string += "<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 150 150\" style=\"enable-background:new 0 0 150 150; width:20px;\" xml:space=\"preserve\">\n"
        card_string += "<path d=\"m 22.143771,121.68765 1.92659,-8.64633 L 37.28518,98.582015 C 55.26548,78.908439 55.595461,78.477236 53.884735,76.890553 42.486462,66.318755 32.58061,58.092155 32.291932,58.958188 c -0.200232,0.600696 -0.928625,1.864266 -1.61865,2.807931 -1.090063,1.490751 -1.642681,1.548365 -4.213936,0.439329 -1.62764,-0.702034 -3.103239,-1.366702 -3.279107,-1.47704 C 22.635394,60.386581 27.1007,52.004426 29.614221,48.650706 30.9264,46.899903 32,44.969814 32,44.361619 32,42.079662 22.516033,31.404326 20.806817,31.762357 c -0.931251,0.195069 -2.480994,-0.515849 -3.443874,-1.579819 -1.688321,-1.865574 -1.585,-2.100181 2.900215,-6.585396 4.520171,-4.520171 4.706436,-4.60065 6.626434,-2.863076 1.086542,0.983307 1.755385,2.361518 1.486319,3.062693 -0.277261,0.72253 2.399672,3.573617 6.178747,6.580718 5.491181,4.369464 6.957158,5.104362 8.30665,4.164139 3.570151,-2.48741 11.756507,-7.019527 13.779461,-7.628564 1.764799,-0.531316 2.341099,-0.06983 3.281479,2.627722 0.62738,1.799725 0.74035,3.405677 0.25104,3.568782 -0.48932,0.163105 -1.64658,0.850026 -2.57171,1.526492 -1.496927,1.094581 -0.69215,2.328683 7.31279,11.213936 4.94715,5.4912 9.48569,9.984 10.08563,9.984 0.59995,0 5.13848,-4.4928 10.08564,-9.984 8.00493,-8.885253 8.80971,-10.119355 7.31278,-11.213936 -0.92512,-0.676466 -2.08239,-1.363387 -2.5717,-1.526492 -0.48932,-0.163105 -0.37635,-1.769057 0.25104,-3.568782 1.50261,-4.310399 2.73598,-3.954082 16.563492,4.785166 1.96132,1.239589 2.70138,0.907612 8.80665,-3.950503 3.77751,-3.005849 6.45344,-5.856171 6.17619,-6.578678 -0.26907,-0.701175 0.39978,-2.079386 1.48632,-3.062693 1.92,-1.737574 2.10626,-1.657095 6.62643,2.863076 4.48522,4.485215 4.58854,4.719822 2.90022,6.585396 -0.96288,1.06397 -2.51263,1.774888 -3.44388,1.579819 C 127.48397,31.404326 118,42.079662 118,44.361619 c 0,0.608195 1.0736,2.538284 2.38578,4.289087 2.51352,3.35372 6.97883,11.735875 6.43398,12.077702 -0.17587,0.110338 -1.65147,0.775006 -3.27911,1.47704 -2.57125,1.109036 -3.12387,1.051422 -4.21393,-0.439329 -0.69003,-0.943665 -1.41354,-2.192607 -1.60782,-2.775427 -0.3219,-0.965695 -22.703272,18.132852 -22.714192,19.382548 -0.003,0.29659 6.958592,8.236798 15.469302,17.644905 l 15.47401,17.105645 1.9174,8.6051 c 2.22743,9.99649 3.05606,9.32492 -9.24779,7.49495 l -7.46406,-1.11014 -17.776792,-15.88986 c -9.77723,-8.73942 -18.04678,-15.889855 -18.37678,-15.889855 -0.32999,0 -8.59954,7.150435 -18.376778,15.889855 l -17.776791,15.88986 -7.464062,1.11014 c -12.305747,1.83025 -11.476388,2.50678 -9.238596,-7.53619 z\"></path>"
        card_string += "</svg>\n"

    elif card.kind == "armor":
        card_string += "<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 150 150\" style=\"enable-background:new 0 0 150 150; width:20px;\" xml:space=\"preserve\">\n"
        card_string += "<path d=\"M 54.311175,116.18667 C 43.746206,110.27388 34.861679,105.19568 34.567783,104.90179 34.273887,104.60789 31.624605,90.151562 28.680489,72.776615 l -5.352937,-31.590812 3.228269,-0.605627 c 5.31643,-0.997368 10.968207,-5.845793 13.972568,-11.986486 l 2.726523,-5.572811 h 31.765296 31.765302 l 2.72652,5.572811 c 3.00039,6.132566 8.65499,10.988901 13.95236,11.982695 l 3.20806,0.601835 -4.77742,28.67133 c -2.62758,15.769231 -5.03896,30.103061 -5.35861,31.85296 -0.53834,2.94709 -2.04817,3.99753 -20.482102,14.25 -10.9455,6.0876 -20.49338,11.04954 -21.21751,11.02653 -0.72413,-0.023 -9.96066,-4.87959 -20.525633,-10.79237 z\"></path>"
        card_string += "</svg>\n"

    elif card.kind == "accessory":
        card_string += "<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 150 150\" style=\"enable-background:new 0 0 150 150; width:20px;\" xml:space=\"preserve\">\n"
        card_string += "<path d=\"M 67.856107,124.58868 C 52.376512,113.79373 37.500208,99.099601 29.68944,86.889398 16.574493,66.387439 16.911556,46.006952 30.611378,31.144399 41.582138,19.24253 59.293637,18.012322 73.033107,28.197862 c 1.92035,1.423619 2.30782,1.382309 4.70251,-0.501355 8.771177,-6.899414 22.197772,-8.422106 31.995423,-3.628562 9.81102,4.800088 17.44214,15.339887 19.61438,27.090614 3.43004,18.554762 -8.89705,41.790969 -32.987291,62.180121 -9.608075,8.13194 -19.698212,15.37547 -21.417802,15.37547 -0.64264,0 -3.83054,-1.85646 -7.08422,-4.12547 z\"></path>"
        card_string += "</svg>\n"


    card_string += "</div>\n"
    if card.mana == 0:
        card_string += "<div class=\"card-info cost\"> - </div>\n"
    else:
        card_string += "<div class=\"card-info cost\">" + str(card.mana) + "</div>\n"
    card_string += "<div class=\"card-info name\">" + card.name + "</div>\n"
    card_string += "</div>\n"






with open("base.html", "r") as file:
        filedata = file.read()

filedata = filedata.replace("<++>", card_string)

with open("index.html", "w") as file:
    file.write(filedata)

