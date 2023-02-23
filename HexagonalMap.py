from PySide6.QtWidgets import (
    QLabel,
)

from PySide6.QtGui import (
    QPixmap,
)

from PySide6.QtCore import (
    Qt,
)

from Geometry import (
    Hexagon,
)

class WidgetDessin(QLabel):
    """Crée un dessin vierge, surlequel on peut dessiner
    """
    def __init__(
        self,
        taille_h = 400,
        taille_v = 400,          
    ):
        """
            taille_h (int, optional): Taille horizontale. Defaults to 400.
            taille_v (int, optional): Taille verticale. Defaults to 400.
        """
        super().__init__()
        self.h = taille_h
        self.v = taille_v
        self.canevas = QPixmap(taille_h,taille_v)
        self.canevas.fill(Qt.white)
        self.setPixmap(self.canevas)

class WidgetHexagonalMap(WidgetDessin):
    def __init__(self,
                taille_h=400,
                taille_v=400,
                taille_hexa = 40,
                ):
        super().__init__(taille_h, taille_v)

        # --- Rayon du cercle circonscrit
        self.r_hexa = taille_hexa

        # --- Distance entre les centres
        dist_deux_centres_h = taille_hexa*(2.0+2**0.5/3)
        dist_deux_centres_v = taille_hexa*(2*(2**0.5)/3)

        # --- Nombre d'hexagones à placer
        self.nb_hex_h = 1+int(2*self.h/dist_deux_centres_h)
        self.nb_hex_v = 1+int(self.v/dist_deux_centres_v)

        # --- Initialise les centres
        self.centres = {}
        self.centres[(0,0)] = (0.0,0.0)
        self.centres[(1,0)] = (
            self.centres[(0,0)][0]+dist_deux_centres_h-taille_hexa,
            self.centres[(0,0)][1]+0.5*dist_deux_centres_v,
        )
        # --- Calcule les deux premières colonnes de centres
        for i in [0,1]:
            for j in range(1,self.nb_hex_v):
                self.centres[(i,j)]=(
                    self.centres[(i,j-1)][0],
                    self.centres[(i,j-1)][1]+dist_deux_centres_v,
                )
        # --- Calcule le reste des colonnes par translation
        for i in range(2,self.nb_hex_h):
            for j in range(self.nb_hex_v):
                self.centres[(i,j)]=(
                    self.centres[(i-2),j][0]+dist_deux_centres_h,
                    self.centres[(i-2),j][1],    
                )
        
        # --- Crée les hexagones
        self.hexs = {}
        for coord in self.centres:
            self.hexs[coord] = Hexagon(
                centre=self.centres[coord],
                rayon=taille_hexa
            )


        

    
if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    a = WidgetHexagonalMap(
        taille_h=200,
        taille_v=400,
        taille_hexa=40,
    )
    print(a.__dict__)