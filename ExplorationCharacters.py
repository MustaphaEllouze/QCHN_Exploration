from Character import (
    Character,
)

from Race import (
    Race,
)

from Class import (
    Class,
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
        
        self.MAX_HUNGER        = self.CON - 3
        self.MAX_THIRST        = self.CON - 3
        self.MAX_FATIGUE       = 10 + self.MOD_CON + max(self.MOD_STR,self.MOD_DEX)
        self.MAX_FROST         = self.MOD_CON + 3
        self.MAX_MAGIC_FATIGUE = self.WIS - 3
        

class ExplorationGroup:
    def __init__(
            self,
            exploration_characters,
    ):
        pass


if __name__ == '__main__':
    test = ExplorationCharacter(
         name='Asfur',
         race=Race.aven_INT,
         classe=Class.rogue_CHR,
         base_strength        = 11  ,
         base_constitution    = 11  ,
         base_intelligence    = 12  ,
         base_dexterity       = 14  ,
         base_charisma        = 14  ,
         base_wisdwom         = 11  ,
    )
    
    print(test.__dict__)