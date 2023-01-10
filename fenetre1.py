import pyglet
from pyglet.window import key
from snake import Snake
from boule import Boule
from bonus import Bonus
from malus import Malus


class Fenêtre(pyglet.window.Window):

    '''
    Class représentant la fenêtre et permettant de visualiser le jeu

    Attributs
    ---------
    width: float
        la largeur de l a fenêtre
    
    height: float
        La hauteur de la fenêtre

    score_value: int
        permet de choisir de combien on souhaite augmenter le score selon les cas de collision par exemple.

    vie_value:int
        permet de choisir de combien on souhaite augmenter le score selon les cas de collision par exemple.

    snake: Snake
        Représente le snake

    boule: Boule
        représente la boule ordinaire

    malus: Malus
        représente le malus
    
    bonus: Bonus
        représente le bonus

    game_over: bool
        indique si le joueur a perdu ou pas pas.

    compteur: int
        s'incrémente de 1 à chaque seconbde jusquà atteidre 13 ^puis se rénitialise. Il détermine le temps que met un bonus ou un malus avant de disparaître de la fenêtre
    
    score: Label
        affiche un message indiquent le score du joueur en cas de pause ou de game_over.


    methodes:
    --------

    fin_jeu: 
        Permet d'arrêter le jeu quand l'une des conditions d'arrêt est vérifiée.
    
    apparition_du_malus(self, dt): 
        permet de recréer l'objet malus chaque 17 secondes.

    apparition_du_bonus(self, dt): 
        permet de recréer l'objet bonus chaque 19 secondes.

    effet_boule_bonus_malus:
        permet d'activer les effets des différentes boules en cas de collision avec la tête du snake.

    on_key_press:
        permet de gérer les changements de direction du snake et l'empêche d'aller à l'opposé de sa direction actuelle.
    
    update_2:
        permet de faire augmenter le score de 1 chaque seconde et de faire incrémenter les compteurs qui gèrent le temps d'apparition des des boules.

    draw:
        Permet de représenter les différents objets dans la fenêtre.
 
    update: 
        permet de réactualiser la taille du snake et de le redessiner après chaque déplacement.

    '''

    def __init__(self, width, heigth):
        super().__init__(width, heigth, "snake game")
        self.width = width
        self.height = heigth
        self.score_value = 0
        self.vie_value = 2
        self.snake = Snake(width, heigth)
        self.boule = Boule(width, heigth)
        self.malus = Malus(width, heigth)
        self.malus.forme.x += 2 * width
        self.bonus = Bonus(width, heigth)
        self.bonus.forme.x += 2 * width
        self.game_over = False
        self.compteur = 0
        self.boule.compteur = 0
        self.score = pyglet.text.Label(
            " ", x=width // 2, y=heigth // 2 + 40, anchor_x="center", anchor_y="center"
        )

        pyglet.clock.schedule_interval(self.draw, 1 / 2000)
        pyglet.clock.schedule_interval(self.update, 1 / 10)
        pyglet.clock.schedule_interval(self.update_2, 1)
        pyglet.clock.schedule_interval(self.apparition_du_malus, 17)
        pyglet.clock.schedule_interval(self.apparition_du_bonus, 19)

        # pour pouvoir gerer la touche space
        self.snake.space_direction = 0
        self.v_space = 1
        self.mesg = pyglet.text.Label(
            " Appuyez sur la touche espace pour jouer.",
            x=width / 2,
            y=heigth / 2,
            anchor_x="center",
            anchor_y="center",
            color=(47, 255, 22, 55),
        )

    def fin_jeu(self):
        """ Permet d'arrêter le jeu quand l'une des conditions d'arrêt est vérifiée.

        """
        self.game_over = True
        self.mesg.draw()

        self.snake.space_direction = 0
        self.snake.x_direction = 0
        self.snake.y_direction = 1
        self.snake = Snake(self.width, self.height)
        self.snake.draw_our_snake()

    def apparition_du_malus(self, dt):
        '''permet de recréer l'objet malus chaque 17 secondes.
        
        '''

        if self.snake.space_direction != 0:
            self.malus = Malus(self.width, self.height)

    def apparition_du_bonus(self, dt):
        '''  permet de recréer l'objet bonus chaque 19 secondes.

        '''
        if self.snake.space_direction != 0:
            self.bonus = Bonus(self.width, self.height)

    def effet_boule_bonus_malus(self):
        '''permet d'activer les effets des différentes boules en cas de collision avec la tête du snake.

        '''

        self.snake.effet_collision_boule(self.boule)

        self.snake.effet_collision_malus(self.malus)
        self.snake.effet_collision_bonus(self.bonus)

    def on_key_press(self, symbol, modifiers):
        '''permet de gérer les changements de direction du snake et l'empêche d'aller à l'opposé de sa direction actuelle
        Paramètres:
        -----------
        symbol: Any
        correspond au symbole de la touche appuyée

        modifiers: Any
            correspond à une touche permettant de réaliser une combinaison de touches.

        '''
        if symbol == key.SPACE and self.game_over == True:
            self.game_over = False
            self.snake.space_direction = 1
            self.snake.score.text = "0"
        if symbol == key.SPACE and self.v_space == 1:
            self.snake.space_direction = 1
            self.v_space -= 1
        elif symbol == key.SPACE and self.v_space == 0:
            self.snake.space_direction = 0
            self.v_space += 1
        elif self.snake.x_direction == 1 and symbol == key.LEFT:
            pass
        elif self.snake.y_direction == -1 and symbol == key.UP:
            pass
        elif self.snake.x_direction == -1 and symbol == key.RIGHT:
            pass
        elif self.snake.y_direction == 1 and symbol == key.DOWN:
            pass

        elif symbol == key.UP and self.snake.space_direction == 1:

            self.snake.y_direction = 1
            self.snake.x_direction = 0

        elif symbol == key.DOWN and self.snake.space_direction == 1:
            self.snake.y_direction = -1
            self.snake.x_direction = 0

        elif symbol == key.LEFT and self.snake.space_direction == 1:
            self.snake.x_direction = -1
            self.snake.y_direction = 0

        elif symbol == key.RIGHT and self.snake.space_direction == 1:
            self.snake.x_direction = 1
            self.snake.y_direction = 0

    # gerer le score et la vie

    def update_2(self, dt):
        '''permet de faire augmenter le score de 1 chaque seconde et de faire incrémenter les compteurs qui gèrent le temps d'apparition des des boules.

        Paramètres:
        -----------
        dt: float
            Donne le temps écoulé depuis le dernier appel de la fonction

        '''
        if self.snake.space_direction == 1:
            self.boule.compteur += 1
        if self.boule.compteur == 5:
            self.boule = Boule(500, 500)
            self.boule.compteur = 0

        vie = self.vie_value
        self.compteur += 1
        if self.game_over == True:
            self.score_value = 0
            self.snake.score.text = str(int(self.snake.score.text) + self.score_value)
        if (
            vie > 0
            and self.snake.space_direction == 1
            and not self.snake.collision(self.boule)
        ):
            self.score_value = 1
            self.snake.score.text = str(int(self.snake.score.text) + self.score_value)
        elif (
            vie > 0
            and self.snake.space_direction == 1
            and self.snake.collision(self.boule)
        ):
            self.score_value = 5
            self.snake.score.text = str(int(self.snake.score.text) + self.score_value)
        if vie > 0 and self.snake.space_direction == 1:
            if self.compteur > 13:
                self.malus.forme.x = self.width * 2
                self.bonus.forme.x = self.width * 2
                self.compteur = 0

        # afficher
        if self.snake.space_direction == 0:
            self.boule.forme.x += 2**self.width

    def draw(self, dt):
        ''' Permet de représenter les différents objets dans la fenêtre.
        
        Paramètres:
        -----------
        dt: float
            Donne le temps écoulé depuis le dernier appel de la fonction

        '''
        self.clear()
        if self.snake.score.text != "0":
            self.score.text = "Votre score: " + self.snake.score.text
        if self.game_over:
            self.score.draw()
        if self.snake.space_direction == 0:
            self.boule.forme.x += 2 * self.width
        self.snake.vie.draw()
        self.snake.draw_our_snake()
        self.snake.score.draw()
        if (
            self.snake.space_direction == 0
            and self.game_over == False
            and int(self.snake.score.text) != 0
        ):
            self.mesg.text = "Pause! Appuyez sur la touche espace pour continuer."
            self.score.draw()
            self.mesg.draw()
        if (
            self.snake.space_direction == 0
            and self.game_over == False
            and int(self.snake.score.text) == 0
        ):
            self.mesg.text = "Appuyez sur la touche espace pour commencer à jouer."
            self.mesg.draw()
        if (
            self.snake.head[1] < 0
            or self.snake.head[1] > self.height + 20
            or self.snake.head[0] < 0
            or self.snake.head[0] > self.width
            or (int(self.snake.vie.text) == 0 and self.snake.score.text != 0)
            or self.snake.auto_collision(self.snake.snake_list)
        ):
            self.mesg.text = "Appuyez sur la touche espace pour commencer à jouer."
            self.mesg.draw()
        if self.game_over == True:
            self.mesg.draw()
        if self.snake.collision(self.malus):
            self.malus.forme.x += 2 * self.width
        if self.snake.collision(self.bonus):
            self.bonus.forme.x += 2 * self.width
        while self.boule.détection_de_boule_sur_snake(self.snake.snake_list):
            print("boom")
            self.boule = Boule(500, 500)
        self.boule.draw()
        while self.malus.détection_de_boule_sur_snake(self.snake.snake_list):
            self.malus = Malus(self.width, self.height)
        self.malus.draw()
        while self.bonus.détection_de_boule_sur_snake(self.snake.snake_list):
            self.bonus = Bonus(self.width, self.height)
        self.bonus.draw()

    def update(self, dt):
        '''permet de réactualiser la taille du snake et de le redessiner après chaque déplacement.

        Paramètres:
        -----------
        dt: float
            Donne le temps écoulé depuis le dernier appel de la fonction

        '''

        if self.snake.space_direction == 1 and self.game_over != True:
            if self.snake.déplacement():
                self.snake.draw_our_snake()

            if self.snake.collision(self.boule):
                self.snake.length += 5
            if (
                len(self.snake.snake_list) > self.snake.length
            ):
                del self.snake.snake_list[-1]
                self.snake.draw_our_snake()
        if (
            self.snake.head[1] < 0
            or self.snake.head[1] > self.height + 20
            or self.snake.head[0] < 0
            or self.snake.head[0] > self.width
            or (int(self.snake.vie.text) == 0 and self.snake.score.text != 0)
            or self.snake.auto_collision(self.snake.snake_list)
        ):
            self.fin_jeu()
        self.effet_boule_bonus_malus()
