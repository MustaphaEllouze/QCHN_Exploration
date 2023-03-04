from Utility import (
    EDateTime,
)

from ExplorationItems import (
    ExplorationTerrain,
    ExplorationPlace,
)

class ExplorationMap : 
    """Représente une carte
    """
    def __init__(
            self,
            name,
            origin_hex = (0,0),
            origin_hex_type = ExplorationTerrain.plains,
            origin_hex_place = None,
    ):
        """Constructeur

        Args:
            name (str): Nom de la carte
            origin_hex ((int,int), optional): Coordonées du point d'origine. Defaults to (0,0).
            origin_hex_type (ExplorationTerrain, optional): Type de l'hex d'origine. Defaults to ExplorationTerrain.plains.
            origin_hex_place (ExplorationPlace, optional): Endroit spécial de l'hex d'origine. Defaults to None.
        """
        
        # --- On check le type des variables
        assert origin_hex_place is None or type(origin_hex_place) is ExplorationPlace

        # --- Attribut name
        self.name = name

        # --- Attribut origin_hex
        self.origin_hex = origin_hex
        
        # --- Initialisation de self.hexs : dict{(int,int):ExplorationTerrain}
        # Contient l'ensemble des types des hex de la carte
        # Tous les hexs définis doivent être dans self.hexs
        self.hexs = {}
        self.hexs[origin_hex] = origin_hex_type

        # --- Idem que self.hexs, avec les endroits spéciaux
        # Seules les endroits spéciaux sont dans self.places
        self.places = {}
        if not origin_hex_place is None:
            self.places[origin_hex]=origin_hex_place

    
    def define_from_coord(
            self,
            coord,
            hex_type=ExplorationTerrain.plains,
            hex_place=None,
    ):
        """Définit un nouveau hex, ou redéfinit un hex existant

        Args:
            coord (int,int): Coordonnée du hex à (re)définir
            hex_type (ExplorationTerrain, optional): Type de l'hex. Defaults to ExplorationTerrain.plains.
            hex_place (ExplorationPlace, optional): Endroit spécial de l'hex. Defaults to None.
        """
        assert hex_place is None or type(hex_place) is ExplorationPlace

        self.hexs[coord] = hex_type
        if not hex_place is None :
            self.places[coord]=hex_place 
    
    def define_from_coord_and_tag(
            self,
            coord,
            hex_type=ExplorationTerrain.plains.tag_name,
            hex_place=None,
            
    ):
        """Définit un nouveau hex, ou redéfinit un hex existant, à partir d'un TAG de terrain/place

        Args:
            coord (int,int): Coordonnée du hex à (re)définir
            hex_type (str, optional): TAG du type de l'hex. Defaults to ExplorationTerrain.plains.tag_name.
            hex_place (str, optional): TAG de l'endroit spécial de l'hex. Defaults to None.
        """
        self.define_from_coord(
            coord=coord,
            hex_type=ExplorationTerrain.TERRAINS_FROM_TAG[hex_type],
            hex_place=ExplorationPlace.PLACES_FROM_TAG[hex_place],
        )

    def define_from_ref(
            self,
            ref_hex,
            hex_type=ExplorationTerrain.plains,
            direction='N',
            hex_place=None,
    ):
        """Définit un nouveau hex, ou redéfinit un hex existant, à partir d'un hex de référence

        Args:
            ref_hex (int,int): Coordonnée du hex de référence
            hex_type (ExplorationTerrain, optional): Type de l'hex à définir. Defaults to ExplorationTerrain.plains.
            direction (str, optional): Direction ref_hex -> target_hex (N,S,NE,NW,SE,SW). Defaults to 'N'.
            hex_place (ExplorationPlace, optional): Endroit spécial de l'hex à définir. Defaults to None.
        """

        # --- Gestion des variables d'entrée
        assert direction in ['N','S','NE','SE','NW','SW']
        assert hex_place is None or type(hex_place) is ExplorationPlace

        # --- Calcul de la coordonnée du target_hex
        # Attention, le calcul diffère en fonction de la colonne choisie
        if direction == 'N':
            decal = ( 0,-1)
        elif direction == 'S':
            decal = ( 0, 1)
        elif direction == 'NE':
            if ref_hex[0]%2==0 : decal = ( 1,-1)
            else :               decal = ( 1, 0)
        elif direction == 'SE':
            if ref_hex[0]%2==0 : decal = ( 1, 0)
            else               : decal = ( 1, 1)
        elif direction == 'NW':
            if ref_hex[0]%2==0 : decal = (-1,-1)
            else               : decal = (-1, 0)
        elif direction == 'SW':
            if ref_hex[0]%2==0 : decal = (-1, 0)
            else               : decal = (-1, 1)
        
        # --- Calcul des coordonnées
        target_hex = (
            ref_hex[0]+decal[0],
            ref_hex[1]+decal[1],
        )

        # --- Définition de l'hex cible dans les attributs d'instance
        self.hexs[target_hex]=hex_type
        if not hex_place is None :
            self.places[target_hex]=hex_place 
    
    def define_from_ref_and_tag(
            self,
            ref_hex,
            hex_type='P',
            direction='N',
            hex_place=None,
    ):
        """Définit un nouveau hex, ou redéfinit un hex existant, à partir d'un hex de référence, et du TAG de type


        Args:
            ref_hex (int,int): Coordonnée du hex de référence
            hex_type (str, optional): TAG du type de l'hex à définir. Defaults to ExplorationTerrain.plains.
            direction (str, optional): Direction ref_hex -> target_hex (N,S,NE,NW,SE,SW). Defaults to 'N'.
            hex_place (str, optional): TAG de l'endroit spécial de l'hex à définir. Defaults to None.
        """
        self.define_from_ref(
            ref_hex=ref_hex,
            hex_type=ExplorationTerrain.TERRAINS_FROM_TAG[hex_type],
            direction=direction,
            hex_place=ExplorationPlace.PLACES_FROM_TAG[hex_place],
        )

    def define_column(
            self,
            column_number=0,
            starting_index=0,
            hex_types=[],
            reverse=False,
    ):
        """Définit toute une colonne de hexs

        Args:
            column_number (int, optional): Numéro de la colonne à définir. Defaults to 0.
            starting_index (int, optional): 1er hex de la colonne à définir. Defaults to 0.
            hex_types (list(ExplorationTerrains), optional): Liste des types d'hexs de la colonne. Defaults to [].
            reverse (bool, optional): True si la colonne est à définir vers le Nord, False vers le Sud. Defaults to False.
        """
        if reverse : reverse_coef = -1
        else: reverse_coef = 1

        for j,coord in enumerate([(column_number,starting_index+i*reverse_coef) for i in range(len(hex_types))]):
            self.define_from_coord(coord=coord,hex_type=hex_types[j])
    
    def define_list_of_coords(
            self,
            list_of_coords = [],
            hex_type=ExplorationTerrain.plains,
            hex_place=None,
    ):
        """Définit des hexs d'un seul type de terrain

        Args:
            list_of_coords (list(int,int), optional): Coordonnées des hexs à définir. Defaults to [].
            hex_type (ExplorationTerrain, optional): Type de terrain à définir. Defaults to ExplorationTerrain.plains.
            hex_place (ExplorationPlace, optional): Type d'endroit spécial à définir. Defaults to None.
        """
        for coord in list_of_coords:
            self.define_from_coord(
                coord=coord,
                hex_type=hex_type,
                hex_place=hex_place
            )
    
    def define_list_of_coords_with_tag(
            self,
            list_of_coords=[],
            hex_type=ExplorationTerrain.plains.tag_name,
            hex_place=None,
    ):
        """Définit des hexs d'un seul type de terrain à partir d'un TAG de terrain

        Args:
            list_of_coords (list(int,int), optional): Coordonnées des hexs à définir. Defaults to [].
            hex_type (str, optional): TAG du type de terrain à définir. Defaults to ExplorationTerrain.plains.
            hex_place (str, optional): TAG du type d'endroit spécial à définir. Defaults to None.
        """
        for coord in list_of_coords:
            self.define_from_coord_and_tag(
                coord=coord,
                hex_type=hex_type,
                hex_place=hex_place,
            )

    def neighbours_of_hex(
            self,
            target_hex_coord,
    ):
        """Retourne l'ensemble des coordonénes des voisins de l'hex
        NOTE : Uniquement ceux définis

        Args:
            target_hex_coord (int,int): Hex dont on veut connaître les voisins

        Returns:
            list(int,int): Coordonnées des hexs voisins
        """
        # --- Attention : Les coordonnées des voisins diffèrent selon la parité de la colonne
        if target_hex_coord[0]%2 == 0 :
            potentials_neighbours = [
                (target_hex_coord[0]  ,target_hex_coord[1]-1),
                (target_hex_coord[0]  ,target_hex_coord[1]+1),
                (target_hex_coord[0]+1,target_hex_coord[1]-1),
                (target_hex_coord[0]+1,target_hex_coord[1]  ),
                (target_hex_coord[0]-1,target_hex_coord[1]-1),
                (target_hex_coord[0]-1,target_hex_coord[1]  ),
            ]
        else:
            potentials_neighbours = [
                (target_hex_coord[0]  ,target_hex_coord[1]-1),
                (target_hex_coord[0]  ,target_hex_coord[1]+1),
                (target_hex_coord[0]+1,target_hex_coord[1]  ),
                (target_hex_coord[0]+1,target_hex_coord[1]+1),
                (target_hex_coord[0]-1,target_hex_coord[1]  ),
                (target_hex_coord[0]-1,target_hex_coord[1]+1),
            ]
        
        # --- Variable de retour
        return [c for c in potentials_neighbours if c in self.hexs.keys()]

    def neighbours_at_range_X(
            self,
            target_hex_coord,
            range=1,
    ):
        """Retourne l'ensemble des coordonénes des voisins de l'hex, à portée 'range'
        NOTE : Uniquement ceux définis

        Args:
            target_hex_coord (int,int): Hex dont on veut connaître les voisins
            range (int, optional): Portée des voisins. Defaults to 1.

        Returns:
            list(int,int): Coordonnées des hexs voisins
        """
        # --- Définie de façon récursive

        # Si range = 1 ; condition d'arrêt évidente
        if range == 1 :
            return self.neighbours_of_hex(target_hex_coord)
        
        # Sinon, on renvoit les voisins des voisins à portée 'range-1'
        else:
            result = []
            for neigh in self.neighbours_at_range_X(target_hex_coord,range=range-1):
                result += self.neighbours_of_hex(neigh)
            return list(set(result))
            

    def bounding_box(self):
        """Renvoie la bounding box de la carte

        Returns:
            int,int,int,int: x_min,x_max,y_min,y_max
        """
        min_x = min([coord[0] for coord in self.hexs.keys()])
        max_x = max([coord[0] for coord in self.hexs.keys()])
        min_y = min([coord[1] for coord in self.hexs.keys()])
        max_y = max([coord[1] for coord in self.hexs.keys()])
        return min_x,max_x,min_y,max_y
    
    def generate_numpy_like(self):
        """Renvoi un tableau contenant les tag de tous les hexs définis

        Returns:
            list(list(str)): Tableau contenant les tag des tous les hex définis
        """
        # --- Récupère la bounding box
        min_x,max_x,min_y,max_y = self.bounding_box()

        # --- Définit le tableau
        result = [['  ' for i in range((max_x-min_x+1))] for j in range((max_y-min_y+1))]
        
        # --- Remplit pour chaque hex défini
        for coord,hex_type in self.hexs.items():
            result[coord[1]-min_y][coord[0]-min_x]=hex_type.tag_name
        
        # --- Variable de retour
        return result
    
    def __str__(self):
        # --- Génère un str image de self.generate_numpy_like()
        result = ''
        for ligne in self.generate_numpy_like():
            for c in ligne:
                result += c+';'
            result += '\n'
        return result
    
    def construct_visibility(self):
        """Définit l'attribut self.visibility, contenant pour chaque hex l'ensemble des hex visibles
        """
        # --- Initialisation de l'attribut 
        self.visibility = {}

        # --- Initialisation des hexs définis
        for coord in self.hexs.keys():
            self.visibility[coord]=[]
        
        # --- Construction inverse : on rajoute chaque hex dans la visibilité de ses voisins
        for coord,hex in self.hexs.items():
            for visible_from_hex in self.neighbours_at_range_X(coord,range=hex.visibility_range):
                self.visibility[visible_from_hex].append(coord)
        

class ExplorationGameManager:
    """Gère toutes les règles du jeu et les calculs
    """
    pass


if __name__ == '__main__':
    map = ExplorationMap(
        name='Scenario1',
        origin_hex=(0,0),
        origin_hex_type=ExplorationTerrain.plains,
    )
    map.define_from_ref(map.origin_hex,ExplorationTerrain.plains,direction='S',hex_place=None)
    map.define_from_coord((1,1),ExplorationTerrain.plains,hex_place=ExplorationPlace.village)
    map.define_from_ref((1,1),ExplorationTerrain.plains,direction='S',hex_place=None)
    print(map.__dict__)