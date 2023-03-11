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

        self.SHIELD_HUNGER        = 0
        self.SHIELD_THIRST        = 0
        self.SHIELD_FATIGUE       = 0
        self.SHIELD_FROST         = 0
        self.SHIELD_MAGIC_FATIGUE = 0
    
    def change_carac(
            self,
            n:int,
            carac:str
    ):
        if carac == 'HUNGER':
            self.CUR_HUNGER += n
            self.CUR_HUNGER = min(self.CUR_HUNGER,self.MAX_HUNGER)
        elif carac == 'THIRST':
            self.CUR_THIRST += n
            self.CUR_THIRST = min(self.CUR_THIRST,self.MAX_THIRST)
        elif carac == 'FATIGUE':
            print(self.name,carac,n)
            self.CUR_FATIGUE += n
            self.CUR_FATIGUE = min(self.CUR_FATIGUE,self.MAX_FATIGUE)
        elif carac == 'FROST':
            self.CUR_FROST += n
            self.CUR_FROST = min(self.CUR_FROST,self.MAX_FROST)
        elif carac == 'MAGIC':
            self.CUR_MAGIC_FATIGUE += n
            self.CUR_MAGIC_FATIGUE = min(self.CUR_MAGIC_FATIGUE,self.MAX_MAGIC_FATIGUE)
        else:
            raise Exception(f'{carac}:Not a caracteristic')

    def change_shield(
            self,
            n:int,
            carac:str
    ):
        if carac == 'HUNGER':
            self.SHIELD_HUNGER += n
            self.SHIELD_HUNGER = min(self.SHIELD_HUNGER,self.MAX_HUNGER)
        elif carac == 'THIRST':
            self.SHIELD_THIRST += n
            self.SHIELD_THIRST = min(self.SHIELD_THIRST,self.MAX_THIRST)
        elif carac == 'FATIGUE':
            self.SHIELD_FATIGUE += n
            self.SHIELD_FATIGUE = min(self.SHIELD_FATIGUE,self.MAX_FATIGUE)
        elif carac == 'FROST':
            self.SHIELD_FROST += n
            self.SHIELD_FROST = min(self.SHIELD_FROST,self.MAX_FROST)
        elif carac == 'MAGIC':
            self.SHIELD_MAGIC_FATIGUE += n
            self.SHIELD_MAGIC_FATIGUE = min(self.SHIELD_MAGIC_FATIGUE,self.MAX_MAGIC_FATIGUE)
        else:
            raise Exception(f'{carac}:Not a caracteristic')

    def traverse_terrain(
            self,
            terrain:ExplorationTerrain,
    ):

        #HUNGER
        self.SHIELD_HUNGER -= terrain.hunger
        remaining_hunger = -min(self.SHIELD_HUNGER,0)
        self.CUR_HUNGER -= remaining_hunger
        self.SHIELD_HUNGER = max(self.SHIELD_HUNGER,0)
        self.CUR_HUNGER = max(self.CUR_HUNGER,0)
        # THIRST
        self.SHIELD_THIRST -= terrain.thirst
        remaining_thirst = -min(self.SHIELD_THIRST,0)
        self.CUR_THIRST -= remaining_thirst
        self.SHIELD_THIRST = max(self.SHIELD_THIRST,0)
        self.CUR_THIRST = max(self.CUR_THIRST,0)
        # FATIGUE
        self.SHIELD_FATIGUE -= terrain.fatigue
        remaining_fatigue = -min(self.SHIELD_FATIGUE,0)
        self.CUR_FATIGUE -= remaining_fatigue
        self.SHIELD_FATIGUE = max(self.SHIELD_FATIGUE,0)
        self.CUR_FATIGUE = max(self.CUR_FATIGUE,0)
        # FROST
        self.SHIELD_FROST -= terrain.frost
        remaining_frost = -min(self.SHIELD_FROST,0)
        self.CUR_FROST -= remaining_frost
        self.SHIELD_FROST = max(self.SHIELD_FROST,0)
        self.CUR_FROST = max(self.CUR_FROST,0)
        # MAGIC_FATIGUE
        self.SHIELD_MAGIC_FATIGUE -= terrain.magic_fatigue
        remaining_magic = -min(self.SHIELD_MAGIC_FATIGUE,0)
        self.CUR_MAGIC_FATIGUE -= remaining_magic
        self.SHIELD_MAGIC_FATIGUE = max(self.SHIELD_MAGIC_FATIGUE,0)
        self.CUR_MAGIC_FATIGUE = max(self.CUR_MAGIC_FATIGUE,0)
    
    def grant_shield(
            self,
            caracteristic:str,
            shield_amount=0,
    ):
        if caracteristic == 'HUNGER':
            self.SHIELD_HUNGER += shield_amount
            self.SHIELD_HUNGER = min(self.SHIELD_HUNGER,self.MAX_HUNGER)
        elif caracteristic == 'THIRST':
            self.SHIELD_THIRST += shield_amount
            self.SHIELD_THIRST = min(self.SHIELD_THIRST,self.MAX_THIRST)
        elif caracteristic == 'FATIGUE':
            self.SHIELD_FATIGUE += shield_amount
            self.SHIELD_FATIGUE = min(self.SHIELD_FATIGUE,self.MAX_FATIGUE)
        elif caracteristic == 'FROST':
            self.SHIELD_FROST += shield_amount
            self.SHIELD_FROST = min(self.SHIELD_FROST,self.MAX_FROST)
        elif caracteristic == 'MAGIC':
            self.SHIELD_MAGIC_FATIGUE += shield_amount
            self.SHIELD_MAGIC_FATIGUE = min(self.SHIELD_MAGIC_FATIGUE,self.MAX_MAGIC_FATIGUE)
        else:
            raise Exception(f'{caracteristic}:Not a caracteristic')
        

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