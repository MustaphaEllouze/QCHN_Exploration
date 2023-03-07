import sys

from PySide6.QtCore import (
    QSize,
    Qt,
    QPointF,
)

from PySide6.QtGui import (
    QAction,
    QPixmap,
    QColor,
    QPolygonF,
    QPen,
    QBrush,
    QFont,
)

from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QMainWindow,
    QLabel,
    QGraphicsScene,
    QGraphicsView,
)

from HexagonalMap import (
    WidgetHexMap,
)

from ExplorationManager import(
    ExplorationGameManager,
)

import math

class MainWindow(QMainWindow):
    def __init__(
        self,
    ):
        super().__init__()
        self.hex_map = WidgetHexMap(
            taille_h=720,
            taille_v=480,
            taille_hexa=40,
        )
        self.setCentralWidget(self.hex_map)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()