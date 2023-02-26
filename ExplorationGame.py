from Utility import (
    EDateTime,
)

from ExplorationItems import (
    ExplorationTerrain,
    ExplorationPlace,
)

from ExplorationMaps import (
    PLAINS,CLIFF,ARID_PLAINS,FOREST,RIVER,BIG_RIVER,
    MOUNTAINS,DESERT,HIGH_MOUNTAIN,SEA,
    CRISTAL,VILLAGE,
)

class ExplorationMap : 
    """Représente une carte
    """
    def __init__(
            self,
            name,
            origin_hex = (0,0),
            origin_hex_type = PLAINS,
            origin_hex_place = None,
    ):
        
        assert origin_hex_place is None or type(origin_hex_place) is ExplorationPlace

        self.name = name
        self.origin_hex = origin_hex
        
        self.hexs = {}
        self.hexs[origin_hex] = origin_hex_type

        self.places = {}
        if not origin_hex_place is None:
            self.places[origin_hex]=origin_hex_place

    
    def define_from_coord(
            self,
            coord,
            hex_type=PLAINS,
            hex_place=None,
    ):
        assert hex_place is None or type(hex_place) is ExplorationPlace

        self.hexs[coord] = hex_type
        if not hex_place is None :
            self.places[coord]=hex_place 

    
    def define_from_ref(
            self,
            ref_hex,
            hex_type=PLAINS,
            direction='N',
            hex_place=None,
    ):
        assert direction in ['N','S','NE','SE','NW','SW']
        assert hex_place is None or type(hex_place) is ExplorationPlace

        if direction == 'N':
            decal = ( 0,-1)
        elif direction == 'S':
            decal = ( 0, 1)
        elif direction == 'NE':
            decal = ( 1,-1)
        elif direction == 'SE':
            decal = ( 1, 1)
        elif direction == 'NW':
            decal = (-1,-1)
        elif direction == 'SW':
            decal = (-1,-1)
        
        target_hex = (
            ref_hex[0]+decal[0],
            ref_hex[1]+decal[1],
        )

        self.hexs[target_hex]=hex_type
        if not hex_place is None :
            self.places[target_hex]=hex_place 
    

class ExplorationGameManager:
    """Gère toutes les règles du jeu et les calculs
    """
    pass


if __name__ == '__main__':
    map = ExplorationMap(
        name='Scenario1',
        origin_hex=(0,0),
        origin_hex_type=PLAINS,
    )
    map.define_from_ref(map.origin_hex,PLAINS,direction='S',hex_place=None)
    map.define_from_coord((1,1),PLAINS,hex_place=VILLAGE)
    map.define_from_ref((1,1),MOUNTAINS,direction='S',hex_place=None)
    print(map.__dict__)