import os
def factorielle():
    
    fact=1
    print('Entrer le nombre a calculer')
    n=int(input())
   
    for i in range(2,n+1):
        fact=fact*i
        
    print("le factoriel du nombre est:",fact)
   
if __name__=='__main__':
    factorielle()
	
	
	
	
	
#os.system('pause')