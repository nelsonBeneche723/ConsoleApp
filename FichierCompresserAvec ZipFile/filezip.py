import zipfile,os
from PIL import Image
from pystray import Menu,MenuItem,Icon
#imp=Image.open('programmeur-bureau-logiciel.jpg')
#menu=(MenuItem('Demarrer',''),MenuItem('Arreter ','')) #les sous menu
#ico=Icon('name',imp,'serveur',menu)#image et menu
#ico.run()
#ZIPFILE
# creation de fichier zipper et ajouter d'un fichier dans ce dossier.
fichier=zipfile.ZipFile('NotesEtudiants.zip','w')
file='fichier.txt'
fichier.write(file,compress_type=zipfile.ZIP_DEFLATED)
print('reussie')

#lecture des donnees
nomfichier=fichier.namelist()
print(nomfichier)
for fich in ['fichier.txt']:
    print(fichier.read(fich)) #lire les valeurs
    print(fichier.infolist()) #afficher les infos du fichier en question
    with open(fich,'w') as f: # ecrire dans le fichier.
        f.write('tout vas bien au usa')
    #print(fi)
fichier.close()    
