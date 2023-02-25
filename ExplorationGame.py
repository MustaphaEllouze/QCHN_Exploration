from Utility import (
    EDateTime,
)

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
    ):
        self.name = name
        self.duration = duration
        self.fatigue = fatigue
        self.hunger = hunger
        self.thirst = thirst

        ExplorationTerrain.TERRAINS[name]=self

class ExplorationMap : 
    """Représente une carte
    """

class ExplorationGameManager:
    """Gère toutes les règles du jeu et les calculs
    """
    pass

