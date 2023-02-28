from math import (
    cos,
    sin,
    pi,
)

from PySide6.QtCore import (
    QPointF,
)

from PySide6.QtGui import (
    QPolygonF,
)

class Point :
    """Représente un point
    """
    def __init__(
        self,
        x,
        y,
    ):
        """Constructeur

        Args:
            x (float): coordonnée x
            y (float): coordonnée y
        """
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
        """Constructeur

        Args:
            centre (Point, optional): Centre de l'hexagone. Defaults to Point(0.0,0.0).
            rayon (float, optional): Rayoun du cercle circonscrit. Defaults to 1.0.
        """
        self.centre = centre
        self.rayon=rayon
    
    def sommets(
        self,
    ):
        """Retourne les points des sommets de l'hexagone

        Returns:
            list(Point): Sommets de l'hexagone
        """
        if Hexagon.orientation == 'H'   : decal = 0.0
        elif Hexagon.orientation == 'V' : decal = pi/6.0
        else : raise Exception('Hexagon.orientation : invalid value')

        # --- Variable de retour
        return [
            Point(
                self.centre.x + cos(k*pi/3.0+decal) * self.rayon,
                self.centre.y + sin(k*pi/3.0+decal) * self.rayon,
            )
            for k in range(6)
        ]
    
    def convert_to_polygon(self):
        """Convertir l'Hexagon en PySide6.QtGui.QPolygonF

        Returns:
            _type_: _description_
        """
        polygon = QPolygonF()
        for s in self.sommets():
            polygon.append(QPointF(s.x,s.y))
        return polygon

if __name__ == '__main__':
    h = Hexagon(centre=Point(5,7),rayon=1.0)
    for elem in h.sommets() : print(elem)
    print(h.convert_to_polygon())
