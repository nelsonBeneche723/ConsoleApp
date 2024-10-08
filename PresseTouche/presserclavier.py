import tkinter as tk


def onReturn(*args):
   print('REturn pressed')
   value=chp.get()
   #
   print(value)
   chp.delete(0,'end')
   

fen=tk.Tk()
fen.title('Hey')
fen.geometry('300x200')
chp=tk.Entry(fen)
chp.pack()
bout=tk.Button(fen, text="Entrer", command=onReturn)
bout.pack()

chp.bind("Touche retour:", onReturn)

fen.mainloop()