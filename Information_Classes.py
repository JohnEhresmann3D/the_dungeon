from collections import namedtuple
from Character_Options import Class_Options
from Character_Options import Race_Options

class Class_Information():
    #Using namedtuples  here for ease of readability, and because this information should never be changed so immutability isn't a problem.
    #Each class should have a name and a hit dice associated with it at the moment. More to potentially come soon
    character_class = namedtuple('ClassInfo', ['name', 'hit_dice'])
    default_class = character_class('default class', 0)
    
    fighter_class = default_class._replace(name = "Fighter", hit_dice = 10)
    cleric_class = default_class._replace(name = "Cleric", hit_dice = 8)
    wizard_class = default_class._replace(name = "Wizard", hit_dice = 4)
    paladin_class = default_class._replace(name = "Paladin", hit_dice = 12)
    rogue_class = default_class._replace(name = "Rogue", hit_dice = 6)

    potential_classes = {Class_Options.Fighter : fighter_class, Class_Options.Cleric : cleric_class, Class_Options.Wizard : wizard_class, 
                        Class_Options.Paladin : paladin_class, Class_Options.Rogue : rogue_class}

class Race_Information():
    
    #Using namedtuples  here for ease of readability, and because this information should never be changed so immutability isn't a problem.
    #Each race currently has a name, and one of a few potential stat modifiers.
    Character_Races = namedtuple('RacialInfo', ['name', 'str', 'dex', 'con', 'int', 'wis', 'cha'])
    default_race = Character_Races('<default race>', 0, 0, 0, 0, 0, 0)
    

    human_race = default_race._replace(name = "Human")
    elf_race = default_race._replace(name = 'Elf', str = -1, dex = 2, int = +1 )
    dwarf_race = default_race._replace(name = "Dwarf", str = 2, con = 2, cha = -2, int = -2)
    gnome_race = default_race._replace(name="Gnome", str = -2, dex = +2)
    drow_race = default_race._replace(name = "Drow", cha = 2, dex = 2, str = -2, con = -2)


    possibleRaces = {Race_Options.Human : human_race, Race_Options.Elf : elf_race, Race_Options.Dwarf : dwarf_race, Race_Options.Gnome : gnome_race, Race_Options.Drow : drow_race}

