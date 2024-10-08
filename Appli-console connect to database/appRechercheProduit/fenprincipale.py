#creation d'une application console qui permet de rechercher des produits et ensuite le met dans le stock pour vente
import pymysql,os
desc=input('Entrer la description du produit \n')
connection=pymysql.connect(host='localhost',user='root',db='benecheboutique',passwd='')
cur=connection.cursor()
req=cur.execute("select * from vetement where description='"+desc+"'")
connection.commit()
result=cur.fetchall()
if len(result):
    #parcourir les differentes valeurs retourner par la requete sql
    for res in result:
        print(res[0],'/',res[1],'/',res[2],'/',res[3],'/',res[4],'/',res[5],'/',res[8])
        #print('reussie')
else:
    print('echec')
os.system('pause')