import requests
from tkinter import *



window = Tk()
window.title("Fibonacci Sequence")

orientation_text = Label(window, text="Click below to see a sequence")
orientation_text.grid(column=0, row=0)

buttom = Button(window, text="Number of sequence", command=funcao)
buttom.grid(column=0, row=5)

sequence_text = Label(window, text="")
window.mainloop()