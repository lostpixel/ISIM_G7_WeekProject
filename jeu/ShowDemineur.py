from Plateau import *

class Jeu():

	def __init__(self):
		self.plateau = PlateauApocalypse(9, 9, 10)
		self.creuse = True
		
	def Run(self):
		prompt = "[c : creuser, d : drapeau, q : quitter]\n{0} > "
		
		while not self.plateau.Perdre():
			self.plateau.AfficherTableau()
			entree = input(prompt.format('Creuser' if self.creuse else 'Drapeau'))
			self.parse_input(entree.strip().lower())
			
		self.plateau.AfficherTableau()
		if self.plateau.Gagner():
			print("Gagné !")
		else:
			print("Perdu !")
	
	def parse_input(self, in_str):
		if in_str == 'q':
			raise SystemExit
		if in_str == 'c':
			self.creuse = True
			return
		if in_str == 'd':
			self.creuse = False
			return
		
		L, C = [int(num) for num in in_str.split()]
		if self.creuse:
			self.plateau.JouerCoup()
			self.plateau.CreuserCase(L-1, C-1)
		else:
			self.plateau.Draper(L-1, C-1)
			
if __name__ == '__main__':
	j = Jeu()
	j.Run()