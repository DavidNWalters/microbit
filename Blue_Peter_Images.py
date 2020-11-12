# Playing with custom LED images
import microbit as mb

boat1 = mb.Image('00000:'
                 '00000:'
                 '00000:'
                 '90000:'
                 '00000')

boat2 = mb.Image('60000:'
                 '60000:'
                 '40000:'
                 '99000:'
                 '90000')

boat3 = mb.Image('06000:'
                 '66000:'
                 '04000:'
                 '99900:'
                 '99000')

boat4 = mb.Image('00600:'
                 '66600:'
                 '40400:'
                 '99990:'
                 '99900')

boat5 = mb.Image('06060:'
                 '66660:'
                 '04040:'
                 '99999:'
                 '09990')

boat6 = mb.Image('00606:'
                 '06666:'
                 '00404:'
                 '09999:'
                 '00999')

boat7 = mb.Image('00060:'
                 '00666:'
                 '00040:'
                 '00999:'
                 '00099')

boat8 = mb.Image('00006:'
                 '00066:'
                 '00004:'
                 '00099:'
                 '00009')

boat9 = mb.Image('00000:'
                 '00006:'
                 '00000:'
                 '00009:'
                 '00000')

boat10= mb.Image('00000:'
                 '00000:'
                 '00000:'
                 '00000:'
                 '00000')

all_boats=[boat1, boat2, boat3, boat4, boat5, boat6, boat7, boat8, boat9, boat10, boat10, boat10]
mb.display.show(all_boats,loop=True)
