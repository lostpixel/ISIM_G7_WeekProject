"""
===================================TEST ===================================
-> Variables en privé donc pas de test possible

+++++ Table des partie +++++
- print message varables privé
- print de test confirmation d'accès
- importation
- fonctions de test 
- variable de verbosité à l'execution

+++++ Fonction de test de Case +++++

procédure de test : 
- importer la classe a tester et unittest.
- définir le "set up" : création de l'objet sur le quel on va tester les fonctions de test.
- test de fonction qui modifie la valeur (ex DevenirBombe): - définir mauvaise valeur - executer la fonction - assertEqual de la bonne valeur.
- test de fonction qui retourne une valeur (ex EstUneBombe) : - définir une valeur - assertTrue ou assertFalse de la fonction.

A faire si case.py redevient publique : 
- commenter ligne 30 : print("\n Private method don't you dare to grobe, you'r pervert !")
- décommenter ligne 31 : import unittest
- décommenter les """ """ de la classe testCase
- décommenter ligne 122 #suite = unittest.TestLoader().loadTestsFromTestCase(testCase)
- décommenter ligne 123 #unittest.TextTestRunner(verbosity=2).run(suite)
"""


#test d'accès au fichier	
print("\naccesTo test_Case.py (__main__.gauche) ... ok")

from Case import Case			#0
print("\n Private method cant' acces to it")
#import unittest	

"""

class testCase(unittest.TestCase):

	def setUp(self):			#1
		self.case01 = Case()	#1
	

	def testDevenirBombe(self):												#action de la fonction à tester: fait passer case.mine à true
		#SomeCoolException : " private access, don't grope it u perv !"
		#self.assertRaises(SomeCoolException, self.assertIsInstance(self.case01.mine,bool))
		self.assertIsInstance(self.case01.mine,bool)
		self.case01.mine = False
		self.case01.DevenirBombe()
		#self.assertRaises("SomeCoolException", self.assertTrue(self.case01.mine))			
		self.assertTrue(self.case01.mine)
	
	def testEstUneBombe(self): 												#action de la fonction à tester: retourne l'état de case.mine
		self.case01.mine = True
		#self.assertEqual(True,self.case01.EstUneBombe()) 					#A conserver si on veut comparer avec une autre valeur dans le future
		self.assertTrue(self.case01.EstUneBombe())
		self.case01.mine = False
		#self.assertEqual(False,self.case01.EstUneBombe())
		self.assertFalse(self.case01.EstUneBombe())

	def testRendreVisible(self):											#action de la fonction à tester: retourne l'état de case.visible
		self.assertIsInstance(self.case01.visible,bool)
		self.case01.visible = False
		self.case01.RendreVisible()
		self.assertEqual(True,self.case01.visible)

	def testEstVisible (self):												#action de la fonction à tester: retourne l'état de case.visible
		self.assertIsInstance(self.case01.visible,bool)
		self.case01.visible = True
		#self.assertEqual(True,self.case01.EstVisible())
		self.assertTrue(self.case01.EstVisible())
		self.case01.visible = False
		#self.assertEqual(False,self.case01.EstVisible())
		self.assertFalse(self.case01.EstVisible())

	def testChangeDrapeau(self):											#action de la fonction à tester: faiter passer case.drapeau à sa valeur opposée
		self.assertIsInstance(self.case01.drapeau,bool)
		self.case01.drapeau = True
		self.case01.ChangeDrapeau()
		#self.assertEqual(True,self.case01.drapeau) 
		self.assertFalse(self.case01.drapeau)
		#print("valeur de drapeau 1 = "+ str(self.case01.drapeau)) 			# test de test :p
		
		self.case01.drapeau=False
		#print("valeur de drapeau 2 = "+ str(self.case01.drapeau)) 			# test de test :p
		#self.assertIsInstance(self.case01.drapeau,bool) 					# redondant
		self.case01.ChangeDrapeau()
		#print("valeur de drapeau 3 = "+ str(self.case01.drapeau)) 			# test de test :p
		#self.assertEqual(False,self.case01.drapeau)
		self.assertTrue(self.case01.drapeau)
		
	def testEstDrapeau(self):												#action de la fonction à tester: retourne la valeur de case.drapeau
		self.assertIsInstance(self.case01.visible,bool)
		self.case01.drapeau = True
		#self.assertEqual(True,self.case01.EstDrapeau())
		self.assertTrue(self.case01.EstDrapeau())
		self.case01.drapeau = False
		#self.assertEqual(False,self.case01.EstDrapeau())
		self.assertFalse(self.case01.EstDrapeau())

	def testAvoirMineVoisine(self):											#action de la fonction à tester: ajoute un au nombre de mine voisines
		self.assertIsInstance(self.case01.bomsVois,int)	
		#print("valeur de bomsVois = "+ str(self.case01.bomsVois)) 		
		self.case01.bomsVois = 0
		self.assertTrue(0 <= self.case01.bomsVois <= 9)
		self.case01.AvoirMineVoisine()
		self.assertEqual(1,self.case01.bomsVois)
	

	def testANbrBombesVoisins(self):										#action de la fonction à tester: retourne le nombre de mine autour de la case
	self.assertIsInstance(self.case01.bomsVois,int)
	self.case01.bomsVois = 0
	self.assertEqual(0,self.case01.AvoirMineVoisine())
"""


# Executer le scripte de test non verbeux ; permet l"execution de unittest sans devoir le précisier dans la commande
#if __name__ == '__main__': 
#unittest.main()

#Executer le scripte de test de manière verbeuse

#suite = unittest.TestLoader().loadTestsFromTestCase(testCase)
#unittest.TextTestRunner(verbosity=2).run(suite)

#0 (quiet): you just get the total numbers of tests executed and the global result
#1 (default): you get the same plus a dot for every successful test or a F for every failure
#2 (verbose): you get the help string of every test and the result


	

