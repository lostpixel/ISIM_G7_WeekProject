"""
===================================TEST INTERNE===================================
test interne =  soft test / test de fonctionalité | test externe = hard test / test de posibilitées

+++++ Table des partie +++++

- print de test confirmation d'accès
- importation
- fonctions de test 
- variable de verbosité à l'execution

+++++ Fonction de test de Case ++++

procédure de test : 
- importer la classe a tester et unittest.
- définir le "set up" : création de l'objet sur le quel on va tester les fonctions de test.
- test de fonction qui modifie la valeur (ex DevenirBombe): - définir mauvaise valeur - executer la fonction - assertEqual de la bonne valeur.
- test de fonction qui retourne une valeur (ex EstUneBombe) : - définir une valeur - assertTrue ou assertFalse de la fonction.
"""

#test d'accès au fichier	
print("\naccesTo test_Plateau.py (__main__.gauche) ... ok")


from Case import Case
from plateau import plateau
import random
import unittest
class testPlateau(unittest.TestCase):
	def setUp(self):
		self.plateau01 = plateau()
	
	def testremplirCases(self): #self.cases = [Case() for x in range(self.hauteur * self.largeur)]
		
		
		
		self.plateau01.remplirCases(self)