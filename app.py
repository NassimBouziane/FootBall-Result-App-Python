from tkinter import *
from tkinter import ttk
root = Tk()
root.title('Football result app by Nassim Bouziane')
root.geometry('500x500')

frm = ttk.Frame(root, padding=0)
frm.grid()
n = StringVar()
n.set('Premier League')
def checkcombobox(index, value, op):
    print(test2)
    


n.trace('w', checkcombobox)
cmb = ttk.Combobox(frm,textvariable=n, values=['Premier League','Liga','Ligue 1','Serie A','Liga Nos'],justify='center',).grid(column=2, row=0)
print(cmb)
test2 = n.get()










root.mainloop()