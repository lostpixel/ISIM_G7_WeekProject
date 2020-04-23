"""
-- Fiche de classe et de  fonction --
nom : Fenetre

fonction/utilité attendue : interface graphique : frame, radio, label, combo, bouton 
type valeur en entrée :
type valeur en sortie : 
liste appel d'autre fonction :
    fonction quitter
    fonction niveau
    fonction timer

"""

"""
================================================CLASS FENETRE : TENTATIVE TOUT PACK() =========================
++++++++++++ STRUCURE DU FICHIER ++++++++++++++++++++++++
- IMPORTATION
- DECLARTION VARIABLE (PATH)
- CLASS application
- DECLARATION de la loop()
+++++++++++++ STRUCURE DE LA CLASS application ++++++++++++++++++++++++++
class application 
|--->def __init__
		|---> configuration de la fenetre (titre,bg,taille,centré)
		|---> Barre de menu (var = bar_menu,creation,déclarations)
		|---> Frame 
		|--->
		|--->
		|--->

	- fonction
+++++++++++++++ STRUCTURE TKinter ++++++++++++++++++++++++++++++++
pack LEFT - pack RIGHT
grid in pack LEFT
canvas in pack RIGHT
"""

# IMPORTATION
import os 							# utilisé pour définir PATH
from tkinter import *
from tkinter import ttk 			# utilisé pour le combobox
from timeit import default_timer
from tkinter import messagebox

PATH = os.path.dirname(os.path.realpath('__file__')) # déclaration de PATH pour chemin relatif

class appTK:
	def __init__(self, master):
		# configuration de la fenetre
		maFenetre.title("DECORONA VISEUR")
		maFenetre.configure(bg="#151515")
		maFenetre.resizable(width=False, height=False)

		screen_x=int(maFenetre.winfo_screenwidth()) #Permet un affichage centré sur l'écran
		screen_y=int(maFenetre.winfo_screenheight())
		window_x=850
		window_y=650
		posX=(screen_x // 2) - (window_x // 2)
		posY=(screen_y // 2) - (window_y // 2)
		geo="{}x{}+{}+{}".format(window_x, window_y, posX, posY)
		maFenetre.geometry(geo)

		#Barre de menu   (rajouter commande)
		bar_menu=Menu(maFenetre) 

		premier_menu=Menu(bar_menu) 
		premier_menu.add_command(label="Nouvelle partie")
		premier_menu.add_command(label="Afficher score")
		premier_menu.add_command(label="Statistique")
		premier_menu.add_separator()
		premier_menu.add_command(label="Quitter", command=maFenetre.destroy)

		second_menu=Menu(bar_menu) 
		second_menu.add_command(label="Aide")
		second_menu.add_command(label="Règle du jeu")

		bar_menu.add_cascade(label="Options", menu=premier_menu) # déclaration du premier menu
		bar_menu.add_cascade(label="Aide", menu=second_menu)    # déclaration du second menu

		maFenetre.config(menu=bar_menu) 

		#Frame : compteurs, niveaux, boutons, timer, joueur""" 
		frame_general=Frame(maFenetre)  
		frame_general.configure(bg="#151515")

		#frame jouer: permet d'introduire info joueur :: A prévoir classe récupération dans un fichier texte les nom et les score
		frame_joueur=LabelFrame(frame_general, text="Player", padx=10, pady=10)
		frame_joueur.configure(bg="#151515", fg="green")
		
		#bouton pour valider et enregistrer les données récoltées
		btn_valider=Button(frame_joueur, text="Inscription", width=20, relief=GROOVE, bg="#990505", fg="white", cursor="spraycan")
		#btn_valider.pack(padx=5, pady=5)
		btn_valider.grid()
		#frame_joueur.grid(row=0, column=0, padx=10, pady=10)
		frame_joueur.grid()
		
		#frame minuteur   (voir fonction timer)
		frame_timer=LabelFrame(frame_general, text="Timer", padx=10, pady=5)
		frame_timer.configure(bg="#151515",fg="green")
		frame_timer.grid(row=1, column=0, padx=20, pady=20)

		# entree=Entry(frame_timer, width=30)
		# entree.pack()    
		label = Label(frame_timer,width=30 )
		label.pack()


		#Frame pour les compteurs : voir pour l'affichage (fonction)
		frame_compteur=LabelFrame(frame_general, text="Compteurs", padx=10, pady=5)
		frame_compteur.configure(bg="#151515", fg="green")

		#affichage décompte bombe
		texte_bombe=Label(frame_compteur, text="Bombe restantes :", bg="#151515", fg="white")
		decompte_bombe=Label(frame_compteur, text="100", bg="#151515", fg="white")
		texte_bombe.grid(row=4, column=1, sticky="NW")
		decompte_bombe.grid(row=4, column=2, sticky="NE")

		#affichage décompte coups
		texte_cases=Label(frame_compteur, text="Nombre de coup :", bg="#151515", fg="white")
		decompte_cases=Label(frame_compteur, text="100", bg="#151515", fg="white")
		texte_cases.grid(row=5, column=1, sticky="NW")
		decompte_cases.grid(row=5, column=2, sticky="NE")

		frame_compteur.grid(row=2, column=0, padx=10, pady=10)  
			
			#Fonction choix du niveau
		def niveau():
			global nb_col, nb_ligne, nb_bombes
			niveau=choix.get()
			if niveau == 1 :
				nb_col, nb_lig, nb_bombes = 9, 9, 10
			elif niveau == 2 :
				nb_col, nb_lig, nb_bombes = 16, 16, 40
			else :
				nb_col, nb_lig, nb_bombes = 30, 30, 99
				
			plateau.configure(width=(bn_col*dim)+gap, height=(nb_lig*dim)+gap)  #taille plateau par niveau
		 
			#Frame radioButton : choix niveau
		frame_niveau=LabelFrame(frame_general, text="Niveau", padx=10, pady=5)
		frame_niveau.configure(bg="#151515", fg="green")
		
		choix=IntVar()
		case1=Radiobutton(frame_niveau)
		case1.configure(text="Débutant", command=niveau, variable=choix, value=1, bg="#151515", fg="white")
		case1.pack(anchor=NW, padx=30)
		case2=Radiobutton(frame_niveau)
		case2.configure(text="Moyen", command=niveau, variable=choix, value=2, bg="#151515", fg="white")
		case2.pack(anchor=NW, padx=30)   
		case3=Radiobutton(frame_niveau)
		case3.configure(text="Expert", command=niveau, variable=choix, value=3, bg="#151515", fg="white")
		case3.pack(anchor=NW, padx=30)

		frame_niveau.grid(row=3, column=0, padx=10, pady=10)

			#Frame bouton : nouvelle partie, règles du jeux, quitter, mode de jeux
		frame_bouton=LabelFrame(frame_general, text="Options", padx=10, pady=5)
		frame_bouton.configure(bg="#151515", fg="green")

				#bouton nouvelle partie
		btn_jouer=Button(frame_bouton, width=20, text="Nouvelle partie", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan")
		btn_jouer.pack(padx=5, pady=5)

				#bouton règles du jeux
		btn_guide=Button(frame_bouton, width=20, text="Règles du jeu", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan")
		btn_guide.pack(padx=5, pady=5)
		   
		#Combobox : liste déroulante pour les différent mode de jeux

		#Combobox : liste des mode
		liste_mode=["Classique", "Propagation", "Apocalypse"]
		liste_combo_mode=ttk.Combobox(frame_bouton, value=liste_mode, state="readonly", justify="center")

		liste_combo_mode.current(0)
		liste_combo_mode.bind("<<ComboboxSelected>>")
		liste_combo_mode.pack(padx=5, pady=5)

		#fonction pour quitter le jeux 
		def quitter():
			val = messagebox.askokcancel("QUITTER", "Voullez vous vraiment partir ?", icon="error",default="ok")
			if val == True :
				maFenetre.quit()
			else : pass
			
		#bouton quitter : fermeture (détruire la fenetre)
		btn_quitter=Button(frame_bouton, width=20, text="Quitter", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan",command=quitter)
		btn_quitter.pack(padx=5, pady=5)

		frame_bouton.grid(row=4, column=0, padx=10, pady=10)    
		frame_general.pack(side=LEFT, padx=5, pady=5)   #fermeture du frame général

		# canvas TKinter
		BG = PhotoImage(file=PATH+"\\bg.png")
		canvasBG = Canvas(maFenetre)
		canvasBG.create_image(0, 0, anchor=NW, image=BG)
		canvasBG.pack(side=RIGHT,padx=10,pady=10)


		#Timers
		def updateTime():
			
			now = default_timer() - start
			minutes, secondes = divmod(now, 60)
			str_time="%02d:%02d" % (minutes, secondes)
			canvas_times.itemconfigure(text_clock, text=str_time)
			maFenetre.after(100, updateTime)          

			
		frame_timers=Frame(maFenetre, padx=20, pady=20)
		start=default_timer()
		canvas_times=Canvas(maFenetre, width=800, height=800, bg="white")
		canvas_times.pack()   
		text_clock=canvas_times.create_text(40, 20)

		frame_timers.pack()
		default_timer()
		updateTime()   
		

		"++++ FIN DE LA CLASSE ++++"

""" Déclaration de la fenêtre principal"""
maFenetre=Tk()								#start loop
app = appTK(maFenetre)
maFenetre.mainloop()						# re loop
 