from ExplorationCharacters import (
    ExplorationGroup,
    ExplorationCharacter,
)

from ExplorationItems import (
    ExplorationTerrain,
)

from ExplorationMaps import(
    ExplorationMap,
)

from Utility import (
    EDateTime,
)

class ExplorationGame:
    def __init__(
            self,
            exploration_group:ExplorationGroup,
            exploration_map:ExplorationMap,
            hour:EDateTime,
            starting_point:tuple=(0,0),
    ):
        self.group = exploration_group
        self.map = exploration_map
        self.time = hour
        self.starting_point = starting_point
        self.current_point = self.starting_point

        self.revealed_hexs = {coord:False for coord in self.map.hexs.keys()}
        self.revealed_hexs[self.starting_point]=True
    
    def terrain_at_coord(
            self,
            coord:tuple,
    )->ExplorationTerrain:
        return self.map.hexs[coord]

    def current_terrain(
            self,
    )->ExplorationTerrain:
        return self.terrain_at_coord(self.current_point)

    def accessible_hexs(self):
        return [elem for elem in self.map.neighbours_of_hex(self.current_point) if self.terrain_at_coord(elem).traversable]

    def go_to_direction(
            self,
            direction='N',
    ):
        assert direction in ['N','S','NE','NW','SE','SW']
        target_hex = self.map.get_neighbour_from_direction(
            ref_hex=self.current_point,
            direction=direction,
        )
        assert target_hex in self.accessible_hexs()
        
        self.group.traverse_terrain(self.current_terrain())

        self.time.pass_hours(self.current_terrain().duration)

        self.current_point=target_hex

        return target_hex


if __name__ == '__main__':
    from ExplorationMaps_input import map1
    from Class import Class
    from Race import Race

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

    h = EDateTime(heure_depart=8,jour_depart=1)

    a = ExplorationGame(
        exploration_group=group,
        exploration_map=map1,
        hour=h,
    )

    a.go_to_direction(direction='N')

    print(char1.__dict__)

    