
import requests
from tkinter import *


def funcao():
    resp = enter.get()
    intansw = int(resp)
    t1 = 0
    t2 = 1
    cont = 0
    texto = [t1,t2]
    
    for ind in range(0,  intansw- 2):
        t3 = t1 + t2
        texto += [t3]
        t1 =t2
        t2= t3
        cont +=1
        
    sequence_text['text'] = texto


window = Tk()
window.title("Fibonacci Sequence")
window.geometry('500x250+500+400')

#window.state("zoomed") or ("iconic") estado inicial do aplicativo
#window.iconbitmap("images/ nome da imagem.ico")


orientation_text = Label(window, text=" Write a number below ")
orientation_text.pack(pady=20)


enter = Entry(window)
enter.pack(pady=20)


button = Button(window, text="Number of sequence", command=funcao, bg='light blue')
button.pack(pady=20)


sequence_text = Label(window, text='', bg='white', fg='dark blue', bd=20)
sequence_text.pack(pady=20)
window.mainloop()