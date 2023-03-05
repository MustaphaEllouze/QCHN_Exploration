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
        ExplorationTerrain.arid_plains : 'images\\AridPlains_clean.png'
    }

    def __init__(
            self,
            managed_widget:WidgetHexMap,
            exploration_group:ExplorationGroup,
            exploration_map:ExplorationMap,
            hour:EDateTime=EDateTime(heure_depart=8,jour_depart=1),
            starting_point:tuple=(0,0),
    ):
        
        self.managed_game = ExplorationGame(
            exploration_group=exploration_group,
            exploration_map=exploration_map,
            hour=hour,
            starting_point=starting_point
        )

        self.managed_widget = managed_widget

    def reveal_hex(
            self,
            coord,
    ):
        self.managed_widget.draw_hex_from_coord(
            coord
        )
        self.managed_widget.draw_image_inside_hex(
            coord=coord,
            image_path=ExplorationGameManager.IMAGE_PATH[self.managed_game.terrain_at_coord(coord)]
        )

        
    def begin_game(
        self,
    ):
        self.reveal_hex(self.managed_game.starting_point)
        
        

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    a = WidgetHexMap(
        taille_h=1000,
        taille_v=1000,
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
    )

    manager.begin_game()

    app.exec()