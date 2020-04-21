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
"""

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
			ligne = caseIndex // largeur
			"""
			La ligne de la case est obtenue en divisant l'index de la case par la largeur du plateau, 
			soit le nombre de colonnes
			"""
			colonne = caseIndex % largeur
			"""
			La colonne est donc le reste de la division ci-dessus
			"""
			self.cases[caseIndex].mine = true #On passe l'état de la case choisie à miné.