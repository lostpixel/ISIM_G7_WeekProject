"""
================================================CLASS FENETRE  =========================
VERSON 3.6.3

++++++++++++ STRUCURE DU FICHIER ++++++++++++++++++++++++
- IMPORTATION
- DECLARTION VARIABLE (PATH)
- FONCTION niveau
- FONCTION create_plateau ( ClicGauche() + ClicDroit() )
- FONCTION resultat
- FONCTION regle_jeu
- FONCTION inscription

- CLASS appTK
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

b = []
labels = []
#niveau ='global'

# IMPORTATION
import os
from tkinter import *
from tkinter import ttk
from timeit import default_timer
from tkinter import messagebox
from Plateau import *
from user import User

PATH = os.path.dirname(os.path.realpath('__file__'))

# def niveau():
        # global nb_col, nb_ligne, nb_bombes
        # niveau=choix.get()
        # if niveau == 1 :
            # nb_col, nb_lig, nb_bombes = 9, 9, 10
        # elif niveau == 2 :
            # nb_col, nb_lig, nb_bombes = 16, 16, 40
        # else :
            # nb_col, nb_lig, nb_bombes = 30, 30, 99

        # plateu.configure(width=(bn_coldim)+gap, height=(nb_ligdim)+gap)  #taille plateu par niveau

def addUser():
	u = User(textButtonValider.get())
	u.save()

def callNiveau1():
	global niveau
	niveau = int('1')
	print("val = 1")
def callNiveau2():
	global niveau
	niveau = int('2')
	print("val = 2")
def callNiveau3():
	global niveau
	niveau = int('3')
	print("val = 3")

def callMode1():
	global mode
	mode = int('1')
	print("val = 1")
def callMode2():
	global mode
	mode = int('2')
	print("val = 2")
def callMode3():
	global mode
	mode = int('3')
	print("val = 3")

def create_plateau():
	print("niveau = "+"%d" %niveau)
	print("mode = "+"%d" %mode )
	fen=Toplevel()
	#fen.title("Plateau de jeu")
	fen.configure(bg="#f0f0f0")#bg="#151515"
	#fen.resizable(width=False, height=False)

	#Permet un affichage centré sur l'écran
	screen_x=int(fen.winfo_screenwidth())
	screen_y=int(fen.winfo_screenheight())
	window_x=800
	window_y=650
	posX=(screen_x // 2) - (window_x // 2)
	posY=(screen_y // 2) - (window_y // 2)
	geo="{}x{}+{}+{}".format(window_x, window_y, posX, posY)
	fen.geometry(geo)


	btn_fermer=Button(fen, text="Fermer", width=15, relief=GROOVE, bg="#990505", fg="white", cursor="spraycan", command=fen.destroy)
	btn_fermer.pack(side=BOTTOM, padx=10, pady=10)

	drapeau = PhotoImage(file = PATH+r'\gif\docteur.gif')
	virusA = PhotoImage(file = PATH+r'\png\virusA.png')
	# virusB = PhotoImage(file = PATH+r'\img\virusB.png')
	# virusC = PhotoImage(file = PATH+r'\img\virusC.png')
	# virusD = PhotoImage(file = PATH+r'\img\virusD.png')
	lb = Label (fen, image=virusA)
	lb.pack(side=BOTTOM)


	def ClicGauche (ref):
		plateau.CreuserCase(b,ref)
		if plateau.Perdre() :
			#messagebox.showinfo(message="Vous avez perdu")
			print("Perdu !")
		if plateau.Gagner():
			print("Gagné !")

	def ClicDroit (ref):
		plateau.Draper(ref)
		if plateau._cases[ref].EstDrapeau() :
			b[ref].config(image=drapeau)
		else : b[ref].config(image=' ')
		print("Drape !")
	nb_col = 0
	nb_lig = 0
	nb_bombes = 0
	if niveau == 1 :
		nb_col, nb_lig, nb_bombes = 9, 9, 10
	elif niveau == 2 :
		nb_col, nb_lig, nb_bombes = 16, 16, 40
	else :
		nb_col, nb_lig, nb_bombes = 16, 30, 99

	plateau = PlateauNormal(nb_col, nb_lig, nb_bombes) #hauteur  - latrgeur - Nb Mine
	canvasPlateau = Canvas (fen, width=780, height=800, bg="#151515" ) #width=780, height=800
	canvasPlateau.pack(padx=1,pady=1)
	index=0
	labels
	for ligne in range(plateau._hauteur):
		for colonne in range(plateau._largeur):
			contenu = ''
			img = ''
			if plateau._cases[index].EstUneBombe() :
				#contenu = 'M'
				img=virusA
			else : contenu = "%d " % (plateau._cases[index].ANbrBombesVoisins())

			labels.append(Label(canvasPlateau,text=contenu,bd=1,justify=CENTER,relief=SUNKEN,font=("Helvetica", 9),image='',width=1,height=1,padx=9,pady=5))#
			labels[index].grid(column=colonne,row=ligne)

			b.append(Button(canvasPlateau,text="",image="",padx=8,pady=1))
			b[index].grid(column=colonne,row=ligne)

			b[index].bind("<Button-1>",lambda ligne,ref=index: ClicGauche(ref))
			b[index].bind("<Button-3>",lambda ligne,ref=index: ClicDroit(ref))
			b[index].config(relief=RAISED)
			index+=1
	index=0
	for ligne in range(plateau._hauteur):
		for colonne in range(plateau._largeur):
			if plateau._cases[index].EstUneBombe():
				labels[index].config(image=virusA ,relief=GROOVE,bd=1,width=25,height=25)#
			index+=1

def resultat():
	fen=Toplevel()
	fen.title("Sore")
	fen.configure(bg="#151515")
	fen.resizable(width=False, height=False)

	#Permet un affichage centré sur l'écran
	screen_x=int(fen.winfo_screenwidth())
	screen_y=int(fen.winfo_screenheight())
	window_x=500
	window_y=400
	posX=(screen_x // 2) - (window_x // 2)
	posY=(screen_y // 2) - (window_y // 2)
	geo="{}x{}+{}+{}".format(window_x, window_y, posX, posY)
	fen.geometry(geo)

	btn_fermer=Button(fen, text="Fermer", width=15, relief=GROOVE, bg="#990505", fg="white", cursor="spraycan", command=fen.destroy)
	btn_fermer.pack(side=BOTTOM, padx=10, pady=10)


def regle_jeu():
	fene=Toplevel()
	fene.title("Règle du Decorona viseur")
	fene.configure(bg="#151515")
	fene.resizable(width=False, height=False)

	#Permet un affichage centré sur l'écran
	screen_x=int(fene.winfo_screenwidth())
	screen_y=int(fene.winfo_screenheight())
	window_x=500
	window_y=400
	posX=(screen_x // 2) - (window_x // 2)
	posY=(screen_y // 2) - (window_y // 2)
	geo="{}x{}+{}+{}".format(window_x, window_y, posX, posY)
	fene.geometry(geo)

	btn_fermer=Button(fene, text="Fermer", width=15, relief=GROOVE, bg="#990505", fg="white", cursor="spraycan", command=fene.destroy)
	btn_fermer.pack(side=BOTTOM, padx=10, pady=10)

	#fonction pour ouverture de la fenêtre inscription, qui contient la possibilité d'entré ce nom
	#ainsi que un bouton pour valider.


def inscription():
	fenetre=Toplevel()
	fenetre.title("CORONA VISEUR : Inscription")
	fenetre.configure(bg="#151515")
	fenetre.resizable(width=False, height=False)

    #Permet un affichage centré sur l'écran
	screen_x=int(fenetre.winfo_screenwidth())
	screen_y=int(fenetre.winfo_screenheight())
	window_x=500
	window_y=400
	posX=(screen_x // 2) - (window_x // 2)
	posY=(screen_y // 2) - (window_y // 2)
	geo="{}x{}+{}+{}".format(window_x, window_y, posX, posY)
	fenetre.geometry(geo)

            #zone de saisie
	frame_entree=Frame(fenetre)
	frame_entree.configure(bg="#151515")

	label_joueur1=Label(frame_entree, text="Joueur un", bg="#151515", fg="white", padx=20, pady=20)
	label_joueur1.pack()

	global textButtonValider
	textButtonValider = StringVar(frame_entree)
	entree=Entry(frame_entree, width=30,textvariable=textButtonValider)
	entree.pack()

	frame_entree.pack(side=TOP, padx=20, pady=20)

	frame_btn_utilisateur=Frame(fenetre)
	frame_btn_utilisateur.configure(bg="#151515")

	#label texte d'avertissement
	label_text=Label(fenetre, text="Tu dois t'inscrire si tu veux pouvoir jouer !!", bg="#151515", fg="green")
	label_text.pack(padx=40, pady=40)

	#var = text.get()
	#bouton de validation
	btn_valider=Button(frame_btn_utilisateur, text="Valider", width=15, relief=GROOVE, bg="#990505", fg="white", cursor="spraycan", command = addUser)
	btn_valider.pack(side=LEFT, padx=10, pady=10)

	#bouton annuler
	btn_annuler=Button(frame_btn_utilisateur, text="Annuler", width=15, relief=GROOVE, bg="#990505", fg="white", cursor="spraycan", command=fenetre.destroy)
	btn_annuler.pack(side=RIGHT, padx=10, pady=10)

	frame_btn_utilisateur.pack(side=BOTTOM, padx=20, pady=20)




    #initialisation de la fenêtre principale du jeu :


 #avec toutes les options de jeux.
class appTK:
	def __init__(self, master):
				#configuration de la fenêtre
		maFenetre.title("DECORONA VISEUR")
		maFenetre.configure(bg="#151515")
		maFenetre.resizable(width=False, height=False)

				#Permet un affichage centré sur l'écran
		screen_x=int(maFenetre.winfo_screenwidth())
		screen_y=int(maFenetre.winfo_screenheight())
		window_x=900
		window_y=750
		posX=(screen_x // 2) - (window_x // 2)
		posY=(screen_y // 2) - (window_y // 2)
		geo="{}x{}+{}+{}".format(window_x, window_y, posX, posY)
		maFenetre.geometry(geo)

				#fonction pour quitter le jeux
		def quitter():
			val =messagebox.askokcancel("Quitter", "Voulez-vous vraiment partir ?", icon="error", default="ok")
			if val==True:
				maFenetre.quit()
			else: pass


				#Frame : compteurs, niveaux, boutons, timer, joueur

		frame_general=Frame(maFenetre, padx=5, pady=5)    #ouverture du frame gauche principale
		frame_general.configure(bg="#151515")   #configuration

				#frame jouer: permet d'introduire info joueur :: A prévoir classe récupération dans un fichier texte les nom et les score


		frame_joueur=LabelFrame(frame_general, text="Player", padx=5, pady=5)
		frame_joueur.configure(bg="#151515", fg="green")

		label_nom=Label(frame_joueur, width=20, bg="#151515", fg="white")
		label_nom.pack()

				#bouton pour introduire et enregistrer les données son nom
		btn_inscription=Button(frame_joueur, text="Inscription", width=20, relief=GROOVE, bg="#990505", fg="white", cursor="spraycan", command=inscription)
		btn_inscription.pack(padx=5, pady=5)
		frame_joueur.grid(row=0, column=0, padx=5, pady=5)

				#Frame pour les compteurs : voir pour l'affichage (fonction)
		frame_compteur=LabelFrame(frame_general, text="Compteurs", padx=5, pady=5)
		frame_compteur.configure(bg="#151515", fg="green")

				#affichage décompte bombe
		texte_bombe=Label(frame_compteur, text="Bombe restantes :", bg="#151515", fg="white")
		decompte_bombe=Label(frame_compteur, text="100", bg="#151515", fg="white")
		texte_bombe.grid(row=4, column=0, sticky="NW")
		decompte_bombe.grid(row=4, column=0, sticky="NE")

				#affichage décompte coups
		texte_cases=Label(frame_compteur, text="Nombre de coup :", bg="#151515", fg="white")
		decompte_cases=Label(frame_compteur, text="100", bg="#151515", fg="white")
		texte_cases.grid(row=5, column=0, sticky="NW")
		decompte_cases.grid(row=5, column=0, sticky="NE")

		def updateTime():   #fonction pour le timer

			now = default_timer() - start
			minutes, secondes = divmod(now, 60)
			str_time="%02d:%02d" % (minutes, secondes)
			canvas_times.itemconfigure(text_clock, text=str_time)
			maFenetre.after(100, updateTime)

				#frame minuteur
		frame_timer=Frame(frame_compteur)
		frame_timer.configure(bg="#151515",)
		start=default_timer()
		canvas_times=Canvas(frame_timer, width=120, height=40, bg="#990505")
		canvas_times.pack()
		text_clock=canvas_times.create_text(60, 20)
		frame_timer.grid(row=2, column=0, padx=10, pady=10)
		frame_compteur.grid(row=1, column=0, padx=5, pady=5)

				#frame général bouton d'option jeux
		frame_option=LabelFrame(frame_general, text="Options", padx=5, pady=5)
		frame_option.configure(bg="#151515", fg="green")
				#frame bouton
		frame_niveau=LabelFrame(frame_option, text="Niveau", bg="#151515", fg="#FC8C00")
		frame_niveau.configure(bg="#151515")




				#bouton niveau débutant
		btn_debutant=Button(frame_niveau, width=20, text="Débutant", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan", command=callNiveau1)
		btn_debutant.pack(padx=5, pady=5)
				#bouton niveau moyen
		btn_moyen=Button(frame_niveau, width=20, text="Moyen", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan",command=callNiveau2)
		btn_moyen.pack(padx=5, pady=5)
				#bouton niveau expert
		btn_expert=Button(frame_niveau, width=20, text="Expert", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan",command=callNiveau3)
		btn_expert.pack(padx=5, pady=5)
		frame_niveau.pack(side=TOP, padx=5, pady=5)

				# frame bouton mode
		frame_mode=LabelFrame(frame_option, text="Mode", bg="#151515", fg="#FC8C00")
		frame_mode.configure(bg="#151515")
				#bouton mode classique
		btn_classique=Button(frame_mode, width=20, text="Classique", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan",command = callMode1)
		btn_classique.pack(padx=5, pady=5)
				#bouton mode propagation
		btn_propagation=Button(frame_mode, width=20, text="Propagation", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan",command = callMode2)
		btn_propagation.pack(padx=5, pady=5)
				#bouton mmode apocalypse
		btn_apocalypse=Button(frame_mode, width=20, text="Apocalypse", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan",command = callMode3)
		btn_apocalypse.pack(padx=5, pady=5)

		frame_mode.pack(side=BOTTOM, padx=2, pady=2)
		frame_option.grid(row=3, column=0, padx=5, pady=5)

				#Frame bouton : nouvelle partie, règles du jeux, quitter, score
		frame_bouton=LabelFrame(frame_general, text="Action", padx=10, pady=5)
		frame_bouton.configure(bg="#151515", fg="green")

				#bouton nouvelle partie
		btn_jouer=Button(frame_bouton, width=20, text="Nouvelle partie", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan", command=create_plateau)
		btn_jouer.pack(padx=5, pady=5)

				#bouton score
		btn_score=Button(frame_bouton, width=20, text="Résultat", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan", command=resultat)
		btn_score.pack(padx=5, pady=5)

				#bouton règles du jeux
		btn_guide=Button(frame_bouton, width=20, text="Règles du jeu", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan", command=regle_jeu)
		btn_guide.pack(padx=5, pady=5)

				#bouton quitter : fermeture
		btn_quitter=Button(frame_bouton, width=20, text="Quitter", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan",command=quitter)
		btn_quitter.pack(padx=5, pady=5)

		frame_bouton.grid(row=4, column=0, padx=5, pady=5)
		frame_general.pack(side=LEFT, padx=20, pady=10)           #fermeture du frame général

				# canvas : affiche l'image d'ouverture du jeu
		BG = PhotoImage(file= PATH+r'\bg.png')
		maFenetre.BG = BG
		canvasBG = Canvas(maFenetre, width=780, height=800 ) # , bg="#151515"
		canvasBG.create_image(0, 0, anchor=NW, image=BG)
		canvasBG.pack(side=RIGHT,padx=50,pady=50)

		#appel de fonction : associé au timer
		default_timer()
		updateTime()


#Déclaration de la fenêtre principal
maFenetre=Tk()								#start loop
app = appTK(maFenetre)
maFenetre.mainloop()						# re loop
