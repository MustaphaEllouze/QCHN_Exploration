class ExplorationTerrain : 
    """Représente un type de terrain différent pour le jeu
    """
    TERRAINS = {None:None}              # Tous les terrains définis          {self.name:self}
    TERRAINS_FROM_TAG = {None:None}     # Tous les tags des terrains définis {self.tag_name:self}

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
            visibility_range=1,
    ):
        """Constructeur

        Args:
            name (str): Nom du terrain
            tag_name (str): Tag du terrain
            duration (float, optional): Durée de traversée du terrain. Defaults to 1.0.
            fatigue (float, optional): Fatigue générée par la traversée du terrain. Defaults to 1.0.
            hunger (float, optional): Faim générée par la traversée du terrain. Defaults to 1.0.
            thirst (float, optional): Soif générée par la traversée du terrain. Defaults to 1.0.
            frost (float, optional): Froid généré par la traversée du terrain. Defaults to 0.0.
            magic_fatigue (float, optional): Magie consommée par la traversée du terrain. Defaults to 0.0.
            traversable (bool, optional): True si le terrain est traversable, False sinon. Defaults to True.
            height (int, optional): Hauteur du terrain (unité arbitraire relative). Defaults to 1.
            visibility_range (int, optional): Portée de vue. Defaults to 1.
        """
        # --- Data-structure like
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
        self.visibility_range=visibility_range

        # --- Ajout dans les attributs de classe
        ExplorationTerrain.TERRAINS[name]=self
        ExplorationTerrain.TERRAINS_FROM_TAG[self.tag_name]=self

class ExplorationPlace : 
    """Représente un lieu spécial (se superpose à un terrain)
    """

    PLACES = {None:None}                # Tous les endroits définis          {self.name:self}
    PLACES_FROM_TAG = {None:None}       # Tous les tags des endroits définis {self.tag_name:self}

    def __init__(
            self,
            name,
            tag_name,
            detect_distance=1,
    ):
        """Constructeur

        Args:
            name (str): Nom de l'endroit
            tag_name (_type_): Tag de l'endroit
            detect_distance (int, optional): Distance de détection de l'endroit. Defaults to 1.
        """

        # --- Data-structure like
        self.name = name
        self.tag_name=tag_name
        self.detect_distance = detect_distance

        # --- Ajout dans les attributs de classe
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
    visibility_range=2,
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
    visibility_range=3
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