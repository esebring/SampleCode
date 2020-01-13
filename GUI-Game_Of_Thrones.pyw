import time, pyodbc, csv, numpy as np, pandas as pd, datetime, os, getpass,  xlsxwriter, glob, requests, smtplib, matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from datetime import datetime
from io import BytesIO
#Labeling the tkinter variable
master = tk.Tk()

#Creating a title for the window - shown in the white space @ the top of the window
master.title("Game of Thrones!")

#All the necessary attributes to the window are stored at the top of the script, then functions are listed, and then buttons/labels/etc are stored to ensure the functions are defined before the function is called.

master.grid_columnconfigure(0,weight=1)
master.grid_columnconfigure(1,weight=1)
master.grid_columnconfigure(2,weight=1)
master.grid_rowconfigure(0,weight=1)
master.grid_rowconfigure(1,weight=1)

def Exception():
    master = tk.Tk()

    master.title("Oops, something went wrong!")

    tk.Label(master,
             text="Oops, something went wrong! Please review your inputs and try to run the query again.").grid(row=0, column=0,columnspan=4,pady=0)

    tk.mainloop()

def WinPercentage():


    url = 'https://raw.githubusercontent.com/chrisalbon/war_of_the_five_kings_dataset/master/5kings_battles_v1.csv'

    df = pd.read_csv(url, error_bad_lines=False)

    df = df.replace(to_replace ="win",
                 value =1)
    df = df.replace(to_replace ="loss",
                 value =0)

    king = variable.get()

    KingInfo = df.query(f'attacker_1 == "{king}"')

    Tab1 = pd.DataFrame(KingInfo, columns=['attacker_king','attacker_outcome'])

    wins = Tab1['attacker_outcome'].sum()
    total = Tab1['attacker_outcome'].count()

    winpercentage = wins / total
    losspercentage = 1 - (wins - total)
    breakdown = [winpercentage, losspercentage]

    plt.pie(breakdown,
        startangle=90,
        shadow= True,
        autopct='%1.1f%%')
    plt.show()


tk.Label(master,
         text="Email:").grid(row=1, column=0,pady=0)
var1 = IntVar()
Checkbutton(master, text="Click here to be emailed a confirmation of the report!", variable=var1,borderwidth=0,highlightthickness=0).grid(row=2,column=1,sticky=W,pady=0) #var1.get() = 1 if checked

e1 = tk.Entry(master)
e1.grid(row=2, column=0,pady=0)

OPTIONS = ['Lannister','Stark','Greyjoy','Bolton','Baratheon','Darry','Brotherhood without Banners','Frey','Free folk','Brave Companions','Bracken']


variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS).grid(row=3,
                          column=0,
                          sticky=E,
                          pady=0)
tk.Button(master,
          text='View Win Percentages by King', command=WinPercentage).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=0)


img_url = "http://pluspng.com/img-png/game-of-thrones-logo-png-download-game-of-thrones-logo-png-images-transparent-gallery-advertisement-advertisement-400.png"
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

panel = tk.Label(master, image=img).grid(row=0,
                          column=0,
                          pady=0, columnspan=5)


tk.mainloop()
