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
from tkinter import *
from tkinter import ttk
from timeit import default_timer


class fenetre():
    
    """ Déclaration de la fenêtre principal"""
    
    maFenetre=Tk()
    maFenetre.title("DECORONA VISEUR")
    maFenetre.configure(bg="red")
    
    
        #Permet un affichage centré sur l'écran
    screen_x=int(maFenetre.winfo_screenwidth())
    screen_y=int(maFenetre.winfo_screenheight())
    window_x=800
    window_y=600
    posX=(screen_x // 2) - (window_x // 2)
    posY=(screen_y // 2) - (window_y // 2)
    geo="{}x{}+{}+{}".format(window_x, window_y, posX, posY)
    maFenetre.geometry(geo)
    


    """ Frame : compteurs, niveaux, boutons, timer""" 

     
        #Frame pour les compteurs
    frame_compteur=LabelFrame(maFenetre, text="compteurs", padx=20, pady=20)
        #affichage décompte bombe
    texte_bombe=Label(frame_compteur, text="Bombe restantes :")
    decompte_bombe=Label(frame_compteur, text="100")
    texte_bombe.grid(row=4, column=1, sticky="NW")
    decompte_bombe.grid(row=4, column=2, sticky="NE")
    
        #affichage décompte cases
    texte_cases=Label(frame_compteur, text="Nombre de cases :")
    decompte_cases=Label(frame_compteur, text="10")
    texte_cases.grid(row=5, column=1, sticky="NW")
    decompte_cases.grid(row=5, column=2, sticky="NE")
    
    frame_compteur.pack()  
    
    
        #Fonction choix du niveau
    def niveau():
        global nb_col, nb_ligne, nb_bombes
        niveau=choix.get()
        if niveau == 1 :
            nb_col, nb_lig, nb_bombes = 10, 10, 12
        elif niveau == 2 :
            nb_col, nb_lig, nb_bombes = 15, 15, 30
        else :
            nb_col, nb_lig, nb_bombes = 20, 20, 50
            
        plateu.configure(width=(bn_col*dim)+gap, height=(nb_lig*dim)+gap)  #taille plateu par niveau
     

        #Frame radioButton : choix niveau
    frame_niveau=LabelFrame(maFenetre, text="Niveau", padx=20, pady=20)
    
    choix=IntVar()
    case1=Radiobutton(frame_niveau)
    case1.configure(text="Débutant", command=niveau, variable=choix, value=1)
    case1.pack(anchor=NW, padx=30)
    case2=Radiobutton(frame_niveau)
    case2.configure(text="Moyen", command=niveau, variable=choix, value=2)
    case2.pack(anchor=NW, padx=30)   
    case3=Radiobutton(frame_niveau)
    case3.configure(text="Expert", command=niveau, variable=choix, value=3)
    case3.pack(anchor=NW, padx=30)
    
    frame_niveau.pack()
    
        #Frame bouton : nouvelle partie, règles du jeux, quiter
    frame_bouton=LabelFrame(maFenetre, text="Options", padx=20, pady=20)
    
            #bouton nouvelle partie
    btn_jouer=Button(frame_bouton, width=14, text="Nouvellepartie")
    btn_jouer.grid()
    
            #bouton règles du jeux
    btn_guide=Button(frame_bouton, width=14, text="Règles du jeu")
    btn_guide.grid()
    
            #bouton quitter : fermeture (détruire la fenetre)
    btn_quitter=Button(frame_bouton, width=14, text="Quitter", command=maFenetre.destroy)
    btn_quitter.grid()

   
    """Combobox : liste déroulante pour les différent mode de jeux"""

    
        #Fonction pour les combo : A MODIFIER
    def action(event):
        select=liste_combo_mode.get()
    
        #Combobox : liste des mode
    label_mode=Label(frame_bouton, text="Mode")
    label_mode.grid()
    liste_mode=["Classique", "Propagation", "Apocalypse"]
    liste_combo_mode=ttk.Combobox(frame_bouton, value=liste_mode)
    liste_combo_mode.current(0)
    liste_combo_mode.bind("<<ComboboxSelected>>", action)
    liste_combo_mode.grid()
        
    frame_bouton.pack()

        
    """Canvas : image de fond"""

    
    plateau=Canvas(maFenetre)
    plateau.pack()
            
    photo=PhotoImage(file="/Users/Séverine/Desktop/image1.png")   #chargement photo : A MODIFIER
    plateau.create_image(0,0, anchor=NW, image=photo)
    
    """Tmers"""
    """
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
    """    
    maFenetre.mainloop()
 


 