from ExplorationItems import (
    ExplorationTerrain,
    ExplorationPlace,
)

from ExplorationMaps import (
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
map1.construct_visibility()

# =============================================================================================

# SCENARIO 3 
map2 = ExplorationMap(
    'Scenario3',
    origin_hex=(0,0),
    origin_hex_type=ARID_PLAINS,
    origin_hex_place=VILLAGE,
)

columns_filled = {
    (-17,0)  : [
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        CLIFF,
        CLIFF,
        CLIFF,
        CLIFF,
        CLIFF,
        PLAINS,
        PLAINS,
        ARID_PLAINS,
        DESERT,
        DESERT,
        DESERT,
        ],
    
    (-16,1)  : [
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        CLIFF,
        PLAINS,
        CLIFF,
        CLIFF,
        CLIFF,
        PLAINS,
        PLAINS,
        ARID_PLAINS,
        DESERT,
        DESERT,
        DESERT,
        ],

    (-15,0)  : [
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        CLIFF,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        ARID_PLAINS,
        DESERT,
        DESERT,
        ],

    (-14,1)  : [
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        CLIFF,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        DESERT,
        DESERT,
        ],

    (-13,0)  : [
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        CLIFF,
        PLAINS,
        PLAINS,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        DESERT,
        ],
        
    (-12,1)  : [
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        DESERT,
        DESERT,
        ],

    (-11,0)  : [
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        PLAINS,
        FOREST,
        PLAINS,
        CLIFF,
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        DESERT,
        DESERT,
        ],

    (-10,1)  : [
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        CLIFF,
        CLIFF,
        PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        DESERT,
        DESERT,
        ],
        
    ( -9,0)  : [
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        CLIFF,
        PLAINS,
        PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        DESERT,
        DESERT,
        ],
        
    ( -8,1)  : [
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        CLIFF,
        CLIFF,
        MOUNTAINS,
        CLIFF,
        CLIFF,
        PLAINS,
        PLAINS,
        PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        DESERT,
        DESERT,
        ARID_PLAINS,
        ],

    ( -7,0)  : [
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        FOREST,
        PLAINS,
        CLIFF,
        MOUNTAINS,
        MOUNTAINS,
        CLIFF,
        RIVER,
        RIVER,
        PLAINS,
        PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ],

    ( -6,1)  : [
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
        MOUNTAINS,
        MOUNTAINS,
        FOREST,
        FOREST,
        RIVER,
        RIVER,
        PLAINS,
        PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ],

    ( -5,0)  : [
        ARID_PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        PLAINS,
        CLIFF,
        MOUNTAINS,
        MOUNTAINS,
        MOUNTAINS,
        MOUNTAINS,
        MOUNTAINS,
        CLIFF,
        FOREST,
        RIVER,
        PLAINS,
        PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ],
        
    ( -4,1)  : [
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
        HIGH_MOUNTAIN,
        HIGH_MOUNTAIN,
        MOUNTAINS,
        MOUNTAINS,
        CLIFF,
        PLAINS,
        RIVER,
        PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ],

    ( -3,0)  : [
        CLIFF,
        ARID_PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        CLIFF,
        MOUNTAINS,
        HIGH_MOUNTAIN,
        HIGH_MOUNTAIN,
        HIGH_MOUNTAIN,
        MOUNTAINS,
        MOUNTAINS,
        CLIFF,
        RIVER,
        PLAINS,
        PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ],

    ( -2,1)  : [
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
        HIGH_MOUNTAIN,
        HIGH_MOUNTAIN,
        MOUNTAINS,
        MOUNTAINS,
        CLIFF,
        PLAINS,
        RIVER,
        PLAINS,
        PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        PLAINS,
        ],
        
    ( -1,0)  : [
        CLIFF,
        CLIFF,
        PLAINS,
        PLAINS,
        FOREST,
        CLIFF,
        CLIFF,
        MOUNTAINS,
        MOUNTAINS,
        MOUNTAINS,
        MOUNTAINS,
        MOUNTAINS,
        MOUNTAINS,
        MOUNTAINS,
        FOREST,
        RIVER,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        ],
        
    (  0,1)  : [
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
        MOUNTAINS,
        MOUNTAINS,
        MOUNTAINS,
        MOUNTAINS,
        CLIFF,
        FOREST,
        RIVER,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        ],
    
    (  1,0)  : [
        CLIFF,
        CLIFF,
        PLAINS,
        PLAINS,
        PLAINS,
        RIVER,
        CLIFF,
        MOUNTAINS,
        CLIFF,
        RIVER,
        FOREST,
        MOUNTAINS,
        MOUNTAINS,
        CLIFF,
        PLAINS,
        RIVER,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        BEACH,
        ],

    (  2,1)  : [
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
        RIVER,
        FOREST,
        FOREST,
        CLIFF,
        FOREST,
        RIVER,
        FOREST,
        PLAINS,
        FOREST,
        PLAINS,
        BEACH,
        SEA,
        ],

    (  3,0)  : [
        ARID_PLAINS,
        ARID_PLAINS,
        PLAINS,
        RIVER,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        RIVER,
        FOREST,
        PLAINS,
        PLAINS,
        RIVER,
        RIVER,
        PLAINS,
        PLAINS,
        PLAINS,
        BEACH,
        SEA,
        ],
        
    (  4,1)  : [
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
        RIVER,
        RIVER,
        RIVER,
        RIVER,
        RIVER,
        FOREST,
        RIVER,
        RIVER,
        PLAINS,
        PLAINS,
        BEACH,
        SEA,
        ],

    (  5,0)  : [
        PLAINS,
        PLAINS,
        FOREST,
        RIVER,
        PLAINS,
        PLAINS,
        PLAINS,
        RIVER,
        RIVER,
        FOREST,
        RIVER,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        RIVER,
        PLAINS,
        BEACH,
        SEA,
        ],

    (  6,1)  : [
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        RIVER,
        FOREST,
        RIVER,
        RIVER,
        FOREST,
        RIVER,
        RIVER,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        RIVER,
        BEACH,
        SEA,
        SEA,
        ],
        
    (  7,0)  : [
        PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        RIVER,
        RIVER,
        FOREST,
        FOREST,
        PLAINS,
        FOREST,
        RIVER,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        CLIFF,
        PLAINS,
        BEACH,
        BEACH,
        BEACH,
        SEA,
        ],
        
    (  8,1)  : [
        PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        CLIFF,
        PLAINS,
        FOREST,
        RIVER,
        FOREST,
        PLAINS,
        PLAINS,
        CLIFF,
        CLIFF,
        CLIFF,
        BEACH,
        SEA,
        SEA,
        SEA,
        ],

    (  9,0)  : [
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        CLIFF,
        PLAINS,
        FOREST,
        PLAINS,
        RIVER,
        RIVER,
        RIVER,
        PLAINS,
        PLAINS,
        PLAINS,
        BEACH,
        SEA,
        SEA,
        SEA,
        ],

    ( 10,1)  : [
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        CLIFF,
        PLAINS,
        FOREST,
        PLAINS,        
        PLAINS,        
        FOREST,
        RIVER,
        PLAINS,
        PLAINS,
        PLAINS,
        BEACH,
        SEA,
        SEA,
        SEA,
        ],

    ( 11,0)  : [
        ARID_PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        FOREST,
        RIVER,
        RIVER,
        RIVER,
        RIVER,
        PLAINS,
        PLAINS,
        PLAINS,
        BEACH,
        SEA,
        SEA,
        SEA,
        ],
        
    ( 12,1)  : [
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        FOREST,
        FOREST,
        RIVER,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        BEACH,
        SEA,
        SEA,
        SEA,
        SEA,
        ],

    ( 13,0)  : [
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        PLAINS,
        CLIFF,
        PLAINS,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        RIVER,
        RIVER,
        RIVER,
        RIVER,
        RIVER,
        PLAINS,
        BEACH,
        SEA,
        SEA,
        SEA,
        SEA,
        ],

    ( 14,1)  : [
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        CLIFF,
        FOREST,
        PLAINS,
        PLAINS,
        PLAINS,
        RIVER,
        PLAINS,
        BEACH,
        SEA,
        SEA,
        SEA,
        SEA,
        ],
        
    ( 15,0)  : [
        DESERT,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        CLIFF,
        PLAINS,
        FOREST,
        BEACH,
        CLIFF,
        PLAINS,
        RIVER,
        PLAINS,
        BEACH,
        SEA,
        SEA,
        SEA,
        ],
        
    ( 16,1)  : [
        DESERT,
        DESERT,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        ARID_PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        BEACH,
        BEACH,
        BEACH,
        PLAINS,
        RIVER,
        BEACH,
        SEA,
        SEA,
        SEA,
        SEA,
        ],
    
    ( 17,0)  : [
        DESERT,
        ARID_PLAINS,
        ARID_PLAINS,
        DESERT,
        DESERT,
        ARID_PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        PLAINS,
        BEACH,
        SEA,
        SEA,
        BEACH,
        BEACH,
        BEACH,
        SEA,
        SEA,
        SEA,
        SEA,
        ],
    
    ( 18,1)  : [
        DESERT,
        DESERT,
        DESERT,
        DESERT,
        DESERT,
        DESERT,
        ARID_PLAINS,
        PLAINS,
        PLAINS,
        FOREST,
        PLAINS,
        BEACH,
        BEACH,
        SEA,
        SEA,
        SEA,
        SEA,
        SEA,
        SEA,
        SEA,
        SEA,
        SEA,
        ],
    
}

for column_info,hex_type in columns_filled.items():
    map2.define_column(
        column_number=column_info[0],
        starting_index=column_info[1],
        hex_types=hex_type,
        reverse=True,
    )

map2.define_from_coord((1,-5),hex_type=RIVER,hex_place=CAVE)
map2.construct_visibility()
