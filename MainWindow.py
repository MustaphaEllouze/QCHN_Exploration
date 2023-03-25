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
    QIcon,
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
    QToolBar,
    QInputDialog,
)

from functools import (
    partial,
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

from ExplorationGroupSheet import (
    ExplorationGroupSheet,
)

from ExplorationSave import (
    ExplorationSave,
)

from Utility import (
    EDateTime,
)


class ExplorationInterface(QMainWindow):
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
        height_progress_bar=30,
        taille_police=15,
        police='Helvetica',
    ):
        super().__init__()

        self.setWindowTitle('Exploration - JDR')
        self.setWindowIcon(QIcon('images\\hex_images\\high_mountains.png'))

        # ------ PARAMETRES GENERAUX ----
        self.width_layoutv1 = 525
        self.width_layoutv3 = 325
        self.mini_height = min(
                max(
                    taille_v_view,
                    self.width_layoutv1+5*height_progress_bar+300,
                ),
                1000,
            )
        self.mini_width = min(
            self.width_layoutv1+taille_h_view+self.width_layoutv3+50,
            1750
        )
        self.resize(QSize(self.mini_width,self.mini_height))
        self.setMinimumHeight(self.mini_height)
        self.setMinimumWidth(self.mini_width)

        self._font = QFont(police,taille_police)

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
            managed_hex_map=self.main_hex_map_widget,
            exploration_group=group,
            exploration_map=map,
            hour=start_hour,
            starting_point=starting_point,
            corresponding_map_point=corresponding_map_point,
        )
        
        self.layout_V2.addWidget(self.game_manager.managed_hex_map.view)

        self.layout_V2_H1 = QHBoxLayout()
        self.widget_layout_V2_H1 = QWidget()
        self.widget_layout_V2_H1.setLayout(self.layout_V2_H1)
        self.layout_V2.addWidget(self.widget_layout_V2_H1)
        self.zoom_in_button = QPushButton('Zoom')
        self.zoom_in_button.clicked.connect(self.game_manager.managed_hex_map.zoom_in)
        self.zoom_out_button = QPushButton('Dézoom')
        self.zoom_out_button.clicked.connect(self.game_manager.managed_hex_map.zoom_out)
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
        
        self.rot_ahor_button.clicked.connect(self.game_manager.managed_hex_map.rotate_anti_horaire)
        self.rot_ahor_button.clicked.connect(self.image_rose_cycle_anti)
        self.rot_hor_button.clicked.connect(self.game_manager.managed_hex_map.rotate_horaire)
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
        
        for character in self.game_manager.managed_game.group.characters :
            tab_to_add = self.game_manager.managed_character_sheets[character.name]
            self.tab.addTab(tab_to_add,character.name)
            # ------ Monkey patching, il faudrait changer ce qui suit
            for button in tab_to_add.all_buttons:
                button.clicked.connect(self.update_widgets)
            # ------ Fin monkey-patching
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

        # Group Sheet
        self.layout_v3_sub.addWidget(self.game_manager.managed_group_sheet)
        self.layout_v3_sub.addWidget(ExplorationInterface.h_line())

        # Jour
        self.display_jour = self.game_manager.managed_day_widget
        self.display_jour.setFont(self._font)
        self.layout_v3_sub.addWidget(self.display_jour,Qt.AlignCenter)

        self.layout_v3_sub.addWidget(ExplorationInterface.h_line())
        
        # Heure
        self.display_heure = self.game_manager.managed_hour_widget
        self.display_heure.setFont(self._font)
        self.layout_v3_sub_day = QHBoxLayout()
        self.layout_v3_sub.addLayout(self.layout_v3_sub_day)
        self.layout_v3_sub_day.addWidget(self.display_heure)
        self.layout_v3_sub_day_buttons = QVBoxLayout()
        self.layout_v3_sub_day.addLayout(self.layout_v3_sub_day_buttons)
        self.layout_v3_sub_day_buttons.addWidget(self.game_manager.button_recorver_1hour)
        self.layout_v3_sub_day_buttons.addWidget(self.game_manager.button_recorver_15mn)
        self.layout_v3_sub_day_buttons.addWidget(self.game_manager.button_pass_15mn)
        self.layout_v3_sub_day_buttons.addWidget(self.game_manager.button_pass_1hour)
        
        self.layout_v3_sub.addWidget(ExplorationInterface.h_line())
    
        # Current hex
        self.display_current_hex = self.game_manager.managed_terrain_widget
        self.display_current_hex.setFont(self._font)
        self.layout_v3_sub.addWidget(self.display_current_hex,Qt.AlignCenter)
        self.layout_v3_sub.addWidget(ExplorationInterface.h_line())

        # Direction action
        self.direction_widget = QWidget()
        self.layout_v3_sub.addWidget(self.direction_widget)
        self.grid_direction = QGridLayout()
        self.direction_widget.setLayout(self.grid_direction)
        self.grid_direction.addWidget(self.game_manager.N,0,1)
        self.grid_direction.addWidget(self.game_manager.S,3,1)
        self.grid_direction.addWidget(self.game_manager.NE,1,2)
        self.grid_direction.addWidget(self.game_manager.NW,1,0)
        self.grid_direction.addWidget(self.game_manager.SE,2,2)
        self.grid_direction.addWidget(self.game_manager.SW,2,0)

        # -----------------------------------
        # ----------- MENU BAR --------------
        # -----------------------------------

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.show_summary = QAction('Résumé ', self)
        self.show_summary.setStatusTip('Résumé des caractéristiques du groupe')
        self.show_summary.setCheckable(True)
        self.show_summary.setChecked(True)
        self.window_summary_hidden = False
        
        self.show_summary.triggered.connect(self.create_summary)

        toolbar.addAction(self.show_summary)

        self.save_button = QAction('Sauver partie', self)
        self.save_button.setStatusTip('Sauver la partie')
        self.save_button.triggered.connect(self.save_game)
        toolbar.addAction(self.save_button)

    def save_game(self):
        path_file,sucess = QInputDialog.getText(
            self,
            'Sauver la partie',
            'Entrer le chemin du fichier',
        )
        if sucess :
            ExplorationSave.write_save(path_fichier=path_file)

    def create_summary(self):
        if self.window_summary_hidden:
            self.game_manager.managed_group_sheet.show()
            self.window_summary_hidden = False
        else:
            self.game_manager.managed_group_sheet.hide()
            self.window_summary_hidden = True

    def h_line():
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        return line

    def update_widgets(self):
        self.game_manager.update_managed_widgets()

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
    
    def _reveal_all_map(self):
        for hex in self.game_manager.managed_game.map.hexs:
            self.game_manager.reveal_hex(hex)