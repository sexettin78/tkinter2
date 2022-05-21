from tkinter import *
pr = Tk()
pr.title("listler vs")
pr.geometry("500x500")

list = Listbox()
list.pack()
list.insert(END, "eleman1")
list.insert(END, "eleman2")
mainloop()