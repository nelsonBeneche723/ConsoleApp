# from menu import menu,Inscription,Eleve,exit
# import os
#
# menu()#affiche le menu
# choix=int(input('Choisissez\nEntrer le numero choisi:'))
# while choix!=0:
#
#     if choix==1:
#         os.system('clear')
#         Inscription()
#     elif choix==2:
#         os.system('clear')
#         Eleve()
#     elif choix==4:
#         os.system('clear')
#         exit()
#     else:
#         print("mauvais choix.")
#     #Re-afficher le menu et la barre d'entree
#     menu()
#     choix=int(input("Choisissez\nEntrer le numero choisi:1"
#                     ""))
#
# print("Merci!!!!!!!!")
# os.system('pause')

import matplotlib.pyplot as plt
import pandas as pd

#definir les notes des etudiants
notes=[10,11,12,14,23,24,9]
nombreetudiants=len(notes)
print(nombreetudiants)

#tracer la graphe
# plt.hist(notes,bins=[9,14,20,22,25],width=2,color='red') #bins c'est le nombre d'intervalle dans le histogramme
# plt.title('Histogramme de distribution de note des etudiants')
# plt.xlabel('Notes')
# plt.ylabel('Nombre des eleves')
# plt.show()

#Creation de graphique avec le module
gr=pd.DataFrame({'Notes':[10,10,12,14,23,24,9]})
gr.hist(bins=9,width=2,color='black')
# plt.xlabel('Notes')
# plt.ylabel('Nombre')
# plt.legend('Graphique')
plt.axis()
plt.legend()

# plt.arrow(x=0,y=3,dx=4,dy=5)
# plt.bar(x=0,height=20)
plt.show() #affichage de l'histogramme