#-----:::::::::::::::::::Ing Nelson Beneche::::::::::::::::::::::::::::::::::::::
#Module PICKLE---::::::::::::::::::::
import pickle #ce module permet de sauvegarder des objets dans des fichiers en python
import zlib
import base64

#Ecriture
with open('pickledonnees.txt','wb') as f:

    pickledata={'code':'001','Nom':'Beneche','Prenom':'Nelson'}
    mon_fichier=pickle.Pickler(f)
    mon_fichier.dump(pickledata)
    f.close()

        
 #lecture     
with open('pickledonnees.txt','rb') as f:
    l=pickle.Unpickler(f)
    mon_f=l.load()
    print(mon_f['Nom'])
	
    #if 'Nom' in mon_f: #le Nom indique le nom de la cle qu'on demande d'afficher la valeur qu'elle contient.
        #print(l['Nom'])
