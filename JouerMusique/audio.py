import pygame
import os
import tkinter
from tkinter import filedialog
#player music in tkinter
fen=tkinter.Tk()
fen.title('Nelson Multiplayer Music...')
larg=400
haut=200
largecran=fen.winfo_screenwidth()
hautecran=fen.winfo_screenheight()
x=(largecran/2)-(larg/2)
y=(hautecran/2)-(haut/2)
fen.geometry('%dx%d+%d+%d' %(larg,haut,x,y))
mainmenu=tkinter.Menu(fen)
menu1=tkinter.Menu(mainmenu,tearoff=0)
menu2=tkinter.Menu(mainmenu,tearoff=0)

menu1.add_command(label='Ouvrir',command='')
mainmenu.add_cascade(label='Fichier',menu=menu1)
fen.configure(menu=mainmenu)
lb=tkinter.Label(fen,text='Selectionner votre morceau...')

def selectionner():
    chmusic=filedialog.askopenfilename(initialdir='/',title='Choisir une musique',filetypes=(('mp3 files','*.mp3'),('All files','*.*')))
    pygame.mixer.init()
    pygame.mixer.Sound(chmusic).play() 
    for ch in chmusic:
        lbb=tkinter.Label(fen,text=chmusic)
        lbb.grid(row=1,column=1)
but=tkinter.Button(fen,text='selectionner',command=lambda:selectionner())


print('playing music player Nelson')
lb.grid(row=0,column=0)
but.grid(row=1,column=0)
fen.mainloop()

#os.system('pause')
#print('playing music player Nelson')
#import vlc
##instance de la classe

#m=vlc.MediaPlayer('C://Users//Nelson//Desktop//projectpython//CONSOLE App//JouerMusique//k-zino-santiman-pa-dyaman.wav')
#m.play()



