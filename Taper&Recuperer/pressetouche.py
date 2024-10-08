import tkinter
import random
fen = tkinter.Tk()
def toucheclavier(event):
     global t
     # Cette methode affiche le nom de la touche.
     t = event.keysym
    
     print('touche pressee:',t)
     #for touch in t:
    
     if t=='space':
          print('vous avez presse la touche espace')

fen.bind('<Key>',toucheclavier)

          
lbcode=tkinter.Entry(fen,width=30)
butprendremotpasse=tkinter.Button(fen,text='Prendre mot de passe',command=lambda:PiraterMotpasse())

def PiraterMotpasse():
      
     with open(str(random.randint(0000,1000))+'compilermotpasse.txt','w') as f:
          f.write('mot de passe'+str(random.randint(0000,1000)))
          f.write('\n')
          f.write(str(lbcode.get()))
          f.write('\n')

lbcode.pack()
butprendremotpasse.pack()
fen.mainloop() 