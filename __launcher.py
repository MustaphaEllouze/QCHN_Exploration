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
    map1,map2,
)

from Characters_input import (
    GROUP1,GROUP1_SMALL,GROUP2,GROUP2_SMALL,
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

groupe1 = False

if groupe1 : 
    window = ExplorationInterface(
                map=map2,
                group=GROUP1_SMALL,
                starting_point=(0,0),
                corresponding_map_point=(25,25),
                taille_h_scene=5000,
                taille_v_scene=5000,
                taille_h_view=2500,
                taille_v_view=2500,
                couleur=couleur
            )
else:
    window = ExplorationInterface(
                map=map1,
                group=GROUP2_SMALL,
                starting_point=(0,0),
                corresponding_map_point=(25,25),
                taille_h_scene=5000,
                taille_v_scene=5000,
                taille_h_view=2500,
                taille_v_view=2500,
                couleur=couleur
            )
window._begin_game()
window.show()
app.exec()