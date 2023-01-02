from tkinter import *
from tkinter import ttk
import requests
from dotenv import dotenv_values
import datetime
import pandas as pd


root = Tk()
root.title('Football result app by Nassim Bouziane')
root.geometry('500x500')
scrollbar = Scrollbar(root,orient='vertical')


year = datetime.datetime.today().year - 1
lst_Years = list(range(year, year - 20, -1)) # Getting a list of year from todays year to 20years ago
print(lst_Years)

config = dotenv_values('.env')
print(config['API_KEY'])

frm = ttk.Frame(root, padding=0)
frm.grid()

# Define Leagues Tuple
Leagues= ('Premier League','Liga','Ligue 1','Serie A','Liga Nos')

# Function to print the index of selected option in Combobox
def callback(*arg):
   label['text'] = 'Result of '+var.get()

   

   #https://v3.football.api-sports.io/leagues to get leagues

   headers = {'x-rapidapi-key': config['API_KEY'] }
   #r = requests.get('https://v3.football.api-sports.io/standings?season='+varYears.get()+'&league=39',headers=headers)
   #print(r.json()['response'][0]['league']['standings'][0][0])
   #standing = r.json()['response'][0]['league']['standings'][0] # from standing retrieve rank, team name, ponts, goaldiff form, description played win draw lose
   test = []
   for i in range(20):
      #j = i + 1 a tester demain 
      # label2 = Label(frm,text=str(standing[i]['rank'])+' '+ standing[i]['team']['name'] +' ' + str(standing[i]['points']) + ' ' + str(standing[i]['goalsDiff'])  
      # + ' ' + standing[i]['form']+ ' ' + str(standing[i]['description'])+ ' ' + str(standing[i]['all']['played'])+ ' ' + str(standing[i]['all']['win'])
      # + ' ' + str(standing[i]['all']['draw'])+ ' ' + str(standing[i]['all']['lose']))
      # label2.pack()
      
      test.append('c\'est le '+str(i)+'eme label'+str(varYears.get())+'\n')


   labelStanding['text'] = "\n.".join(test)
   labelStanding['font'] = ('Times'),13
   labelStanding['borderwidth'] = '2'
   labelStanding['relief'] = 'solid'
   
         
      
   
   
# Create a combobox widget
var = StringVar() # the var we are tracing 
var.set('Premier League')

varYears = StringVar()
varYears.set(datetime.datetime.today().year - 1)

cb= ttk.Combobox(frm, textvariable= var)
cb['values']= Leagues
cb['state']= 'readonly'
cb.pack(fill='x',padx= 5, pady=5)

label = Label(frm, text='Result of '+var.get())
label.pack()

cbYear = ttk.Combobox(frm,textvariable=varYears)
cbYear['values'] = lst_Years
cbYear['state'] = 'readonly'
cbYear.pack(fill='x', padx='10',pady='5')

labelStanding = Label(frm)
labelStanding.pack( padx='50')


# Set the tracing for the given variable
var.trace('w', callback)
varYears.trace('w', callback)







root.mainloop()