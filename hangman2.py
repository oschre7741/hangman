#hangman, 11/9/17

#Olivia S
import random
import os

def show_start_screen():
    path = 'art'

    file_names = os.listdir(path)

    file = path + "/" + file_names[7]
    
    with open(file, 'r') as f:
        lines = f.read()
        print(lines)

def show_end_screen():
    path = 'art'

    file_names = os.listdir(path)

    file = path + "/" + file_names[6]
    
    with open(file, 'r') as f:
        lines = f.read()
        print(lines)
    
def get_puzzle(name):
    path = 'puzzles'

    file_names = os.listdir(path)

    for i, f in enumerate(file_names):
        with open(path + "/" + file_names[i], 'r') as f:
            category = f.read().splitlines()
        print(str(i+1) + ") " + str(category[0]))

    print()

    choice = input("pick a category, " + str(name) + " ")
    choice = int(choice)

    print()

    file = path + "/" + file_names[choice - 1]

    with open(file, 'r') as f:
        lines = f.read().splitlines()

    category_name = lines[0]
    puzzle = random.choice(lines[1:])

    print(category_name)
    return(puzzle)

def get_strikes():
    strikes = 0
    limit = 6
    strikesleft = limit - strikes
    return strikesleft
    
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
        
def display_board(solved, guesses, strikesleft):
    print(solved, [guesses])
    print()
    print("You have " + str(strikesleft) + " tries left.")
    print()
    
def show_result(solved, puzzle, name, strikes):
        if solved == puzzle:
            print("You win, " + str(name) + "!")
            print()
        elif strikes >= 6:
            print("sorry " + str(name) + ", you ran out of tries.")
            print()
            
def play_again():
        while True:
            decision = input("Would like to play again? (y/n) ")

            if decision.lower() == "y" or decision.lower() == "yes":
                return True
            elif decision.lower() == "n" or decision.lower() == "no":
                return False
            else:
                print("I don't understand, please answer 'y' or 'n'.")
                
def play():
    name = get_name()
    puzzle = get_puzzle(name)
    strikesleft = get_strikes()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved, guesses, strikesleft)

    limit = 6
    strikes = 0
    
    while solved != puzzle:
        letter = get_guess(guesses, name)

        if (len(str(letter)) > 1) or (letter == '' or letter == ' ') or (letter not in "abcdefghijklmnopqrstuvwxyz") or (letter in guesses):
            strikes -= 1
            
        if str(letter) not in puzzle:
            strikes += 1
            strikesleft = limit - strikes
            if strikes == 1:
                print()
                path = 'art'

                file_names = os.listdir(path)

                file = path + "/" + file_names[0]
                
                with open(file, 'r') as f:
                    lines = f.read()
                    print(lines)
                print()
            elif strikes == 2:
                print()
                path = 'art'

                file_names = os.listdir(path)

                file = path + "/" + file_names[1]
                
                with open(file, 'r') as f:
                    lines = f.read()
                    print(lines)
                print()
            elif strikes == 3:
                print()
                path = 'art'

                file_names = os.listdir(path)

                file = path + "/" + file_names[2]
                
                with open(file, 'r') as f:
                    lines = f.read()
                    print(lines)
                print()
            elif strikes == 4:
                print()
                path = 'art'

                file_names = os.listdir(path)

                file = path + "/" + file_names[3]
                
                with open(file, 'r') as f:
                    lines = f.read()
                    print(lines)
                print()
            elif strikes == 5:
                print()
                path = 'art'

                file_names = os.listdir(path)

                file = path + "/" + file_names[4]
                
                with open(file, 'r') as f:
                    lines = f.read()
                    print(lines)
                print()
            elif strikes == 6:
                print()
                path = 'art'

                file_names = os.listdir(path)

                file = path + "/" + file_names[5]
                
                with open(file, 'r') as f:
                    lines = f.read()
                    print(lines)
                print()
           
        if strikes == limit:
            break
        
        guesses += str(letter)
        solved = get_solved(puzzle, guesses)
        display_board(solved, guesses, strikesleft)

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
