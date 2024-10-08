#-----:::::::::::::::::::Ing Nelson Beneche:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#Module ZLIB--------------------------------------------------------------------------------------------------------
#MODULE base64 pour crypter les valeurs du fichier::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import zlib
import base64
from distutils.core import setup
#import py2exe
#compresser le fichier    
liref=open('data.txt').read()    
#il faut encoder la valeur qui se trouve dans le fichier texte dans le niveau 9.
comp=base64.b64encode(zlib.compress(liref.encode('utf-8'),9))
lire=comp.decode('utf-8')
print(comp)

#Ecriture
f=open('data.txt','w')
f.write(lire)
f.close()

#Decompresser le fichier
lirecompress=open('data.txt').read()
l=zlib.decompress(base64.b64decode(lirecompress.encode('utf-8')))
ll=l.decode('utf-8')
print(ll)


setup(console=['CompressionFichier-ZLIB.py'])
