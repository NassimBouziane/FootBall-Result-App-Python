from tkinter import *
from tkinter import ttk
import requests
from dotenv import dotenv_values
import datetime


root = Tk()
root.title('Football result app by Nassim Bouziane')
root.geometry('500x500')



year = datetime.datetime.today().year - 1
lst_Years = list(range(year, year - 13, -1)) # Getting a list of year from todays year to 13years ago


config = dotenv_values('.env') # getting api key from .env


frm = ttk.Frame(root, padding=0)
frm.pack()

# Define Leagues Tuple
Leagues= ('Premier League','Liga','Ligue 1','Serie A','Liga Nos')

# Function to print the index of selected option in Combobox
def callback(*arg):
   label['text'] = 'Result of '+var.get() 

   #https://v3.football.api-sports.io/leagues to get leagues
   league = 0
   if var.get() == 'Premier League':
    league = 39
   elif var.get() == 'Liga':
        league = 140
   elif var.get() == 'Ligue 1':
        league = 61
   elif var.get() == 'Liga Nos':
        league = 94
   elif var.get() == 'Serie A':
        league = 135

   if league == 94:
    if(int(varYears.get()) >= 2014):
        len = 18
    elif int(varYears.get()) < 2014:
        len = 16
   elif league != 94:
    len = 20               

   headers = {'x-rapidapi-key': config['API_KEY'] }
   r = requests.get('https://v3.football.api-sports.io/standings?season='+varYears.get()+'&league='+str(league),headers=headers)
   standing = r.json()['response'][0]['league']['standings'][0] # from standing retrieve rank, team name, ponts, goaldiff form, description played win draw lose
   list = []

   for i in range(len):
      list.append(str(standing[i]['rank'])+' '+ standing[i]['team']['name'] +' ' + str(standing[i]['points']) + ' ' + str(standing[i]['goalsDiff'])  
      + ' ' + standing[i]['form']+ ' ' + str(standing[i]['description'])+ ' ' + str(standing[i]['all']['played'])+ ' ' + str(standing[i]['all']['win'])
      + ' ' + str(standing[i]['all']['draw'])+ ' ' + str(standing[i]['all']['lose']))


   labelStanding['text'] = "\n.".join(list)
   labelStanding['font'] = ('Times'),13
   labelStanding['borderwidth'] = '2'
   labelStanding['relief'] = 'solid'
   labelStanding['justify'] ='left'
   
#Canvas :   
canvas = Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set,borderwidth=0,highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


   
   
# Create a combobox widget
var = StringVar() # the var we are tracing 
var.set('Premier League')

varYears = StringVar()
varYears.set(datetime.datetime.today().year - 1)

cb= ttk.Combobox(scrollable_frame, textvariable= var)
cb['values']= Leagues
cb['state']= 'readonly'
cb.pack(fill='x',padx= 5, pady=5)

label = Label(scrollable_frame, text='Result of '+var.get())
label.pack()

cbYear = ttk.Combobox(scrollable_frame,textvariable=varYears)
cbYear['values'] = lst_Years
cbYear['state'] = 'readonly'
cbYear.pack(fill='x', padx='10',pady='5')

labelStanding = Label(scrollable_frame)
labelStanding.pack()


# Set the tracing for the given variable
var.trace('w', callback)
varYears.trace('w', callback)




root.mainloop()