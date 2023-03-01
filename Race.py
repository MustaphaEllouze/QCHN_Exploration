class Race:
    RACES = {}
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

        Race.RACES[name]=self

# --------------------------------------------- DEFINITION DES RACES

Race.human = Race(
    name='Humain',
    bonuses={
        'CON' : 1,
        'CHR' : 1,
    }
)

Race.saurian = Race(
    name='Saurien',
    bonuses={
        'DEX' : 1,
        'WIS' : 1,
    }
)

Race.leonin = Race(
    name='Léonin',
    bonuses={
        'DEX' : 1,
        'STR' : 1,
    }
)

Race.murissian = Race(
    name='Murissien',
    bonuses={
        'DEX' : 2,
    }
)

Race.aven_INT = Race(
    name='Avemain_INT',
    bonuses={
        'INT' : 1,
    }
)

Race.aven_WIS = Race(
    name='Avemain_WIS',
    bonuses={
        'WIS' : 1,
    }
)

Race.elf = Race(
    name='Elf',
    bonuses={
        'WIS' : 1,
        'INT' : 1,
    }
)

Race.minotaur = Race(
    name='Minotaure',
    bonuses={
        'STR' : 2,
    }
)