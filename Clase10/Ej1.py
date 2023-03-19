from tkinter import *

def select():
    window.config(text="{}".format(opcion.get()))
    
def reset():
    opcion.set(None)
    window.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(root, text="opcion1", variable=opcion, value='opcion1', command=select).pack(anchor=W)
Radiobutton(root, text="opcion2", variable=opcion, value='opcion2', command=select).pack(anchor=W)
Radiobutton(root, text="opcion3", variable=opcion, value='opcion3', command=select).pack(anchor=W)

window = Label(root)
window.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()