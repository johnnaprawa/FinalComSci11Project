import pyglet
import time
from os.path import abspath
def muplay(times, file):
    for x in range(times):

        music = pyglet.resource.media(file)
        music.play()

        time.sleep(1)
    pyglet.app.run()

