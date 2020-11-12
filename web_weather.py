#
# Code to display weather data passed via the serial USB interface from Linux.
# This code works with data from from Open Weather Map (OWM)
# or from the Met Office datapoint API, for which I have different python codes.
#
# Corresponding python3 programs are:
# ~/python/OpenWeatherMapToMicorbit.py
# ~/python/MetOfficeDataPointToMicrobit.py

import microbit as mb

# Set up micro:bit images for various weather types
# Some of these are animated, so we also set up a delay period
# for each one, to fit into the looping period. Non-animated
# images use the default delay of 400
sun = mb.Image('09990:99999:99999:99999:09990:')
sun_delay = 400
moon = mb.Image('00990:00099:00099:00099:00990:')
moon_delay = 400
some_cloud = mb.Image('04040:44444:00000:00000:00000:')
some_cloud_delay = 400
broken_cloud = mb.Image('06060:66666:00000:00000:00000:')
broken_cloud_delay = 400
cloud = mb.Image('08080:88888:00000:00000:00000:')
cloud_delay = 400
shower = [mb.Image('08080:88888:00600:00000:00000:'),
          mb.Image('08080:88888:00006:00600:00000:'),
          mb.Image('08080:88888:00000:00006:00600:'),
          mb.Image('08080:88888:00000:00000:00006:')]
shower_delay = 150
rain = [mb.Image('08080:88888:40400:00000:00000:'),
          mb.Image('08080:88888:00000:04040:00000:'),
          mb.Image('08080:88888:00000:00000:00404:')]
rain_delay = 400
thunder = [mb.Image('08080:88888:00000:00000:00000:'),
           mb.Image('08080:88888:00090:00000:00000:'),
           mb.Image('08080:88888:00090:00900:00000:'),
           mb.Image('08080:88888:00090:00990:00000:'),
           mb.Image('08080:88888:00090:00990:00900:'),
           mb.Image('08080:88888:09000:00000:00000:'),
           mb.Image('08080:88888:09000:90000:00000:'),
           mb.Image('08080:88888:09000:99000:00000:'),
           mb.Image('08080:88888:09000:99000:90000:')]
thunder_delay = 133
snow = [mb.Image('88888:07070:70707:07070:70707:'),
        mb.Image('88888:70700:07070:70700:07070:'),
        mb.Image('88888:07070:70707:07070:70707:'),
        mb.Image('88888:00707:07070:00707:07070:')]
snow_delay = 300
fog = [mb.Image('22222:44444:22222:44444:22222:'),
       mb.Image('44444:22222:44444:22222:44444:')]
fog_delay = 600
# Add these to dictionaries, ensuring that there is an image/delay
# for every OWM weather type. Met Office data are mapped onto these
# simpler weather types.
icons = {'01d':sun, '01n':moon, '02d':some_cloud, '02n':some_cloud,
         '03d':cloud, '03n':cloud, '04d':broken_cloud, '04n':broken_cloud,
         '09d':shower, '09n':shower, '10d':rain, '10n':rain,
         '11d':thunder, '11n':thunder, '13d':snow, '13n':snow,
         '50d':fog, '50n':fog}

delays = {'01d':sun_delay, '01n':moon_delay, '02d':some_cloud_delay, '02n':some_cloud_delay,
         '03d':cloud_delay, '03n':cloud_delay, '04d':broken_cloud_delay, '04n':broken_cloud_delay,
         '09d':shower_delay, '09n':shower_delay, '10d':rain_delay, '10n':rain_delay,
         '11d':thunder_delay, '11n':thunder_delay, '13d':snow_delay, '13n':snow_delay,
         '50d':fog_delay, '50n':fog_delay}

# Define a function to return whether the buttons have been pressed since
# the last call. We also return whether any buttons have been pressed.
def get_sensor_data():
    a, b = mb.button_a.was_pressed(), mb.button_b.was_pressed()
    print(a, b)
    if (a or b):
        return True
    else:
        return False

while True:
    button_pressed=get_sensor_data()
#   This is quite a long sleep period, but is long enough for the
#   animations to work
    mb.sleep(1200)

#   Set up a "try" to read the incoming data and display it
    try:
        bytestring = mb.uart.readline()
        # If one of the buttons has been pressed, display the
        # date and time.
        if button_pressed:
            mb.display.scroll(str(bytestring)[5:-1],delay=75)
            button_pressed = False
        # And whether pressed or not, display the weather type icon
        icon = icons[str(bytestring)[2:5]]
        mb.display.show(icon,wait=False,loop=True,delay=delays[str(bytestring)[2:5]])
    except:
	    pass
