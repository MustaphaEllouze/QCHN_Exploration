from ExplorationCharacters import (
    ExplorationCharacter,
    ExplorationGroup,
)

from Race import (
    Race,
)
from Class import (
    Class,
)

# ----------------------------- DEFINITION DES PERSONNAGES DU GROUPE 1 --------------------

VIKRAM = ExplorationCharacter(
    name='Vikram',
    race=Race.minotaur,
    classe=Class.monk_STR_CON,
    base_strength=15,
    base_charisma=8,
    base_constitution=17,
    base_dexterity=17,
    base_intelligence=10,
    base_wisdwom=14,
)

BEDOMAI = ExplorationCharacter(
    name='Bedomai',
    race=Race.leonin,
    classe=Class.warrior_STR,
    base_constitution=13,
    base_intelligence=9,
    base_dexterity=14,
    base_charisma=10,
    base_strength=16,
    base_wisdwom=9,
)

BLURP = ExplorationCharacter(
    name='Blurp',
    race=Race.leonin,
    classe=Class.shaman,
    base_constitution=13,
    base_intelligence=14,
    base_dexterity=8,
    base_charisma=13,
    base_strength=10,
    base_wisdwom=16,
)

PENNE = ExplorationCharacter(
    name='Penne',
    race=Race.aven_INT,
    classe=Class.prescient,
    base_constitution=14,
    base_intelligence=12,
    base_dexterity=18,
    base_charisma=10,
    base_strength=14,
    base_wisdwom=14,
)

CHEESY_SWING = ExplorationCharacter(
    name='Cheesy Swing',
    race=Race.murissian,
    classe=Class.bard,
    base_constitution=9,
    base_intelligence=13,
    base_dexterity=13,
    base_charisma=16,
    base_strength=8,
    base_wisdwom=12,
)

GROUP1 = ExplorationGroup(
    name='GROUPE 1',
    exploration_characters=[
        VIKRAM,
        CHEESY_SWING,
        PENNE,
        BLURP,
        BEDOMAI,
    ]
)

if __name__ == '__main__':
    c_to_check = CHEESY_SWING
    print(c_to_check.name,
          c_to_check.CON,
          c_to_check.INT,
          c_to_check.DEX,
          c_to_check.CHR,
          c_to_check.STR,
          c_to_check.WIS)