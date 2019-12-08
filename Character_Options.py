from enum import Enum

class Stats(Enum):
    Str = 1
    Dex = 2
    Con = 3
    Int = 4
    Wis = 5
    Cha = 6

class Race_Options(Enum):
    Human = 1
    Elf = 2
    Dwarf = 3
    Gnome = 4
    Golem = 5
    Drow = 6

class Class_Options(Enum):
    Fighter = 1
    Cleric = 2
    Wizard = 3
    Paladin = 4
    Rogue = 5