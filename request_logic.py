from Information_Classes import Class_Information
from Information_Classes import Race_Information

class User_Requests():

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
            for key in Race_Information.possibleRaces.keys():
                if (player_input.lower() == key.name.lower()):
                    is_valid = True
                    return key
            
            if (is_valid == False):
                print("Please try again\n")
    
    def Class_Request(self):
        print("And now at last, it is time to pick your class")

        is_valid = False
        while(is_valid != True):

            player_input = str(input("Please enter 'Fighter', 'Cleric', 'Paladin', 'Wizard', or 'Rogue' "))
            for key in Class_Information.potential_classes.keys():
                if(player_input.lower() == key.name.lower()):
                    is_valid = True
                    return key
            
            if(is_valid == False):
                print("Invalid selection, please try again")