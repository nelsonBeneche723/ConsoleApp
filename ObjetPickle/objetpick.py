#-----:::::::::::::::::::Ing Nelson Beneche::::::::::::::::::::::::::::::::::::::
#Module PICKLE---::::::::::::::::::::
import pickle #ce module permet de sauvegarder des objets dans des fichiers en python
import zlib,pymysql
import base64,json

from PIL import Image,ImageTk
#Ecriture
with open('websit.png','rb') as f:

    p=pickle.dumps(f.read())
    str_=base64.b64encode(p)
    ph=str_.decode(encoding='utf-8')
    
    numerocarte='909'
    nom='Nelson'
    prenom='Beneche'
    print (ph)
    
    connection=pymysql.connect(host='localhost',db='pharmatech',user='root',password='')   
    cur=connection.cursor()
    req=cur.execute("insert into Essai values(%s,%s,%s,%s)",(numerocarte,nom,prenom,ph))
    
    connection.commit()
    if req!=0:
        print('insertion reussie')
    else:
        print("echec d'insertion de donnnes")
    #connection.close()        
    ##dt=f.read()
    ##mon_=pickle.Pickler(f)
    ##mon_.dump(dt)
    
    
with open('monimage.txt','wb')as l:
    #dt=l.write()
    #dt='hello'
    #mon_=pickle.Pickler(l)
    #mon_.dump(dt)    
    l.write(str_)
    #mon_fichier=pickle.dump(pickledata,f)
    ##monf=base64.b64encode(mon_fichier)
    ##monf.dump(pickledata)
    #f.close()


#with open('imagemere.txt','wb')as f:   
    
    #fic=json.dumps(f)
 #lecture     
#with open('pickledonnees.txt','rb') as f:
    #l=pickle.Unpickler(f)
    #mon_f=l.load()
    #print(mon_f['Nom'])
	
    #if 'Nom' in mon_f: #le Nom indique le nom de la cle qu'on demande d'afficher la valeur qu'elle contient.
        #print(l['Nom'])
