"""
--Fiche de classe/fonction-- 

nom : Case
fonction/utilité attendue : 
	- Construction d'une Case
	- Retour de son contenu en fonction de son état.
type valeur en entrée : /
type valeur en sortie : 
	- Objet Case et son contenu
liste appel d'autre fonction : /
"""

class Case():
	#Case du champs de mine
	
	""" Attributs:
	- Mine 			-> Bool : True = Mine, False = Pas mine
	- Drapeau		-> Bool : True = Drapeau, False = Pas Drapeau
	- Visible		-> Bool : True = La case est découverte
	- BombesVoisins	-> Int : Nombre de bombes dans les cases abjacentes
	"""
	
	def __init__(self):
		#Initialisation de la case. Par défaut :
		
		self.mine = False 			#Une case n'a pas de mine.
		self.drapeau = False 		#Une case n'a pas de drapeau.
		self.visible = False		#Son contenu n'est pas visible
		self.bomsVois = 0			#Elle n'a pas de bombes dans son voisinnage
	
	def RetourCase(self):
		#Retourne un caractère symboliasant l'état de la cas.
		if self.visible: #Si la case est découverte
			if self.Mine: #Si elle a une mine
				return 'Mine'
			else: #Si elle n'a pas de mine
				return str(self.bomsVois) if self.bomsVois else '' #On retoune le nombre de bombes voisines si elle en a
		else :
			return 'drapeau' if self.drapeau else '' #On affiche le drapeau si elle en a un.
			