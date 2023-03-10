from Race import (
     Race,
)

from Class import (
     Class,
)

class Character:
    
    """Représente un personnage à partir de ses caractéristiques
    """

    # Contient toutes les instances
    CHARACTERS = {}

    def __init__(
            self,
            name:str,
            race:Race,
            classe:Class,
            base_strength:int,
            base_constitution:int,
            base_dexterity:int,
            base_charisma:int,
            base_wisdwom:int,
            base_intelligence:int,
    ):
        """_summary_

         Args:
             name (str): _description_
             race (Race): _description_
             classe (Class): _description_
             base_strength (int): _description_
             base_constitution (int): _description_
             base_dexterity (int): _description_
             base_charisma (int): _description_
             base_wisdwom (int): _description_
             base_intelligence (int): _description_
        """
        self.name = name
        self.race = race
        self.classe = classe
        self.base_strength = base_strength
        self.base_constitution = base_constitution
        self.base_dexterity = base_dexterity
        self.base_charisma = base_charisma
        self.base_wisdwom = base_wisdwom
        self.base_intelligence = base_intelligence

        self.STR = self.base_strength     + self.race.bonuses['STR'] + self.classe.bonuses['STR']  
        self.CON = self.base_constitution + self.race.bonuses['CON'] + self.classe.bonuses['CON']      
        self.INT = self.base_intelligence + self.race.bonuses['INT'] + self.classe.bonuses['INT']      
        self.DEX = self.base_dexterity    + self.race.bonuses['DEX'] + self.classe.bonuses['DEX']   
        self.CHR = self.base_charisma     + self.race.bonuses['CHR'] + self.classe.bonuses['CHR']  
        self.WIS = self.base_wisdwom      + self.race.bonuses['WIS'] + self.classe.bonuses['WIS'] 

        self.MOD_STR = int((self.STR-10)/2)
        self.MOD_CON = int((self.CON-10)/2)
        self.MOD_INT = int((self.INT-10)/2)
        self.MOD_DEX = int((self.DEX-10)/2)
        self.MOD_CHR = int((self.CHR-10)/2)
        self.MOD_WIS = int((self.WIS-10)/2)

        self.W = int((self.MOD_CON + self.MOD_INT)/2) + self.MOD_WIS + self.race.bonuses['W'] + self.classe.bonuses['W']
        self.U = int((self.MOD_INT + self.MOD_DEX)/2) + self.MOD_WIS + self.race.bonuses['U'] + self.classe.bonuses['U']
        self.B = int((self.MOD_DEX + self.MOD_CHR)/2) + self.MOD_WIS + self.race.bonuses['B'] + self.classe.bonuses['B']
        self.R = int((self.MOD_CHR + self.MOD_STR)/2) + self.MOD_WIS + self.race.bonuses['R'] + self.classe.bonuses['R']
        self.G = int((self.MOD_STR + self.MOD_CON)/2) + self.MOD_WIS + self.race.bonuses['G'] + self.classe.bonuses['G']
        

        Character.CHARACTERS[name]=self

if __name__ == '__main__':
    test = Character(
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