from player_actor import Player_Actor
from request_logic import User_Requests

       

class Game_Driver():
    
    user_reqests = User_Requests()
    test_actor = Player_Actor()

    player_input = user_reqests.Stat_Request()
    test_actor.Stat_Roll(player_input)
    
    player_input = user_reqests.Race_Request()
    test_actor.Race_Selection(player_input)

    player_input = user_reqests.Class_Request()
    test_actor.Class_Selection(player_input)

    test_actor.Character_Sheet()
            
            


    

input()

