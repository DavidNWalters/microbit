# Code to read the accelerometer and use the microbit
# as a theromin-like instrument

import microbit as mb
import music


# Max and min frequency values
# Note these values are for +/-1g
# Higher/lower values are possible by accelerating
# rather than tilting the microbit
freq_min = 261.63   #C4
freq_max = 1046.5  #C7

# Always on loop
while True:
    # Read x acceleration
    x_accel = mb.accelerometer.get_x()

    #
    if mb.button_a.is_pressed():
        # x_accel runs from -1024 to 1024
        # convert this to a float from 0 to 1
        freq = (1024 + float(x_accel)) / 2048
        # Then convert this to a frequency between freq_min and freq_max
        freq= freq_min + (freq_max - freq_min) * freq
        # The max/min values relate to +/-1g
        # If the microbit is shaken or accelerated it can go out of this range
        # Here, we cap the values, although these caps
        # could be set to different values than the max/min
        freq_cap_max = 2093  # C7
        freq_cap_min = 65.41 # C2
        freq = max(freq,freq_cap_min)
        freq = min(freq,freq_cap_max)

        #mb.display.show(freq)
        music.pitch(int(freq),200)



    mb.sleep(1)
