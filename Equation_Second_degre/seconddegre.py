import math #pour les fonctions mathematiques.
import numpy as np #pour les calcules algebre lineaire
from matplotlib import pyplot as plt # pour afficher les graphes
#Cacul equation second degre
print("Entrer le coefficient de a:")
a=int(input())
print("Entrer le coefficient de b:")
b=int(input())
print("Entrer le coefficient de c:")
c=int(input())
#les differentes calculs de
delta=((b*b)-(4*a*c))
if delta>0:
                    
                    x1=(-b-math.sqrt(delta))/(2*a)
                    x2=(-b+math.sqrt(delta))/(2*a)
                    print("la solution est:","x1:",int(x1),"et","x2:",int(x2))
                    xmin=x1
                    xmax=x2
                    x=np.linspace(xmin,xmax,100)
                    y=a*x**2+b*x+c
                    plt.plot(x,y)
                    plt.title('le trace')
                    plt.axvline(x=0,color='black') #la ligne verticale
                    plt.axhline(y=0,color='black') #la ligne horizontale
                    
                                       
                    plt.show()
elif (delta==0):      
                    x1=x2=-b/2*a          
                    print("la solution est:","x1:",int(x1),"et","x2:",int(x2))
else:  
                    
                    print("pas de resultat:") 

#Calcul de la graphe



                  
                  
                  
                    
                    #if __name__ == "__main__":

