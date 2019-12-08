import random

from actor import Actor
from collections import namedtuple
from Information_Classes import Race_Information
from Information_Classes import Class_Information
from Character_Options import Stats
from Character_Options import Race_Options
from Character_Options import Class_Options
from request_logic import User_Requests

class Player_Actor(Actor):

    #class variables

    character_race = ""
    character_class = ""
    character_name = ""
    character_gold = ""
    character_level = ""
    character_experience = ""

    dice_roll = [0,0,0,0]

    def Stat_Roll(self,player_input):
        self.player_input = player_input

        self.valid_input = False
        while(self.valid_input != True):

            #1. Should be roll 3d6
            if(self.player_input == 1):
                
                for key in self.actor_stats.keys():
                    dice_roll = random.sample(range(1,6), 3)
                    self.actor_stats[key] = sum(dice_roll)
                    self.valid_input = True
            
            #2 should be roll 4d6 and we drop the lowest
            if(self.player_input == 2):

                for key in self.actor_stats.keys():
                    dice_roll = random.sample(range(1,6),4)
                    self.actor_stats[key] = sum(dice_roll) - min(dice_roll)
                    self.valid_input = True
                
            #3 should be roll 1d6 and add 8
            if(self.player_input == 3):
                for key in self.actor_stats.keys():
                    self.actor_stats[key] = random.randint(1,6) + 8
                    self.valid_input = True
            
            #4 should be roll 1d20
            if(self.player_input == 4):
                for key in self.actor_stats.keys():
                    self.actor_stats[key] = random.randint(1,20)
                    self.valid_input = True
    
    def Race_Selection(self,player_input):
        self.player_input = player_input
        
        #Taking the key that was returned from the players selection earlier and using that to set the race by searching our stored race information
        selected_race = Race_Information.possibleRaces.get(self.player_input)

        #this is potentially not as efficient as it could be, but for the time being setting the name of the race stored in the player_actor to the one we've obtained
        self.character_race = getattr(selected_race, 'name')
        index = 1

        #Cycling through our stats to adjust based on the selected race
        for key in self.actor_stats.keys():
            self.actor_stats[key] = self.actor_stats[key] + selected_race[index]
            index += 1
    
    def Class_Selection(self,player_input):
        self.player_input = player_input

        selected_class = Class_Information.potential_classes.get(self.player_input)

        self.character_class = getattr(selected_class, "name")
        self.actor_hit_dice = getattr(selected_class, "hit_dice")

        self.actor_hit_points = random.randint(1, self.actor_hit_dice)

    
    def Character_Sheet(self):
        print("Race: " + self.character_race + " Class: " + self.character_class + "\n")
        print( "Hit Dice: " + str(self.actor_hit_dice) + " HP : " + str(self.actor_hit_points))
        for key in self.actor_stats.keys():
            print(key.name + ":" + str(self.actor_stats[key]))                   