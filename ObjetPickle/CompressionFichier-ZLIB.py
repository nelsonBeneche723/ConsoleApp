#-----:::::::::::::::::::Ing Nelson Beneche::::::::::::::::::::::::::::::::::::::
#Module PICKLE---::::::::::::::::::::
import pickle #ce module permet de sauvegarder des objets dans des fichiers en python
import zlib
import base64
#ecriture
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
#with open('data.txt','a') as f:
    #f.write('mes fichiers compresses.')

#compresser le fichier    
liref=open('data.txt').read()    
#il faut encoder la valeur qui se trouve dans le fichier texte dans le niveau 9.
comp=base64.b64encode(zlib.compress(liref.encode('utf-8'),9))
lire=comp.decode('utf-8')
#print(comp)

#Ecriture
f=open('data.txt','w')
f.write(lire)
f.close()

#Decompresser le fichier
lirecompress=open('data.txt').read()
l=zlib.decompress(base64.b64decode(lirecompress))
ll=l.decode('utf-8')
print(l)