import random
from Information_Classes import Class_Information
from Information_Classes import Race_Information
from player_actor import Player_Actor

class Character_Creation():
    dice_roll = [0,0,0,0]
    player_input = ""

    def Stat_Roll(self,player_choice,player_actor=Player_Actor()):
        character_actor = player_actor
        
        player_input = player_choice

        valid_input = False
        while(valid_input != True):

            #1. Should be roll 3d6
            if(player_input == 1):
                
                for key in character_actor.actor_stats.keys():
                    dice_roll = random.sample(range(1,6), 3)
                    player_actor.actor_stats[key] = sum(dice_roll)
                    valid_input = True
            
            #2 should be roll 4d6 and we drop the lowest
            if(player_input == 2):

                for key in character_actor.actor_stats.keys():
                    dice_roll = random.sample(range(1,6),4)
                    character_actor.actor_stats[key] = sum(dice_roll) - min(dice_roll)
                    valid_input = True
                
            #3 should be roll 1d6 and add 8
            if(player_input == 3):
                for key in character_actor.actor_stats.keys():
                    character_actor.actor_stats[key] = random.randint(1,6) + 8
                    valid_input = True
            
            #4 should be roll 1d20
            if(player_input == 4):
                for key in character_actor.actor_stats.keys():
                    character_actor.actor_stats[key] = random.randint(1,20)
                    valid_input = True
            
            return character_actor.actor_stats
    
    def Race_Selection(self,player_input, **player_stats):
        actor_stats = player_stats
        self.player_input = player_input
        
        #Taking the key that was returned from the players selection earlier and using that to set the race by searching our stored race information
        selected_race = Race_Information.possibleRaces.get(self.player_input)

        #this is potentially not as efficient as it could be, but for the time being setting the name of the race stored in the player_actor to the one we've obtained
        self.character_race = getattr(selected_race, 'name')
        index = 1

        #Cycling through our stats to adjust based on the selected race
        for key in actor_stats.keys():
            actor_stats[key] = actor_stats[key] + selected_race[index]
            index += 1
        return actor_stats
    
    def Class_Selection(self,player_input):
        self.player_input = player_input

        selected_class = Class_Information.potential_classes.get(self.player_input)

        self.character_class = getattr(selected_class, "name")
        self.actor_hit_dice = getattr(selected_class, "hit_dice")

        self.actor_hit_points = random.randint(1, self.actor_hit_dice)

    
              