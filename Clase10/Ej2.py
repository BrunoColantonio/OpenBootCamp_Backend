from tkinter import *

root = Tk()
listbox = Listbox(root)

for item in ["Jazz", "Rock", "Rap", "Pop", "Techno", "Reggaeton"]:
 listbox.insert(END, item)
 
 
listbox.pack()
label = Label(text="Generos musicales")
label.pack()
root.mainloop()