from tkinter import *
pencere = Tk()
pencere.title("hesap makinesi 2")
pencere.geometry("600x600")

x = StringVar()

def topla():
    a = int(veri.get())
    b = int(veri2.get())
    etiket["text"] = a+b
def cikar():
    a = int(veri.get())
    b = int(veri2.get())
    etiket["text"] = a-b
def bol():
    a = float(veri.get())
    b = float(veri2.get())
    etiket["text"] = float(a/b)
def carp():
    a = int(veri.get())
    b = int(veri2.get())
    etiket["text"] = a*b

x.set(0)

etiket2 = Label(text="Python Tkinter Hesap Makinesine Hoşgeldin!",font = ("Open Sans","13","bold"))
etiket2.pack()
veri = Entry()
veri.pack()

veri2 = Entry()
veri2.pack()

etiket3 = Label(text="\nSeçenekler:")
etiket3.pack()

topla = Radiobutton(text="[+] Topla",value="topla",variable=x,command=topla)
topla.pack()

cikar= Radiobutton(text="[-] Çıkar",value="cikar",variable=x,command=cikar)
cikar.pack()

bol = Radiobutton(text="[/] Böl",value="bol",variable=x,command=bol)
bol.pack()

carp = Radiobutton(text="[*] Çarp",value="carp",variable=x,command=carp)
carp.pack()

etiket4 = Label(text="Sonuç:")
etiket4.pack()


etiket = Label()
etiket.pack()

mainloop()