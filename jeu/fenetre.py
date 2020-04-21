"""
-- Fiche de classe et de  fonction --
nom Zerque Séverine

fonction/utilité attendue : classe fenêtre (bouton)
type valeur en entrée :
type valeur en sortie : 
liste appel d'autre fonction :


"""

import tkinter as tk

class Fenetre():

	#fenetre acceuil du démineur
	maFenetre = tk.Tk()
	maFenetre.title('Decorona Viseur')
	maFenetre.minsize(640, 480)
	
	#Centrage fêtre
	screen_x = int(maFenetre.winfo_screenwidth())
	screen_y = int(maFenetre.winfo_screenheight())
	window_x = 800
	window_y = 600
	posX = (screen_x // 2) - (window_x // 2)
	posY = (screen_y // 2) - (window_y // 2)
	geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
	maFenetre.geometry(geo)
	
	#texte d'intro
	label_intro = tk.Label(maFenetre, text = "DECORONA VISEUR ", fg = "green")
	label_intro.pack()
	
	#Fonction jouer
	def jouer():
		new_fenetre = tk.Toplevel()
		label_niveau = tk.Label(new_fenetre, text = "Niveau", fg= "green")
		
		btn_debutant = tk.Button(new_fenetre, text = "Débutant")
		btn_debutant.pack()
		
		btn_medium = tk.Button(new_fenetre, text= "medium")
		btn_medium.pack()
		
		btn_master = tk.Button(new_fenetre, text = "Master")
		btn_master.pack()
		
	#Fonction information
	def information():
		fen_info = tk.Toplevel()
		label_info = tk.Label(fen_info, text = "Information général", fg= "green")
		label_info.pack()

	#Bouton quiter le jeux (détruit la fenêtre)
	btn_quitter = tk.Button(maFenetre, text= "Quitter", width = 20, command = maFenetre.destroy)
	btn_quitter.pack()
	
	#Bouton lancement partie (avec menu de difficulté) redirige avec la fonction
	btn_jouer = tk.Button(maFenetre, text = "Jouer", width = 20, command = jouer)
	btn_jouer.pack()
	
	#Bouton information
	btn_info = tk.Button(maFenetre, text= "Information", width=20, command=information)
	btn_info.pack()
	
	# affiche les core
	
	#compteur de bombe
	
	#Garde la fenêtre ouverte
	maFenetre.mainloop()
    
    
    
    
    
    
    
    
    
    
