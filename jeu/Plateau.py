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
from abc import ABC
from Case import Case
import random

class PlateauTemplate(ABC):
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
	
	def __init__(self, hauteur, largeur, nbr_mines):
		#Initialisation du plateau
		
		self.__hauteur = hauteur
		self.__largeur = largeur
		self.__nbrMines = 0 #Nombre de drapeau sur la grille
		self.__nbrDrapeaux = 0 #Nombre de mines sur la grille
		self.__nbrCoups = 0
		self.__nbrCasesCaches = hauteur * largeur
		self.__gameOver = False
		self.__cases = []
		self.__Taille = 16
		
		self.remplirCases() #Initialisation du plateau
		self.placerMines(nbr_mines)
		
		def getHauteur(self):
			return self.__hauteur
			
		def getLargeur(self):
			return self.__largeur
			
		def getMines(self):
			return self.__nbrMines
			
		def getCoups(self):
			return self.__nbrCoups
			
		def getCasesCachees(self):
			return self.__nbrCasesCaches
		
	def remplirCases(self):
		#Remplit le plateau de cases initialisée
		
		self.__cases = [Case() for x in range(self.__hauteur * self.__largeur)]
		
	def determinerMines(self, type_partie, nbr_mines):
			nbr_spcl_mines = nbr_mines // 5
			self.placerMines(nbr_mines - 3*nbr_spcl_mines, 1)
			self.placerMines(nbr_spcl_mines, 2)
			self.placerMines(nbr_spcl_mines, 3)
			self.placerMines(nbr_spcl_mines, 4)

	def placerMines(self, nbr_mines):
		#Place les mines aléatoirement dans le plateau
		
		for x in range(nbr_mines):
			caseIndex = random.randint(0, self.__hauteur * self.__largeur - 1) #On choisit aléatoirement une case du plateau
			while self.__cases[caseIndex].EstUneBombe() or self.__cases[caseIndex].EstVisible() :  #Tant que la case choisi à déjà une bombe...
				caseIndex = random.randint(0, self.__hauteur * self.__largeur - 1) #On recommence
			ligne = caseIndex // self.__largeur
			"""
			La ligne de la case est obtenue en divisant l'index de la case par la largeur du plateau, 
			soit le nombre de colonnes
			"""
			colonne = caseIndex % self.__largeur
			"""
			La colonne est donc le reste de la division ci-dessus
			"""
			self.__cases[caseIndex].DevenirBombe(1) #La Case devient une bombe
			self.SignalerMineAuxVoisins(ligne, colonne)
			self.__nbrMines +=1
			
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
		for L in range(max(0,ligne-1), min(ligne+2, self.__hauteur)):
			for C in range(max(0,colonne-1), min(colonne+2, self.__largeur)):
				self.__cases[L * self.__largeur + C].AvoirMineVoisine() #On signale à la case qu'elle a une mine parmi ses voisins
	
	def Gagner(self):
		#Verifie que le nombre de case cachées est égale au nombre de mine
		return self.__nbrCasesCaches == self.__nbrMines
		
	def Perdre(self):
		return self.__gameOver
		
	def JouerCoup(self):
		self.__nbrCoups += 1
	
	def Draper(self, ligne, colonne):
		
		#Pose ou retire un drapeau à la position (ligne, colonne)
		#Incrémente ou décrémente le nombre de nbr_drapeau du plateau en fonction
		#ne fait rien si le contenu de la cellule est visible
		
		
		#On récupère l'index de la case
		case = self.__cases[ligne * self.__largeur + colonne]
		if not case.EstVisible(): #Si la case n'est pas visible
			case.ChangeDrapeau() #On change l'état Drapeau
			if case.EstDrapeau():
				self.__nbrDrapeaux +=1
			else:
				self.__nbrDrapeaux -=1
				
	def CreuserCase(self, ligne, colonne):
		#Creuse la case à la position (ligne, colonne)
		
		#On récupère l'index de la case
		case = self.__cases[ligne * self.__largeur + colonne]
		
		#Si la case est visible ou a un drapeau, on ne fait rien
		if case.EstVisible() or case.EstDrapeau():
			return
		#Sinon, on rend visible le contenu et on diminue le nombre de cases cachées
		else:
			case.RendreVisible()
			self.__nbrCasesCaches -=1
			
			#Si la case est minée, la partie est perdue
			#Donc, si EstBombe est différent de 0
			if (case.EstUneBombe() > 0):
				self.__gameOver = True
			
			#Si la case n'a aucune bombe dans parmi ses voisins
			if (case.ANbrBombesVoisins() == 0):
				#On parcout ses voisins
				for L in range(max(0,ligne-1), min(ligne+2, self.__hauteur)):
					for C in range(max(0,colonne-1), min(colonne+2, self.__largeur)):
						#Et on les joue
						self.CreuserCase(L, C)
			#On finit par vérifier si la partie est gagnée
			self.__gameOver = self.Gagner()
			
	def DessinerTableau(self):
		offsetY = 0
		for Y in self.__hauteur:
			offsetX = 0
			for X in self.__largeur:
				case = self.__cases[Y * self.__largeur + X]
				#case.Dessiner(X + offsetX, Y + offsetY, self.__Taille, self.__Taille)
				offsetX += self.__Taille
			offsetY += self.__Taille
				
	def EstPosition(self, PosX, PosY):
		offsetY = 0
		for Y in self.__hauteur:
			offsetX = 0
			for X in self.__largeur:
				if (X + offsetX <= PosX and PosX <= X + offsetX and Y + offsetY <= PosY and PosY <= Y + offsetY):
					return Y, X
				offsetX += self.__Taille
			offsetY += self.__Taille
	
	
	def AfficherTableau(self):
		#Retourne la grille sous forme de string, Affichage Test
		
		for L in range(self.__hauteur):
			print(" ", end='')
			for C in range(self.__largeur) :
				case = self.__cases[L * self.__largeur + C]
				if self.__gameOver and case.EstUneBombe():
					print("M ", end ='')
				elif not case.EstVisible():
					if case.EstDrapeau():
						print("D ", end='')
					else:
						print("X ", end='')
				else:
					print("%d " % (case.ANbrBombesVoisins()), end ='')	
			print ()
		print()
		print("Mines restantes = %d" % (self.__nbrMines-self.__nbrDrapeaux))
		print("Coups =  %d" % (self.__nbrCoups))
		print()
		
class PlateauNormal(PlateauTemplate):
	
	def __init__(self, hauteur, largeur, nbr_mines):
		PlateauTemplate.__init__(self, hauteur, largeur, nbr_mines)

class PlateauPropagation(PlateauTemplate):

	def __init__(self, hauteur, largeur, nbr_mines):
		PlateauTemplate.__init__(self, hauteur, largeur, nbr_mines)

	def CreuserCase(self, ligne, colonne):
		PlateauTemplate.CreuserCase(self, ligne, colonne)
		if (self.getCoups() % 5) == 0 :
			nbrCasesLibres = self.getCasesCachees() - self.getMines()
			self.PlacerMines(nbrCasesLibres // 20, 1)
			
class PlateauApocalypse(PlateauTemplate): 

	def __init__(self, hauteur, largeur, nbr_mines):
		PlateauTemplate.__init__(self, hauteur, largeur, nbr_mines)

	def PlacerMines(self, nbr_mines):
		nbr_spcl_mines = nbr_mines // 5
		self.placerMines(nbr_mines - 3*nbr_spcl_mines, 1)
		self.placerMines(nbr_spcl_mines, 2)
		self.placerMines(nbr_spcl_mines, 3)
		self.placerMines(nbr_spcl_mines, 4)
			
	def PlacerMines(self, nbr_mines, type):
		for x in range(nbr_mines):
			caseIndex = random.randint(0, self.__hauteur * self.__largeur - 1) #On choisit aléatoirement une case du plateau
			while self.__cases[caseIndex].EstUneBombe() or self.__cases[caseIndex].EstVisible() :  #Tant que la case choisi à déjà une bombe...
				caseIndex = random.randint(0, self.__hauteur * self.__largeur - 1) #On recommence
			ligne = caseIndex // self.__largeur
			"""
			La ligne de la case est obtenue en divisant l'index de la case par la largeur du plateau, 
			soit le nombre de colonnes
			"""
			colonne = caseIndex % self.__largeur
			"""
			La colonne est donc le reste de la division ci-dessus
			"""
			self.__cases[caseIndex].DevenirBombe(type) #La Case devient une bombe
			self.SignalerMineAuxVoisins(ligne, colonne)
			self.__nbrMines +=1
			
	def CreuserCase(self, ligne, colonne):
		#Creuse la case à la position (ligne, colonne)
		
		#On récupère l'index de la case
		case = self.__cases[ligne * self.__largeur + colonne]
		
		#Si la case est visible ou a un drapeau, on ne fait rien
		if case.EstVisible() or case.EstDrapeau():
			return
		#Sinon, on rend visible le contenu et on diminue le nombre de cases cachées
		else:
			case.RendreVisible()
			self.__nbrCasesCaches -=1
			
			#Si la case est minée, la partie est perdue
			#Donc, si EstBombe est différent de 0
			if (case.EstUneBombe() > 0):
				if (case.EstUneBombe() == 1):
					self.__gameOver = True
				if (case.EstUneBombe() == 2):
					for X in range(1, 5):
						self.PlacerMines(1, X)
				if (case.EstUneBombe() == 3):
					print("10 secondes de plus")
				if (case.EstUneBombe() == 4):
					self.__nbrCoups += 5
				
			#Si la case n'a aucune bombe dans parmi ses voisins
			if (case.ANbrBombesVoisins() == 0):
				#On parcout ses voisins
				for L in range(max(0,ligne-1), min(ligne+2, self.__hauteur)):
					for C in range(max(0,colonne-1), min(colonne+2, self.__largeur)):
						#Et on les joue
						self.CreuserCase(L, C)
			#On finit par vérifier si la partie est gagnée
			self.__gameOver = self.Gagner()