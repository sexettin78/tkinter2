from cProfile import label
from tkinter import *
pr = Tk()
pr.title("yazilar vs")
pr.geometry("500x500")
degisken = 0

def mesaj_yaz():
    degisken = int(veri.get())
    degisken2 = int(veri2.get())
    yazi["text"] = degisken+degisken2 
yazi = Label(text="")
yazi.pack()

veri = Entry()
veri.pack()
veri2 = Entry()
veri2.pack()
tus = Button(text="tus yazisi", command= mesaj_yaz)
tus.pack()

mainloop()