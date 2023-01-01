from tkinter import *
from tkinter import ttk
import requests
root = Tk()
root.title('Football result app by Nassim Bouziane')
root.geometry('500x500')

frm = ttk.Frame(root, padding=0)
frm.grid()

# Define Leagues Tuple
Leagues= ('Premier League','Liga','Ligue 1','Serie A','Liga Nos')

# Function to print the index of selected option in Combobox
def callback(*arg):
   print(var.get())
   #https://api.sofascore.com/api/v1/unique-tournament/17/featured-events links for non-ended matchs
   #https://api.sofascore.com/api/v1/unique-tournament/17/season/41886/standings/total links for standings
   r = requests.get('https://api.sofascore.com/api/v1/unique-tournament/17/featured-events')
   print(r.json())
   
# Create a combobox widget
var= StringVar() # the var we are tracing 
cb= ttk.Combobox(frm, textvariable= var)
cb['values']= Leagues
cb['state']= 'readonly'
cb.pack(fill='x',padx= 5, pady=5)

# Set the tracing for the given variable
var.trace('w', callback)









root.mainloop()