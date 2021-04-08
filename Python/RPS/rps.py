#Final Project for INFOTC 1040

#Import random for computer choice, sys for exit()
import random
import sys

def gameplay(total_games):
    #Function for the game proper
    #Returns 1 for win, 2 for loss, 3 for tie
    #If the user inputs an integer that isn't valid, returns False
    
    #Present game options to player
    print('Round {}'.format(int(total_games)+1))
    print('\n  1. Rock')
    print('  2. Paper')
    print('  3. Scissors')

    #Recieve player choice and make sure it works
    while True:
        try:
            player_choice = int(input('\nWhat will it be? '))
            if player_choice > 3 or player_choice < 1:
                print('Please choose one of the given options.')
                continue
            break
        except ValueError:
            print('Please only input a valid number.')

    #Calculate computer choice
    computer_choice = random.randint(1,3)

    #Compare player's and computer's choices

    #Check for tie
    if player_choice == computer_choice:
        result = 'tied'
    #Main checks
    if player_choice == 1:
        if computer_choice == 2:
            result = 'lose'
        elif computer_choice == 3:
            result = 'win'
    elif player_choice == 2:
        if computer_choice == 1:
            result = 'win'
        elif computer_choice == 3:
            result = 'lose'
    elif player_choice == 3:
        if computer_choice == 1:
            result = 'lose'
        elif computer_choice == 2:
            result = 'win'
        
    #Print result to the user
    #User
    if player_choice == 1:
        player_obj = 'Rock'
    elif player_choice == 2:
        player_obj = 'Paper'
    elif player_choice == 3:
        player_obj = 'Scissors'
    #Computer
    if computer_choice == 1:
        computer_obj = 'Rock'
    elif computer_choice == 2:
        computer_obj = 'Paper'
    elif computer_choice == 3:
        computer_obj = 'Scissors'

    print('You chose ' + player_obj + '. The computer chose ' + computer_obj + '. You ' + result + '!')
    input('Press enter to continue. ')
    
    #Return result
    if result == 'win':
        return 1
    elif result == 'lose':
        return 2
    elif result == 'tied':
        return 3

def main():
    #The main function for the program

    #MAIN MENU
    while True:
        #Main menu text
        print('Welcome to Rock, Paper, Scissors!')
        print('\n  1. Start New Game')
        print('  2. Load Game')
        print('  3. Quit')

        #Recieve player input and convert it to int
        while True:
            try:
                main_menu_choice = int(input('\nEnter choice: '))
                if main_menu_choice > 3 or main_menu_choice < 1:
                    print('Please select one of the given options.')
                    continue
                break
            except ValueError:
                print('Please input a valid number.')

        #Check user input and perform the three possible options

        #New Game
        if main_menu_choice == 1:
            #Declare user stats variables as 0 and get name
            user_name = input('What is your name? ')
            user_wins = 0
            user_loss = 0
            user_tie = 0
            total_games = 0
            #Greet user
            print("Hello {}. Let's play!".format(user_name))
            break
        #Load Game
        elif main_menu_choice == 2:
            #Get user's name
            user_name = input('What is your name? ')
            #Open the file and get stats
            try:
                with open(user_name + '.rps', 'r') as file:
                    stats = file.readlines()
                stats = [x.strip() for x in stats] 
                user_wins = int(stats[1])
                user_loss = int(stats[2])
                user_tie = int(stats[3])
                total_games = user_wins + user_loss + user_tie
            except:
                print('{}, your game could not be found.'.format(user_name))
                input('Press enter to continue.')
                continue
            print("Welcome back {}. Let's play!".format(user_name))
            break
        #Quit
        elif main_menu_choice == 3:
            sys.exit()

    #GAMEPLAY

    #Run game once before menu loop
    game_result = gameplay(total_games)

    #Update statistics
    if game_result == 1:
        user_wins += 1
    elif game_result == 2:
        user_loss += 1
    elif game_result == 3:
        user_tie += 1
    total_games += 1

    #Menu loop
    while True:
        #Menu Text
        print('What would you like to do?')
        print('\n  1. Play Again')
        print('  2. View Statistics')
        print('  3. Quit')

        #User input for menu
        while True:
            try:
                game_menu_input = int(input('\nEnter choice: '))

                if game_menu_input < 1 or game_menu_input > 3:
                    print('Please select one of the given options.')
                    continue
                break
            except ValueError:
                print('Please only print a number')

        #Play again
        if game_menu_input == 1:
            game_result = gameplay(total_games)

            #Update statistics
            if game_result == 1:
                user_wins += 1
            elif game_result == 2:
                user_loss += 1
            elif game_result == 3:
                user_tie += 1
            total_games += 1
            continue

        #View Statistics
        elif game_menu_input == 2:
            #Calculate win/loss ratio
            if user_loss == 0:
                wlratio = user_wins
            else:
                wlratio = round(user_wins / user_loss, 2)
                
            print('{}, here are your game play statistics...'.format(user_name))
            print('Wins: {}'.format(user_wins))
            print('Losses: {}'.format(user_loss))
            print('Ties: {}'.format(user_tie))
            print('Win/Loss Ratio: {}'.format(wlratio))
            input('Press enter to continue ')

        #Quit
        elif game_menu_input == 3:
            user_stats = [user_name, user_wins, user_loss, user_tie]
            with open(user_name + '.rps', 'w') as file:
                for element in user_stats:
                    file.write(str(element) + '\n')
            sys.exit()

main()
