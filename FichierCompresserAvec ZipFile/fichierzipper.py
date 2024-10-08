import zipfile,os

#ZIPFILE
##la lecture
ecr=zipfile.ZipFile('monpremiertest.zip',mode='r',compression=zipfile.ZIP_DEFLATED)
print(ecr.namelist())
for file in ['fichier.txt']:
    print(ecr.read(file))

#with zipfile.ZipFile('monpremier.zip',mode='a',compression=zipfile.ZIP_DEFLATED) as e:
    #name=zipfile.ZipFile('monpremier.zip').namelist()
    #os.chdir('monpremier.zip')
    #with open('txt.txt','a') in name:
        #print('a')
#ecriture
#fo=zipfile.ZipFile('monprojetapplication_web.zip',mode='w',compression=zipfile.ZIP_DEFLATED)
#fo.write('C:/Users/Bryce/Documents/projectpython/CONSOLE App/FichierCompresserAvec ZipFile/monprojetapplication_web/fichier.txt','ga')

#print(fich.namelist()) #afficher lA LISTE DE FICHIERS ARCHIVES
##parcourir tout

#for filename in ['infos.txt']:
    ##try:
    #dp=fich.read(filename) # LE CONTENU DE FICHIER TXT 
    #inf=fich.getinfo(filename) #information specifique du fichier txt
    ##os.chdir('./')
    #with open(filename,'w')as f:
        #f.write('filename')
    ##fi.write('un peu de douceur ')
    
    
    #print(dp)
    #print(inf)
    #except :
        #print('no')