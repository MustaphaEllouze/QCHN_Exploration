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
            base_intelligence,
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

        self.frozen = False
        self.FROZEN_HUNGER = False
        self.FROZEN_THIRST = False
        self.FROZEN_FATIGUE = False
        self.FROZEN_FROST = False
        self.FROZEN_MAGIC_FATIGUE = False
    
    def set_freeze_state(
            self,
            freeze_state:bool=None,
    ):
        self.frozen = freeze_state
        for carac in ['HUNGER','THIRST','FATIGUE','FROST','MAGIC'] : 
            self.set_freeze_state_carac(carac=carac,freeze_state=freeze_state)
    
    def get_value_of_shield(
            self,
            carac:str,
    ):
        if carac == 'HUNGER':
            return self.SHIELD_HUNGER
        elif carac == 'THIRST':
            return self.SHIELD_THIRST
        elif carac == 'FATIGUE':
            return self.SHIELD_FATIGUE
        elif carac == 'FROST':
            return self.SHIELD_FROST
        elif carac == 'MAGIC':
            return self.SHIELD_MAGIC_FATIGUE
    
    def get_value_of_cara(
            self,
            carac:str,
    ):
        if carac == 'HUNGER':
            return self.CUR_HUNGER
        elif carac == 'THIRST':
            return self.CUR_THIRST
        elif carac == 'FATIGUE':
            return self.CUR_FATIGUE
        elif carac == 'FROST':
            return self.CUR_FROST
        elif carac == 'MAGIC':
            return self.CUR_MAGIC_FATIGUE

    def set_freeze_state_carac(
            self,
            carac:str,
            freeze_state:bool=True,
    ):
        if carac == 'HUNGER':
            self.FROZEN_HUNGER = freeze_state
        elif carac == 'THIRST':
            self.FROZEN_THIRST = freeze_state
        elif carac == 'FATIGUE':
            self.FROZEN_FATIGUE = freeze_state
        elif carac == 'FROST':
            self.FROZEN_FROST = freeze_state
        elif carac == 'MAGIC':
            self.FROZEN_MAGIC_FATIGUE = freeze_state
    
    def change_carac(
            self,
            n:int,
            carac:str
    ):
        if not self.frozen : 
            if carac == 'HUNGER' and not self.FROZEN_HUNGER:
                self.CUR_HUNGER += n
                self.CUR_HUNGER = max(min(self.CUR_HUNGER,self.MAX_HUNGER),0)
            elif carac == 'THIRST' and not self.FROZEN_THIRST:
                self.CUR_THIRST += n
                self.CUR_THIRST = max(min(self.CUR_THIRST,self.MAX_THIRST),0)
            elif carac == 'FATIGUE' and not self.FROZEN_FATIGUE:
                self.CUR_FATIGUE += n
                self.CUR_FATIGUE = max(min(self.CUR_FATIGUE,self.MAX_FATIGUE),0)
            elif carac == 'FROST' and not self.FROZEN_FROST:
                self.CUR_FROST += n
                self.CUR_FROST = max(min(self.CUR_FROST,self.MAX_FROST),0)
            elif carac == 'MAGIC' and not self.FROZEN_MAGIC_FATIGUE:
                self.CUR_MAGIC_FATIGUE += n
                self.CUR_MAGIC_FATIGUE = max(min(self.CUR_MAGIC_FATIGUE,self.MAX_MAGIC_FATIGUE),0)

    def change_shield(
            self,
            n:int,
            carac:str
    ):
        if not self.frozen:
            if carac == 'HUNGER' and not self.FROZEN_HUNGER:
                self.SHIELD_HUNGER += n
                self.SHIELD_HUNGER = max(min(self.SHIELD_HUNGER,self.MAX_HUNGER),0)
            elif carac == 'THIRST'and not self.FROZEN_THIRST:
                self.SHIELD_THIRST += n
                self.SHIELD_THIRST = max(min(self.SHIELD_THIRST,self.MAX_THIRST),0)
            elif carac == 'FATIGUE'and not self.FROZEN_FATIGUE:
                self.SHIELD_FATIGUE += n
                self.SHIELD_FATIGUE = max(min(self.SHIELD_FATIGUE,self.MAX_FATIGUE),0)
            elif carac == 'FROST'and not self.FROZEN_FROST:
                self.SHIELD_FROST += n
                self.SHIELD_FROST = max(min(self.SHIELD_FROST,self.MAX_FROST),0)
            elif carac == 'MAGIC'and not self.FROZEN_MAGIC_FATIGUE:
                self.SHIELD_MAGIC_FATIGUE += n
                self.SHIELD_MAGIC_FATIGUE = max(min(self.SHIELD_MAGIC_FATIGUE,self.MAX_MAGIC_FATIGUE),0)

    def consume_car_or_shield(
            self,
            n:int,
            carac:str,
    ):
        if not self.frozen:
            if carac == 'HUNGER' and not self.FROZEN_HUNGER :
                #HUNGER
                self.SHIELD_HUNGER -= n
                remaining_hunger = -min(self.SHIELD_HUNGER,0)
                self.CUR_HUNGER -= remaining_hunger
                self.SHIELD_HUNGER = max(self.SHIELD_HUNGER,0)
                self.CUR_HUNGER = max(self.CUR_HUNGER,0)
            if carac == 'THIRST' and not self.FROZEN_THIRST :
                # THIRST
                self.SHIELD_THIRST -= n
                remaining_thirst = -min(self.SHIELD_THIRST,0)
                self.CUR_THIRST -= remaining_thirst
                self.SHIELD_THIRST = max(self.SHIELD_THIRST,0)
                self.CUR_THIRST = max(self.CUR_THIRST,0)
            if carac == 'FATIGUE' and not self.FROZEN_FATIGUE:
                # FATIGUE
                self.SHIELD_FATIGUE -= n
                remaining_fatigue = -min(self.SHIELD_FATIGUE,0)
                self.CUR_FATIGUE -= remaining_fatigue
                self.SHIELD_FATIGUE = max(self.SHIELD_FATIGUE,0)
                self.CUR_FATIGUE = max(self.CUR_FATIGUE,0)
            if carac == 'FROST' and not self.FROZEN_FROST:
                # FROST
                self.SHIELD_FROST -= n
                remaining_frost = -min(self.SHIELD_FROST,0)
                self.CUR_FROST -= remaining_frost
                self.SHIELD_FROST = max(self.SHIELD_FROST,0)
                self.CUR_FROST = max(self.CUR_FROST,0)
            if carac == 'MAGIC' and not self.FROZEN_MAGIC_FATIGUE:
                # MAGIC_FATIGUE
                self.SHIELD_MAGIC_FATIGUE -= n
                remaining_magic = -min(self.SHIELD_MAGIC_FATIGUE,0)
                self.CUR_MAGIC_FATIGUE -= remaining_magic
                self.SHIELD_MAGIC_FATIGUE = max(self.SHIELD_MAGIC_FATIGUE,0)
                self.CUR_MAGIC_FATIGUE = max(self.CUR_MAGIC_FATIGUE,0)


    def traverse_terrain(
            self,
            terrain:ExplorationTerrain,
    ):
        self.consume_car_or_shield(terrain.fatigue,'FATIGUE')
        self.consume_car_or_shield(terrain.hunger,'HUNGER')
        self.consume_car_or_shield(terrain.thirst,'THIRST')
        self.consume_car_or_shield(terrain.frost,'FROST')
        self.consume_car_or_shield(terrain.magic_fatigue,'MAGIC')
        

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