# Playing with custom LED images
import microbit as mb

# This is a list of strings to represent a wider image
# that we want to scroll across the screen
fullboat=['0000000606000000',
          '0000006666000000',
          '0000000404000000',
          '0000009999900000',
          '0000000999000000']

# Create a list of Images, each made by joining together
# 5x5 subsets of the full image
#
# Initialise the list
all_boats=[]
# Start 5 pixels from the right of the list and work to the left
i=len(fullboat[0])-5
while i > 1:
    all_boats.append( mb.Image( fullboat[0][i:i+5] + ':' + \
                                fullboat[1][i:i+5] + ':' + \
                                fullboat[2][i:i+5] + ':' + \
                                fullboat[3][i:i+5] + ':' + \
                                fullboat[4][i:i+5] ))
    i=i-1

# Now display the list of images in a loop
mb.display.show(all_boats,loop=True)
