class ExplorationTerrain : 
    """Représente un type de terrain différent pour le jeu
    """
    TERRAINS = {None:None}
    TERRAINS_FROM_TAG = {None:None}

    def __init__(
            self,
            name,
            tag_name,
            duration=1.0,
            fatigue=1.0,
            hunger=1.0,
            thirst=1.0,
            frost=0.0,
            magic_fatigue=0.0,
            traversable=True,
            height=1,
    ):
        self.name = name
        self.tag_name=tag_name
        self.duration = duration
        self.fatigue = fatigue
        self.hunger = hunger
        self.thirst = thirst
        self.frost=frost
        self.magic_fatigue=magic_fatigue
        self.traversable=traversable
        self.height=height

        ExplorationTerrain.TERRAINS[name]=self
        ExplorationTerrain.TERRAINS_FROM_TAG[self.tag_name]=self

class ExplorationPlace : 
    """Représente un lieu spécial (se superpose à un terrain)
    """

    PLACES = {None:None}
    PLACES_FROM_TAG = {None:None}

    def __init__(
            self,
            name,
            tag_name,
            detect_distance=1,
    ):
        self.name = name
        self.tag_name=tag_name
        self.detect_distance = detect_distance

        ExplorationPlace.PLACES[name]=self
        ExplorationPlace.PLACES_FROM_TAG[self.tag_name]=self

# ---------------------------------- DEFINITION DES TERRAINS ------------------------------
ExplorationTerrain.plains = ExplorationTerrain(
    name='Plaine',
    tag_name='P ',
    duration=1.0,
    fatigue=1.0,
    hunger=1.0,
    thirst=1.0,
    height=0,
)

ExplorationTerrain.cliff = ExplorationTerrain(
    name='Falaise',
    tag_name='C ',
    duration=1.5,
    fatigue=2.0,
    hunger=1.0,
    thirst=2.0,
    height=1,
)

ExplorationTerrain.arid_plains = ExplorationTerrain(
    name='Plaine Aride',
    tag_name='AP',
    duration=1.0,
    fatigue=1.0,
    hunger=1.0,
    thirst=2.0,
    height=0,
)

ExplorationTerrain.forest = ExplorationTerrain(
    name='Forêt',
    tag_name='F ',
    duration=2.0,
    fatigue=1.0,
    hunger=1.0,
    thirst=1.0,
    height=0,
)

ExplorationTerrain.river = ExplorationTerrain(
    name='Rivière',
    tag_name='R ',
    duration=1.0,
    fatigue=1.0,
    hunger=1.0,
    thirst=1.0,
    height=0,
)

ExplorationTerrain.big_river = ExplorationTerrain(
    name='Grande Rivière',
    tag_name='BR',
    duration=2.0,
    fatigue=2.0,
    hunger=1.0,
    thirst=1.0,
    frost=1.0,
    height=0,
)

ExplorationTerrain.mountain = ExplorationTerrain(
    name='Montagne',
    tag_name='M ',
    duration=2.0,
    fatigue=3.0,
    hunger=2.0,
    thirst=2.0,
    frost=1.0,
    height=2,
)

ExplorationTerrain.desert = ExplorationTerrain(
    name='Desert',
    tag_name='D ',
    duration=1.0,
    fatigue=2.0,
    hunger=1.0,
    thirst=3.0,
    magic_fatigue=3.0,
    height=0,
)

ExplorationTerrain.high_mountain = ExplorationTerrain(
    name='Haute Montagne',
    tag_name='HM',
    duration=3.0,
    fatigue=4.0,
    hunger=2.0,
    thirst=1.0,
    frost=2.0,
    height=3,
)

ExplorationTerrain.sea = ExplorationTerrain(
    name='Mer',
    tag_name='S ',
    duration=3.0,
    fatigue=1.0,
    hunger=1.0,
    thirst=1.0,
    traversable=False,
    height=0,
)

ExplorationTerrain.beach = ExplorationTerrain(
    name='Plage',
    tag_name='B ',
    duration=1.0,
    fatigue=1.0,
    hunger=1.0,
    thirst=1.0,
    traversable=False,
    height=0,
)

# ---------------------------------- DEFINITION DES LIEUX ADDITIONNELS ------------------------------

ExplorationPlace.cristal = ExplorationPlace(
    name='Cristal',
    tag_name='C ',
    detect_distance=3,
)

ExplorationPlace.village = ExplorationPlace(
    name='Village',
    tag_name='V ',
    detect_distance=2,
)

ExplorationPlace.cave = ExplorationPlace(
    name='Grotte',
    tag_name='Ca',
    detect_distance=2,
)