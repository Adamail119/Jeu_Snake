from boule import Boule


class Malus(Boule):
    '''Représente le malus; il hérite de la classe Boule.

    Specific Attributes
    -------------------
    forme : Circle
        Un disque de rayon 40 pixels et de couleur bleue créé à une position aléatoire dans la fenêtre.

     Methods
    -------
    __init__(self, indow_width, window_heigth):
        hérite de la méthode __init__() de la classe boule et crée à une position aléatoire de la fenêtre un objet de type Bonus.
    '''
    def __init__(self, window_width, window_heigth):
        ''' Hérite de la méthode __init__() de la classe boule et crée à une position aléatoire de la fenêtre un objet de type Malus.
        Parameters
        ----------
        window_didth : float
            La largeur de la fenêtre 
        window_heigth: float
            la hauteur de la fenêtre
        '''
        super().__init__(window_width, window_heigth)
        self.forme.color = (255, 0, 0)
