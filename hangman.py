#hangman, 11/9/17

#Olivia S

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
    return "hangman"

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

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

def show_result(solved, puzzle, name):
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
    display_board(solved, guesses)
    name = get_name()

    limit = 6
    strikes = 0
    
    while solved != puzzle:
        letter = get_guess(guesses, name)
        
        if str(letter) not in puzzle:
            solved  = get_solved(puzzle, guesses)
            strikes = strikes + 1
        
        guesses += str(letter)
        solved = get_solved(puzzle, guesses)
        display_board(solved, guesses)

    show_result(solved, puzzle, name)
    if strikes == 1:
        print("------------")
        print("|         | ")        
        print("|         O ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")

    if strikes == 2:
        print("------------")
        print("|         | ")        
        print("|         O ")
        print("|         | ")
        print("|           ")
        print("|           ")
        print("|           ")

    if strikes == 3:
        print("------------")
        print("|         | ")        
        print("|         O ")
        print("|        /| ")
        print("|           ")
        print("|           ")
        print("|           ")


    if strikes == 4:
        print("------------")
        print("|         | ")        
        print("|         O ")
        print("|        /|\ ")
        print("|           ")
        print("|           ")
        print("|           ")

    if strikes == 5:
        print("------------")
        print("|         | ")        
        print("|         O ")
        print("|        /|\ ")
        print("|        /  ")
        print("|           ")
        print("|           ")

    if strikes == 6:
        print("------------")
        print("|         | ")        
        print("|         O ")
        print("|        /|\ ")
        print("|        / \ ")
        print("|           ")
        print("|           ")
        
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
