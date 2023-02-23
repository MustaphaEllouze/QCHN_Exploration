import sys

from PySide6.QtCore import (
    QSize,
    Qt,
)

from PySide6.QtGui import (
    QAction,
    QPixmap,
)

from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QMainWindow,
    QLabel,
)

from HexagonalMap import (
    WidgetHexagonalMap
)

class MainWindow(QMainWindow):
    def __init__(
        self,
    ):
        super().__init__()
        self.widget_dessin = WidgetHexagonalMap(taille_h=200,taille_v=400,taille_hexa=40)
        self.setCentralWidget(self.widget_dessin)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()