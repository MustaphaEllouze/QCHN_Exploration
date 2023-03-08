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
    QFrame,
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

from ExplorationCharacterSheet import (
    ExplorationCharacterSheet,
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

        # ------ PARAMETRES GENERAUX ----
        self.width_layoutv1 = 350
        self.width_layoutv3 = 200
        self.resize(QSize(self.width_layoutv1+taille_h_view+self.width_layoutv3+50,taille_v_view))

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
        self.character_description = {}
        for character in group.characters:
            self.character_description[character.name] = ExplorationCharacterSheet(
                character=character,
                image_path=f'images\\characters\\{character.name}.png',
                largeur=self.width_layoutv1
            )
            self.tab.addTab(self.character_description[character.name],character.name)
        self.layout_V1.addWidget(self.tab)
        self.tab.setFixedWidth(self.width_layoutv1)
        self.tab.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Ignored)

        # ------ WIDGET DROITE ----------
        # Informations diverses
        # -------------------------------
        
        self.right_widget = QWidget()
        self.layout_v3_sub = QVBoxLayout()
        self.right_widget.setLayout(self.layout_v3_sub)
        self.right_widget.setFixedWidth(self.width_layoutv3)
        self.layout_V3.addWidget(self.right_widget)

        # Jour
        self.layout_v3_sub.addWidget(QLabel(f'Jour : {self.game_manager.managed_game.time.day}'))

        self.layout_v3_sub.addWidget(ExplorationGame.h_line())
        
        # Heure
        self.layout_v3_sub.addWidget(QLabel(f'Heure : {self.game_manager.managed_game.time.str_without_day()}'))
        
        self.layout_v3_sub.addWidget(ExplorationGame.h_line())
    
        # Current hex
        self.layout_v3_sub.addWidget(QLabel(f'Terrain : {self.game_manager.managed_game.current_terrain().name}'))

    def h_line():
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        return line
   
    def _begin_game(self):
        self.game_manager.begin_game()