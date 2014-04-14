# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables used in your code
lowerMsg = "Lower!"
higherMsg = "Higher!"
correctMsg = "Correct!"
message = "Welcome!"
secret = 0
lowerBound = 0
upperBound = 100
numGuessesRemaining = 7


# helper function to start and restart the game
def new_game():
    # remove this when you add your code  
    global secret
    secret = random.randrange(lowerBound, upperBound)
    init_num_guesses()
    print "Starting new game. Range is from %d to %d" %(numGuessesRemaining, lowerBound, upperBound)
    print "Secret to guess is %d with %d guesses remaining" %(secret, numGuessesRemaining) 
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global lowerBound
    global upperBound
    lowerBound = 0
    upperBound = 100
    new_game()
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global lowerBound
    global upperBound
    lowerBound = 0
    upperBound = 1000
    new_game()

def init_num_guesses():
    global numGuessesRemaining 
    if upperBound == 100:
       numGuessesRemaining = 7
    else:
       numGuessesRemaining = 10
         
def input_guess(guess):
    # main game logic goes here	
    if can_make_guess() == False:
        print "Oops, you ran out of guesses. Please try again."
        new_game()
    else:    
        global numGuessesRemaining
        global message
        
        guessInt = int(guess)
        numGuessesRemaining = numGuessesRemaining - 1
        print "Guess was", guessInt
        print "Number of remaining guesses is", numGuessesRemaining        
        
        if secret < guessInt:
            message = lowerMsg
            print message
        elif secret > guessInt:
            message = higherMsg
            print message
        else:
            message = correctMsg
            print message
            inp.set_text("")
            new_game()

def can_make_guess():
    if numGuessesRemaining > 0:
        return True
    else:
        return False
    
# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 36, "Red")
    
# create frame
frame = simplegui.create_frame("Guess The Number", 300, 200)
frame.add_button("Range: 0 - 100", range100)
frame.add_button("Range: 0 - 1000", range1000)
inp = frame.add_input('Guess', input_guess, 50)

frame.set_draw_handler(draw)

# call new_game and start frame
# Start the frame animation
frame.start()
new_game()


# always remember to check your completed program against the grading rubric

