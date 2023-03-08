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
    QPushButton,
    QGridLayout,
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

        self.setWindowTitle('Exploration - JDR')

        # ------ PARAMETRES GENERAUX ----
        self.width_layoutv1 = 350
        self.width_layoutv3 = 200
        self.resize(QSize(self.width_layoutv1+taille_h_view+self.width_layoutv3+50,taille_v_view))
        self.setMinimumHeight(taille_v_view)
        self.setMinimumWidth(self.width_layoutv1+taille_h_view+self.width_layoutv3+50)

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
        
        self.layout_V2.addWidget(self.game_manager.managed_widget.view)

        self.layout_V2_H1 = QHBoxLayout()
        self.widget_layout_V2_H1 = QWidget()
        self.widget_layout_V2_H1.setLayout(self.layout_V2_H1)
        self.layout_V2.addWidget(self.widget_layout_V2_H1)
        self.zoom_in_button = QPushButton('Zoom')
        self.zoom_in_button.clicked.connect(self.game_manager.managed_widget.zoom_in)
        self.zoom_out_button = QPushButton('Dézoom')
        self.zoom_out_button.clicked.connect(self.game_manager.managed_widget.zoom_out)
        self.layout_V2_H1.addWidget(self.zoom_in_button)
        self.layout_V2_H1.addWidget(self.zoom_out_button)

        self.layout_V2_H2 = QHBoxLayout()
        self.widget_layout_V2_H2 = QWidget()
        self.widget_layout_V2_H2.setLayout(self.layout_V2_H2)
        self.layout_V2.addWidget(self.widget_layout_V2_H2)
        self.rot_ahor_button = QPushButton('Rot. Anti Horaire')
        self.rot_hor_button = QPushButton('Rot. Horaire')
        self.image_rose = QLabel()
        self.images_rose_cycle = [
            'images\\others\\rose_vents_clean_0deg.png',
            'images\\others\\rose_vents_clean_30deg.png',
            'images\\others\\rose_vents_clean_60deg.png',
            'images\\others\\rose_vents_clean_90deg.png',
            'images\\others\\rose_vents_clean_120deg.png',
            'images\\others\\rose_vents_clean_150deg.png',
            'images\\others\\rose_vents_clean_180deg.png',
            'images\\others\\rose_vents_clean_210deg.png',
            'images\\others\\rose_vents_clean_240deg.png',
            'images\\others\\rose_vents_clean_270deg.png',
            'images\\others\\rose_vents_clean_300deg.png',
            'images\\others\\rose_vents_clean_330deg.png',
        ]
        self.images_rose_cycle_index = 0
        self.set_image_rose_cycle()
        
        self.rot_ahor_button.clicked.connect(self.game_manager.managed_widget.rotate_anti_horaire)
        self.rot_ahor_button.clicked.connect(self.image_rose_cycle_anti)
        self.rot_hor_button.clicked.connect(self.game_manager.managed_widget.rotate_horaire)
        self.rot_hor_button.clicked.connect(self.image_rose_cycle)
        self.layout_V2_H2.addWidget(self.rot_ahor_button)
        self.layout_V2_H2.addWidget(self.rot_hor_button)
        self.layout_V2_H2.addWidget(self.image_rose)

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
        self.display_jour = QLabel()
        self.layout_v3_sub.addWidget(self.display_jour)

        self.layout_v3_sub.addWidget(ExplorationGame.h_line())
        
        # Heure
        self.display_heure = QLabel()
        self.layout_v3_sub.addWidget(self.display_heure)
        
        self.layout_v3_sub.addWidget(ExplorationGame.h_line())
    
        # Current hex
        self.display_current_hex = QLabel()
        self.layout_v3_sub.addWidget(self.display_current_hex)
        self.layout_v3_sub.addWidget(ExplorationGame.h_line())

        # Direction action
        self.direction_widget = QWidget()
        self.layout_v3_sub.addWidget(self.direction_widget)
        self.grid_direction = QGridLayout()
        self.direction_widget.setLayout(self.grid_direction)
        self.N  = QPushButton('N')
        self.N.clicked.connect(self.go_to_N)
        self.S  = QPushButton('S')
        self.S.clicked.connect(self.go_to_S)
        self.NE = QPushButton('NE')
        self.NE.clicked.connect(self.go_to_NE)
        self.NW = QPushButton('NW')
        self.NW.clicked.connect(self.go_to_NW)
        self.SE = QPushButton('SE')
        self.SE.clicked.connect(self.go_to_SE)
        self.SW = QPushButton('SW')
        self.SW.clicked.connect(self.go_to_SW)
        self.grid_direction.addWidget(self.N,0,1)
        self.grid_direction.addWidget(self.S,3,1)
        self.grid_direction.addWidget(self.NE,1,2)
        self.grid_direction.addWidget(self.NW,1,0)
        self.grid_direction.addWidget(self.SE,2,2)
        self.grid_direction.addWidget(self.SW,2,0)



    def h_line():
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        return line

    def update_widgets(self):
        self.display_jour.setText(f'Jour : {int(self.game_manager.managed_game.time.day)}')
        self.display_heure.setText(f'Heure : {self.game_manager.managed_game.time.str_without_day()}')
        self.display_current_hex.setText(f'Terrain : {self.game_manager.managed_game.current_terrain().name}')

    def go_to_N(self):
        self.game_manager.go_to_direction('N')
        self.update_widgets()

    def go_to_S(self):
        self.game_manager.go_to_direction('S')
        self.update_widgets()

    def go_to_NW(self):
        self.game_manager.go_to_direction('NW')
        self.update_widgets()

    def go_to_NE(self):
        self.game_manager.go_to_direction('NE')
        self.update_widgets()

    def go_to_SW(self):
        self.game_manager.go_to_direction('SW')
        self.update_widgets()

    def go_to_SE(self):
        self.game_manager.go_to_direction('SE')
        self.update_widgets()


    def set_image_rose_cycle(self):
        self.image_rose.setPixmap(QPixmap(self.images_rose_cycle[self.images_rose_cycle_index]).scaled(
        100, 
        100, 
        Qt.IgnoreAspectRatio,
        Qt.SmoothTransformation))
    
    def image_rose_cycle(self):
        self.images_rose_cycle_index = (self.images_rose_cycle_index-1)%(len(self.images_rose_cycle))
        self.set_image_rose_cycle()


    def image_rose_cycle_anti(self):
        self.images_rose_cycle_index = (self.images_rose_cycle_index+1)%(len(self.images_rose_cycle))
        self.set_image_rose_cycle()
   
    def _begin_game(self):
        self.game_manager.begin_game()
        self.update_widgets()