class ExplorationTerrain : 
    """Représente un type de terrain différent pour le jeu
    """
    TERRAINS = {}

    def __init__(
            self,
            name,
            duration=1.0,
            fatigue=1.0,
            hunger=1.0,
            thirst=1.0,
            frost=0.0,
            magic_fatigue=0.0,
            traversable=True,
            detect_distance=1,
    ):
        self.name = name
        self.duration = duration
        self.fatigue = fatigue
        self.hunger = hunger
        self.thirst = thirst
        self.frost=frost
        self.magic_fatigue=magic_fatigue
        self.traversable=traversable
        self.detect_distance=detect_distance

        ExplorationTerrain.TERRAINS[name]=self

ExplorationTerrain.plains = ExplorationTerrain(
    name='Plaine',
    duration=1.0,
    fatigue=1.0,
    hunger=1.0,
    thirst=1.0,
)

ExplorationTerrain.cliff = ExplorationTerrain(
    name='Falaise',
    duration=1.5,
    fatigue=2.0,
    hunger=1.0,
    thirst=2.0,
)

ExplorationTerrain.arid_plains = ExplorationTerrain(
    name='Plaine Aride',
    duration=1.0,
    fatigue=1.0,
    hunger=1.0,
    thirst=2.0,
)

ExplorationTerrain.forest = ExplorationTerrain(
    name='Forêt',
    duration=2.0,
    fatigue=1.0,
    hunger=1.0,
    thirst=1.0,
)

ExplorationTerrain.river = ExplorationTerrain(
    name='Rivière',
    duration=1.0,
    fatigue=1.0,
    hunger=1.0,
    thirst=1.0,
)

ExplorationTerrain.big_river = ExplorationTerrain(
    name='Grande Rivière',
    duration=2.0,
    fatigue=2.0,
    hunger=1.0,
    thirst=1.0,
    frost=1.0,
)

ExplorationTerrain.mountain = ExplorationTerrain(
    name='Montagne',
    duration=2.0,
    fatigue=3.0,
    hunger=2.0,
    thirst=2.0,
    frost=1.0,
)

ExplorationTerrain.desert = ExplorationTerrain(
    name='Desert',
    duration=1.0,
    fatigue=2.0,
    hunger=1.0,
    thirst=3.0,
    magic_fatigue=3.0,
)

ExplorationTerrain.high_mountain = ExplorationTerrain(
    name='Haute Montagne',
    duration=3.0,
    fatigue=4.0,
    hunger=2.0,
    thirst=1.0,
    frost=2.0,
)

ExplorationTerrain.sea = ExplorationTerrain(
    name='Mer',
    duration=3.0,
    fatigue=1.0,
    hunger=1.0,
    thirst=1.0,
    traversable=False,
)

ExplorationTerrain.cristal = ExplorationTerrain(
    name='Cristal',
    duration=1.0,
    fatigue=1.0,
    hunger=1.0,
    thirst=1.0,
    traversable=False,
)

ExplorationTerrain.village = ExplorationTerrain(
    name='Village',
    duration=1.0,
    fatigue=1.0,
    hunger=1.0,
    thirst=1.0,
    detect_distance=2,
)