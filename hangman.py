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

def get_guess():
    letter = input("Guess a letter: ")
    return letter

def display_board(solved):
    print(solved)

def show_result(solved, puzzle):
    if solved == puzzle:
        print("You win!")
    else:
        print("sorry, you lost.")

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
    display_board(solved)

    strikes = 0
    limit = 6

    while solved != puzzle:
        letter = get_guess()
        
        if letter not in puzzle and strikes < limit:
            strikes += 1
        
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result(solved, puzzle)
    
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
