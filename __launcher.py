import sys

from PySide6.QtWidgets import (
    QApplication,
)

from PySide6.QtGui import (
    QColor,
)

from MainWindow import(
    ExplorationInterface,
)

from ExplorationMaps_input import (
    map1,
)

from Characters_input import (
    GROUP1,
)

from Utility import (
    EDateTime,
)

import qdarktheme

app = QApplication(sys.argv)

darktheme = True

if darktheme : 
    qdarktheme.setup_theme()
    couleur = QColor('white')
else:
    couleur = QColor('black')

window = ExplorationInterface(
            map=map1,
            group=GROUP1,
            starting_point=(0,0),
            corresponding_map_point=(7,7),
            couleur=couleur
        )
window._begin_game()
window.show()
app.exec()