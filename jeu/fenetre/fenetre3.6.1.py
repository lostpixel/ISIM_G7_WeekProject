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
import os
from tkinter import *
from tkinter import ttk
from timeit import default_timer
from tkinter import messagebox
PATH = os.path.dirname(os.path.realpath('__file__'))

def regle_jeu():      
    fene=Toplevel()
    fene.title("Comment jouer au DECORONA VISEUR")
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
    
    btn_fermer=Button(fene, text="Fermer", width=15, relief=GROOVE, bg="#990505", fg="white", cursor="spraycan", command=quitter)
    btn_fermer.pack(side=BOTTOM, padx=10, pady=10)


def quitterFene():
	val =messagebox.askokcancel("Quitter", "Voulez-vous vraiment partir ?", icon="error", default="ok")
	if val==True:
		, command=fenetre.quit()
	else: pass
     
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
    entree=Entry(frame_entree, width=30)
    entree.pack()  

    frame_entree.pack(side=TOP, padx=20, pady=20)
    
    frame_btn_utilisateur=Frame(fenetre)
    frame_btn_utilisateur.configure(bg="#151515")
    
            #label texte d'avertissement    
    label_text=Label(fenetre, text="Tu dois t'inscrire si tu veux pouvoir jouer !!", bg="#151515", fg="green")
    label_text.pack(padx=40, pady=40)
     
            #bouton de validation
    btn_valider=Button(frame_btn_utilisateur, text="Valider", width=15, relief=GROOVE, bg="#990505", fg="white", cursor="spraycan")
    btn_valider.pack(side=LEFT, padx=10, pady=10)
    
            #bouton annuler
    btn_annuler=Button(frame_btn_utilisateur, text="Annuler", width=15, relief=GROOVE, bg="#990505", fg="white", cursor="spraycan", command=quitterFene )
    btn_annuler.pack(side=RIGHT, padx=10, pady=10)
    
    frame_btn_utilisateur.pack(side=BOTTOM, padx=20, pady=20)


    #initialisation de la fenêtre principale du jeu :
    #avec toutes les options de jeux.

maFenetre=Tk()
maFenetre.title("DECORONA VISEUR")
maFenetre.configure(bg="#151515")
maFenetre.resizable(width=False, height=False)

        #Permet un affichage centré sur l'écran
screen_x=int(maFenetre.winfo_screenwidth())
screen_y=int(maFenetre.winfo_screenheight())
window_x=850
window_y=650
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

frame_general=Frame(maFenetre)    #ouverture du frame gauche principale
frame_general.configure(bg="#151515")   #configuration 

        #frame jouer: permet d'introduire info joueur :: A prévoir classe récupération dans un fichier texte les nom et les score
frame_joueur=LabelFrame(frame_general, text="Player", padx=10, pady=10)
frame_joueur.configure(bg="#151515", fg="green")

        #bouton pour introduire et enregistrer les données son nom
btn_inscription=Button(frame_joueur, text="Inscription", width=20, relief=GROOVE, bg="#990505", fg="white", cursor="spraycan", command=inscription)
btn_inscription.pack(padx=5, pady=5)
frame_joueur.grid(row=0, column=0, padx=10, pady=10)

        #Frame pour les compteurs : voir pour l'affichage (fonction)
frame_compteur=LabelFrame(frame_general, text="Compteurs", padx=10, pady=5)
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
frame_timer=Frame(frame_compteur, padx=10, pady=5)
frame_timer.configure(bg="#151515",)
start=default_timer()
canvas_times=Canvas(frame_timer, width=150, height=40, bg="#990505")
canvas_times.pack()   
text_clock=canvas_times.create_text(75, 20)  
frame_timer.grid(row=2, column=0, padx=10, pady=10) 
frame_compteur.grid(row=1, column=0, padx=10, pady=10)  


        #Frame radioButton : choix niveau
frame_option=LabelFrame(frame_general, text="Options", padx=10, pady=5)
frame_option.configure(bg="#151515", fg="green")
frame_niveau=Frame(frame_option)
frame_niveau.configure(bg="#151515")
btn_debutant=Button(frame_niveau, width=20, text="Débutant", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan")
btn_debutant.pack()
btn_moyen=Button(frame_niveau, width=20, text="Moyen", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan")
btn_moyen.pack()
btn_expert=Button(frame_niveau, width=20, text="Expert", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan")
btn_expert.pack()
frame_niveau.grid(row=0, column=0, padx=5, pady=5)


frame_mode=Frame(frame_option)
frame_mode.configure(bg="#151515")
btn_classique=Button(frame_niveau, width=20, text="Classique", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan")
btn_classique.pack()
btn_propagation=Button(frame_niveau, width=20, text="Propagation", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan")
btn_propagation.pack()
btn_apocalypse=Button(frame_niveau, width=20, text="Apocalypse", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan")
btn_apocalypse.pack()
frame_niveau.grid(row=0, column=0, padx=5, pady=5)
frame_option.grid(row=3, column=0, padx=10, pady=10)

        #Frame bouton : nouvelle partie, règles du jeux, quitter, mode de jeux
frame_bouton=LabelFrame(frame_general, text="Options", padx=10, pady=5)
frame_bouton.configure(bg="#151515", fg="green")
#Combobox : liste déroulante pour les différent mode de jeux

        #Combobox : liste des modes
liste_mode=["Classique", "Propagation", "Apocalypse"]
liste_combo_mode=ttk.Combobox(frame_bouton, value=liste_mode, state="readonly", justify="center")

liste_combo_mode.current(0)
liste_combo_mode.bind("<<ComboboxSelected>>")
liste_combo_mode.pack(padx=5, pady=5)
        #bouton nouvelle partie
btn_jouer=Button(frame_bouton, width=20, text="Nouvelle partie", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan")
btn_jouer.pack(padx=5, pady=5)

        #bouton règles du jeux
btn_guide=Button(frame_bouton, width=20, text="Règles du jeu", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan", command=regle_jeu)
btn_guide.pack(padx=5, pady=5)
   		
        #bouton quitter : fermeture 
btn_quitter=Button(frame_bouton, width=20, text="Quitter", relief=GROOVE, bg="#990505", fg="white", cursor="spraycan",command=quitter)
btn_quitter.pack(padx=5, pady=5)

frame_bouton.grid(row=4, column=0, padx=10, pady=10)    
frame_general.pack(side=LEFT, padx=5, pady=5)           #fermeture du frame général

        # canvas : affiche l'image d'ouverture du jeu
BG = PhotoImage(file=PATH+"\\bg.png")
canvasBG = Canvas(maFenetre, width=680, height=720)
canvasBG.create_image(0, 0, anchor=NW, image=BG)
canvasBG.pack(side=RIGHT,padx=10,pady=10)

#appel de fonction : associé au timer
default_timer()
updateTime()    

maFenetre.mainloop()        #maintien la fenetre jusqu'à la fermeture