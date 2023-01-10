import pyglet
import random


class Snake:
    """
    Classe représentant le serpent.

    ...

    Attributes
    ----------
    forme : Rectangle
        un carré de côté 20 pixel .
    head : tuple[float | Any, float | Any]
        Liste des cordonnées du centre de l'attribut forme
    length: int
       Représente la taille du snake
    x0: int
        sert à récupérer le l'abscisse de la tête du snake pendant le déplacement
    y0: int
        sert à récupérer le l'ordonnée de la tête du snake pendant le déplacement
    self.snake_list: list de list
        Contient les couples de coordonnées des carrés constituant le snake.
    x_direction: int:
        0: le snake ne se déplacement pas selon les abscisses; 1: il y a déplacement vers la droite et -1: il y a déplacement vers vers la gauche.
    y_direction: int:
        0: le snake ne se déplacement pas selon les ordonnées; 1: il y a déplacement vers le haut et -1: il y a déplacement vers vers le bas.
    score: Label
        Affiche le score du joueur.
    space_direction: int
        initialement il vaut 0. Sa valeur alterne entre 0 et 1 à chaque fois qu'on clique sur la touche espace.
        0: Le jeu est en pause.
        1: Le jeu est en cours.
    vie: Label
        Affiche la restante du snake et est initialisée à 2.


    Methods
    -------
    __init__(self, window_width, window_heigth):
        Crée un objet de type Snake à une position aléatoire de la fenêtre dont les dimensions sont passées en paramètre.
    draw_our snake(self):
        Dessine le snake dans la fenêtre.
    déplacement(self):
        Assure le déplacement continuel du snake dans la fenêtre.

    auto_collision(self, snake_list, dist_head=0, auto_collision=False):
        Détecte les cas de coïncidence de la tête du snake avec une autre partie de son corps.

    effet_bonus(self, bonus, window_width=1000):
        Assure que le bonus disparaît en cas de collision avec la tête du snake et que soit le score augmente de 15 soit la taille du snake est réduite de 5 unités.

    effet_malus(self,malus, window_width=1000):
        Assure que le malus disparaît de la fenêtre en cas de collision avec la tête du snake et que la vie du snake est réduite d'une unité.

    effet_boule(self, boule, window_width=1000):
        Assure que le boule ordinaire disparaît en cas de collision avec la tête du snake et que le score augmente de 5 unités.
    
    collision(self, boule):
         Détecte les cas de collision entre la tête du snake et la boule

    redéfinir_boule(self, window_width, window_heigth, boule=None):
        Permet de redéfinir l'objet boule à une nouvelle position quand on le souhaite. Elle est utilisée pour redéfinir les boules coïncident avec le snake de sortes qu'aucune boule n'est aperçu sur le snake.
    """
    def __init__(self, window_width, window_heigth):
        ''' Crée un objet de type Snake à une position aléatoire de la fenêtre dont les dimensions sont passées en paramètre
        Parameters
        ----------
        window_didth : float
            La largeur de la fenêtre 
        window_heigth: float
            la hauteur de la fenêtre
        '''

        self.forme = pyglet.shapes.Rectangle(
            ((window_width - 20)) / 2, (window_heigth - 20) / 2, 20, 20
        )
        self.head =  [(window_width - 20) / 2, (window_heigth - 20) / 2 + 20]
        self.snake_list = [
            [(window_width - 20) / 2, (window_heigth - 20) / 2 + 20],
            [(window_width - 20) / 2, (window_heigth - 20) / 2],
            [(window_width - 20) / 2, (window_heigth - 20) / 2 - 20],
        ]
        self.length = 3
        self.x0 = 0
        self.y0 = 0
        self.x_direction = 0
        self.space_direction = 0
        self.score = pyglet.text.Label(
            "0", x=window_width, y=window_heigth + 30, anchor_x="right", anchor_y="top"
        )
        self.y_direction = 1
        self.vie = pyglet.text.Label(
            "2", x=window_width / 2, y=20, anchor_x="center", anchor_y="center"
        )

    def déplacement(self):
        '''Assure le déplacement continuel du snake dans la fenêtre.

        Returns
        ------
        bool
        '''
        déplacement=False
        [self.x0, self.y0] = list(self.head)
        self.head[1] += self.space_direction * self.y_direction * 20
        self.head[0] += self.space_direction * self.x_direction * 20
        self.snake_list.insert(0, [self.x0, self.y0])
        if len(self.snake_list) > self.length:
            del self.snake_list[-1]
            déplacement = True
        return déplacement

    def draw_our_snake(self):
        ''' Dessine le snake dans la fenêtre. '''

        for x in self.snake_list:
            pyglet.shapes.Rectangle(
                x[0], x[1], self.forme.width, self.forme.height
            ).draw()

    def auto_collision(self, snake_list, dist_head=0):
        '''Détecte les cas de coïncidence de la tête du snake avec une autre partie de son corps.

        Paramètres:
        ----------
        snake_list: list
            Une liste des cordonnées des carrés constituant le snake
        
        dist_head: float
            Distance séparant la tête de snake d'un autre carré de corps. 
            '''
        auto_collision = False
        for i in range(0, len(self.snake_list)):
            if auto_collision == True:
                break
            dist_head = (
                (self.head[0] - snake_list[i][0]) ** 2
                + (self.head[1] - snake_list[i][1]) ** 2
            ) ** 0.5
            if dist_head < 20:
                auto_collision = True
        return auto_collision

    def effet_collision_bonus(self, bonus, window_width=1000):
        '''Assure que le bonus disparaît en cas de collision avec la tête du snake et que soit le score augmente de 15 soit la taille du snake est réduite de 5 unités.
        Paramètres:
        ----------
        bonus : Bonus
            Un objet de type bonus
        window_width: float
            La largeur de la fenêtre
        '''

        if self.collision(bonus):
            bonus.forme.x += window_width * 2
            if len(self.snake_list) > 3 and random.uniform(0, 1) > 0.6:
                print(
                    "longueur avant collision avec le bonus: "
                    + str(len(self.snake_list))
                )
                for i in range(0, 5):
                    del self.snake_list[-1]
                print(
                    "longueur après collision avec le bonus: "
                    + str(len(self.snake_list))
                )
                self.length = len(self.snake_list)
            else:
                self.score.text = str(int(self.score.text) + 15)

    def effet_collision_malus(self, malus, window_width=1000):
        ''' Assure que le malus disparaît de la fenêtre en cas de collision avec la tête du snake et que la vie du snake est réduite d'une unité.
 .
        Paramètres:
        ----------
        malus : Malus
            Un objet de type Malus
        window_width: float
            La largeur de la fenêtre
        '''
        if self.collision(malus):
            malus.forme.x += window_width * 2
            self.vie.text = str(int(self.vie.text) - 1)

    def effet_collision_boule(self, boule, window_width=1000):
        '''Assure que le boule ordinaire disparaît en cas de collision avec la tête du snake et que le score augmente de 5 unités.
        Paramètres:
        ----------
        boule : Boule
            Un objet de type Boule
        window_width: float
            La largeur de la fenêtre
            '''
        if self.collision(boule):
            if boule.forme.color[1] == 255:
                self.score.text = str(int(self.score.text) + 5)
                boule.forme.x += 2 * window_width

    def collision(self, boule):
        '''Détecte les cas de collision entre la tête du snake et la boule afin de  

        Paramètres:
        ----------
        boule : Boule
            Un objet de type Boule
        '''
        dist_x = min(
            (boule.forme.x - self.snake_list[0][0]) ** 2,
            (boule.forme.x - self.snake_list[0][0] - self.forme.width) ** 2,
        )
        dist_y = min(
            (boule.forme.y - self.snake_list[0][1]) ** 2,
            (boule.forme.y - self.snake_list[0][1] - self.forme.height) ** 2,
        )

        if (
            self.snake_list[0][0]
            <= boule.forme.x
            <= self.snake_list[0][0] + self.forme.width
        ) and (
            self.snake_list[0][1]
            <= boule.forme.y
            <= self.snake_list[0][1] + self.forme.height
        ):
            return True
        elif (
            self.snake_list[0][0]
            <= boule.forme.x
            <= self.snake_list[0][0] + self.forme.width
        ):
            return dist_y < boule.forme.radius**2
        elif (
            self.snake_list[0][1]
            <= boule.forme.y
            <= self.snake_list[0][1] + self.forme.height
        ):
            return dist_x < boule.forme.radius**2
        else:
            return dist_x + dist_y < boule.forme.radius**2
