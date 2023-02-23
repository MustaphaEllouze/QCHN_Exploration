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

        # Trace les hexagones
        pass