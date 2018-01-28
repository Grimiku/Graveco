# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Frank", kind=nvl)
define narrator = nvl_narrator

# family characters var
default ann = 7
default persistent.frank = 0

# female characters var
default dorothy = 0
default joanne = 0
default cath = 0
default shouko = 0

# male characters var
default george = 0
default jeremy = 0
default christoph = 0
default wan = 0

# The game starts here.

label start:
    
    # if persistent.frank == 1:
        
    #    jump again

    # $ persistent.frank += 1

    nvl clear
    
    f "This is a test!"
    
    "And this is some narration shit."
    "More of it coming."
    "In fact, all of this is still shitty."

    f "I wouldn't say so."

    # This ends the game.
    
    return
    
    
    
    
    
label again:
    
    scene bg room
    
    show eileen happy
    
    f "Oh, so you have been here before."
    
    $ persistent.frank = 0
        
    return
