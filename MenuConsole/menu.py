import sys
import sqlite3
import sys
import datetime


# on affiche l'entete du menu console


def affichage():
    print('------------------------------College Mixte de la Renaissance---------------------------')
    print('---------------------------------------Menu Principal-----------------------------------')
    print('__________________________________________1-Eleve_______________________________________')
    print('__________________________________________2-Professeur__________________________________')
    print('__________________________________________3-Note________________________________________')
    print('__________________________________________4-Sortie______________________________________')
    entre = int(input('Selectionner un module\n'))
    match entre:
        case 1:
            eleve()
        case 2:
            print('professeur')
        case 3:
            print('note')
        case 4:
            exit()
        case _:
            print('mauvais choix')


# creation du menu principale
# creation de sous menu


def eleve():
    print('1-Enregistrer nouveau eleve')
    print('2-Rechercher un eleve')
    print('3-Modifier un eleve')
    print('4-supprimer un eleve')
    print('5-Retour au menu principal')
    entre = int(input('Selectionner\n'))
    match entre:
        case 1: enregistrereleve()
        case 5: affichage()


def enregistrereleve():
    nom = input("Entrer le nom:\n")
    prenom = input("Entrer le prenom:\n")
    sexe = input("Entrer le sexe:\n")
    datenaissance = input("Entrer la date de naissance:\n")
    lieunaissance = input("Entrer le lieu de naissance:\n")
    nouvelleclasse= input("Entrer la nouvelle classe:\n")
    parent = input("Entrer le nom de parent:\n")
    telephoneresponsable = input("Entrer le telephone du responsable:\n")
    domicilie = input("Entrer le domicilie:\n")
    adresse = input("Entrer l'adresse:\n")
    groupesanguin = input('Entrer le groupe sanguin:\n')
    dateenregistrer = datetime.date.today()
    connection = sqlite3.connect('menu.db')
    curs = connection.cursor()
    curs.execute('create table if not exists eleve(id integer primary key autoincrement, nom varchar(30),'
                 ' prenom varchar(30), sexe varchar(30),datenaissance varchar(20),lieunaissance varchar(20), '
                 'nouvelleclasse varchar(30), parent varchar(20),telephoneresponsable varchar(20),'
                 'domicilie varchar(20),adresse varchar(30), groupesanguin varchar(10),dateenregistrer varchar(20))')
    cur = connection.cursor()
    req = cur.execute("insert into eleve values(?,?,?,?,?,?,?,?,?,?,?,?,?)", (cur.lastrowid, nom, prenom, sexe, datenaissance, lieunaissance, nouvelleclasse, parent, telephoneresponsable, domicilie, adresse, groupesanguin, dateenregistrer))
    connection.commit()
    print(f'insertion reussie...')
    print(f"Vous avez enregistre {nom} {prenom}")
    connection.close()


def exit():
    sys.exit(1)



if __name__ == '__main__': # la fonction main
    affichage()
    # menuprincipale()

# os.system('pause')
# os.system('cls')


