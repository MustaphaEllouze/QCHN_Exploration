from Character import (
    Character,
)

class ExplorationCharacter(Character):
    def __init__(
            self,
            name,
            race,
            classe,
            base_strength,
            base_constitution,
            base_dexterity,
            base_charisma,
            base_wisdwom,
            base_intelligence
    ):
        super().__init__(name, race, classe, base_strength, base_constitution, base_dexterity, base_charisma, base_wisdwom, base_intelligence)
        pass

class ExplorationGroup:
    def __init__(
            self,
            exploration_characters,
    ):
        pass