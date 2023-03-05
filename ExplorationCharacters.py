from Character import (
    Character,
)

from Race import (
    Race,
)

from Class import (
    Class,
)

from ExplorationItems import (
    ExplorationTerrain,
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

        self.CUR_HUNGER        = self.MAX_HUNGER       
        self.CUR_THIRST        = self.MAX_THIRST       
        self.CUR_FATIGUE       = self.MAX_FATIGUE      
        self.CUR_FROST         = self.MAX_FROST        
        self.CUR_MAGIC_FATIGUE = self.MAX_MAGIC_FATIGUE
    
    def traverse_terrain(
            self,
            terrain:ExplorationTerrain,
    ):
        self.CUR_HUNGER  -= terrain.hunger
        self.CUR_THIRST  -= terrain.thirst
        self.CUR_FATIGUE -= terrain.fatigue
        self.CUR_FROST   -= terrain.frost
        self.MAX_FATIGUE -= terrain.fatigue  
        

class ExplorationGroup:
    def __init__(
            self,
            name:str,
            exploration_characters:list,
    ):
        for character in exploration_characters :
            assert type(character) is ExplorationCharacter
        
        self.name = name
        self.characters = exploration_characters
    
    def traverse_terrain(
            self,
            terrain:ExplorationTerrain,
    ):
        for character in self.characters:
            character.traverse_terrain(terrain)


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