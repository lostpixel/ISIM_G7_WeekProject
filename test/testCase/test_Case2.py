"""
###################### COMMENTAIRE A REFAIRE ###################################
+++++ Composition +++++
- print de test confirmation d'accès
- importation
- fonctions de test 
- variable de verbosité à l'execution
+++++ Fonction de test de Case ++++
procédure de test : 
a) importer la classe a tester et unittest.
b) définir le "set up" : création de l'objet sur le quel on va tester les fonctions de test.
c) test de fonction qui modifie la valeur (ex DevenirBombe): - définir mauvaise valeur - executer la fonction - assertEqual de la bonne valeur.
d) test de fonction qui retourne une valeur (ex EstUneBombe) : - définir une valeur - assertTrue ou assertFalse de la fonction.
"""


#test d'accès au fichier	
print("\naccesTo test_Case.py (__main__.gauche) ... ok")


from Case import Case			#0
import unittest	#0
import inspect


class testCase(unittest.TestCase):

	def setUp(self):			#1
		self.case01 = Case()
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
	def testDevenirBombe(self):												#action de la fonction à tester: fait passer case.mine à true (bool)	
		varTest = [None,True,False,-1,0,0.1,1,'a','A','?','.','/','§','-0b100101']
		print("\n")
		for i in range(0,len(varTest)):
			self.case01.mine = varTest[i]
			print("la valeur de mine avant F = " + str(self.case01.mine))
			#self.assertIsInstance(self.case01.mine,bool)
			#self.case01.mine = False
			self.case01.DevenirBombe()
			print("la valeur de mine après F = " + str(self.case01.mine))
			#self.assertEqual(True,self.case01.mine)
			self.assertTrue(self.case01.mine)
		#self.case01.mine = False
		#self.assertTrue(self.case01.mine)

	def testEstUneBombe(self): 												#action de la fonction à tester: retourne l'état (bool) de case.mine
		varTest = [True,False,-1,0,0.1,1,'a','A','?','.','/','§','-0b100101']
		for i in range(0,len(varTest)):
			self.case01.mine = varTest[i]
			#print("la valeur de mine avant F = " + str(self.case01.mine))
			self.case01.EstUneBombe()
			self.assertIsInstance(self.case01.mine,bool)
			#print("la valeur de mine après F = " + str(self.case01.mine))

	def testRendreVisible(self):											#action de la fonction à tester: retourne l'état (bool) de case.visible
		varTest = [True,False,-1,0,0.1,1,'a','A','?','.','/','§',0b100101]
		for i in range(0,len(varTest)):
			self.case01.visible = varTest[i]
			self.case01.RendreVisible()
			self.assertTrue(self.case01.visible)
		#self.case01.visible = False
		#self.assertEqual(True,self.case01.visible)

	def testEstVisible (self):												#action de la fonction à tester: retourne l'état (bool) de case.visible
		varTest = [True,False,-1,0,0.1,1,'a','A','?','.','/','§',0b100101]
		for i in range(0,len(varTest)):
			self.case01.visible = varTest[i]		
			self.case01.EstVisible()
			self.assertIsInstance(self.case01.visible,bool)
		#self.case01.visible = True
		#self.assertEqual(True,self.case01.EstVisible())
		#self.assertTrue(self.case01.EstVisible())
		#self.case01.visible = False
		#self.assertEqual(False,self.case01.EstVisible())
		#self.assertFalse(self.case01.EstVisible())

	def testChangeDrapeau(self):											#action de la fonction à tester: faiter passer case.drapeau à sa valeur (bool) opposée
		varTest = [True,False,-1,0,0.1,1,'a','A','?','.','/','§',0b100101]
		for i in range(0,len(varTest)):
			self.case01.drapeau = varTest[i]		
			self.case01.ChangeDrapeau()
			self.assertIsInstance(self.case01.drapeau,bool)
		
		#self.case01.drapeau = True
		
		#self.assertEqual(True,self.case01.drapeau) 
		#self.assertFalse(self.case01.drapeau)
		#print("valeur de drapeau 1 = "+ str(self.case01.drapeau)) 			# test de test :p
		
		#self.case01.drapeau=False
		#print("valeur de drapeau 2 = "+ str(self.case01.drapeau)) 			# test de test :p
		#self.assertIsInstance(self.case01.drapeau,bool) 					# redondant
		#self.case01.ChangeDrapeau()
		#print("valeur de drapeau 3 = "+ str(self.case01.drapeau)) 			# test de test :p
		#self.assertEqual(False,self.case01.drapeau)
		#self.assertTrue(self.case01.drapeau)
		
	def testEstDrapeau(self):												#action de la fonction à tester: retourne la valeur (bool) de case.drapeau
		varTest = [True,False,-1,0,0.1,1,'a','A','?','.','/','§',0b100101]
		for i in range(0,len(varTest)):
			self.case01.drapeau = varTest[i]		
			self.case01.EstDrapeau()
			self.assertIsInstance(self.case01.drapeau,bool)

	def testAvoirMineVoisine(self):													#action de la fonction à tester: ajout un au nombre (int) de bombes voisines (bombsVois)
		varTest = [True,False,-1,0,0.1,1,'a','A','?','.','/','§',0b100101]
		for i in range(0,len(varTest)):
			self.case01.bomsVois = varTest[i]		
			self.case01.AvoirMineVoisine()
			self.assertIsInstance(self.case01.bomsVois,int)
			self.assertTrue(0 <= self.case01.bomsVois <= 9)	
			
		#print("valeur de bomsVois = "+ str(self.case01.bomsVois)) 		
		#self.case01.bomsVois = 0
		#self.case01.AvoirMineVoisine()
		#self.assertEqual(1,self.case01.bomsVois)

	def testANbrBombesVoisins(self):												#action de la fonction à tester: retoune le nombre (int) de bombes voisines (bombVois)
		varTest = [True,False,-1,0,0.1,1,'a','A','?','.','/','§',0b100101]
		for i in range(0,len(varTest)):
			self.case01.bomsVois = varTest[i]
			#print("Valeur bomsVois avant test int "+ str(self.case01.bomsVois))
			if type(self.case01.bomsVois) is bool : 								# ajout du test car un bool est compris dans les sous type de int
				self.assertEqual(True or False, self.case01.ANbrBombesVoisins())
			else : 
				self.assertIsInstance(self.case01.ANbrBombesVoisins(),int)
			#print("Valeur bomsVois avant test range "+ str(self.case01.bomsVois))
			self.assertTrue(0 <= self.case01.ANbrBombesVoisins() <= 9)	
		

# Executer le scripte de test non verbeux ; permet l"execution de unittest sans devoir le précisier dans la commande
#if __name__ == '__main__': 
#unittest.main()

#Executer le scripte de test de manière verbeuse
	
suite = unittest.TestLoader().loadTestsFromTestCase(testCase)
unittest.TextTestRunner(verbosity=2).run(suite)
#0 (quiet): you just get the total numbers of tests executed and the global result
#1 (default): you get the same plus a dot for every successful test or a F for every failure
#2 (verbose): you get the help string of every test and the result
