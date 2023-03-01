class Class:
    CLASSES = {}
    def __init__(
            self,
            name,
            bonuses,
    ):
        self.bonuses = {
                'STR':0,
                'CON':0,
                'INT':0,
                'DEX':0,
                'CHR':0,
                'WIS':0,
                'W':0,
                'U':0,
                'B':0,
                'R':0,
                'G':0,
        }
        for key,bonus in bonuses.items():
            assert key in self.bonuses.keys()
            self.bonuses[key]=bonus
            
        Class.CLASSES[name]=self

# --------------------------------------------- DEFINITION DES CLASSES

Class.warrior_DEX = Class(
     name='Guerrier_DEX',
     bonuses={
        'CON':1,
        'INT':-2,
        'DEX':1,
     }
)

Class.warrior_STR = Class(
     name='Guerrier_STR',
     bonuses={
        'CON':1,
        'INT':-2,
        'STR':1,
     }
)

Class.battle_mage = Class(
     name='Mage de bataille',
     bonuses={
        'CON':1,
        'DEX':-2,
        'WIS':1,
     }
)

Class.rogue_CHR = Class(
     name='Gredin',
     bonuses={
        'DEX':1,
        'STR':-2,
        'CHR':1,
        'B':1,
     }
)

Class.rogue_WIS = Class(
     name='Gredin',
     bonuses={
        'DEX':1,
        'STR':-2,
        'B':1,
     }
)

Class.shaman = Class(
     name='Shamane',
     bonuses={
        'WIS':1,
        'CON':1,
        'CHR':-2,
        'G':1,
     }
)


Class.berserker = Class(
     name='Barbare',
     bonuses={
        'STR':2,
        'CON':-1,
        'R':1,
     }
)

Class.prescient = Class(
     name='Prescient',
     bonuses={
        'WIS':2,
        'CON':-2,
        'W':1,
     }
)

Class.scholar = Class(
     name='Erudit',
     bonuses={
        'INT':2,
        'STR':-2,
        'U':1,
     }
)

Class.bard = Class(
     name='Barde',
     bonuses={
        'CHR':2,
        'STR':-1,
     }
)

Class.monk_STR_DEX = Class(
     name='Moine_STR_DEX',
     bonuses={
        'STR':1,
        'DEX':1,
        'CHR':-2,
     }
)

Class.monk_STR_CON = Class(
     name='Moine_STR_CON',
     bonuses={
        'STR':1,
        'CON':1,
        'CHR':-2,
     }
)

Class.monk_DEX_CON = Class(
     name='Moine_DEX_CON',
     bonuses={
        'DEX':1,
        'CON':1,
        'CHR':-2,
     }
)

Class.crafter_NoSTR = Class(
     name='Artisan_NoSTR',
     bonuses={
        'DEX':1,
        'INT':1,
        'STR':-1,
     }
)

Class.crafter_NoCON = Class(
     name='Artisan',
     bonuses={
        'DEX':1,
        'INT':1,
        'CON':-1,
     }
)