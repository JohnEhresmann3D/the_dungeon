import random

from collections import namedtuple
from enum import IntEnum
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

class Class_Information():
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
    Character_Races = namedtuple('RacialInfo', ['name', 'str', 'dex', 'con', 'int', 'wis', 'cha'])
    default_race = Character_Races('<default race>', 0, 0, 0, 0, 0, 0)
    

    human_race = default_race._replace(name = "Human")
    elf_race = default_race._replace(name = 'Elf', str = -1, dex = 2, int = +1 )
    dwarf_race = default_race._replace(name = "Dwarf", str = 2, con = 2, cha = -2, int = -2)
    gnome_race = default_race._replace(name="Gnome", str = -2, dex = +2)
    drow_race = default_race._replace(name = "Drow", cha = 2, dex = 2, str = -2, con = -2)


    possibleRaces = {Race_Options.Human : human_race, Race_Options.Elf : elf_race, Race_Options.Dwarf : dwarf_race, Race_Options.Gnome : gnome_race, Race_Options.Drow : drow_race}


class Actor():
    actor_stats = {}
    
    #setting stats
    actor_stats[Stats.Str] = 0
    actor_stats[Stats.Dex] = 0
    actor_stats[Stats.Con] = 0
    actor_stats[Stats.Int] = 0
    actor_stats[Stats.Wis] = 0
    actor_stats[Stats.Cha] = 0

class Player_Actor(Actor):

    #class variables
    class_information = Class_Information()
    race_information = Race_Information()

    character_race = ""

    dice_roll = [0,0,0,0]

    def Stat_Roll(self,player_input):
        self.player_input = player_input

        self.valid_input = False
        while(self.valid_input != True):

            if(self.player_input == 1):
                
                for key in self.actor_stats.keys():
                    dice_roll = random.sample(range(1,6), 3)
                    self.actor_stats[key] = sum(dice_roll)
                    self.valid_input = True
            
            if(self.player_input == 2):

                for key in self.actor_stats.keys():
                    dice_roll = random.sample(range(1,6),4)
                    self.actor_stats[key] = sum(dice_roll) - min(dice_roll)
                    self.valid_input = True
                
            if(self.player_input == 3):
                for key in self.actor_stats.keys():
                    self.actor_stats[key] = random.randint(1,6) + 8
                    self.valid_input = True
            
            if(self.player_input == 4):
                for key in self.actor_stats.keys():
                    self.actor_stats[key] = random.randint(1,20)
                    self.valid_input = True
    
    def Race_Selection(self,player_input):
        self.player_input = player_input
        
        selected_race = self.race_information.possibleRaces.get(self.player_input)

        self.character_race = getattr(selected_race, 'name')
        index = 1

        for key in self.actor_stats.keys():
            self.actor_stats[key] = self.actor_stats[key] + selected_race[index]
            index += 1
    
    def Character_Sheet(self):
        print("Race: " + self.character_race + "\n")
        for key in self.actor_stats.keys():
            print(key.name + ":" + str(self.actor_stats[key]))
        

        
                

class User_Requests():

    class_information = Class_Information()
    race_information = Race_Information()

    def Stat_Request(self):
        
        print("How would you like to enter have your characters stats generated?\n 1.Roll 3d6\n2.Roll 4d6 and drop the lowest\n3.Roll 1d6 and add 8\n 4.Roll 1d20\n")

        is_valid = False
        while(is_valid != True):
        
            player_input = int(input("Please enter 1,2,3, or 4 to make your selection "))
            if (player_input == 1 or player_input == 2 or player_input == 3 or player_input == 4):
                is_valid = True
            else:
                print("Please enter a valid selection\n")

        return player_input

    def Race_Request(self):
        print("With the dice falling into their place, the time has come to select a race.")

        is_valid = False
        while(is_valid != True):

            player_input = str(input("Please enter in 'Human', 'Elf', 'Dwarf', 'Gnome', or 'Golem' "))
            for key in self.race_information.possibleRaces.keys():
                if (player_input.lower() == key.name.lower()):
                    is_valid = True
                    return key
            
            if (is_valid == False):
                print("Please try again\n")
    
    def Class_Request(self):
        print("stuff happened")

                    
            


          
        
class Game_Driver():
    
    user_reqests = User_Requests()
    test_actor = Player_Actor()

    player_input = user_reqests.Stat_Request()
    test_actor.Stat_Roll(player_input)
    
    player_input = user_reqests.Race_Request()
    test_actor.Race_Selection(player_input)

    test_actor.Character_Sheet()
            
            


    

input()

