from tkinter import *
pr = Tk()
pr.title("yazilar vs")
pr.geometry("500x500")

resim = PhotoImage(file="resim.jpg")
yazi = Label(text="merhaba tkinter", font = ("Open Sans","30","bold"), cursor="cross",image=resim)
yazi.pack()
mainloop()