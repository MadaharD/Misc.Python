import random as rand
#list of the three choices
choice_list : list = ["Rock","Paper","Scissors"]

#Function for the game
def RPS_game(game_status):
     #setting the scores for player and computer
     comp_score : int = 0
     player_score : int = 0
     while game_status == "Y":
        #computer chooses a random option and player types their choice
        comp_choice = choice_list[rand.randint(0,2)]
        player_choice = input("Choose Rock, Paper, or Scissors: ").upper()
        # all the possible iterations and their results(Print winner and update score)
        if player_choice == "ROCK" and comp_choice == "Scissors":
            print("You win!")
            player_score += 1
        elif player_choice == "ROCK" and comp_choice == "Paper":
            print("The Computer wins!")
            comp_score += 1
        elif player_choice == "PAPER" and comp_choice == "Scissors":
            print("The Computer wins!")
            comp_score += 1
        elif player_choice == "PAPER" and comp_choice == "Rock":
            print("you win!")
            player_score += 1
        elif player_choice == "SCISSORS" and comp_choice == "Rock":
            print("The computer wins!")
            comp_score += 1
        elif player_choice == "SCISSORS" and comp_choice == "Paper":
            print("you win!")
            player_score += 1
        else:
            print("It's a tie!")
        # prints scores + what both player and computer chose
        print(player_choice.capitalize() + " vs " + comp_choice + "!")
        print("Your score is: " + str(player_score))
        print("The computer's score is: " + str(comp_score))
        #checks if player wants to play again
        game_status = input("Would you like to play again:\nY/N: ").upper()
     if game_status == "N":
         print("Ok, see you later!")
    

#decides if the player wants to play or not
game_status : str = input("Would you like to play Rock Paper Scissors?\nY/N: ").upper()

#if the player wants to play, the game commences
if game_status == "Y":
   RPS_game(game_status)
else:
   print("Ok, maybe another time!")
