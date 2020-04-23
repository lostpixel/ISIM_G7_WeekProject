#!/usr/bin/python2.7
# -*-coding:Latin-1 -*
"""
Barre de menu du code du d�mineur. 
    Tous droits r�serv�s Demisn � 2016

D�mineur.py, ainsi que menubar.py sont essentiels au bon fonctionnement du programme g�n�rale.
Cependant le programme est autonome, on peut le tester tout seul pour v�rifier sont bon focntionnement gr�ce au commentaire pr�sents dans les diff�rentes focntions
Le but de ce fichier est d'�tablir un lien vers un ftp pour pouvoir transf�rer des informations et en recevoirs
"""

from ftplib import *
import os

host,user,mdp='warzok.atspace.cc',"2057446_1","abc123def456"


connexion=False

try :   #On essaye de se connecter si cela echoue notre valeur connexion reste fausse
    ftp = FTP(host)
    ftp.login(user,mdp)
    connexion=True
except:
    connexion=False
    print("Erreur de connexion")


def connecter():
    """Retourne l'�tat de connexion"""
    return connexion

def dir():
    """Permet d'afficher le contenu du dossier ftp o� l'on se trouve"""
    data = []

    ftp.dir(data.append)
    for line in data:
        print ("-", line)

def recup_donnees():
    """R�cup�re les informations de sauvegardes du serveur"""
    content =[]
    try :
        ftp.retrbinary('RETR sauvegarde', content.append)
    except:
        a = open(os.getcwd()+"\$cache", 'a')
        a.close()
        with open(os.getcwd()+"\$cache", 'rb') as cache:
            ftp.storbinary("STOR sauvegarde",cache)
            cache.close()
            os.remove(os.getcwd()+'\$cache')
        
    if len(content)==0:
        content = ""
    else:
        content= str(content[0], encoding='UTF-8')
    
    return content


def ajoute_score(pseudo,*args):
    """Permet d'ajouter un score dans le fichier de sauvegarde du serveur"""

    content = recup_donnees()
    ftp.delete('sauvegarde')

    
    content+='\n'+str(pseudo)
    for count,thing in enumerate(args):
        content+=' {0}'.format(thing)
    content= str(content)

    
    with open(os.getcwd()+"\$cache", 'a') as cache:
        cache.write(content)
        cache.close()
        
    uploadftp(ftp, os.getcwd()+'\$cache','sauvegarde')
    os.remove(os.getcwd()+'\$cache')

def command(command,*args):
    """Effectuer la commande FTP que vous voulez"""
    print(ftp.sendcmd(command,*args))
    
    
def uploadftp(ftp, ficdsk, ficftp=None):
    """t�l�charge le fichier ficdsk du disque dans le r�p. courant du Serv. ftp
       - ftp: variable 'ftplib.FTP' sur une session ouverte
       - ficdsk: nom du fichier disque avec son chemin
       - ficftp: si mentionn� => c'est le nom qui sera utilis� sur ftp
    """
    repdsk, ficdsk2 = os.path.split(ficdsk)
    if ficftp==None:
        ficftp = ficdsk2
    
    with open(ficdsk, "rb") as f:
        ftp.storbinary("STOR " + ficftp, f)


def classer():
    """Classe les donn�es de sauvegarde pour pouvoir les retourner � la fonction score dans menubar.py"""

    #Niveau : 3�me argument, 1=D�butant 2=Interm�diaire 3=Expert

    score = []
        
    content = recup_donnees()
    content = content.split("\n")

    for i in content:
        if i.split()!=[]:
            score.append(i.split())

    pseudo_classes={"D�butant":[],"Interm�diaire":[],"Expert":[]}
    classement_final = {"D�butant":[],"Interm�diaire":[],"Expert":[]}

    for i in score:
        if str(i[2])=="1":
            pseudo_classes["D�butant"].append(i)
        elif str(i[2])=="2":
            pseudo_classes["Interm�diaire"].append(i)
        elif str(i[2])=="3":
            pseudo_classes["Expert"].append(i)
    a=0
    for niveau in pseudo_classes:
        
        score_niv=[]

        for t in pseudo_classes[niveau]:
            score_niv.append(int(t[1]))
        score_niv.sort()
        
        
        for t in range(len(score_niv)):
            for j in pseudo_classes[niveau]:
                if int(j[1])==score_niv[t]:
                    
                    classement_final[niveau].append(j)
        
        a+=1
            
            
    return(classement_final)
    
    
