from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
)

from ExplorationCharacterSheet import (
    ExplorationCharacterSheet,
)

from ExplorationGroupSheet import (
    ExplorationGroupSheet,
)

from ExplorationItems import(
    ExplorationTerrain,
    ExplorationPlace,
)

from ExplorationMaps import (
    ExplorationMap,
)

from ExplorationCharacters import (
    ExplorationCharacter,
    ExplorationGroup,
)

from ExplorationGame import (
    ExplorationGame,
)

from HexagonalMap import (
    WidgetHexMap,
)

from Utility import (
    EDateTime,
)


class ExplorationGameManager:
    """Donne les ordres aux objets et widgets déja définis
    """
    
    IMAGE_PATH = {
        ExplorationTerrain.arid_plains  : 'images\\hex_images\\AridPlains_clean.png',
        ExplorationTerrain.plains       : 'images\\hex_images\\plains_clean.png',
        ExplorationTerrain.cliff        : 'images\\hex_images\\cliff_clean.png',
        ExplorationTerrain.forest       : 'images\\hex_images\\forest_clean.png',
        ExplorationTerrain.mountain     : 'images\\hex_images\\mountain_clean.png',
        ExplorationTerrain.high_mountain: 'images\\hex_images\\Hmountain_clean.png',
        ExplorationTerrain.beach        : 'images\\hex_images\\beach_clean.png',
        ExplorationTerrain.big_river    : 'images\\hex_images\\Briver_clean.png',
        ExplorationTerrain.desert       : 'images\\hex_images\\desert_clean.png',
        ExplorationTerrain.river        : 'images\\hex_images\\river_clean.png',
        ExplorationTerrain.sea          : 'images\\hex_images\\sea_clean.png',
    }

    def __init__(
            self,
            managed_hex_map:WidgetHexMap,
            exploration_group:ExplorationGroup,
            exploration_map:ExplorationMap,
            hour:EDateTime=EDateTime(heure_depart=8,jour_depart=1),
            starting_point:tuple=(0,0),
            corresponding_map_point:tuple=(0,0),
            width_character_sheets:int=500,
    ):
        
        # ---------- Définition du coeur de jeu : ExplorationGame
        if (corresponding_map_point[0]-starting_point[0])%2==0:
            self.decalage_x = corresponding_map_point[0]-starting_point[0]
        else:
            self.decalage_x = corresponding_map_point[0]-starting_point[0]+1
        self.decalage_y = corresponding_map_point[1]-starting_point[1]

        self.managed_game = ExplorationGame(
            exploration_group=exploration_group,
            exploration_map=exploration_map,
            hour=hour,
            starting_point=starting_point
        )

        # ---------- Définition des widgets managés
        
        # Widget central - Carte
        self.managed_hex_map = managed_hex_map

        # Widgets de droite - Date et temps, terrains
        self.managed_day_widget = QLabel()
        self.managed_hour_widget = QLabel()
        self.managed_terrain_widget = QLabel()

        # Widgets de droite - Aller dans une direction
        self.N  = QPushButton('N')
        self.S  = QPushButton('S')
        self.NE = QPushButton('NE')
        self.NW = QPushButton('NW')
        self.SE = QPushButton('SE')
        self.SW = QPushButton('SW')

        # Widget de droite - Boutons passage de temps
        self.button_recorver_1hour = QPushButton('- 1h')
        self.button_recorver_15mn = QPushButton('- 15mn')
        self.button_pass_15mn = QPushButton('+ 15mn')
        self.button_pass_1hour = QPushButton('+ 1h')

        # Widget de gauche - ExplorationCharacterSheet
        self.managed_character_sheets = {}
        for character in self.managed_game.group.characters:
            self.managed_character_sheets[character.name]=ExplorationCharacterSheet(
                character=character,
                image_path=f'images\\characters\\{character.name}.png',
                largeur=width_character_sheets,
            )
        
        # Widget résumé - ExplorationGroupSheet
        self.managed_group_sheet = ExplorationGroupSheet(
            group=self.managed_game.group,
        )

        # ---------- Connexion des Widgets

        # Widgets de droite - Boutons temps
        self.button_recorver_1hour.clicked.connect(lambda x :self.managed_game.time.go_back_hours(1))
        self.button_recorver_15mn.clicked.connect (lambda x :self.managed_game.time.go_back_minutes(15))
        self.button_pass_15mn.clicked.connect     (lambda x :self.managed_game.time.pass_minutes(15))
        self.button_pass_1hour.clicked.connect    (lambda x :self.managed_game.time.pass_hours(1))

        self.button_recorver_1hour.clicked.connect(self.update_managed_widgets)
        self.button_recorver_15mn.clicked.connect (self.update_managed_widgets)
        self.button_pass_15mn.clicked.connect     (self.update_managed_widgets)
        self.button_pass_1hour.clicked.connect    (self.update_managed_widgets)

        # Widget de droite - Aller dans une direction
        self.N.clicked.connect(lambda :self.go_to_direction('N'))
        self.S.clicked.connect(lambda :self.go_to_direction('S'))
        self.NE.clicked.connect(lambda :self.go_to_direction('NE'))
        self.NW.clicked.connect(lambda :self.go_to_direction('NW'))
        self.SE.clicked.connect(lambda :self.go_to_direction('SE'))
        self.SW.clicked.connect(lambda :self.go_to_direction('SW'))
        
        self.N.clicked.connect (self.update_managed_widgets)
        self.S.clicked.connect (self.update_managed_widgets)
        self.NE.clicked.connect(self.update_managed_widgets)
        self.NW.clicked.connect(self.update_managed_widgets)
        self.SE.clicked.connect(self.update_managed_widgets)
        self.SW.clicked.connect(self.update_managed_widgets)

        # ---------- Autres paramètres
        self.revealed_hexes = []
        self.visited_hexes = []

    def retrace_visited(
            self
    ):
        for hex_coord in self.visited_hexes:
            coord_widget = (
                    hex_coord[0]+self.decalage_x,
                    hex_coord[1]+self.decalage_y
                )
            self.managed_hex_map.draw_hex_from_coord(
                coord=coord_widget,
                secondary_pen=False,
            )

    def update_managed_widgets(self):
        # Time / Date / Terrain
        self.managed_day_widget.setText(f'Jour : {int(self.managed_game.time.day)}')
        self.managed_hour_widget.setText(f'Heure : {self.managed_game.time.str_without_day()}')
        self.managed_terrain_widget.setText(f'Terrain : {self.managed_game.current_terrain().name}')

        # Character sheets
        for character in self.managed_game.group.characters:
            self.managed_character_sheets[character.name].w_fatigue.set_current_value(character.CUR_FATIGUE)
            self.managed_character_sheets[character.name].w_hunger.set_current_value(character.CUR_HUNGER)
            self.managed_character_sheets[character.name].w_thirst.set_current_value(character.CUR_THIRST)
            self.managed_character_sheets[character.name].w_frost.set_current_value(character.CUR_FROST)
            self.managed_character_sheets[character.name].w_magic.set_current_value(character.CUR_MAGIC_FATIGUE)
            
            self.managed_character_sheets[character.name].w_fatigue.set_shield_value(character.SHIELD_FATIGUE)
            self.managed_character_sheets[character.name].w_hunger.set_shield_value(character.SHIELD_HUNGER)
            self.managed_character_sheets[character.name].w_thirst.set_shield_value(character.SHIELD_THIRST)
            self.managed_character_sheets[character.name].w_frost.set_shield_value(character.SHIELD_FROST)
            self.managed_character_sheets[character.name].w_magic.set_shield_value(character.SHIELD_MAGIC_FATIGUE)

        # Widget group Sheet
        self.managed_group_sheet.update_widgets()

        # Les boutons de direction 
        self.freeze_direction_buttons()

    def freeze_direction_buttons(self):
        pass
    
    def reveal_hex(
            self,
            coord,
            secondary_pen=False,
    ):
        if not coord in self.revealed_hexes : 
            coord_widget = (
                    coord[0]+self.decalage_x,
                    coord[1]+self.decalage_y
                )
            self.managed_hex_map.draw_hex_from_coord(
                coord=coord_widget,
                secondary_pen=secondary_pen,
            )
            self.managed_hex_map.draw_image_inside_hex(
                coord=coord_widget,
                image_path=ExplorationGameManager.IMAGE_PATH[self.managed_game.terrain_at_coord(coord)]
            )
            self.revealed_hexes.append(coord)

        
    def begin_game(
        self,
    ):
        self.visited_hexes.append(self.managed_game.starting_point)
        self.reveal_hex(self.managed_game.starting_point)
        if self.managed_game.current_terrain().can_see_surroundings :
            for hex_coord in self.managed_game.map.visibility[self.managed_game.current_point]:
                if hex_coord not in self.revealed_hexes : self.reveal_hex(hex_coord,secondary_pen=True)
        self.retrace_visited()
    
    def go_to_direction(
            self,
            direction='N',
    ):
        assert direction in ['N','S','NE','NW','SE','SW']

        self.managed_game.go_to_direction(direction=direction)
        self.visited_hexes.append(self.managed_game.current_point)
        self.reveal_hex(self.managed_game.current_point)
        # Pour voir ce qu'il y a autour
        if self.managed_game.current_terrain().can_see_surroundings :
            for hex_coord in self.managed_game.map.visibility[self.managed_game.current_point]:
                if hex_coord not in self.revealed_hexes : self.reveal_hex(hex_coord,secondary_pen=True)
        # Pour voir les objets éloignés, même lors que les terrains sont distants
        else:
            for hex_coord in self.managed_game.map.visibility[self.managed_game.current_point]:
                if hex_coord not in self.revealed_hexes and self.managed_game.terrain_at_coord(hex_coord).visibility_range>1 : 
                    self.reveal_hex(hex_coord,secondary_pen=True)
        self.retrace_visited()
    
    def change_carac_of_character(
            self,
            character:ExplorationCharacter,
            n:int,
            carac:str,
    ):
        character.change_carac(n=n,carac=carac)
    
    def change_shield_of_character(
            self,
            character:ExplorationCharacter,
            n:int,
            carac:str,
    ):
        character.change_shield(n=n,carac=carac)
    
    def freeze_direction_buttons(self):
        directions = self.managed_game.map.neighbours_of_hex(self.managed_game.current_point,direction_only=True)
        dir_buttons = {
            'N':self.N,
            'S':self.S,
            'NW':self.NW,
            'SW':self.SW,
            'NE':self.NE,
            'SE':self.SE,
        }
        for direction in ['N','S','NW','SW','NE','SE']:
            if direction not in directions:
                dir_buttons[direction].setDisabled(True)
            else:
                dir_buttons[direction].setEnabled(True)
    