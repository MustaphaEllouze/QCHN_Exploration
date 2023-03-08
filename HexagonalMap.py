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
    QPointF,
    QRectF,
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
            taille_h_scene=480,
            taille_v_scene=600,
            taille_h_view=480,
            taille_v_view=600,
            taille_hexa=40, 
            couleur= QColor('black'),
            couleur_secondaire=QColor('red'),
            epaisseur = 1,
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
        self.h = taille_h_scene
        self.v = taille_v_scene
        self.h_view = taille_h_view
        self.v_view = taille_v_view

        # Les painters
        self.pen = QPen(couleur)
        self.pen.setWidth(epaisseur)
        self.pen_secondaire=QPen(couleur_secondaire)
        self.pen_secondaire.setWidth(epaisseur)

        # Crée la scène
        self.scene = QGraphicsScene()

        # Crée la vue
        self.view = QGraphicsView(self.scene,parent=self)
        # self.view.setGeometry(0,0,self.h_view,self.v_view)

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
    
    def draw_hexs(self,secondary_pen=False):
        if secondary_pen:
            pen_to_use = self.pen_secondaire
        else:
            pen_to_use = self.pen
        # --- Trace les hexagones
        for coord,hex in self.hexs.items():
            self.scene.addPolygon(hex.convert_to_polygon(),pen=pen_to_use)
    
    def draw_hex_from_coord(
            self,
            coord,
            secondary_pen=False,
    ):
        if secondary_pen:
            pen_to_use = self.pen_secondaire
        else:
            pen_to_use = self.pen
        assert coord in self.hexs.keys()
        self.scene.addPolygon(self.hexs[coord].convert_to_polygon(),pen=pen_to_use)
    
    def draw_image_inside_hex(
            self,
            coord:tuple,
            image_path:str,
    ):
        d_cercle_inscrit = self.r_hexa*(3**0.5)
        pixmap = QPixmap(image_path).scaled(
            2*self.r_hexa, 
            d_cercle_inscrit, 
            Qt.IgnoreAspectRatio,
            Qt.SmoothTransformation)

        p = QPointF(
            self.centres[coord][0]-self.r_hexa,
            self.centres[coord][1]-0.5*d_cercle_inscrit,
        )
        image_placed = self.scene.addPixmap(pixmap)
        image_placed.setPos(p)
    
    def zoom_in(self):
        self.view.scale(1.1,1.1)

    def zoom_out(self):
        self.view.scale(0.9,0.9)
    
    def rotate_horaire(self):
        self.view.rotate(30)

    def rotate_anti_horaire(self):
        self.view.rotate(-30)
        
        
if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    a = WidgetHexMap(
        taille_h_scene=2000,
        taille_v_scene=2000,
        taille_h_view=750,
        taille_v_view=750,
    )
    a.draw_hex_from_coord((0,0))
    a.draw_image_inside_hex((0,0),'images\\AridPlains_clean.png')
    a.show()
    app.exec()