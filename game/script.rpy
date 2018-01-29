# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Frank", kind=nvl)
define narrator = nvl_narrator

# family characters var
default ann = 7
default persistent.ann = 0
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
    
    # other lives go here
    
    jump prologo
    
    nvl clear
    
    f "This is a test!"

    "And this is some narration shit."
    "More of it coming."
    "In fact, all of this is still shitty."

    f "I wouldn't say so."

    # This ends the game.
    
    return
    
    
    
label prologo:
    
    nvl clear
    
    #transition shit
    
    "Winter has come."
    "Snowflakes begun to fall down to the ground, dancing their way through air."
    "Each of them melted as it landed on a warm surface."
    "Yet they kept falling, burying the ground under a deadly, {w=1.0}soft carpet."    
    
    
    return
    
label again:
    
    scene bg room
    
    show eileen happy
    
    f "Oh, so you have been here before."
    
    $ persistent.frank = 0
        
    return
