import pyglet
import random


class Boule:
    """
    Classe représentant la nourriture du serpent.

    ...

    Attributes
    ----------
    forme : Circle
        Un disque de rayon 40 pixels et de couleur verte créé à une position aléatoire dans la fenêtre.
    centre : tuple[int | Any, int | Any]
        Liste des cordonnées du centre du disque de nourriture
    dist_y: float
        Le minimum de la distance en y entre le centre de la boule en le cordonnées d'un carreau donné du corps du snake
    dist_x: float
        Le minimum de la distance en x entre le centre de la boule en le cordonnées d'un carreau donné du corps du snake
    compteur: int
        permet de compteur le temps écoulé depuis la création du dernier objet de la classe afin d'en créer un nouveau toutes les 5 secondes
    

    Methods
    -------
    __init__(self, window_width, window_heigth):
        Crée un objet de type Boule à une position aléatoire de la fenêtre dont les dimensions sont passées en paramètre.
    draw(self):
        Dessine la boule dans la fenêtre
    détection_de_boule_sur_snake(self, snake_list, collision_généralisée=False):
        permet de détecter les boules créées dont une partie coïncide avec un carreau du snake
    redéfinir_régulièrement_boule(self, window_width, window_heigth, boule=None):
        Permet de redéfinir l'objet boule à une nouvelle position dans la fenêtre à chaque fois que le compteur atteint 5 de sorte qu'une nouvelle boule apparaît et disparaît de la fenêtre chaque 5 secondes.
    redéfinir_boule(self, window_width, window_heigth, boule=None):
        Permet de redéfinir l'objet boule à une nouvelle position quand on le souhaite. Elle est utilisée pour redéfinir les boules coîncident avec le snake de sortes qu'aucune boule n'est apercu sur le snake.
    """
    def __init__(self, window_width, window_heigth):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
        window_didth : float
            La largeur de la fenêtre 
        window_heigth: float
            la hauteur de la fenêtre
        """
        self.forme = pyglet.shapes.Circle(
            x=random.uniform(40, window_width - 40),
            y=random.uniform(40, window_heigth),
            radius=40,
            color=(0, 255, 0),
        )
        self.centre = (self.forme.x, self.forme.y)
        self.dist_y = 0
        self.dist_x = 0
        self.compteur = 0

    def draw(self):
        """
        Dessine la boule dans la fenêtre
        """
        self.forme.draw()

    def détection_de_boule_sur_snake(self, snake_list):
        """
        Permet de détecter les boules créées dont une partie coïncide avec un carreau du snake
        Parameters
        ----------
        snake_list : list, non optionnel
            La liste des couples de coordonnées de rectangles du snake.

        Returns
        -------
        bool
        """
        collision_généralisée = False
        for i in range(0, len(snake_list)):
            if collision_généralisée == True:
                break
            self.dist_x = min(
                (self.forme.x - snake_list[i][0]) ** 2,
                (self.forme.x - snake_list[i][0] - 20) ** 2,
            )

            self.dist_y = min(
                (self.forme.y - snake_list[i][1]) ** 2,
                (self.forme.y - snake_list[i][1] - 20) ** 2,
            )

            if (snake_list[i][0] <= self.forme.x <= snake_list[i][0] + 20) and (
                snake_list[i][1] <= self.forme.y <= snake_list[i][1] + 20
            ):
                collision_généralisée = True
            elif snake_list[i][0] <= self.forme.x <= snake_list[i][0] + 20:
                collision_généralisée = self.dist_y < self.forme.radius**2
            elif snake_list[i][1] <= self.forme.y <= snake_list[i][1] + 20:
                collision_généralisée = self.dist_x < self.forme.radius**2
            else:
                collision_généralisée = (
                    self.dist_x + self.dist_y < self.forme.radius**2
                )

        return collision_généralisée

    def redéfinir_régulièrement_boule(self, window_width, window_heigth):
        """
        Permet de redéfinir l'objet boule à une nouvelle position dans la fenêtre à chaque fois que le compteur atteint 5 de sorte qu'une nouvelle boule apparaît et disparaît de la fenêtre chaque 5 secondes.
        parameters
        ----------
        window_width: float, non optionnel
            La largeur de la fenêtre
        window_width: float, non optionnel
            La hauteur de la fenêtre
        boule : bool, optionnel
    
        Returns
        -------
        bool
        """
        boule=None
        if self.compteur == 5:
            boule = Boule(window_width, window_heigth)
        return boule
