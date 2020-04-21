from Plateau import Plateau
import time

if __name__ == '__main__':
	NORMAL = 0
	PROPA = 1
	APO = 2
	
	HAUTEUR = 6
	LARGEUR = 5
	MINES = 5
	
	def testPlateau(type): 
	
		plateau = Plateau(type, HAUTEUR, LARGEUR, MINES)
		
		for L in range(HAUTEUR):
			for C in range(LARGEUR) :
				print("%d " % (plateau.cases[L * LARGEUR + C].ANbrBombesVoisins()), end ='')
			print('   ', end='')	
			for C in range(LARGEUR) :
				print("%d " % (plateau.cases[L * LARGEUR + C].EstUneBombe()), end ='')	
			print ()
		print()
		print()
		
	testPlateau(NORMAL)
	
	HAUTEUR = 8
	LARGEUR = 8
	MINES = 20
	
	testPlateau(NORMAL)
	testPlateau(APO)
	
	