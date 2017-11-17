#hangman, 11/9/17

#Olivia S

import random

def show_start_screen():
    print(" ('-. .-.   ('-.         .-') _            _   .-')      ('-.         .-') _  ")
    print("( OO )  /  ( OO ).-.    ( OO ) )          ( '.( OO )_   ( OO ).-.    ( OO ) ) ")
    print(",--. ,--.  / . --. /,--./ ,--,'  ,----.    ,--.   ,--.) / . --. /,--./ ,--,'  ")
    print("|  | |  |  | \-.  \ |   \ |  |\ '  .-./-') |   `.'   |  | \-.  \ |   \ |  |\  ")
    print("|   .|  |.-'-'  |  ||    \|  | )|  |_( O- )|         |.-'-'  |  ||    \|  | ) ")
    print("|       | \| |_.'  ||  .     |/ |  | .--, \|  |'.'|  | \| |_.'  ||  .     |/  ")
    print("|  .-.  |  |  .-.  ||  |\    | (|  | '. (_/|  |   |  |  |  .-.  ||  |\    |   ")
    print("|  | |  |  |  | |  ||  | \   |  |  '--'  | |  |   |  |  |  | |  ||  | \   |   ")
    print("`--' `--'  `--' `--'`--'  `--'   `------'  `--'   `--'  `--' `--'`--'  `--'   ")
    
def show_end_screen():
    print("███╗   ███╗ █████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗     ██████╗ ██╗     ██╗██╗   ██╗██╗ █████╗      ██╗ ██╗    ██╗ ██╗██████╗     ██╗ ██╗███████╗")
    print("████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝    ██╔═══██╗██║     ██║██║   ██║██║██╔══██╗    ███║███║   ██╔╝███║╚════██╗   ██╔╝███║╚════██║")
    print("██╔████╔██║███████║██║  ██║█████╗      ██████╔╝ ╚████╔╝     ██║   ██║██║     ██║██║   ██║██║███████║    ╚██║╚██║  ██╔╝ ╚██║ █████╔╝  ██╔╝ ╚██║    ██╔╝")
    print("██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██╔══██╗  ╚██╔╝      ██║   ██║██║     ██║╚██╗ ██╔╝██║██╔══██║     ██║ ██║ ██╔╝   ██║ ╚═══██╗ ██╔╝   ██║   ██╔╝ ")
    print("██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██████╔╝   ██║       ╚██████╔╝███████╗██║ ╚████╔╝ ██║██║  ██║     ██║ ██║██╔╝    ██║██████╔╝██╔╝    ██║   ██║  ")
    print("╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═════╝    ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═╝     ╚═╝ ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝     ╚═╝   ╚═╝  ")
                                                                                                                                                        
def get_puzzle():
    choice = None

while choice != "0":
    print('''
    --------------------
    Welcome to Hangman
    --------------------

    Choose a category:

    0 - Instruments
    1 - Cities
    2 - random words

    ''')
    choice = input("Enter you choice: ")

    if choice == "0":
        List = open("instruments.txt").readlines()
    elif choice =="1":
        List = open("cities.txt").readlines()
    elif choice == "2":
        List = open("random.txt").readlines()

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved
'''
def get_language():
    print("Would you like to play in English or Spanish?")
    language = input()
    return language

    if language == English:
        return English
    elif language == Spanish:
        return Spanish
'''
def get_name():
        print("What is your name?")
        name = input()
        return name
 
def get_guess(guesses, name):
        letter = input("Guess a letter, " + str(name) + ": ")
        
        if len(letter) > 1:
            print("please guess only one letter " + str(name) + ".")
        elif letter == '' or letter == ' ':
              print("You need to enter a letter, " + str(name))
        elif letter not in "abcdefghijklmnopqrstuvwxyz":
            print("You must enter a letter " + str(name) + ".")
        elif letter in guesses:
            print("You have already entered that letter " + str(name) + ".")
        else:
            return letter
        
def display_board(solved, guesses):
    print(solved, [guesses])
    )
    
def show_result(solved, puzzle, name, strikes):
        if solved == puzzle:
            print("You win, " + str(name) + "!")
        elif strikes >= 6:
            print("sorry " + str(name) + ", you ran out of tries.")
            
def play_again():
        while True:
            decision = input("Would like to play again? (y/n)")

            if decision.lower() == "y" or decision.lower() == "yes":
                return True
            elif decision.lower() == "n" or decision.lower() == "no":
                return False
            else:
                print("I don't understand, please answer 'y' or 'n'.")
                
def play():
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    name = get_name()
    display_board(solved, guesses, strikes)
    #language = get_language()
    

    limit = 6
    strikes = 0
    
    while solved != puzzle:
        letter = get_guess(guesses, name)
        
        if str(letter) not in puzzle:
            strikes += 1 
            if strikes == 1:
                print("  (     )   ")
                print("  `-...-'   ")
            elif strikes == 2:
                print("   (   )    ")
                print("  (     )   ")
                print("  `-...-'   ")
            elif strikes == 3:
                print("    ( )     ")
                print("   (   )    ")
                print("  (     )   ")
                print("  `-...-'   ")
            elif strikes == 4:
                print("     _      ") 
                print("   _[_]_    ")
                print("    ( )     ")
                print("   (   )    ")
                print("  (     )   ")
                print("  `-...-'   ")
            elif strikes == 5:
                print("     _      ") 
                print("   _[_]_    ")
                print("    ( )     ")
                print("   (   )--' ")
                print("  (     )   ")
                print("  `-...-'   ")
            elif strikes == 6:
                print("     _      ") 
                print("   _[_]_    ")
                print("    ( )     ")
                print("`--(   )--' ")
                print("  (     )   ")
                print("  `-...-'   ")
                
        if strikes == limit:
            break
        
        guesses += str(letter)
        solved = get_solved(puzzle, guesses)
        display_board(solved, guesses, strikes)

    show_result(solved, puzzle, name, strikes)
   
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_end_screen()

'''
           _      
         _[_]_  
          (")  
      `--( : )--'
        (  :  )
      ""`-...-'"" 
'''

