from tkinter import *
pr = Tk()
pr.title("yazilar vs")
pr.geometry("500x500")

def mesaj_yaz():
    print("tuşa basıldı")

tus = Button(text="tus yazisi", command= mesaj_yaz)
tus.pack()

mainloop()