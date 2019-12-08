from request_logic import User_Requests
from player_actor import Player_Actor

class Game_Start():

    def Character_Initialize(self, player_actor = Player_Actor()):
    
        print("Welcome to 'THE DUNGEON', a dungeon crawling adventure. Let's get started")
        
        player_input = User_Requests().Stat_Request()
        player_actor.Stat_Roll(player_input)
        
        player_input = User_Requests().Race_Request()
        player_actor.Race_Selection(player_input)

        player_input = User_Requests().Class_Request()
        player_actor.Class_Selection(player_input)

        player_actor.Character_Sheet()