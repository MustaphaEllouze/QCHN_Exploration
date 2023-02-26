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
            hex_type=ExplorationTerrain.plains,
            hex_place=None,
    ):
        assert hex_place is None or type(hex_place) is ExplorationPlace

        self.hexs[coord] = hex_type
        if not hex_place is None :
            self.places[coord]=hex_place 
    
    def define_from_coord_and_tag(
            self,
            coord,
            hex_type=ExplorationTerrain.plains.tag_name,
            hex_place=None,
            
    ):
        self.define_from_coord(
            coord=coord,
            hex_type=ExplorationTerrain.TERRAINS_FROM_TAG[hex_type],
            hex_place=ExplorationPlace.PLACES_FROM_TAG[hex_place],
        )

    def define_from_ref(
            self,
            ref_hex,
            hex_type=ExplorationTerrain.plains,
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
            decal = ( 1, 0)
        elif direction == 'NW':
            decal = (-1,-1)
        elif direction == 'SW':
            decal = (-1, 0)
        
        target_hex = (
            ref_hex[0]+decal[0],
            ref_hex[1]+decal[1],
        )

        self.hexs[target_hex]=hex_type
        if not hex_place is None :
            self.places[target_hex]=hex_place 
    
    def define_from_ref_and_tag(
            self,
            ref_hex,
            hex_type='P',
            direction='N',
            hex_place=None,
    ):
        self.define_from_ref(
            ref_hex=ref_hex,
            hex_type=ExplorationTerrain.TERRAINS_FROM_TAG[hex_type],
            direction=direction,
            hex_place=ExplorationPlace.PLACES_FROM_TAG[hex_place],
        )

    def define_column(
            self,
            column_number=0,
            starting_index=0,
            hex_types=[],
            reverse=False,
    ):
        if reverse : reverse_coef = -1
        else: reverse_coef = 1

        for j,coord in enumerate([(column_number,starting_index+i*reverse_coef) for i in range(len(hex_types))]):
            self.define_from_coord(coord=coord,hex_type=hex_types[j])
    
    def define_list_of_coords(
            self,
            list_of_coords = [],
            hex_type=ExplorationTerrain.plains,
            hex_place=None,
    ):
        for coord in list_of_coords:
            self.define_from_coord(
                coord=coord,
                hex_type=hex_type,
                hex_place=hex_place
            )
    
    def define_list_of_coords_with_tag(
            self,
            list_of_coords=[],
            hex_type=ExplorationTerrain.plains.tag_name,
            hex_place=None,
    ):
        for coord in list_of_coords:
            self.define_from_coord_and_tag(
                coord=coord,
                hex_type=hex_type,
                hex_place=hex_place,
            )

    def bounding_box(self):
        min_x = min([coord[0] for coord in self.hexs.keys()])
        max_x = max([coord[0] for coord in self.hexs.keys()])
        min_y = min([coord[1] for coord in self.hexs.keys()])
        max_y = max([coord[1] for coord in self.hexs.keys()])
        return min_x,max_x,min_y,max_y
    
    def generate_numpy_like(self):
        min_x,max_x,min_y,max_y = self.bounding_box()
        result = [['  ' for i in range((max_x-min_x+1))] for j in range((max_y-min_y+1))]
        for coord,hex_type in self.hexs.items():
            result[coord[1]-min_y][coord[0]-min_x]=hex_type.tag_name
        return result
    
    def __str__(self):
        result = ''
        for ligne in self.generate_numpy_like():
            for c in ligne:
                result += c+';'
            result += '\n'
        return result
    

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
    map.define_from_ref(map.origin_hex,ExplorationTerrain.plains,direction='S',hex_place=None)
    map.define_from_coord((1,1),ExplorationTerrain.plains,hex_place=ExplorationPlace.village)
    map.define_from_ref((1,1),ExplorationTerrain.plains,direction='S',hex_place=None)
    print(map.__dict__)