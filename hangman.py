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
    return solved

def show_result():
    print("you win!")
    
def play():
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)

    strikes = 0
    limit = 6

    print(solved)

    while solved != puzzle:
        letter = get_guess()

        if letter not in puzzle:
            pass

        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result()
    
play()
           _      
         _[_]_  
          (")  
      `--( : )--'
        (  :  )
      ""`-...-'"" 
