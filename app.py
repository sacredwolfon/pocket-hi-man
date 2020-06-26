import pyglet, random
song = pyglet.media.load(str(random.randint(1, 5)) + '.mp3')
song.play()
pyglet.app.run()
