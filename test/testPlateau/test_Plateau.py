
from Case import Case
from plateau import plateau
import random
import unittest
class testPlateau(unittest.TestPlateau):
	def setUp(self):
		self.plateau01 = plateau()
	
	def testremplirCases(self): #self.cases = [Case() for x in range(self.hauteur * self.largeur)]
		
		
		
		self.plateau01.remplirCases(self)