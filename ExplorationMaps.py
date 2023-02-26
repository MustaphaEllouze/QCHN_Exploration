from ExplorationItems import (
    ExplorationTerrain,
    ExplorationPlace,
)

from ExplorationGame import (
    ExplorationMap,
)

# ----------------- GLOBAL VARIABLES -------------------

PLAINS        ,P       = (ExplorationTerrain.plains       ,ExplorationTerrain.plains.tag_name       )
CLIFF         ,C       = (ExplorationTerrain.cliff        ,ExplorationTerrain.cliff.tag_name        )
ARID_PLAINS   ,AP      = (ExplorationTerrain.arid_plains  ,ExplorationTerrain.arid_plains.tag_name  )
FOREST        ,F       = (ExplorationTerrain.forest       ,ExplorationTerrain.forest.tag_name       )
RIVER         ,R       = (ExplorationTerrain.river        ,ExplorationTerrain.river.tag_name        )
BIG_RIVER     ,BR      = (ExplorationTerrain.big_river    ,ExplorationTerrain.big_river.tag_name    )
MOUNTAINS     ,M       = (ExplorationTerrain.mountain     ,ExplorationTerrain.mountain.tag_name     )
DESERT        ,D       = (ExplorationTerrain.desert       ,ExplorationTerrain.desert.tag_name       )
HIGH_MOUNTAIN ,HM      = (ExplorationTerrain.high_mountain,ExplorationTerrain.high_mountain.tag_name)
SEA           ,S       = (ExplorationTerrain.sea          ,ExplorationTerrain.sea.tag_name          )

CRISTAL       ,C       = (ExplorationPlace.cristal        ,ExplorationPlace.cristal.tag_name        )
VILLAGE       ,V       = (ExplorationPlace.village        ,ExplorationPlace.village.tag_name        )

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