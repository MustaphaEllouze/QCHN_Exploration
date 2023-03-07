import sys

from PySide6.QtWidgets import (
    QApplication,
)

from MainWindow import(
    ExplorationGame,
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


app = QApplication(sys.argv)
window = ExplorationGame(
            map=map1,
            group=GROUP1,
            starting_point=(0,0),
            corresponding_map_point=(10,10),
        )
window._begin_game()
window.show()
app.exec()