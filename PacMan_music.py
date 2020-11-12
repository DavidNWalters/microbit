# First attempt at working towards a Pac Man demo
# Here, we start with the music
# Taken from the score published on this webpage:
# https://musescore.com/user/85429/scores/107109
#

import microbit as mb
import music

music.set_tempo(ticks=7)
PacMan_tune = ["B4:2","B5","F#","D#",  "B:1", "F#:3","D#:2",
               "C:2", "C6","G5","E",   "C6:1","G5:3","E:2",
               "B4:2","B5","F#","D#",  "B:1", "F#:3","D#:2",
               "D#:1","E", "F:2",   "F:1","F#","G:2",   "G:1","G#","A:2","B:5"]

while True:
    if mb.button_a.is_pressed():
        mb.display.show(mb.Image.PACMAN)
        music.play(PacMan_tune, wait=False)
    elif mb.button_b.is_pressed():
        mb.display.clear()
