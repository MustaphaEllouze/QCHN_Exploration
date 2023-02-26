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
BEACH         ,B       = (ExplorationTerrain.beach        ,ExplorationTerrain.beach.tag_name        )

CRISTAL       ,C       = (ExplorationPlace.cristal        ,ExplorationPlace.cristal.tag_name        )
VILLAGE       ,V       = (ExplorationPlace.village        ,ExplorationPlace.village.tag_name        )
CAVE          ,Ca      = (ExplorationPlace.cave           ,ExplorationPlace.cave.tag_name           )

# ------------------- DEFINE MAPS ---------------------

# SCENARIO 1
map1 = ExplorationMap(
    'Scenario1',
    origin_hex=(0,0),
    origin_hex_type=ARID_PLAINS,
    origin_hex_place=VILLAGE,
)

columns_filled = {
    (0,1)  : [
        CLIFF,
        ARID_PLAINS,
        ARID_PLAINS,
        PLAINS,
        PLAINS,
        CLIFF,
        MOUNTAINS,
        MOUNTAINS,
        MOUNTAINS,
        MOUNTAINS,
        ],
    (1,0)  : [
        CLIFF,
        CLIFF,
        PLAINS,
        PLAINS,
        PLAINS,
        RIVER,
        CLIFF,
        MOUNTAINS,
        CLIFF,
        ],
    (2,1)  : [
        CLIFF,
        ARID_PLAINS,
        PLAINS,
        FOREST,
        RIVER,
        RIVER,
        PLAINS,
        CLIFF,
        PLAINS,
        FOREST,
        ],   
    (3,0)  : [
        ARID_PLAINS,
        ARID_PLAINS,
        PLAINS,
        RIVER,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
    ] ,
    (4,1)  : [
        ARID_PLAINS,
        ARID_PLAINS,
        PLAINS,
        RIVER,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
    ],
    (5,0)  : [
        PLAINS,
        PLAINS,
        FOREST,
        RIVER,
        PLAINS,
        PLAINS,
        PLAINS,
        RIVER,
        RIVER,
    ],
    (6,1)  : [
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        RIVER,
        FOREST,
        RIVER,
        RIVER,
        FOREST,
        RIVER
    ],
    (7,0)  : [
        PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        RIVER,
        RIVER,
        FOREST,
        FOREST,
        PLAINS,
    ],
    (-1,0) : [
        CLIFF,
        CLIFF,
        PLAINS,
        PLAINS,
        FOREST,
        CLIFF,
        CLIFF,
        MOUNTAINS,
        MOUNTAINS,
    ],
    (-2,1) : [
        CLIFF,
        ARID_PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        CLIFF,
        MOUNTAINS,
        MOUNTAINS,
    ],
    (-3,0) : [
        CLIFF,
        ARID_PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        CLIFF,
        MOUNTAINS,
    ],
    (-4,1) : [
        ARID_PLAINS,
        ARID_PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        CLIFF,
        MOUNTAINS,
        MOUNTAINS,
    ],
    (-5,0) : [
        ARID_PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        PLAINS,
        CLIFF,
        MOUNTAINS,
    ],
    (-6,1) : [
        ARID_PLAINS,
        ARID_PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        CLIFF,
        MOUNTAINS,
        MOUNTAINS,
    ],
    (-7,0) : [
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        FOREST,
        PLAINS,
        CLIFF,
    ]
}

for column_info,hex_type in columns_filled.items():
    map1.define_column(
        column_number=column_info[0],
        starting_index=column_info[1],
        hex_types=hex_type,
        reverse=True,
    )

map1.define_from_coord((1,-5),hex_type=RIVER,hex_place=CAVE)

print(map1)

map1.construct_visibility()
print(map1.visibility[(0,-6)])