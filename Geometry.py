from math import (
    cos,
    sin,
    pi,
)

class Point :
    """Représente un point
    """
    def __init__(
        self,
        x,
        y,
    ):
        self.x = x
        self.y = y

    def __str__(
        self,
    ):
        return f'({self.x},{self.y})'
        

class Hexagon:
    """Représente un héxagone
    """

    orientation = 'H'           # H ou V

    def __init__(
        self,
        centre=Point(0.0,0.0),
        rayon=1.0
    ):
        self.centre = centre
        self.rayon=rayon
    
    def sommets(
        self,
    ):
        if Hexagon.orientation == 'H'   : decal = 0.0
        elif Hexagon.orientation == 'V' : decal = pi/6.0
        else : raise Exception('Hexagon.orientation : invalid value')

        return [
            Point(
                self.centre.x + cos(k*pi/3.0+decal) * self.rayon,
                self.centre.y + sin(k*pi/3.0+decal) * self.rayon,
            )
            for k in range(6)
        ]

h = Hexagon(centre=Point(5,7),rayon=1.0)
for elem in h.sommets() : print(elem)
