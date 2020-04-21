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
	- nbr_drapeau		-> Int : Nombre de drapeau sur la grille
	- nbr_Cases_Caches 	-> Int (hauteur * largeur) : Nombre de cases cachées au départ
	- gameOver			-> Bool : Indique la fin de partie. True = Partie Perdue
	"""
	
	def __init__(self, type_partie, hauteur, largeur, nbr_mines):
		#Initialisation du plateau
		
		self.hauteur = hauteur
		self.largeur = largeur
		self.nbr_Mines = 0 #Nombre de drapeau sur la grille
		self.nbr_drapeau = 0 #Nombre de mines sur la grille
		self.nbr_Cases_Caches = hauteur * largeur
		self.gameOver = False
		self.cases = []
		
		self.remplirCases() #Initialisation du plateau
		self.determinerMines(type_partie, nbr_mines)
		
	def remplirCases(self):
		#Remplit le plateau de cases initialisée
		
		self.cases = [Case() for x in range(self.hauteur * self.largeur)]
		
	def determinerMines(self, type_partie, nbr_mines):
		LETHAL = 1
		PROPA = 2
		TIMER = 3
		COUP = 4
		
		if (type_partie < 2):
			self.placerMines(nbr_mines, 1)
		else:
			nbr_spcl_mines = nbr_mines // 5
			self.placerMines(nbr_mines - 3*nbr_spcl_mines, 1)
			self.placerMines(nbr_spcl_mines, 2)
			self.placerMines(nbr_spcl_mines, 3)
			self.placerMines(nbr_spcl_mines, 4)

	def placerMines(self, nbr_mines, type):
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
			self.cases[caseIndex].DevenirBombe(type) #La Case devient une bombe
			self.SignalerMineAuxVoisins(ligne, colonne)
			self.nbr_Mines +=1
			
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
		for L in range(max(0,ligne-1), min(ligne+2, self.hauteur)):
			for C in range(max(0,colonne-1), min(colonne+2, self.largeur)):
				self.cases[L * self.largeur + C].AvoirMineVoisine() #On signale à la case qu'elle a une mine parmi ses voisins
	
	def Gagner(self):
		#Verifie que le nombre de case cachées est égale au nombre de mine
		return self.nbr_Cases_Caches == self.nbr_Mines
	
	def Draper(self, ligne, colonne):
		
		#Pose ou retire un drapeau à la position (ligne, colonne)
		#Incrémente ou décrémente le nombre de nbr_drapeau du plateau en fonction
		#ne fait rien si le contenu de la cellule est visible
		
		
		#On récupère l'index de la case
		case = self.cases[ligne * self.largeur + colonne]
		if not case.EstVisible(): #Si la case n'est pas visible
			case.ChangeDrapeau() #On change l'état Drapeau
			if case.EstDrapeau():
				self.nbr_drapeau +=1
			else:
				self.nbr_drapeau -=1
				
	def CreuserCase(self, ligne, colonne):
		#Creuse la case à la position (ligne, colonne)
		
		#On récupère l'index de la case
		case = self.cases[ligne * self.largeur + colonne]
		
		#Si la case est visible ou a un drapeau, on ne fait rien
		if case.EstVisible() or case.EstDrapeau():
			return
		#Sinon, on rend visible le contenu et on diminue le nombre de cases cachées
		else:
			case.RendreVisible()
			self.nbr_Cases_Caches -=1
			
			#Si la case est minée, la partie est perdue
			#Donc, si EstBombe est différent de 0
			if (case.EstUneBombe() > 0):
				self.gameOver = True
			
			#Si la case n'a aucune bombe dans parmi ses voisins
			if (case.ANbrBombesVoisins() == 0):
				#On parcout ses voisins
				for L in range(max(0,ligne-1), min(ligne+2, self.hauteur)):
					for C in range(max(0,colonne-1), min(colonne+2, self.largeur)):
						#Et on les joue
						self.CreuseCase(L, C)
			#On finit par vérifier si la partie est gagnée
			self.gameOver = self.Gagner()
	
	def AfficherTableau(self):
		#Retourne la grille sous forme de string, Affichage Test
		
		for L in range(self.hauteur):
			print(" ", end='')
			for C in range(self.largeur) :
				case = self.cases[L * self.largeur + C]
				if self.gameOver and case.EstUneBombe():
					print("M ", end ='')
				if not case.EstVisible():
					if case.EstDrapeau():
						print("D ", end='')
					else:
						print("X ", end='')
				else:
					print("%d " % (case.ANbrBombesVoisins()), end ='')	
			print ()
		print()
		print()