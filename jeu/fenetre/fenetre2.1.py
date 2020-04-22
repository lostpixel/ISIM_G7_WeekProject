"""
-- Fiche de classe et de  fonction --
nom : Fenetre

fonction/utilité attendue : interface graphique : frame, radio, label, combo, bouton 
type valeur en entrée :
type valeur en sortie : 
liste appel d'autre fonction :
    guide
    jeux
    niveau
    action

"""
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *
import time

class Fenetre():
    """ 
    -- fenetre principal 
    """

    maFenetre=tk.Tk()
    maFenetre.title('Decorona Viseur')
    maFenetre.configure(bg="black")
   # maFenetre.resizable(width=false, height=false)   ????

    
	#Centrage fêtre
    screen_x = int(maFenetre.winfo_screenwidth())
    screen_y = int(maFenetre.winfo_screenheight())
    window_x = 800
    window_y = 600
    posX = (screen_x // 2) - (window_x // 2)
    posY = (screen_y // 2) - (window_y // 2)
    geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
    maFenetre.geometry(geo)
    
    
    """ 
    -- frames 
    """    

    #Frame pour les compteurs
    frame_compteur=tk.LabelFrame(maFenetre, text="compteurs", padx=20, pady=20)
        #affichage décompte bombe
    texte_bombe=tk.Label(frame_compteur, text="Bombe restantes :")
    decompte_bombe=tk.Label(frame_compteur, text="100")
    texte_bombe.grid(row=4, column=1, sticky="NW")
    decompte_bombe.grid(row=4, column=2, sticky="NE")
    
        #affichage décompte cases
    texte_cases=tk.Label(frame_compteur, text="Nombre de cases :")
    decompte_cases=tk.Label(frame_compteur, text="10")
    texte_cases.grid(row=5, column=1, sticky="NW")
    decompte_cases.grid(row=5, column=2, sticky="NE")
    
        #affichage timer
    """
    clock=Label(frame_compteur, justify="center")
    clock.pack()
    timer()
       
    def timer():
        t=time.strftime("%I:%S", time.localtime())
        if t!='':
            clock.config(text=t, font="times 25")
        after(100, timer)
              
    """
    # fonction: Choix des niveaux
    def init_niveau():
        global nb_col, nb_ligne, nb_bombes
        niveau=choix.get()
        if niveau == 1 :
            nb_col, nb_lig, nb_bombes = 10, 10, 12
        elif niveau == 2 :
            nb_col, nb_lig, nb_bombes = 15, 15, 30
        else :
            nb_col, nb_lig, nb_bombes = 20, 20, 50
            #taille plateu par niveau
        plateu.configure(width=(bn_col*dim)+gap, height=(nb_lig*dim)+gap)
        
    #Frame pour les niveaux : boutons radios
    frame_niveau=tk.LabelFrame(maFenetre, text="Niveaux", padx=20, pady=20)
    choix=tk.IntVar()
    case1=tk.Radiobutton(frame_niveau)
    case1.configure(text="Débutant", command=init_niveau, variable=choix, value=1)
    case1.pack()
    case2=tk.Radiobutton(frame_niveau)
    case2.configure(text="Moyen", padx=3, command=init_niveau, variable=choix, value=2)
    case2.pack()
    case3=tk.Radiobutton(frame_niveau)
    case3.configure(text="Expert", padx=3, command=init_niveau, variable=choix, value=3)
    case3.pack()
    
    frame_niveau.pack()
    
    #fonction : affiche une nouvelle fenêtre avec les règles du jeu /! VOIR COMMENT CHARGER FICHER.DOC OU AUTRE
    def guide():
        fen_guide=tk.Toplevel()
        label_guide=tk.Label(fen_guide, text = "Règles du jeux")
        label_guide.pack()
    


    #Frame pour les boutons
    frame_bouton=tk.LabelFrame(maFenetre, text="Options", padx=20, pady=20)
    
    btn_jouer=tk.Button(frame_bouton, width=14, text="Nouvelle partie")
    btn_jouer.grid()
    
    btn_guide=tk.Button(frame_bouton, width=14, text="Règles de jeux", command=guide)
    btn_guide.grid()
    
    btn_quitter=tk.Button(frame_bouton, width=14, text="Quitter", command=maFenetre.destroy)
    btn_quitter.grid()
    
        
        #combox choix des mode
    def action(event):
        select=liste_combo_mode.get()
             
        
        
    label_mode=tk.Label(frame_bouton, text="Mode")
    label_mode.grid()
    liste_mode=["classique", "Propagation", "Apocalypse"]
    liste_combo_mode=ttk.Combobox(frame_bouton, value=liste_mode)
    liste_combo_mode.current(0)
    liste_combo_mode.bind("<<ComboboxSelected>>", action)
    liste_combo_mode.grid()
    

    #canvas  A VOIR POUR CHARGER IMAGE VIRUS
    plateau=Canvas(maFenetre, width=400, height=250)
    plateau.pack()
    photo=PhotoImage(file="/Users/Séverine/Desktop/image1.png")
    plateau.create_image(0,0, anchor=NW, image=photo)
    
    




    maFenetre.mainloop()
    
    
    
    
    
    
    
    
    
    