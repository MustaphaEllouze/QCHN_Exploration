from PySide6.QtWidgets import (
    QLabel,
    QGraphicsView,
    QGraphicsScene,
    QWidget,
)

from PySide6.QtGui import (
    QPixmap,
    QPen,
    QColor,
    QPainter,
    QBrush,
)

from PySide6.QtCore import (
    Qt,
)

from Geometry import (
    Hexagon,
    Point,
)

class WidgetHexMap(QWidget):
    """Widget de carte hexagonale
    """
    def __init__(
            self,
            taille_h=480,
            taille_v=600,
            taille_hexa=40, 
            couleur= QColor('black'),
            epaisseur = 5,
    ):
        """Constructeur

        Args:
            taille_h (int, optional): Taille horizontale. Defaults to 480.
            taille_v (int, optional): Taille verticale. Defaults to 600.
            taille_hexa (int, optional): Taille des hexagones (distance centre-sommet). Defaults to 40.
            couleur (_type_, optional): Couleur de tracé. Defaults to QColor('black').
            epaisseur (int, optional): Epaisseur du tracé. Defaults to 5.
        """
        super().__init__()

        #Attributs
        self.h = taille_h
        self.v = taille_v

        # Les painters
        self.pen = QPen(couleur)
        self.pen.setWidth(epaisseur)

        # Crée la scène
        self.scene = QGraphicsScene()

        # Crée la vue
        self.view = QGraphicsView(self.scene,parent=self)
        self.view.setGeometry(0,0,self.h,self.v)

        # --- Rayon du cercle circonscrit
        self.r_hexa = taille_hexa

        # --- Distance entre les centres
        dist_deux_centres_h = 3*taille_hexa
        dist_deux_centres_v = taille_hexa*(2*(3**0.5)/2)

        # --- Nombre d'hexagones à placer
        self.nb_hex_h = 1+int(2*self.h/dist_deux_centres_h)
        self.nb_hex_v = 1+int(self.v/dist_deux_centres_v)

        # --- Initialise les centres
        self.centres = {}
        self.centres[(0,0)] = (0.0,0.0)
        self.centres[(1,0)] = (
            self.centres[(0,0)][0]+0.5*dist_deux_centres_h,
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
                centre=Point(*self.centres[coord]),
                rayon=taille_hexa
            )
        
        # --- Trace les hexagones
        for coord,hex in self.hexs.items():
            self.scene.addPolygon(hex.convert_to_polygon())
        
if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    a = WidgetHexMap(
        taille_h=1000,
        taille_v=1000,
    )
    a.show()
    app.exec()