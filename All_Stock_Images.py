# Display all of the pre-defined images under user control
# Instructions:
#   a:   show last image
#   b:   show next image
#   a+b: loop through images

import microbit as mb

# List of all predefined images
images=['HEART', 'HEART_SMALL',
        'HAPPY',  'SMILE',     'SAD',   'CONFUSED', 'ANGRY',
        'ASLEEP', 'SURPRISED', 'SILLY', 'FABULOUS', 'MEH',
        'YES', 'NO',
        'CLOCK1', 'CLOCK2', 'CLOCK3', 'CLOCK4',  'CLOCK5',  'CLOCK6',
        'CLOCK7', 'CLOCK8', 'CLOCK9', 'CLOCK10', 'CLOCK11', 'CLOCK12',
        'ARROW_N', 'ARROW_NE', 'ARROW_E', 'ARROW_SE', 'ARROW_S', 'ARROW_SW', 'ARROW_W', 'ARROW_NW',
        'TRIANGLE', 'TRIANGLE_LEFT', 'CHESSBOARD', 'DIAMOND', 'DIAMOND_SMALL', 'SQUARE', 'SQUARE_SMALL',
        'RABBIT', 'COW', 'DUCK', 'TORTOISE', 'BUTTERFLY', 'SNAKE', 'GIRAFFE', 'STICKFIGURE',
        'MUSIC_CROTCHET', 'MUSIC_QUAVER', 'MUSIC_QUAVERS',
        'PITCHFORK', 'XMAS', 'PACMAN', 'GHOST', 'TARGET', 'TSHIRT',
        'ROLLERSKATE', 'HOUSE',   'SWORD', 'SKULL', 'UMBRELLA']

n_images=len(images) # Total number of images
i=0                  # Image number: initialise to 0
looping=False        # Logical: are we looping over images: initialise to False

# Forever loop in which to run main code
while True:
    # Show image using current value of i
    image=images[i]
    eval('mb.display.show(mb.Image.'+image+')')

    # Move to next image and switch off looping if button b is pressed
    if mb.button_b.is_pressed():
        i=(i+1) % n_images #don't let value go above number of images
        looping=False
        mb.sleep(250)
    # Move to next image and switch off looping if button b is pressed
    elif mb.button_a.is_pressed():
        looping=False
        i=(i-1) % n_images #don't let value go below 0
        mb.sleep(250)

    # Swich on looping if both buttons are pressed
    if (mb.button_a.is_pressed() and mb.button_b.is_pressed()):
        looping=True
        mb.sleep(250)

    # Loop over images is "looping" is True
    if looping:
        i=(i+1) % n_images
        mb.sleep(500)


