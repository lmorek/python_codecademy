__author__ = 'morek'
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

num_range = 100
secret_num = 0
guesses_left = 0


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    global secret_num
    global guesses_left
    
    secret_num = random.randrange(0, num_range)
    
    if num_range==100:
        guesses_left=7
    elif num_range==1000:
        guesses_left=10
        
        
    print "New game. The range is from 0 to", num_range, ". Good luck!"
    print "Number of remaining guesses is ", guesses_left, "\n"
    return secret_num

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range=100
    return new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range=1000
    return new_game()
    
    
def input_guess(guess):    
    # main game logic goes here	
    global guesses_left
    global secret_num 
    
    won = False
    
    print "You guessed: ",guess
    guesses_left = guesses_left - 1
    print "Number of remaining guesses is ", guesses_left
    
    if int(guess) == secret_num:       
        won = True
    elif int(guess) > secret_num:
        result = "Lower!"
    else:
        result = "Higher!"                
        
        
    if won:
        print "Correct!\n"
        return new_game()
        
    elif guesses_left == 0:
        print "Game over. You didn't guess the number in time!"   
        return new_game()
        
    else:
        print result
        
            
    
# create frame
f = simplegui.create_frame("Game: Guess the number!", 250, 250)
# f.set_canvas_background('Green')

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)	
f.add_input("Enter your guess", input_guess, 200)

# call new_game and start frame
new_game()
f.start()



# always remember to check your completed program against the grading rubric