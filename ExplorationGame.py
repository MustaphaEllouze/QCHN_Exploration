from Utility import (
    EDateTime,
)

from ExplorationItems import (
    ExplorationTerrain,
    ExplorationPlace,
)

class ExplorationMap : 
    """Représente une carte
    """
    def __init__(
            self,
            name,
            origin_hex = (0,0),
            origin_hex_type = ExplorationTerrain.plains,
    ):
        self.name = name
        self.origin_hex = origin_hex
        
        self.hexs = {}
        self.hexs[origin_hex] = origin_hex_type

    
    def define_N(
            self,
            ref_hex,
            hex_type,
    ):
        pass
    
    def define_NW(
            self,
            ref_hex,
            hex_type,
    ):
        pass
    
    def define_SW(
            self,
            ref_hex,
            hex_type,
    ):
        pass
    
    def define_NE(
            self,
            ref_hex,
            hex_type,
    ):
        pass
    
    def define_SE(
            self,
            ref_hex,
            hex_type,
    ):
        pass
    
    def define_N(
            self,
            ref_hex,
            hex_type,
    ):
        pass
    

class ExplorationGameManager:
    """Gère toutes les règles du jeu et les calculs
    """
    pass


if __name__ == '__main__':
    map = ExplorationMap(
        name='Scenario1',
        origin_hex=(0,0),
        origin_hex_type=ExplorationTerrain.plains,
    )
    print(map.__dict__)