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
    """Représente un personnage d'exploration

        MAX_HUNGER                : int  : Valeur maximale de faim                     
        MAX_THIRST                : int  : Valeur maximale de soif                     
        MAX_FATIGUE               : int  : Valeur maximale de fatigue                     
        MAX_FROST                 : int  : Valeur maximale de froid                     
        MAX_MAGIC_FATIGUE         : int  : Valeur maximale d'endurance magique                     
                                          
        CUR_HUNGER                : int  : Valeur courante de faim                                  
        CUR_THIRST                : int  : Valeur courante de soif                                  
        CUR_FATIGUE               : int  : Valeur courante de fatigue                               
        CUR_FROST                 : int  : Valeur courante de froid                                 
        CUR_MAGIC_FATIGUE         : int  : Valeur courante d'endurance magique                     
                                         
        SHIELD_HUNGER             : int  : Valeur de bouclier de faim                                     
        SHIELD_THIRST             : int  : Valeur de bouclier de soif                                     
        SHIELD_FATIGUE            : int  : Valeur de bouclier de fatigue                                  
        SHIELD_FROST              : int  : Valeur de bouclier de froid                                    
        SHIELD_MAGIC_FATIGUE      : int  : Valeur de bouclier d'endurance magique                        
                                        
        FROZEN                    : bool : Etat de gel du personnage            
        FROZEN_HUNGER             : bool : Etat de gel de faim                 
        FROZEN_THIRST             : bool : Etat de gel de soif                  
        FROZEN_FATIGUE            : bool : Etat de gel de fatigue                   
        FROZEN_FROST              : bool : Etat de gel de froid                 
        FROZEN_MAGIC_FATIGUE      : bool : Etat de gel d'endurance magique                         
    """
    
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
        """
        Args:
            name (str): Nom du personnage
            race (Race): Race du personnage
            classe (Class): Classe du personnage
            base_strength (int): Force de base (hors bonus)
            base_constitution (int): Constitution de base (hors bonus)
            base_dexterity (int): Dextérité de base (hors bonus)
            base_charisma (int): Charisme de base (hors bonus)
            base_wisdwom (int): Sagesse de base (hors bonus)
            base_intelligence (int): Intelligence de base (hors bonus)
        """

        # Constructeur de la classe mère
        super().__init__(name, race, classe, base_strength, base_constitution, base_dexterity, base_charisma, base_wisdwom, base_intelligence)
        
        # Calcul des caractéristiques spécifiques à l'exploration (cara MAX)
        self.MAX_HUNGER        = self.CON - 3
        self.MAX_THIRST        = self.CON - 3
        self.MAX_FATIGUE       = 10 + self.MOD_CON + max(self.MOD_STR,self.MOD_DEX)
        self.MAX_FROST         = self.MOD_CON + 3
        self.MAX_MAGIC_FATIGUE = self.WIS - 3

        # Initialisation des caractéristiques courantes
        self.CUR_HUNGER        = self.MAX_HUNGER       
        self.CUR_THIRST        = self.MAX_THIRST       
        self.CUR_FATIGUE       = self.MAX_FATIGUE      
        self.CUR_FROST         = self.MAX_FROST        
        self.CUR_MAGIC_FATIGUE = self.MAX_MAGIC_FATIGUE

        # Initialisation des boucliers des caractéristiques
        self.SHIELD_HUNGER        = 0
        self.SHIELD_THIRST        = 0
        self.SHIELD_FATIGUE       = 0
        self.SHIELD_FROST         = 0
        self.SHIELD_MAGIC_FATIGUE = 0

        # Initilisations des états de gel
        self.FROZEN                 = False
        self.FROZEN_HUNGER          = False
        self.FROZEN_THIRST          = False
        self.FROZEN_FATIGUE         = False
        self.FROZEN_FROST           = False
        self.FROZEN_MAGIC_FATIGUE   = False
    
    def set_freeze_state_carac(
            self,
            carac:str,
            freeze_state:bool=True,
    ):
        """Gèle ou dégèle une caractéristique particulière

        Args:
            carac (str): _description_
            freeze_state (bool, optional): _description_. Defaults to True.
        """
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
        else:
            raise Exception(f'in ExplorationCharacters.set_freeze_state_carac, {carac} not a characteristic')

    def set_freeze_state(
            self,
            freeze_state:bool,
    ):
        """Gèle ou dégèle le personnage

        Args:
            freeze_state (bool): Etat de gel
        """

        self.FROZEN = freeze_state
    
    def get_value_of_shield(
            self,
            carac:str,
    ):
        """Renvoie la valeur de bouclier d'une caractéristique

        Args:
            carac (str): Caractéristique à récupérer

        Returns:
            int: Valeur de bouclier
        """
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
        else:
            raise Exception(f'in ExplorationCharacters.get_value_of_shield, {carac} not a characteristic')
    
    def get_value_of_cara(
            self,
            carac:str,
    ):
        """Renvoie la valeur d'une caractéristique

        Args:
            carac (str): Caractéristique à récupérer

        Returns:
            int: Valeur de la caractéristique
        """
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
        else:
            raise Exception(f'in ExplorationCharacters.get_value_of_cara, {carac} not a characteristic')
 
    def change_carac(
            self,
            n:int,
            carac:str
    ):
        """Change la valeur courante d'une caractéristique si le personnage et la caractéristiques sont dégelés.

        Args:
            n (int): De combien on doit changer la cara
            carac (str): Nom de la caractéristique

        """
        # La fonction n'est pas appellée si le personnage est gelé
        if not self.FROZEN : 

            # Et idem pour chaque caractéristique
            # NOTE : On cap chaque caractéristique entre 0 et la valeur max

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
            else:
                raise Exception(f'in ExplorationCharacters.change_carac, {carac} not a characteristic')

    def change_shield(
            self,
            n:int,
            carac:str
    ):
        """Change la valeur bouclier d'une caractéristique si le personnage et la caractéristiques sont dégelés.

        Args:
            n (int): De combien on doit changer le bouclier
            carac (str): Nom de la caractéristique

        """
        # La fonction n'est pas appellée si le personnage est gelé
        if not self.FROZEN:

            # Et idem pour chaque caractéristique
            # NOTE : On cap chaque caractéristique entre 0 et la valeur max

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
            else:
                raise Exception(f'in ExplorationCharacters.change_shield, {carac} not a characteristic')

    def consume_car_or_shield(
            self,
            n:int,
            carac:str,
    ):
        """Consomme la caractéristique. Fait perdre d'abord le bouclier.

        Args:
            n (int): Combien il faut consommer 
            carac (str): La caractéristique à consommer
        """

        assert n>=0

        # La fonction n'est pas appellée si le personnage est gelé
        if not self.FROZEN:
            
            if carac == 'HUNGER' and not self.FROZEN_HUNGER :
                #HUNGER
                self.SHIELD_HUNGER -= n                         # On ôte n du bouclier
                remaining_hunger = -min(self.SHIELD_HUNGER,0)   # On calcule si on est passé en négatif en bouclier
                self.CUR_HUNGER -= remaining_hunger             # On enlève ce qui reste à la valeur courante
                self.SHIELD_HUNGER = max(self.SHIELD_HUNGER,0)  # On remet le bouclier à 0 si on est passé en négatif
                self.CUR_HUNGER = max(self.CUR_HUNGER,0)        # On remet la valeur courante à 0 si on est passé en négatif

            elif carac == 'THIRST' and not self.FROZEN_THIRST :
                # THIRST
                self.SHIELD_THIRST -= n
                remaining_thirst = -min(self.SHIELD_THIRST,0)
                self.CUR_THIRST -= remaining_thirst
                self.SHIELD_THIRST = max(self.SHIELD_THIRST,0)
                self.CUR_THIRST = max(self.CUR_THIRST,0)
            
            elif carac == 'FATIGUE' and not self.FROZEN_FATIGUE:
                # FATIGUE
                self.SHIELD_FATIGUE -= n
                remaining_fatigue = -min(self.SHIELD_FATIGUE,0)
                self.CUR_FATIGUE -= remaining_fatigue
                self.SHIELD_FATIGUE = max(self.SHIELD_FATIGUE,0)
                self.CUR_FATIGUE = max(self.CUR_FATIGUE,0)
            
            elif carac == 'FROST' and not self.FROZEN_FROST:
                # FROST
                self.SHIELD_FROST -= n
                remaining_frost = -min(self.SHIELD_FROST,0)
                self.CUR_FROST -= remaining_frost
                self.SHIELD_FROST = max(self.SHIELD_FROST,0)
                self.CUR_FROST = max(self.CUR_FROST,0)
            
            elif carac == 'MAGIC' and not self.FROZEN_MAGIC_FATIGUE:
                # MAGIC_FATIGUE
                self.SHIELD_MAGIC_FATIGUE -= n
                remaining_magic = -min(self.SHIELD_MAGIC_FATIGUE,0)
                self.CUR_MAGIC_FATIGUE -= remaining_magic
                self.SHIELD_MAGIC_FATIGUE = max(self.SHIELD_MAGIC_FATIGUE,0)
                self.CUR_MAGIC_FATIGUE = max(self.CUR_MAGIC_FATIGUE,0)
            
            else:
                raise Exception(f'in ExplorationCharacters.consume_car_or_shield, {carac} not a characteristic')

    def traverse_terrain(
            self,
            terrain:ExplorationTerrain,
    ):
        """Consomme toutes les caractéristiques à la traversée d'un terrain

        Args:
            terrain (ExplorationTerrain): Terrain à traverser
        """
        self.consume_car_or_shield(terrain.fatigue,'FATIGUE')
        self.consume_car_or_shield(terrain.hunger,'HUNGER')
        self.consume_car_or_shield(terrain.thirst,'THIRST')
        self.consume_car_or_shield(terrain.frost,'FROST')
        self.consume_car_or_shield(terrain.magic_fatigue,'MAGIC')
        

class ExplorationGroup:
    """Représente un groupe d'ExplorationCharacter

        name : str
        characters : list(ExplorationCharacter)
    """
    def __init__(
            self,
            name:str,
            exploration_characters:list,
    ):
        """
        Args:
            name (str): Nom du groupe
            exploration_characters (list(ExplorationCharacter)): Liste des ExplorationCharacter formant le groupe
        """

        # Check du paramètre d'entrée
        for character in exploration_characters :
            assert type(character) is ExplorationCharacter
        
        # Attribution des paramètres
        self.name = name
        self.characters = exploration_characters
    
    def traverse_terrain(
            self,
            terrain:ExplorationTerrain,
    ):
        """Fait traverser un terrain au groupe

        Args:
            terrain (ExplorationTerrain): Terrain à traverser
        """
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