from tkinter import *
from tkinter import ttk
root = Tk()
root.title('Football result app by Nassim Bouziane')
root.geometry('500x500')

frm = ttk.Frame(root, padding=0)
frm.grid()

ttk.Label(frm, text='test').grid(column=0, row=0)
ttk.Button(frm,text='test2').grid(column=3, row=0)
Combobox['values'] = ('valeur1','valeur2','valeur3')

ttk.Combobox(frm,textvariable=Combobox).grid(column=2, row=0)

root.mainloop()