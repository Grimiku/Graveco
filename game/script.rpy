# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# family characters var
default ann = 7
default frank = -1

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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy
    
    # These display lines of dialogue.
    
if frank == 1:
        
    jump again

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to 
    the world!"
    
    $ frank = frank +1

    # This ends the game.

    return
    
label again:
    
    scene bg room
    
    show eileen happy
    
    e "Oh, so you have been here before."
    
    # $ frank = 0
        
    return
