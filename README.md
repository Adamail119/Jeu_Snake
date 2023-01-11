# Jeu du snake



## Prérequis & Installation 

Pour utiliser ce projet, vous avez besoin de :

- Une version de python,  de préférence python3
- Bibliothèques: random, pyglet, 

## Fonctionnalités

### Classe Snake

#####   __init__(self, window_width, window_heigth):
        Crée un objet de type Snake à une position aléatoire de la fenêtre dont les dimensions sont passées en paramètre.

#### draw_our snake(self):
        Dessine le snake dans la fenêtre.

#### déplacement(self):
        Assure le déplacement continuel du snake dans la fenêtre.

#### auto_collision(self, snake_list, dist_head=0, auto_collision=False):
        Détecte les cas de coïncidence de la tête du snake avec une autre partie de son corps.

#### effet_bonus(self, bonus, window_width=1000):
        Assure que le bonus disparaît en cas de collision avec la tête du snake et que soit le score augmente de 15 soit la taille du snake est réduite de 5 unités.

#### effet_malus(self,malus, window_width=1000):
        Assure que le malus disparaît de la fenêtre en cas de collision avec la tête du snake et que la vie du snake est réduite d'une unité.

#### effet_boule(self, boule, window_width=1000):
        Assure que le boule ordinaire disparaît en cas de collision avec la tête du snake et que le score augmente de 5 unités.
    
#### collision(self, boule):
         Détecte les cas de collision entre la tête du snake et la boule

#### redéfinir_boule(self, window_width, window_heigth, boule=None):
        Permet de redéfinir l'objet boule à une nouvelle position quand on le souhaite. Elle est utilisée pour redéfinir les boules coïncident avec le snake de sortes qu'aucune boule n'est aperçu sur le snake.

### Classe Boule

#### __init__(self, window_width, window_heigth):
        Crée un objet de type Boule à une position aléatoire de la fenêtre dont les dimensions sont passées en paramètre.
    
#### draw(self):
        Dessine la boule dans la fenêtre
    
#### détection_de_boule_sur_snake(self, snake_list, collision_généralisée=False):
        permet de détecter les boules créées dont une partie coïncide avec un carreau du snake

#### redéfinir_régulièrement_boule(self, window_width, window_heigth, boule=None):
        Permet de redéfinir l'objet boule à une nouvelle position dans la fenêtre à chaque fois que le compteur atteint 5 de sorte qu'une nouvelle boule apparaît et disparaît de la fenêtre chaque 5 secondes.

#### redéfinir_boule(self, window_width, window_heigth, boule=None):
        Permet de redéfinir l'objet boule à une nouvelle position quand on le souhaite. Elle est utilisée pour redéfinir les boules coîncident avec le snake de sortes qu'aucune boule n'est apercu sur le snake.


### Classe Fenêtre

#### fin_jeu: 
        Permet d'arrêter le jeu quand l'une des conditions d'arrêt est vérifiée.
    
#### apparition_du_malus(self, dt):
        permet de recréer l'objet malus chaque 17 secondes.

#### apparition_du_bonus(self, dt): 
        permet de recréer l'objet bonus chaque 19 secondes.

#### effet_boule_bonus_malus:
        permet d'activer les effets des différentes boules en cas de collision avec la tête du snake.

#### on_key_press:
        permet de gérer les changements de direction du snake et l'empêche d'aller à l'opposé de sa direction actuelle.
    
#### update_2:
        permet de faire augmenter le score de 1 chaque seconde et de faire incrémenter les compteurs qui gèrent le temps d'apparition des des boules.

#### draw:
        Permet de représenter les différents objets dans la fenêtre.
 
#### update: 
        permet de réactualiser la taille du snake et de le redessiner après chaque déplacement.


## Utilisation 

Pour utiliser ce projet, suivez ces étapes:

Ouvrez un terminal et naviguez jusqu'au répertoire du projet.
Utilisez la commande python `main.py` pour lancer le jeu.
Utilisez la commande `python -m pytest` pour exécuter l'ensemble des test

<img src="image.jpg" width="500" height="150" />
## Crédits

Membres de l'équipe projet:
### Boro Adama
### Yeboua kouamé Franck
### Akharmouch Mohamed
### Méa Mounou Akoua Grace-Marie


## License

Informations sur la license du projet.
