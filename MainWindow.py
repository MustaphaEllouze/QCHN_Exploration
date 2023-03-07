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
    QVBoxLayout,
    QHBoxLayout,
    QTabWidget,
    QSizePolicy,
)

from HexagonalMap import (
    WidgetHexMap,
)

from ExplorationManager import(
    ExplorationGameManager,
)

from ExplorationMaps import (
    ExplorationMap,
)

from ExplorationCharacters import (
    ExplorationGroup,
)

from Utility import (
    EDateTime,
)


class ExplorationGame(QMainWindow):
    def __init__(
        self,
        map:ExplorationMap,
        group:ExplorationGroup,
        start_hour:EDateTime=EDateTime(heure_depart=8,jour_depart=1),
        starting_point:tuple=(0,0),
        corresponding_map_point:tuple=(0,0),
        taille_h_scene=1000,
        taille_v_scene=1000,
        taille_h_view=500,
        taille_v_view=500,
        taille_hexa=50,
        couleur=QColor('black'),
        couleur_secondaire=QColor('red'),
        epaisseur=1,
    ):
        super().__init__()

        # ------ WIDGET PARENT ----------
        # Widget virtuel 
        # -------------------------------
        self.widget_central = QWidget()
        self.setCentralWidget(self.widget_central)
        self.layout_H = QHBoxLayout()
        self.layout_V1 = QVBoxLayout()
        self.layout_V2 = QVBoxLayout()
        self.layout_V3 = QVBoxLayout()
        self.layout_H.addLayout(self.layout_V1)
        self.layout_H.addLayout(self.layout_V2)
        self.layout_H.addLayout(self.layout_V3)
        self.widget_central.setLayout(self.layout_H)

        # ------ WIDGET CENTRAL ---------
        # Interface de jeu
        # -------------------------------

        self.main_hex_map_widget = WidgetHexMap(
            taille_h_scene=taille_h_scene,
            taille_v_scene=taille_v_scene,
            taille_h_view=taille_h_view,
            taille_v_view=taille_v_view,
            taille_hexa=taille_hexa,
            couleur=couleur,
            couleur_secondaire=couleur_secondaire,
            epaisseur=epaisseur,
        )
        self.game_manager = ExplorationGameManager(
            managed_widget=self.main_hex_map_widget,
            exploration_group=group,
            exploration_map=map,
            hour=start_hour,
            starting_point=starting_point,
            corresponding_map_point=corresponding_map_point,
        )
        
        self.layout_V2.addWidget(self.game_manager.managed_widget)

        # ------ WIDGET GAUCHE ---------
        # Interface de description des personnages
        # -------------------------------
        self.tab = QTabWidget()
        self.tab.setTabPosition(QTabWidget.West)
        self.tab.setMovable(True)
        for character in group.characters:
            self.tab.addTab(QLabel(character.name),character.name)
        self.layout_V1.addWidget(self.tab)
        self.tab.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Ignored)

    
    def _begin_game(self):
        self.game_manager.begin_game()