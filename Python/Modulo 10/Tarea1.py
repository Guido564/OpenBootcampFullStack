from tkinter import *

root = Tk()
root.title("Mi primer programita")
root.geometry("200x150")

r = IntVar()
r.set(0)

def reset():
    r.set(0)
    

boton1 = Radiobutton(root, text="Pizza", variable=r, value=1).pack()
boton2 = Radiobutton(root, text="Empanadas", variable=r, value=2).pack()
boton3 = Radiobutton(root, text="Milanesas", variable=r, value=3).pack()

myButton = Button(root, text="Reset!", command=reset)
myButton.pack()

mainloop()