import json,os,platform
import pygame
#declaration de dictionnaire de donnees
dict={'0012':'Sony','00120':'Beneche'} # un dictionnaire est forme par son cle et par sa valeur separant une virgule si on ajoute d'autre element
dict['1234']='Nelson' #ajouter de nouvelles element dans le dictionnaire
print(dict['0012'])   # un liste contient un ensemble de donnee stocke quand on peut utiliser grace a son cle

#declaration de liste de donnees
nom=['ident','son','di','love','you']
code=[1,2,3,4,5]
code[2]=340 #reaffectation de valeur
nom.append(['benecheamour']) #ajout de l'element dans la liste
nom.extend(nom[5]) #extraire l'element retirer le crochet
print(nom)
#Afficher le premier element
#On affiche un donnee avec le tuple de l'element
print(nom[1],nom[4])
print(code[0:4])
print(code[0:4].pop()) #Supprimer le dernier de la liste ensuit l'afficher celui qui a ete retire...
del code[1] #Supprimer le deuxieme valeur de la liste
del code[:]#Supprimer tout valeur de la liste

print(code)
nomut=os.getenv('username') # nom utilisateur de la session en cours de la machine
#ch="C:\users\\"+nomutil+"Desktop\dictpython\fichier.txt')"
#os.uname_result()
#KeyError erreur il faut rechercher un element avec son cle

#ajouter les donnes dans un fichier texte#
#Creation de repertoire
if not os.path.exists("C:\\Users\\"+nomut+"\\Desktop\\dictpython"):
    os.makedirs("C:\\Users\\"+nomut+"\\Desktop\\dictpython")

  #Ecriture des donnees dans un fichier texte  
with open("C:\\Users\\"+nomut+"\\Desktop\\dictpython\\fichier.txt",'w') as f:
   # json.JSONEncoder(f)
    data=dict['0012']+dict['1234'] #dictionnaire
    data2=str(nom[1]+nom[2])      #list
    f.write(data)
    f.write(data2)
    print('Insertion dans le fichier texte reussie...')
    
#Lecture d'un fichier texte
with open("C:\\Users\\"+nomut+"\\Desktop\\dictpython\\fichier.txt",'r') as f:
    print(f.read())
    print('Lecture du fichier texte en cours...')
    
#lecture de musique
#with open('Criminel-KAÏ-New-Song-2019.mp3') as f:
    #print(f.read())

#jouer=pygame.mixer('Criminel-KAÏ-New-Song-2019.mp3')
#jouer.load()