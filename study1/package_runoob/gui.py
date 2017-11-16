# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']

lista = Listbox(root)
listb = Listbox(root)

for item in li:
    lista.insert(0, item)

for item in movie:
    listb.insert(0, item)

button = Button()
lista.pack()
button.pack()
listb.pack()
root.mainloop()
