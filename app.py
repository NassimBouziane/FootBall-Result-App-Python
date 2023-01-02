from tkinter import *
from tkinter import ttk
import requests
from dotenv import dotenv_values
import datetime

root = Tk()
root.title('Football result app by Nassim Bouziane')
root.geometry('500x500')

year = datetime.datetime.today().year
lst_Years = list(range(year, year - 20, -1)) # Getting a list of year from todays year to 20years ago

config = dotenv_values('.env')
print(config['API_KEY'])

frm = ttk.Frame(root, padding=0)
frm.grid()

# Define Leagues Tuple
Leagues= ('Premier League','Liga','Ligue 1','Serie A','Liga Nos')

# Function to print the index of selected option in Combobox
def callback(*arg):
   print(var.get())
   label['text'] = 'Result of '+var.get()

   #39 PL
   #https://v3.football.api-sports.io/leagues to get leagues
   #r = requests.get('https://api.sofascore.com/api/v1/unique-tournament/17/featured-events')
   #print(r.json())
   r = requests.get()
   
# Create a combobox widget
var = StringVar() # the var we are tracing 
var.set('Premier League')

varYears = StringVar()
varYears.set('2023')

cb= ttk.Combobox(frm, textvariable= var)
cb['values']= Leagues
cb['state']= 'readonly'
cb.pack(fill='x',padx= 5, pady=5)

label = Label(frm,text='Result of '+var.get())
label.pack()

cbYear = ttk.Combobox(frm,textvariable=varYears)
cbYear['values'] = lst_Years
cbYear['state'] = 'readonly'
cbYear.pack(fill='x', padx='10',pady='5')



# Set the tracing for the given variable
var.trace('w', callback)









root.mainloop()