import tkinter
from tkinter import ttk
import random
from ctypes import cdll
from PIL import Image,ImageTk
from tkinter import messagebox
from math import *
#dl=cdll.LoadLibrary("nouveau.dll")
#print(dl)
#dll.
app=tkinter.Tk()
app.title('MATHAPP')
# le menu
main=tkinter.Menu(app)
menu1=tkinter.Menu(main,tearoff=0)
menu2=tkinter.Menu(main,tearoff=0)
menu3=tkinter.Menu(main,tearoff=0)
menu4=tkinter.Menu(main,tearoff=0)
menu5=tkinter.Menu(main,tearoff=0)

menu1.add_command(label='Ouvrir')
menu2.add_command(label="Resoudre un binome",command=lambda:FenEquation())
menu2.add_command(label="Resoudre l'equation du second degre")
menu3.add_command(label='Calculatrice',command=lambda:fencalculatrice())
menu3.add_command(label='Alarme')
menu3.add_command(label='Horloge du monde')
menu3.add_separator()
menu3.add_command(label='Savoir le taux du jour')
menu4.add_command(label='Table',command=lambda:FenTable())
menu4.add_command(label='Factoriel')
menu4.add_separator()
menu4.add_command(label='Matriciel')
menu5.add_command(label='Concernant le logiciel MATHAPP...')

main.add_cascade(label='Fichier',menu=menu1)
main.add_cascade(label='Calcul',menu=menu4)
main.add_cascade(label='Equation',menu=menu2)
main.add_cascade(label='Outils',menu=menu3)
main.add_cascade(label='Aide',menu=menu5)
#les fenetres
def FenTable():
    fen=tkinter.Toplevel(app)
    fen.title('Calcul de table')
    larg=600
    haut=380
    largecran=fen.winfo_screenwidth()
    hautecran=fen.winfo_screenheight()
    x=(largecran/2)-(larg/2)
    y=(hautecran/2)-(haut/2)
    fen.geometry('%dx%d+%d+%d' % (larg,haut,x,y)) #centrer la fenetre fille
    spin=tkinter.Spinbox(fen, values=0)
    sex=tkinter.StringVar()
    rad=tkinter.Radiobutton(fen,variable=sex,value='sexe')
    tabcontrol=ttk.Notebook(fen)
    tab1=ttk.Frame(tabcontrol)
    tab2=ttk.Frame(tabcontrol)
    tabcontrol.add(tab1,text='Mutiplication')
    tabcontrol.add(tab2,text='Addition')
    #tabcontrol.configure(background='yellow')
    lb=tkinter.Label(tab1,text='Entrer un nombre a calculer')
    spin=tkinter.Spinbox(tab1,from_=0,to=100)
    #spin.configure(state='disabled')
    
    bout=tkinter.Button(tab1,text='Calculer',command=lambda:cal())
    tr=ttk.Treeview(tab1,columns=('',''))
    chresult=tkinter.Text(tab1,height=10,width=30)
    #chresult.configure(state='disabled')
    #tab 2
    lbb=tkinter.Label(tab2,text='Faire calcul addition')
    #tab.add(spin)
    #rad.place(x=0,y=0)
    
    
    def cal():
        sp=spin.get()
        chresult.delete('1.0','end')
        for i in range(0,10):
            
            chresult.insert(tkinter.END,int(sp))
            chresult.insert(tkinter.END,'*')
            chresult.insert(tkinter.END,int(i))
            chresult.insert(tkinter.END,'=')
            chresult.insert(tkinter.END,int(sp)*int(i))
            chresult.insert(tkinter.END,'\n')
            
            
    
    
    
    #chresult.configure(state='disabled')
    lb.grid(row=0,column=0,padx=5,pady=5)
    spin.grid(row=0,column=1,padx=5,pady=5)
    bout.grid(row=0,column=2)
    chresult.grid(row=12,column=2,rowspan=12,columnspan=12,sticky=('N','S','W','E'))
    lbb.grid(row=3,column=0)
    
    tabcontrol.place(x=0,y=2)
    fen.resizable(width=False,height=False) #retirer la forme redimensionnable de la fenetre
    fen.transient(app)
    
    fen.mainloop() #affichage de la fenetre


def fencalculatrice():
    fenprinc=tkinter.Toplevel(app)
    fenprinc.title('Calculatrice')
    larg=550
    haut=260
    largecran=fenprinc.winfo_screenwidth()
    hautecran=fenprinc.winfo_screenheight()
    x=(largecran/2)-(larg/2)
    y=(hautecran/2)-(haut/2)
    fenprinc.geometry('%dx%d+%d+%d' % (larg,haut,x,y)) #centrer la fenetre fille
    fenprinc.resizable(width=False,height=False)
    fenprinc.transient(app)
    #Champ de la Calculatrice
    lbcall=tkinter.Label(fenprinc,text='Votre calculatrice',font=('arial',16,'bold'))
    champcalcula=tkinter.Entry(fenprinc,width=40,bg='white',font=('',10,'bold'))
    #les boutons de la calculatrice
    #numero=tkinter.StringVar()
    #nb1=""
    def ajout(nb):
        global nb1
        nb1=nb
        champcalcula.insert(tkinter.INSERT,nb1)
        
    def affval7():
        ajout("7")
        
    def affval8(): 
        ajout("8")
        
    def affval9(): 
        ajout("9")
        
    def affval6(): 
        ajout("6")
             
    def affval5(): 
        ajout("5")
             
    def affval4(): 
        ajout("4")
        
    def affval3(): 
        ajout("3")
             
    def affval2(): 
        ajout("2")
             
    def affval1(): 
        ajout("1")
             
    def affval0(): 
        ajout("0")
        
    def affvalpt(): 
        ajout(".")       
              
    def Additionner():
        global nb1,op,nb2
        nb2=int(nb1)
        nb1=0
        op=1
        champcalcula.insert(tkinter.INSERT,'+')
        
    def Clear():
        global nb1
        nb1=""  
        champcalcula.delete(0,'end')
        
    def egal():
       
        champcalcula.delete(0,'end') #nettoyer le champ
        global nb1,nb2,op,result
        nb1=int(nb1)
        if (op==1):
            result=round(nb2+nb1,10)  
            champcalcula.insert(tkinter.INSERT,str(result))
            nb1=str(result)     # Somme, pour la reutilisation si on continue d'appuyer   
        if op==2:
            result=round(nb2-nb1,10)  
            champcalcula.insert(tkinter.INSERT,str(result))
            nb1=str(result)    # Diviser, par le dernier resultat si on continue d'appuyer .       
        if op==3:
            result=round(nb2*nb1,10)  
            champcalcula.insert(tkinter.INSERT,str(result))
            nb1=str(result)   #multiplier, par le dernier resultat si on continue d'appuyer.            
    def Moins():
        global nb1,nb2,op
        op=2
        nb2=int(nb1)
        champcalcula.insert(tkinter.INSERT,'-')
        
    def Multiplier():
        global nb1,nb2,op
        op=3
        nb2=int(nb1)
        champcalcula.insert(tkinter.INSERT,'*')
        
    but9=tkinter.Button(fenprinc,text='9',command=affval9,width=8,bg='aqua')
    but8=tkinter.Button(master=fenprinc,text='8',command=affval8,width=8,bg='aqua')
    but7=tkinter.Button(fenprinc,text='7',command=affval7,width=8,bg='aqua')
    but6=tkinter.Button(fenprinc,text='6',command=affval6,width=8,bg='aqua')
    but5=tkinter.Button(fenprinc,text='5',command=affval5,width=8,bg='aqua')
    but4=tkinter.Button(fenprinc,text='4',command=affval4,width=8,bg='aqua')
    but3=tkinter.Button(fenprinc,text='3',command=affval3,width=8,bg='aqua')
    but2=tkinter.Button(fenprinc,text='2',command=affval2,width=8,bg='aqua')
    but1=tkinter.Button(fenprinc,text='1',command=affval1,width=8,bg='aqua')
    but0=tkinter.Button(fenprinc,text='0',command=affval0,width=8,bg='aqua')
    butmoins=tkinter.Button(fenprinc,text='-',command=Moins,width=8,bg='aqua')
    butpoint=tkinter.Button(fenprinc,text='.',width=8,command=affvalpt,bg='aqua')
    butplus=tkinter.Button(fenprinc,text='+',width=8,bg='aqua',command=Additionner)
    butegal=tkinter.Button(fenprinc,text='=',width=8,bg='aqua',command=egal)
    butdiv=tkinter.Button(fenprinc,text='/',width=8,bg='aqua')
    butmul=tkinter.Button(fenprinc,text='*',command=Multiplier,width=8,bg='aqua')
    butCE=tkinter.Button(fenprinc,text='CE',width=8,bg='aqua')
    butpourc=tkinter.Button(fenprinc,text='%',width=8,bg='aqua')
    butplusouMoins=tkinter.Button(fenprinc,text='+/-',width=8,bg='aqua')
    butC=tkinter.Button(fenprinc,text='C',width=8,bg='aqua',command=Clear)
    
   
    
    
    champcalcula.grid(row=3,column=10,padx=15,pady=15,rowspan=1,columnspan=1,sticky=('N','S','W','E'))
    
    #positionnement de la bouton de la calculatrice...
    but7.grid(row=4,column=9,padx=5,pady=5)
    but8.grid(row=4,column=10,padx=5,pady=5)
    but9.grid(row=4,column=11,padx=5,pady=5)
    but4.grid(row=5,column=9,padx=5,pady=5)
    but5.grid(row=5,column=10,padx=5,pady=5)
    but6.grid(row=5,column=11,padx=5,pady=5)
    but1.grid(row=6,column=9,padx=5,pady=5)
    but2.grid(row=6,column=10,padx=5,pady=5)
    but3.grid(row=6,column=11,padx=5,pady=5)
    but0.grid(row=7,column=9,padx=5,pady=5)
    butCE.grid(row=8,column=9)
    butpourc.grid(row=8,column=10)
    butplusouMoins.grid(row=8,column=11)
    butpoint.grid(row=7,column=10)
    butegal.grid(row=7,column=11)    
    
    butdiv.grid(row=4,column=13)
    butmul.grid(row=5,column=13)
    butmoins.grid(row=6,column=13)
    butplus.grid(row=7,column=13)
    butC.grid(row=8,column=13)    

    fenprinc.mainloop()





#image en arriere plan de la fenetre
im=Image.open('123-montessori-numbers.png')
imag=ImageTk.PhotoImage(im.resize((1540,800)),master=app)
lbb=tkinter.Label(app,image=imag)
lbb.grid(row=0,column=0)

#creation de notebook
tabcontrol=tkinter.ttk.Notebook(app)
tab1=tkinter.Frame(app)
tabcontrol.add(tab1,text='A')


lbjeu=tkinter.Label(app,text='JOUER SUR MATHAPP',font=('',16,'bold'))
#lbjeu.grid(row=0,column=2)
butdemarrer=tkinter.Button(app,text='Demarrer le jeu..')
#butdemarrer.grid(row=1,column=0)
def FenEquation():
    global tx,tB
    fen=tkinter.Toplevel(app)
    fen.title('Equation')
    larg=800
    haut=300
    largecran=fen.winfo_screenwidth()
    hautecran=fen.winfo_screenheight()
    x=(largecran/2)-(larg/2)
    y=(hautecran/2)-(haut/2)
    fen.geometry('%dx%d+%d+%d' %(larg,haut,x,y))
    tabcontrol=tkinter.ttk.Notebook(fen)
    tab1=tkinter.Frame(tabcontrol)
    tab2=tkinter.Frame(tabcontrol)
    tabcontrol.add(tab1,text='Equation du premier degre')
    lbx=tkinter.Label(tab1,text='La valeur de a:')
    tx=tkinter.Entry(tab1)
    lbB=tkinter.Label(tab1,text='La valeur de b:')
    tB=tkinter.Entry(tab1)
    but=tkinter.Button(tab1,text='Afficher la valeur de x',command=lambda:ResoudreEquationbinome())
    res=tkinter.Label(tab1)
    tabcontrol.add(tab2,text='Equation du second degre')
    #tx.bind('<Enter>','hello')
    #tx.equtB.get()

    def ResoudreEquationbinome():
        #global tx,tB
        a=tx.get()
        b=tB.get()
        ##Resolution de l'equation selon notre algorithme
        ## ax+b
        #if a=='':
            #messagebox.showerror("Message d'erreur","il faut ajouter le coefficient de a.")
        #elif b=='':
            #messagebox.showerror("Message d'erreur ","il faut ajouter le coefficient de b")
             
            
        #elif a=='0':
            #messagebox.showerror('message','erreur, la valeur de a ne doit pas etre nulle.')
        #elif b=='0':
            #messagebox.showerror('message','erreur, la valeur de b ne doit pas etre nulle.')
        #else:
        x1=int(b)/int(a)
        x=str(round(x1,0))
        result='le resultat '+x
            #res.delete('1.0','end')
            #res.insert(tkinter.END,int(x1))
        res.configure(text=result)
        
   # tB.bind('<Return>',ResoudreEquationbinome)
    tabcontrol.grid(row=0,column=0)
    lbx.grid(row=0,column=0)
    tx.grid(row=0,column=1,padx=5,pady=5)
    lbB.grid(row=1,column=0,padx=5,pady=5)
    tB.grid(row=1,column=1,padx=5,pady=5)
    but.grid(row=2,column=1)
    res.grid(row=3,column=0)   
    fen.transient(app)
    fen.mainloop()   
    
questions=['combien de nombre decimal existe t-il?','comment definit la mathematiques?']
lbquest1=tkinter.Label(app,text=questions[0],font=('',14,'bold'))
#lbquest1.grid(row=0,column=5)






app.config(menu=main)
app.state('zoomed')
#app.resizable(width=False,height=False)
app.mainloop()
#menu console
#nombr=int(input('votre nombre: '))
#if nombr==1:
    #print('bonjour')
#elif nombr==2:
    #print('bonsoir')
#else:
    #print('aucun choix')