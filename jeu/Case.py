"""
--Fiche de classe/fonction-- 

nom : Case
fonction/utilité attendue : 
	- Construction d'une Case
	- Retour de son contenu en fonction de son état.
	- Définir une case comme Bombe
	- Augmenter le nombre de Bombe dans le voisinage
	- Changer l'état Drapeau
type valeur en entrée : /
type valeur en sortie :
	- Objet Case
	- Bool : EstVisible, EstDrapeau
	- Int : ANbrBombesVoisins, EstBombe
liste appel d'autre fonction : /
"""

class Case():
	#Case du champs de mine
	
	""" Attributs:
	- Mine 			-> Int : 0 = pas de Mine, 1 = Léthal, 2 = Propagation, 3 = Timer+, 4 = Coup+
	- Drapeau		-> Bool : True = Drapeau, False = Pas Drapeau
	- Visible		-> Bool : True = La case est découverte
	- BombesVoisins	-> Int : Nombre de bombes dans les cases abjacentes
	"""
	
	def __init__(self):
		#Initialisation de la case. Par défaut :
		
		self.mine = 0				#Une case n'a pas de mine.
		self.drapeau = False 		#Une case n'a pas de drapeau.
		self.visible = False		#Son contenu n'est pas visible
		self.bomsVois = 0			#Elle n'a pas de bombes dans son voisinnage
	
	def RetourCase(self):
		#Retourne un caractère symboliasant l'état de la cas. Affichage Test
		if self.visible: #Si la case est découverte
			if self.mine > 0: #Si elle a une mine
				return 'M'
			else: #Si elle n'a pas de mine
				return str(self.bomsVois) if self.bomsVois else ' ' #On retoune le nombre de bombes voisines si elle en a
		else :
			return 'D' if self.drapeau else 'X' #On affiche le drapeau si elle en a un.
			
	def DevenirBombe(self, level): #La case devient piègée
		self.mine = level
		
	def EstUneBombe(self):
		return self.mine
	
	def RendreVisible(self): #La case est découverte
		self.visible = True
		
	def EstVisible(self):
		return self.visible
		
	def ChangeDrapeau(self): #On pose ou on retire un drapeau
		self.drapeau = not self.drapeau
	
	def EstDrapeau(self):
		return self.drapeau
	
	def AvoirMineVoisine(self): #La case a une mine parmi ses voisins
		self.bomsVois += 1 #On augment le nombre de ses voisins de 1
		
	def ANbrBombesVoisins(self):
		return self.bomsVois
			