import pyglet
from fenetre1 import Fenêtre

window = Fenetre(500, 500)

pyglet.app.run()
print("C'est fini ! " + window.score.text)
