from ExplorationItems import (
    ExplorationTerrain,
    ExplorationPlace,
)

from ExplorationGame import (
    ExplorationMap,
)

# ----------------- GLOBAL VARIABLES -------------------

PLAINS = ExplorationTerrain.plains
CLIFF = ExplorationTerrain.cliff
ARID_PLAINS = ExplorationTerrain.arid_plains
FOREST = ExplorationTerrain.forest
RIVER = ExplorationTerrain.river
BIG_RIVER = ExplorationTerrain.big_river
MOUNTAINS = ExplorationTerrain.mountain
DESERT = ExplorationTerrain.desert
HIGH_MOUNTAIN = ExplorationTerrain.high_mountain
SEA = ExplorationTerrain.sea

CRISTAL = ExplorationPlace.cristal
VILLAGE = ExplorationPlace.village

# ------------------- DEFINE MAPS ---------------------

# SCENARIO 1
map = ExplorationMap(
    'Scenario1',
    origin_hex=(0,0),
    origin_hex_type=ARID_PLAINS,
    origin_hex_place=VILLAGE,
)
map.define_from_coord((-1,0),PLAINS,None)
map.define_from_coord((-1,1),MOUNTAINS,None)
map.define_from_ref((0,0),hex_type=MOUNTAINS,direction='SE')

print(map.generate_numpy_like())
print(map)