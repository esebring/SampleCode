import time, pyodbc, csv, numpy as np, pandas as pd, requests, smtplib, matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from io import BytesIO
#Labeling the tkinter variable
master = tk.Tk()

#Creating a title for the window - shown in the white space @ the top of the window
master.title("Game of Thrones!")

#All the necessary attributes to the window are stored at the top of the script, then functions are listed, and then buttons/labels/etc are stored to ensure the functions are defined before the function is called.


#column/row configure w/ weight=1 will allow tkinter to auto adjust according to the window size
master.grid_columnconfigure(0,weight=1)
master.grid_columnconfigure(1,weight=1)
master.grid_columnconfigure(2,weight=1)
master.grid_rowconfigure(0,weight=1)
master.grid_rowconfigure(1,weight=1)


#The following function is to be used as a pop up window in case of an error
def Error1():
    master = tk.Tk()

    master.title("Oops, something went wrong!")

    tk.Label(master,
             text="Oops, something went wrong! Please confirm the email is correct.").grid(row=0, column=0,columnspan=4,pady=0)

    tk.mainloop()

#The following function is to be used as a pop up window in case of an error
def Error2():
    master = tk.Tk()

    master.title("Oops, something went wrong!")

    tk.Label(master,
             text="Oops, something went wrong! The source data appears to have changed or there is no internet connection. Please try again later").grid(row=0, column=0,columnspan=4,pady=0)

    tk.mainloop()

#Defining the function of the button
def WinPercentage():

    #Data is gathered from a Github CSV file - normally a SQL query would be in place of this
    url = 'https://raw.githubusercontent.com/chrisalbon/war_of_the_five_kings_dataset/master/5kings_battles_v1.csv'

    df = pd.read_csv(url, error_bad_lines=False)

    #Changing strings into values for ease of calculations
    df = df.replace(to_replace ="win",
                 value =1)
    df = df.replace(to_replace ="loss",
                 value =0)
    #getting the input from the selection made on the master window
    king = variable.get()

    #quering for the selection
    KingInfo = df.query(f'attacker_king == "{king}"')

    Tab1 = pd.DataFrame(KingInfo, columns=['attacker_king','attacker_outcome'])
    #calculating win percentage and visualing the result
    winpercentage = Tab1['attacker_outcome'].mean()
    losspercentage = 1 - winpercentage
    breakdown = [winpercentage, losspercentage]
    labels = ['Win','Loss']
    plt.pie(breakdown,
        startangle=90,
        shadow= True,
        autopct='%1.1f%%')
    plt.legend(labels, loc='best')
    plt.title(f'Win Percentage for {king}')


    #Now, we will be reviewing if the user wants to receive a confirmation email and sends one if so.
    SendEmail = var1.get()
    Email = e1.get()
    if Email == "" and SendEmail== 1:
        Error1()
    if SendEmail == 1:
        gmail_user = 'ericsebringtestcode@gmail.com'
        gmail_password = 'Mac12345^'

        sent_from = gmail_user
        to = [f'{Email}']
        subject = 'Confirmation'
        body = 'Hello, this is your confirmation email.'

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()

        except:
            Error1()


    plt.show()

#Defining the function of the button
def WarFreq():
    url = 'https://raw.githubusercontent.com/chrisalbon/war_of_the_five_kings_dataset/master/5kings_battles_v1.csv'

    df = pd.read_csv(url, error_bad_lines=False)

    Freq = df['year']

    #configuing the chart
    plt.hist(Freq, bins=5, color='g', linewidth = 1, label='Number of Wars per Year')
    plt.title('Number of wars per year')
    plt.xticks(np.arange(298, 301, 1))
    plt.xlabel('Year')
    plt.ylabel('# of Wars')

    #Now, we will be reviewing if the user wants to receive a confirmation email and sends one if so. If no email is added, but the checkbox is selected, there will be an error message
    SendEmail = var1.get()
    Email = e1.get()
    if Email == "" and SendEmail== 1:
        Error1()
    if SendEmail == 1:
        gmail_user = 'ericsebringtestcode@gmail.com'
        gmail_password = 'Mac12345^'

        sent_from = gmail_user
        to = [f'{Email}']
        subject = 'Confirmation'
        body = 'Hello, this is your confirmation email.'

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()

        except:
            Error1()

    plt.show()

#Defining the function of the button
def MostWars():
    url = 'https://raw.githubusercontent.com/chrisalbon/war_of_the_five_kings_dataset/master/5kings_battles_v1.csv'

    df = pd.read_csv(url, error_bad_lines=False)

    df1 = df.groupby('region')['battle_number'].nunique()

    df1.plot(kind='pie',autopct='%.2f')
    plt.ylabel('')
    plt.legend(loc="best")
    plt.title(f'Breakdown of most war affected areas')


    #Now, we will be reviewing if the user wants to receive a confirmation email and sends one if so. We also confirm that the field is not blank before trying to send the email
    SendEmail = var1.get()
    Email = e1.get()
    if Email == "" and SendEmail== 1:
        Error1()
    if SendEmail == 1:
        gmail_user = 'ericsebringtestcode@gmail.com'
        gmail_password = 'Mac12345^'

        sent_from = gmail_user
        to = [f'{Email}']
        subject = 'Confirmation'
        body = 'Hello, this is your confirmation email.'

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()

        except:
            Error1()

    plt.show()


#Now we will format the window so it is visually appealing.
tk.Label(master,
         text="Hello! And welcome to Eric Sebring's sample project.\n Please enter your email in the box below and check the box \n to ensure a confirmation email is sent. There are three reports \n that can be generated by the buttons below. \n **The drop down list is only required to be selected for the report 'View Win Percentages by King' ").grid(row=1, column=0, columnspan=5, rowspan=2,pady=0)


tk.Label(master,
         text="Email:").grid(row=8, column=1,pady=0)
var1 = IntVar()
Checkbutton(master, text="Click here to be emailed a confirmation of the report!", variable=var1,borderwidth=0,highlightthickness=0).grid(row=9,column=0,sticky=W,pady=0) #var1.get() = 1 if checked

e1 = tk.Entry(master)
e1.grid(row=9, column=1,pady=0)
#optiosn for checkbox
OPTIONS = ['Joffrey/Tommen Baratheon','Robb Stark','Balon/Euron Greyjoy','Stannis Baratheon']


#checkbox
variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS).grid(row=7,
                          column=0,
                          sticky=E,
                          pady=0)
tk.Button(master,
          text='View Win Percentages by King', command=WinPercentage).grid(row=7,
                                                       column=1,
                                                       sticky=tk.E,
                                                       pady=0)

tk.Button(master,
          text='Frequency of Wars per Year', command=WarFreq).grid(row=6,
                                                       column=1,
                                                       sticky=tk.E,
                                                       pady=0)
tk.Button(master,
          text='Highest War Prone Areas', command=MostWars).grid(row=5,
                                                       column=1,
                                                       sticky=tk.E,
                                                       pady=0)

#An image is used from the internet
img_url = "http://pluspng.com/img-png/game-of-thrones-logo-png-download-game-of-thrones-logo-png-images-transparent-gallery-advertisement-advertisement-400.png"
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

panel = tk.Label(master, image=img).grid(row=0,
                          column=0,
                          pady=0, columnspan=5)


tk.mainloop()

