"""
--Fiche de classe/fonction-- 

nom : Plateau
fonction/utilité attendue : Construction du plateau contenant toutess les cases du jeu
type valeur en entrée :
	- Hauteur du plateau(int)
	- Largeur du plateau (Int)
	- Nombres de Mines (Int)
type valeur en sortie : 
	- Objet plateau contenant toutes les cases du Démineur
liste appel d'autre fonction : 
	- Constructeur
		- RemplirCase
		- PlacerMines(int Nombre_de_mines)
	- RemplirCase
		- Constructeur de la classe Case 
	- PlacerMines
		- SignalerMineAuxVoisins
"""
from Case import Case
import random

class Plateau():
	#Plateau du Démineur
	
	"""Attributs :
	- cases				-> Liste : Contient toutes les cases de la grille
	- hauteur 			-> Int : Nombre de lignes du plateau
	- largeur 			-> Int : Nombre de colonne du plateau
	- nbr_Mines			-> Int : Nombre de mines sur le plateau
	- nbr_Cases_Caches 	-> Int (hauteur * largeur) : Nombre de cases cachées au départ
	"""
	
	def __init__(self, hauteur, largeur, nbr_mines):
		#Initialisation du plateau
		
		self.hauteur = hauteur
		self.largeur = largeur
		self.nbr_Mines = nbr_mines
		self.nbr_Cases_Caches = hauteur * largeur
		self.cases = []
		self.remplirCases() #Initialisation du plateau
		self.placerMines(nbr_mines)
		
	def remplirCases(self):
		#Remplit le plateau de cases initialisée
		
		self.cases = [Case() for x in range(self.hauteur * self.largeur)]

	def placerMines(self, nbr_mines):
		#Place les mines aléatoirement dans le plateau
		
		for x in range(nbr_mines):
			caseIndex = random.randint(0, self.hauteur * self.largeur - 1) #On choisit aléatoirement une case du plateau
			while self.cases[caseIndex].mine :  #Tant que la case choisi à déjà une bombe...
				caseIndex = random.randint(0, self.hauteur * self.largeur - 1) #On recommence
			ligne = caseIndex // self.largeur
			"""
			La ligne de la case est obtenue en divisant l'index de la case par la largeur du plateau, 
			soit le nombre de colonnes
			"""
			colonne = caseIndex % self.largeur
			"""
			La colonne est donc le reste de la division ci-dessus
			"""
			self.cases[caseIndex].DevenirBombe() #La Case devient une bombe
			self.SignalerMineAuxVoisins(ligne, colonne)
			
	def SignalerMineAuxVoisins(self, ligne, colonne):
		"""
		Signale la présence d'une mine à tous les voisins de la case
		
		Chaque case est représentée comme le croissement d'une ligne et d'une colonne, et par un numéro d'index
		Chaque index peut être calculée de la manière suivante : Ligne * LargeurPlateau + Colonne.
		Le plateau se représente da la manière suivante :
			Chaque colonne est numérotée de 0 à n-1 largeur
			Chaque ligne est numérotée de 0 à n-1 hauteur
			Il y a donc (Hauteur * Largeur) Index
			
				| C0 | C1 | C2 | C3 |
			 L0	| 0  | 1  | 2  | 3  |
			 L1 | 4  | 5  | 6  | 7  |
			 L2 | 8  | 9  | 10 | 11 |
			 
			 Les voisins d'une case en ligne L et colonne C sont donc la partie du tableau allant de
				- L-1 à L+1
				- C-1 à C+1
		"""
		for L in range(max(0,ligne-1), min(ligne+1, self.hauteur-1)):
			for C in range(max(0,colonne-1), min(colonne+1, self.largeur-1)):
				self.cases[L * self.largeur + C].AvoirMineVoisine() #On signale à la case qu'elle a une mine parmi ses voisins
		