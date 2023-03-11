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
    """Donne les ordres aux objets déja définis
    """
    
    IMAGE_PATH = {
        ExplorationTerrain.arid_plains  : 'images\\hex_images\\AridPlains_clean.png',
        ExplorationTerrain.plains       : 'images\\hex_images\\plains.png',
        ExplorationTerrain.cliff        : 'images\\hex_images\\cliff.png',
        ExplorationTerrain.forest       : 'images\\hex_images\\forest.png',
        ExplorationTerrain.mountain     : 'images\\hex_images\\mountains.png',
        ExplorationTerrain.high_mountain: 'images\\hex_images\\high_mountains.png',
        ExplorationTerrain.beach        : 'images\\hex_images\\beach.png',
        ExplorationTerrain.big_river    : 'images\\hex_images\\big_river.png',
        ExplorationTerrain.desert       : 'images\\hex_images\\desert.png',
        ExplorationTerrain.river        : 'images\\hex_images\\river.png',
        ExplorationTerrain.sea          : 'images\\hex_images\\sea.png',
    }

    def __init__(
            self,
            managed_widget:WidgetHexMap,
            exploration_group:ExplorationGroup,
            exploration_map:ExplorationMap,
            hour:EDateTime=EDateTime(heure_depart=8,jour_depart=1),
            starting_point:tuple=(0,0),
            corresponding_map_point:tuple=(0,0),
    ):
        
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

        self.managed_widget = managed_widget

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
            self.managed_widget.draw_hex_from_coord(
                coord=coord_widget,
                secondary_pen=False,
            )

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
            self.managed_widget.draw_hex_from_coord(
                coord=coord_widget,
                secondary_pen=secondary_pen,
            )
            self.managed_widget.draw_image_inside_hex(
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
        if self.managed_game.current_terrain().can_see_surroundings :
            for hex_coord in self.managed_game.map.visibility[self.managed_game.current_point]:
                if hex_coord not in self.revealed_hexes : self.reveal_hex(hex_coord,secondary_pen=True)
        self.retrace_visited()
        

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    from PySide6.QtGui import QColor
    
    app = QApplication(sys.argv)
    a = WidgetHexMap(
        taille_h_scene=2000,
        taille_v_scene=2000,
        taille_h_view=750,
        taille_v_view=750,
        couleur=QColor('black'),
        couleur_secondaire=QColor('red')
    )
    a.show()
    
    from Race import Race
    from Class import Class
    from ExplorationMaps_input import map1

    char1 = ExplorationCharacter(
    name='Spirale',
    race=Race.aven_WIS,
    classe=Class.rogue_CHR,
    base_strength=12,
    base_charisma=13,
    base_constitution=9,
    base_dexterity=16,
    base_intelligence=10,
    base_wisdwom=11,
    )

    group = ExplorationGroup(exploration_characters=[char1],name='group1')
    
    manager = ExplorationGameManager(
        a,
        exploration_group=group,
        exploration_map=map1,
        starting_point=(0,0),
        corresponding_map_point=(10,10)
    )

    manager.begin_game()
    manager.go_to_direction(direction='N')
    manager.go_to_direction(direction='NW')
    manager.go_to_direction(direction='NW')
    manager.go_to_direction(direction='N')
    app.exec()