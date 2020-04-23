"""
Barre de menu du code du démineur. 
    Tous droits réservés Demisn © 2016

Démineur.py, ainsi que score.py sont essentiels au bon fonctionnement du programme général.
Cependant il est possible de tester juste la barre de menu grâce à la  classe App()
"""
try:
    # Python2
    #!/usr/bin/python2.7
    # -*-coding:Latin-1 -*
    from Tkinter import *
    from tkMessageBox import *
except ImportError:
    # Python3
    #!/usr/bin/python3.5
    # -*-coding:Latin-1 -*
    from tkinter import *
    from tkinter.messagebox import *

from score import classer,connecter
from os import path
import string


class MenuBar(Menu):
    """Classe principale définissant le menu"""

    
    def __init__(self, parent,nouveau,recup_info,option,timer,partie,pseudo_partie):
        
        """
        Initialisation qui nécéssite les informations 'parent,nouveau,recup_info,option,timer,partie' provenants de Démineur.py
        Définition des fonctions des boutons de la barre de menu, ensuite création de la barre de menu avec attribution de chaque fonctions
        """

        Menu.__init__(self, parent)

        
        def lire_pseudo():
            """Permet de lire les pseudos sauvegarder et retourner à la fois une liste contenant les pseudos ainsi qu'un dictionnaire contenant la sauvegarde correspondante"""
            pseudo =[]
            content={}
            if path.isfile("sauvegarde"):
                with open('sauvegarde', 'r') as save:
                    if path.getsize("sauvegarde") != 0:
                        contenu=save.read()
                        contenu=contenu.split()
                        
                        for value in contenu:
                            j=0
                            
                            p=""
                            while j<len(value) and value[j] not in string.printable[10:94]:
                                j+=1
                            if j<len(value):
                                pseudo.append(str(value))
                        for i in pseudo:
                            for value in range(len(contenu)):
                                bool=False
                                if bool:break
                                if str(contenu[value])==str(i):
                                    bool=True
                                if bool:
                                    valeur=[]
                                    d=value+1
                                    while d<len(contenu) and contenu[d] not in pseudo:
                                        valeur.append(str(contenu[d]))
                                        d+=1
                                        
                                        
                                    content[str(contenu[value])]=valeur
                                    
                                
                            
                
            return pseudo,content
            
        def charge():
            """Permet de charger une partie"""
            def on_button():
                recup_save(entree.get(),pseudo,t,entree)
                
            pseudo,content = lire_pseudo()

            def detruire():
                if partie()==False:
                    timer()
                t.destroy()
                                
            t=Toplevel()
            t.grab_set()
            t.title('Charger')
            t.iconbitmap('img/bomb.ico')
            t.resizable(width=False, height=False)
            l = LabelFrame(t, text="Votre pseudo :", padx=10, pady=10)
            l.pack(fill="both", expand="yes")
            l.pack(side=LEFT)

            if partie()==False:
                timer(True)
                t.protocol("WM_DELETE_WINDOW", detruire)
            
            entree = Entry(l)
            entree.pack()
            bou=Button(t,text='Annuler',command=detruire)
            bou.pack(side=BOTTOM)
            bou=Button(t,text='Charger',command=on_button)
            bou.pack(side=BOTTOM)
            entree.pack()
            t.mainloop()

        def recup_save(pseudo,pseudos,parent,entree):
            """Récupère si le pseudo existe les données de sauvegarde pour la fonction charge"""
            if pseudo not in pseudos:
                showinfo('Erreur',"Votre pseudo n'existe pas")
                entree.delete(0,len(pseudo))
            else:
                j=0
                bombe,pos,bou,flag=[],[],[],[]
                coter=0
                
                with open('sauvegarde','r') as save:
                    content = save.read()
                    save.close()
                    content = content.split()
                    for i in content:
                        if str(i)!=str(pseudo):
                            j+=1
                        else:
                            break
                    j+=1
                    coter=int(content[j])
                    j+=1
                    sec=int(content[j])
                    for i in range(j+2,(j+2)+int(content[j+1])):
                        bombe.append(int(content[i]))
                    j+=int(content[j+1])+2
                    for i in range(j+1,(j+1)+int(content[j])):
                        pos.append(int(content[i]))
                    j+=int(content[j])+1
                    for i in range(j+1,(j+1)+int(content[j])):
                        bou.append(int(content[i]))
                    j+=int(content[j])+1
                    for i in range(j+1,(j+1)+int(content[j])):
                        flag.append(int(content[i]))
                        
                parent.destroy()
                option(len(bombe),coter,False,sec)
                nouveau(True,bombe,pos,bou,flag,pseudo)

        
        
        def sauvegarde():
            """Sauvegarde la partie"""
    
            def on_button():
                a=entree.get()
                save_edit(a,pseudo,t,entree)

            def detruire():
                if partie()==False:
                    timer()
                t.destroy() 
                
            pseudo,content =lire_pseudo()
                                
            t=Toplevel()
            t.grab_set()
            t.iconbitmap('img/bomb.ico')
            t.title('Sauvegarde')
            t.resizable(width=False, height=False)
            l = LabelFrame(t, text="Votre pseudo :", padx=10, pady=10)
            l.pack(fill="both", expand="yes")
            l.pack(side=LEFT)
            
            if partie()==False:
                timer(True)
                t.protocol("WM_DELETE_WINDOW", detruire)
            
            entree = Entry(l)
            bou=Button(t,text='Annuler',command=detruire)
            bou.pack(side=BOTTOM)
            bou=Button(t,text='Sauvegarde',command=on_button)
            bou.pack(side=BOTTOM)
            entree.pack()
            t.mainloop()
        

        def save_edit(value,pseudos,parents,entree):
            """Permet d'ajouter des données de sauvegarde à la suite dans le fichier sauvegarde (créer le fichier sauvegarde s'il n'existe pas). Cette focntion est utilisé dans la fonction sauvegarde"""
            bool=False
            bombe,pos,bou,flag,coter,sec=recup_info()
                
            if partie():
                showerror('Erreur', "Votre partie est terminé ou pas commencé vous ne pouvez pas l'enregistré !")
                if partie()==False:
                    timer()
                parents.destroy()
                return
            
            if pseudo_partie()!="":
                showerror('Erreur', "Vous pouvez enregistré une partie qu'une seule fois !")
                if partie()==False:
                    timer()
                parents.destroy()
                return
                
            chiffre=0
            for i in value:
                if i not in string.printable[0:94]:
                    bool=True
                if i in string.printable[0:10]:
                    chiffre+=1
            if chiffre==len(value):
                bool=True
            
            if bool:
                showerror('Erreur', 'Votre pseudo est invalide.')
                entree.delete(0,len(value))
            elif value in pseudos:
                showerror('Erreur', 'Votre pseudo est déjà utilisé veuillez en utiliser un autre.')
                entree.delete(0,len(value))
            else:
                info = str('Etes vous sur de vouloir sauvegarder sous le pseudo '+str(value)+' ?')
                if askokcancel('Attention', info):
                    with open('sauvegarde', 'a') as save:
                        
                        content = str(value)+" "+str(coter)+" "+str(sec)+" "+str(len(bombe))
                        for i in bombe:
                            content+=" "+str(i)
                        content+=" "+str(len(pos))
                        for i in pos:
                            content+=" "+str(i)
                        content+=" "+str(len(bou))
                        for i in bou:
                            content+=" "+str(i)
                        content+=" "+str(len(flag))
                        for i in flag:
                            content+=" "+str(i)
                        content+=" \n"

                        retour=()
                        retour=verif_valeur(content)
                        
                        if retour[0]:    
                            save.write(content)
                            showinfo('Sauvegarde', 'Votre partie a été enregistré '+str(value)+' !')

                        else:showerror('Erreur', 'Votre partie à déjà été enregistré '+str(retour[1])+' !')
                        
                        save.close()
                        parents.destroy()
                        nouveau()
                        
                        

                else:
                    showerror('Erreur', "Une erreur est survenue, veuillez réessayer.")
                    parents.destroy()
                    if partie()==False:
                        timer()
                
        
            
        def verif_valeur(contenu):
            """Vérifie si les données ne correspondent pas à une sauvegarde déjà présente"""
            pseudos,content=lire_pseudo()
            contenu=contenu.split()
            
            same=False
            pseudo=str(contenu[0])
            for i in pseudos:
                if content[i]==contenu[1:len(contenu)]:
                    same=True
                    pseudo=str(contenu[0])
                    
            if same:
                return (False,pseudo)
            else:
                return (True,pseudo)

        def score():
            """Permet d'afficher les scores en utilisant score.py"""
            def detruire():
                if partie()==False:
                    timer()
                t.destroy()

            t=Toplevel()
            t.grab_set()
            t.iconbitmap('img/bomb.ico')
            t.title('Tableau des scores')
            t.resizable(width=False, height=False)
            mainFrame=Frame(t,relief=RIDGE)
            mainFrame.pack()
            lb = LabelFrame(mainFrame,text="Scores",bd = 1,bg='whitesmoke')
            l = []
            lb.pack()
            if partie()==False:
                timer(True)
                t.protocol("WM_DELETE_WINDOW", detruire)
            if connecter()==False:
                detruire()
                showerror('Erreur de connexion',"Vous n'êtes pas connecter, vous ne pouvez donc pas accéder aux scores.")
            else:
                classement = classer()
                expert = len(classement["Expert"])
                inter = len(classement["Intermédiaire"])
                debutant = len(classement["Débutant"])

                vide=False
                longueur = expert + inter + debutant
                
                if longueur==0:
                    vide=True
                    
                longueur+=1
                if longueur>30:longueur=30
                
                a=0
                for i in range(4):
                    for j in range(longueur):

                        w=20
                        texte="test"
                        
                        if i==0:
                            w=10
                            texte=str(j)
                            if j==0:texte="Rang"

                        elif i==1:
                            if j==0:texte="Pseudo"

                        elif i==2:
                            w=10
                            if j==0:texte='Temps (sec)'

                        elif i==3:
                            w=15
                            if j==0:texte='Niveau'
                            elif j>0 and j<=expert:texte='Expert'
                            elif j>expert and j<=expert+inter:texte="Intermédiaire"
                            elif j>inter+expert and j<=longueur:texte="Débutant"
                        

                        l.append(Label(lb,text=texte,width=w,relief=GROOVE))
                        l[a].grid(row=j,column=i)
                        a+=1

                if vide:
                    noscore = Label(mainFrame,text="Pas de scores enregistrés pour l'instant",relief=GROOVE,fg='red')
                    noscore.pack(fill=X)
                    
                if expert>30:expert=29
                if expert+inter>30:inter=longueur-expert-1
                
                
                for i in range(expert):
                    l[(i+1)+longueur].config(text=classement["Expert"][i][0])
                    l[(i+1)+longueur*2].config(text=classement["Expert"][i][1])
                a=0
                for i in range(expert,expert+inter):
                    l[(i+1)+longueur].config(text=classement["Intermédiaire"][a][0])
                    l[(i+1)+longueur*2].config(text=classement["Intermédiaire"][a][1])
                    a+=1
                a=0
                for i in range(expert+inter,longueur-1):
                    l[(i+1)+longueur].config(text=classement["Débutant"][a][0])
                    l[(i+1)+longueur*2].config(text=classement["Débutant"][a][1])
                    a+=1

            

        def options():
            """Défini les options de jeu"""
            def detruire():
                if partie()==False:
                    timer()
                t.destroy()
                
            def applique():
                mines=s1.get()
                dict_inter={'Petite(9x9)':9,'Moyenne(16x16)':16,'Grande(30x16)':30}
                interface=int(dict_inter[s2.get()])

                option(mines,interface)
                t.destroy()

            def niveau():
                    
                if s0.get()=="Personnaliser":
                    s1.config(state="readonly")
                    s1.config(values=(20))
                    
                    
                    if s2.get()=='Petite(9x9)':
                        maxi=50
                    else:
                        maxi=99
                    
                    s1.config(values=(),from_=20,to=maxi)
                    s2.config(state="readonly")
            
                else :
                    s1.config(state=DISABLED)
                    s2.config(state=DISABLED)

                if s0.get()=="Débutant":
                    s1.config(values=10)
                    s2.config(values=('Petite(9x9)','Grande(30x16)','Moyenne(16x16)'))
                elif s0.get()=="Intermédiaire":
                    s1.config(values=40)
                    s2.config(values=('Moyenne(16x16)','Petite(9x9)','Grande(30x16)'))
                elif s0.get()=="Expert":
                    s1.config(values=99)
                    s2.config(values=('Grande(30x16)','Petite(9x9)','Moyenne(16x16)'))
                
            t=Toplevel()
            t.grab_set()
            t.iconbitmap('img/bomb.ico')
            t.title('Options')
            t.resizable(width=False, height=False)
            if partie()==False:
                timer(True)
                t.protocol("WM_DELETE_WINDOW", detruire)

            
            
                    
            mainFrame=LabelFrame(t,text="Options",relief=RIDGE,padx=25,pady=25,bd=2)
            mainFrame.pack()
            Label(mainFrame,text="Choix difficultés :").pack(side=TOP)
            s0= Spinbox(mainFrame,state="readonly",values=('Débutant','Intermédiaire','Expert','Personnaliser'),wrap=True,command=niveau)
            s0.pack()
            Label(mainFrame,text="Nombres de mines :").pack(side=TOP)
            s1 = Spinbox(mainFrame,state=DISABLED,value=(10),from_=10,to=75)
            s1.pack()
            Label(mainFrame,text="Taille de l'interface :").pack()
            s2 = Spinbox(mainFrame,state=DISABLED,values=('Petite(9x9)','Moyenne(16x16)','Grande(30x16)'),wrap=True,command=niveau)
            s2.pack(side=BOTTOM )

            b_app=Button(t,text="Enregistrer",command=applique)
            b_app.pack(side=BOTTOM and LEFT)
            b_quit=Button(t, text="Quitter", command=detruire)
            b_quit.pack(side=BOTTOM and RIGHT)

        def aide():
            """Défini une fenètre avec les règles du jeu, le pricnipe, et ce qu'il faut savoir sur le programme..."""
            t=Toplevel()
            t.grab_set()
            t.iconbitmap('img/bomb.ico')
            t.title('Aide')
            t.resizable(width=False, height=False)
            fileMen = Menu(t, tearoff=False)

            w,h=300,300

            def detruire():
                if partie()==False:
                    timer()
                t.destroy()
            
            def pack_just_one(f):
                for i in [f1,f2,f3,f4]:
                    i.forget()
                f.pack()

            police="Myriad Pro"
                
            f1=LabelFrame(t,text="Principe du jeu",relief=RIDGE,padx=15,pady=15,bd=2,width=w,height=h)
            Label(f1,text="""Le démineur est un jeu de réflexion \ndont le but est de localiser des mines cachées\n
                  dans un champ virtuel avec pour seule indication\n
                  le nombre de mines dans les zones adjacentes.""",font=(police, 14)).pack()
            f2=LabelFrame(t,text="Règles",relief=RIDGE,padx=15,pady=15,bd=2,width=w,height=h)
            Label(f2,text="""Clic gauche => libérer une case.
Clic droit => placer un drapeau.

Le compteur en haut à guauche est un chronomètre.
Le compteur en haut à droite indique le nombre de mines qu'il reste à trouver.
 
Votre but est aussi de terminer la partie de démineur le plus rapidement possible.

Le chiffre qui s'affiche sur les cases cliquées indique le nombre de mines se trouvant à proximité : 
à gauche ou à droite, en haut ou en bas, ou en diagonale.
Grâce aux indications données par ces chiffres, vous pouvez savoir où se trouvent les mines.

Si une case indique "1" et qu'il n'y a qu'une case non découverte à coté, 
c'est donc qu'une mine se cache à cet endroit là !""",font=(police, 14)).pack()
            
            f3=LabelFrame(t,text="Scores",relief=RIDGE,padx=15,pady=15,bd=2,width=w,height=h)
            Label(f3,text="""Vos scores sont enregistrés sur un serveur. 
Vous pouvez à tout moment les consulter via l'onglet Tableau des scores.

N.B: Les scores seront prochainement visible depuis notre
site internet qui est encore en développement.""",font=(police, 14)).pack()
            f4=LabelFrame(t,text="A propos",relief=RIDGE,bd=2,width=w,height=h)
            Label(f4,text="""|_-_-_-_-_-_-_-_Démineur_-_-_-_-_-_-_-_-_|
|_-_-_-_-_-_-_Auteur: Valentin Chmara_-_-_-_-_-_-_-_|
|_-_-_-_-_Contact: valentinchmara@gmail.com_-_-_-_-_|\n
Demisn © 2016
""",font=(police, 15)).pack()

            fileMen.add_command(label='Principe du jeu',underline=0,command=lambda f1=f1:pack_just_one(f1))
            fileMen.add_command(label='Règles',underline=0,command=lambda f2=f2:pack_just_one(f2))
            fileMen.add_command(label='Scores',underline=0,command=lambda f3=f3:pack_just_one(f3))
            fileMen.add_command(label='A propos',underline=0,command=lambda f4=f4:pack_just_one(f4))
            
            t.config(menu=fileMen)
            f1.pack()
            if partie()==False:
                timer(True)
                t.protocol("WM_DELETE_WINDOW", detruire)

            
        fileMenu = Menu(self, tearoff=False)
        fileMenu.add_command(label="Nouveau        Ctrl+N", underline=1, command=nouveau)
        fileMenu.add_command(label="Ouvrir             Ctrl+O", underline=1, command=charge)
        fileMenu.add_command(label="Sauvegarder  Ctrl+S", underline=1, command=sauvegarde)
        fileMenu.add_separator()
        fileMenu.add_command(label="Quitter           Ctrl+Q", underline=1, command=parent.destroy)
        self.add_cascade(label="Fichier",underline=0, menu=fileMenu)
        self.add_command(label="Options",underline=0,command=options)
        self.add_command(label="Tableau des scores",underline=0,command=score)
        self.add_command(label="Aide",underline=0,command=aide)
        
        parent.bind('<Control_L>'+'n',lambda self:nouveau())
        parent.bind('<Control_L>'+'o',lambda self:charge())
        parent.bind('<Control_L>'+'s',lambda self:sauvegarde())
        parent.bind('<Control_L>'+'q',lambda self:parent.destroy())

        
    def delete_save(self,name):
        """Détruit les données sauvegarde pour un pseudo donné"""
        with open('sauvegarde','r') as save:
            lines= save.readlines()
            content=''
            for i in lines:
                j=0
                pseudo=""
                
                while i[j]!=' ':
                    pseudo+=str(i[j])
                    j+=1
                    
                if pseudo!=str(name):
                    content+=str(i)
            save.close()
                
        with open("sauvegarde",'w') as save:
            save.write(content)
            save.close()
        
        


class App(Tk):
    """Classe permettant de tester juste la barre de menu"""
    def __init__(self):
        def nouveau():a=0
        def recup():a=0
        def option(a,b):a=0
        def timer(bool=True):a=0
        def pseudo():a=0
        Tk.__init__(self)
        menubar = MenuBar(self,nouveau,recup,option,timer,recup,pseudo)
        self.config(menu=menubar)
        

if __name__ == "__main__":    #Si menubar.py est lancé en principale alors on utilise la class App()

    app=App()
    app.mainloop()
