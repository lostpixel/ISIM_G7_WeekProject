"""
-- Fiche de classe et de  fonction --
nom : Fenetre

fonction/utilité attendue : interface graphique : frame, radio, label, combo, bouton 
type valeur en entrée :
liste appel d'autre fonction :
    guide
    jeux
    niveau
    action

"""
from tkinter import *
import time

class Fenetre():

""" fenetre principal"""

    maFenetre=Tk()
    maFenetre.title('Decorona Viseur')
    maFenetre.configure(bg="black")
    maFenetre.resizable(width=false, height=false)

	
	#Centrage fêtre
    screen_x = int(maFenetre.winfo_screenwidth())
    screen_y = int(maFenetre.winfo_screenheight())
    window_x = 800
    window_y = 600
    posX = (screen_x // 2) - (window_x // 2)
    posY = (screen_y // 2) - (window_y // 2)
    geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
    maFenetre.geometry(geo)
    
    
""" frames """    
    
    #Frame pour les niveaux : boutons radios
    frame_niveau=LabelFrame(maFenetre, text="Niveaux", padx=20, pady=20)
    choix=IntVar()
    case1=Radiobutton(frame_niveau)
    case1.configure(text="Débutant", command=init_niveau, variable=choix, value=1)
    case1.pack(anchor=NW, padx=30)
    case2=Radiobutton(frame_niveau)
    case2.configure(text="Moyen", padx=3, command=init_niveau, variable=choix, value=2)
    case2.pack(anchor=NW, padx=30)
    case3=Radiobutton(frame_niveau)
    case3.configure(text="Expert", padx=3, command=init_niveau, variable=choix, value=3)
    case3.pack(anchor=NW, padx=30)
    

    frame_niveau.pack()
    
    #Frame pour les compteurs
    frame_compteur=LabelFrame(maFenetre, text="compteurs", padx=20, pady=20)
        #affichage décompte bombe
    texte_bombe=Label(frame_compteur, text="Bombe restantes :")
    decompte_bombe=Label(frame_compteur, text="100")
    texte_bombe.grid(row=4, column=1, sticky="NW")
    decompte_bombe.grid(row=4, column=2, sticky="NE")
    
        #affichage décompte cases
    texte_cases = Label(frame_compteur, text="Nombre de cases :")
    decompte_cases = Label(frame_compteur, text="10")
    texte_cases.grid(row=5, column=1, sticky="NW")
    decompte_cases.grid(row=5, column=2, sticky="NE")
    
        #affichage timer
"""
    clock=Label(frame_compteur, justify="center")
    clock.pack()
    timer()
       
    def timer():
        t=time.strftime("%I:%M:%S", time.localtime())
        if t!='':
            clock.config(text=t, font="times 25")
        tk.after(100, timer)
              
"""
    #Frame pour les boutons
    frame_bouton=LabelFrame(maFenetre, text="Options", padx=20, pady=20)
    
    btn_jouer=Button(frame_bouton, width=14, text="Nouvelle partie", relief=GROOVE, command=init_jeu)
    btn_jouer.grid(row=0, column=2, padx=50, pady=20)
    
    btn_guide=Button(frame_bouton, width=14, text="Règles de jeux", relief=GROOVE, command=guide)
    btn_guide.grid(row=0, column=3, padx=50, pady=20 )
    
    btn_quitter=Button(frame_bouton, width=14, text="Quitter", relief=GROOVE, command=maFenetre.destroy)
    btn_quitter.grid(row=0, column=4, padx=50, pady=20)
    
    #combox choix des mode
    label_mode=Label(frame_bouton, text="Mode")
    lebel_mode.pack(row,0, column=1, padx=50, pady=20)
    liste_mode=["classique", "", ""]
    liste_combo_mode=Combobox(frame_bouton, values=liste_mode)
    liste_combo_mode.current(0)
    liste_combo_mode.bind("<ComboboxSelected>", action)
    listte_combo_mode.pack(row=1, column=1, padx=20, pady=20)
    
    
    #canvas  A VOIR POUR CHARGER IMAGE VIRUS
    plateu=Canvas(maFenetre)
    plateau=canvas_image(file=)
    plateau.pack(side=RIGHT)
    
""" fonctions """
    def guide():
        fen_guide=tk.Toplevel()
        label_guide=tk.Label(fen_guide, text = "Information général")
        label_guide.pack()
    
    # Choix des niveaux
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
    
    # nouvelle partie : bouton
    def init_jeu():
        global nb_bombes_cachees, nb_cases_vue, on_joue
        on_joue=true
        nb_cases_vue=0
        plateau.delete(ALL)
        nb_bombes_cachees = nb_bombes
        affiche_compteurs()
        
            #tableuax avec chaines vide
        y=0
        while y < nb_lig:
           x=1
           y +=1
           while x <= nb_col:
                tab_m[x,y] =0
                tab_j[x,y] =""
                tableau.create_rectangle((x-1)*dim+gap, (y-1)*dim+gap, x*dim+gap, y*dim+gap, width=0, fill="grey")
                x +=1
        grille(nb_col, nb_lig, dim, gap)
   

    # fonction action : redirection diférent mode
    def action(event):
        select=liste_combo_mode.get()
        
"""
A VOIR POUR CHARGER NOUVELLE GRILLE DE JEUX

def grille(nb_col, nb_lignes, dim, origine):
 x1= origine
 y1= origine
 # Détermine la largeur de la grille
 y2 = y1 + (dim*nb_lignes)
 # Détermine la hauteur de la grille
 x2 = x1 + (dim*nb_col)
 colonne = 0
 while colonne <= nb_col:
 colonne=colonne+1
 # Création de la ligne verticale
 can.create_line(x1,y1,x1,y2,width=2,fill="black")
 # Décalage de la ligne vers la droite
 x1 = x1 + dim
 x1 = origine
 ligne = 0
 while ligne <= nb_lignes:
 ligne=ligne+1
 # Création de la ligne horizontale
 can.create_line(x1,y1,x2,y1,width=2,fill="black")
 # Décalage de la ligne vers le bas
 y1 = y1 + dim


"""   
    maFenetre.mainloop()
    
    
    
    
    
    
    
    
    
    