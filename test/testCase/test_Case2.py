"""
++++Fonction de test de Case ++++
procédure de test : 
0) importer la classe a tester et unittest.
1) définir le "set up" : création de l'objet sur le quel on va tester les fonctions de test.
2) test de la fonction : - définir mauvaise valeur - executer la fonction - assertEqual de la bonne valeur.
"""



from Case import Case			#0
import unittest	#0

class testCase(unittest.TestCase):

	def setUp(self):			#1
		self.case01 = Case()	#1
#
#	def testRetourCase(self): 	#2
#		self.case01.mine = True
#		self.case01.drapeau = True
#		self.case01.visible = True
#		self.case01.bomsVois = 9
#		
#		self.case01.RetourCase()
#		
#		self.assertEqual(False,self.case01.mine)
#		self.assertEqual(False,self.case01.drapeau)
#		self.assertEqual(False,self.case01.visible)
#		self.assertEqual(0,self.case01.bomsVois)

	def testDevenirBombe(self):	#2
		self.case01.mine = False
		self.case01.DevenirBombe()
		self.assertEqual(True,self.case01.mine)

	def testEstUneBombe(self):
		self.case01.mine = True
		self.assertEqual(True,self.case01.EstUneBombe())
		self.case01.mine = False
		self.assertEqual(False,self.case01.EstUneBombe())		


	def testRendreVisible(self):	#2
		self.case01.visible = False
		self.case01.RendreVisible()
		self.assertEqual(True,self.case01.visible)

	def testEstVisible (self):
		self.case01.visible = True
		self.assertEqual(True,self.case01.EstVisible())
		self.case01.visible = False
		self.assertEqual(False,self.case01.EstVisible())		

	def testChangeDrapeau(self):	#2
		self.case01.drapeau = False
		self.case01.ChangeDrapeau()
		self.assertEqual(True,self.case01.drapeau)

	def testEstDrapeau(self):	
		self.case01.drapeau = True
		self.assertEqual(True,self.case01.EstDrapeau())
		self.case01.drapeau = False
		self.assertEqual(False,self.case01.EstDrapeau())	

	def testAvoirMineVoisine(self):	#2
		self.case01.bomsVois = 0
		self.case01.AvoirMineVoisine()
		self.assertEqual(1,self.case01.bomsVois)

	# def ANbrBombesVoisins


print("Acces to test_Case OK")
