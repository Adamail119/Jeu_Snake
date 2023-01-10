from snake import Snake
from boule import Boule
from bonus import Bonus
import random
from malus import Malus



def test_auto_collision():
    '''vérifions que la methode auto_collision de la classe Snake arrive à detecter les cas où la tête du snake coïncide avec une autre partie de son corps
    '''
    snake = Snake(
        500, 500
    )  # 500  et 500 représentent respecrtivement la largeur et la hauteur de notre fenêtre actuelle
    snake.head = snake.snake_list[2]
    assert snake.auto_collision(snake.snake_list)


def test_sens_de_déplacement_initial_du_Snake():
    ''' vérifie que le snake se déplace initialement vers le haut.
    '''
    snake = Snake(500, 500)
    snake.space_direction = (
        1  # 1 signifie qu'il  a déplacement et 0 signifie le contraire
    )
    assert (
        snake.x_direction == 0 and snake.y_direction == 1
    )  # 1 signifie sens positif, -1 sens négatif et 0 signifie pas de déplacement selon la direction concernée


def test_position_initiale_du_Snake():
    '''' Vérifie que le snake est initialement au centre de la fenêtre.
    '''
    snake = Snake(
        500, 500
    )  # 500  et 500 représentent respecrtivement la largeur et la hauteur de notre fenêtre actuelle
    assert snake.snake_list == [
        [(500 - 20) / 2, (500 - 20) / 2 + 20],
        [(500 - 20) / 2, (500 - 20) / 2],
        [(500 - 20) / 2, (500 - 20) / 2 - 20],
    ]  # vérifie que le snake se trouve au centre de le la fenêtre et orienté vers le haut, un carré du snake est de coté 20 pixel


def test_constructeur_Boule():
    '''vérifie qu'on crée effectivement un objet de type boule qui est un disque de rayon 40 pixels'''

    boule = Boule(500, 500)
    assert type(boule) == Boule and boule.forme.radius == 40


def test_position_Boule():
    ''' vérifie que la boule est créée à une position aléatoire à chaque fois.'''

    boule1 = Boule(500, 500)
    boule2 = Boule(500, 500)
    boule1.draw()
    boule2.draw()
    assert boule1.forme.x != boule2.forme.x or boule1.forme.y != boule2.forme.y


def test_déplacement_haut():
    '''vérifie que le snake peut  se déplace par carrés de 20 pixels  dans la fenêtre'''
    snake = Snake(500, 500)
    snake.head[1] += 20
    liste = [
        [(500 - 20) / 2, (500 - 20) / 2 + 40],
        [(500 - 20) / 2, (500 - 20) / 2 + 20],
        [(500 - 20) / 2, (500 - 20) / 2],
    ]
    déplacement = snake.déplacement()
    for i in range(0, len(snake.snake_list)):
        assert snake.snake_list[i] == liste[i]
    assert déplacement == True


def test_déplacement_à_droite():
    ''' Vérifie que le snake peut se déplacer à droite'''
    snake = Snake(500, 500)
    snake.head[0] += 20
    liste = [
        [(500 - 20) / 2 + 20, (500 - 20) / 2 + 20],
        [(500 - 20) / 2, (500 - 20) / 2 + 20],
        [(500 - 20) / 2, (500 - 20) / 2],
    ]
    déplacement = snake.déplacement()
    for i in range(0, len(snake.snake_list)):
        assert snake.snake_list[i] == liste[i]
    assert déplacement == True


def test_déplacement_à_gauche():
    ''' Vérifie que le snake peut se déplacer à gauche'''

    snake = Snake(500, 500)
    snake.head[0] -= 20
    liste = [
        [(500 - 20) / 2 - 20, (500 - 20) / 2 + 20],
        [(500 - 20) / 2, (500 - 20) / 2 + 20],
        [(500 - 20) / 2, (500 - 20) / 2],
    ]
    déplacement = snake.déplacement()
    for i in range(0, len(snake.snake_list)):
        assert snake.snake_list[i] == liste[i]
    assert déplacement == True


def test_déplacement_vers_le_bas():  # on considère le cas où le snake est allongé verticalement, la tête en dessous du reste du corps (l'inverse de la position initiale)
    ''' Vérifie que le snake peut se déplacer vers le bas'''

    snake = Snake(500, 500)
    snake.head = [(500 - 20) / 2, (500 - 20) / 2 - 20]
    snake.snake_list = [
        [(500 - 20) / 2, (500 - 20) / 2 - 20],
        [(500 - 20) / 2, (500 - 20) / 2],
        [(500 - 20) / 2, (500 - 20) / 2 + 20],
    ]
    snake.head[1] -= 20
    liste = [
        [(500 - 20) / 2, (500 - 20) / 2 - 40],
        [(500 - 20) / 2, (500 - 20) / 2 - 20],
        [(500 - 20) / 2, (500 - 20) / 2],
    ]
    déplacement = snake.déplacement()
    for i in range(0, len(snake.snake_list)):
        assert snake.snake_list[i] == liste[i]
    assert déplacement == True


def test_détection_de_boule_sur_snake():
    '''Détection des boules créées sur le snake (pour éviter par la suite qu'elles ne soient visibles par le joueur en les redessinant ailleurs)'''

    snake = Snake(500, 500)
    boule = Boule(500, 500)
    i = random.randint(0, len(snake.snake_list) - 1)
    boule.forme.x = snake.snake_list[i][0]
    boule.forme.y = snake.snake_list[i][1]
    assert boule.détection_de_boule_sur_snake(snake.snake_list)


def test_non_apparition_de_boule_sur_le_Snake():
    ''' vérifie que les boules coincidant avec le snake sont redessinées ailleurs de sorte que la boule n'apparait jamais vue sur le corps du snake'''

    snake = Snake(500, 500)
    boule2 = Boule(500, 500)
    i = random.randint(0, len(snake.snake_list) - 1)
    boule2.forme.x = snake.snake_list[i][0]
    boule2.forme.y = snake.snake_list[i][1]
    while boule2.détection_de_boule_sur_snake(
        snake.snake_list
    ):  # le test précédent assure que la condition est vérifiée
        boule2 = Boule(500, 500)
    assert (
        boule2.forme.x != snake.snake_list[i][0]
        or boule2.forme.y != snake.snake_list[i][1]
    )


def test_constructeur_bonus():
    '''vérifions que Bonus hérite de boule et qu'un bonus peut être distingué d'une boule ordinaire à partir de sa couleur'''

    boule = Boule(500, 500)
    bonus = Bonus(500, 500)
    assert type(bonus == Boule)
    assert bonus.forme.color != boule.forme.color


def test_constructeur_malus():
    '''vérifie que Bonus hérite de boule et qu'un bonus peut être distingué d'une boule ordinaire et d'un bonus à partir de sa couleur'''

    boule = Boule(500, 500)
    bonus = Bonus(500, 500)
    malus = Malus(500, 500)
    assert type(malus == Boule)
    assert malus.forme.color != boule.forme.color
    assert malus.forme.color != bonus.forme.color


def test_apparition_régulière_de_la_Boule():
    '''Vérifions que la boule apparaît chaque 5 secondes, ce qui revient à dire que la boule apparaît chaque 5 secondes.'''


    boule = Boule(500, 500)
    boule.compteur = random.randint(
        0, 5
    )  # L'attribut compteur5 de la boule est vaut initialement  0 est incrémenté de 1 chaque seconde et sa valeur est reinitialisée quand elle atteint 5.

    if boule.compteur != 5:
        boule1 = boule.redéfinir_régulièrement_boule(500, 500)
        assert boule1 is None
    else:
        boule1 = Boule(500, 500)
        assert not (boule1 is boule)


def test_collision():
    '''Vérifions que la méthode collision de la classe snake arrive à détecter les cas de collision dune boule avec la tête de snake'''

    snake = Snake(500, 500)
    # On sait qu'initialement le snake est au centre de l'éran et que son corps est constitué de 3 carrés de 20 pixels chacun; celui du milieu occupe exactement le centre de la fenêtre
    boule = Boule(500, 500)
    boule.forme.x = snake.head[0]
    boule.forme.y = snake.head[1]
    assert snake.collision(boule)


def test_effet_malus():
    '''vérifie que la vie du sanake diminue d'une unité quand il y a coollsion entre sa tête te malus.'''

    malus = Malus(500, 500)
    snake = Snake(500, 500)
    vie = int(snake.vie.text)
    malus.forme.x = (500 - 20) // 2
    malus.forme.y = (500 - 20) // 2 + 20
    snake.effet_collision_malus(malus)
    assert int(snake.vie.text) == vie - 1


def test_effet_boule():
    '''Vérifie que le sore augmante de 5 en cas de cpollision entre la tête du snake et la boule ordinaire.'''

    boule = Boule(500, 500)
    snake = Snake(500, 500)
    score = int(snake.score.text)
    boule.forme.x = (500 - 20) // 2
    boule.forme.y = (500 - 20) // 2 + 20
    snake.effet_collision_boule(boule)
    assert int(snake.score.text) == score + 5


def test_effet_bonus():
    '''Vérifie qu'en cas de  collision entre la tête du snake et un bonus, soit le sore augmente de 15 u soit la taille du snake est réduite de 5 unités'''
    bonus = Bonus(500, 500)
    snake = Snake(500, 500)
    score = int(snake.score.text)
    longueur = len(snake.snake_list)
    bonus.forme.x = (500 - 20) // 2
    bonus.forme.y = (500 - 20) // 2 + 20
    snake.effet_collision_bonus(bonus)
    assert int(snake.score.text) == score + 15 or len(snake.snake_list) == longueur - 5
