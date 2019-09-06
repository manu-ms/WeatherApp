""" 
This is an app for getting current weather. 
Created on Mon Aug 19 15:53:15 2019.
Author: Manu M. S 
**************************************************
Python version required: Python 3.0
Module documentation:
    Required Modules:
        * tkinter
        * requests
        * time

"""

import tkinter as tk
import time
from tkinter import font
import requests
root= tk.Tk()
root.title('Manu Weather App')
root.geometry("440x440")
root.resizable(width=False, height=False)


def get_weather(city):
    proxies = {
      'http': '',
      'https': '',
    }  
    app_key = '517ce200b93aa5d81c4c6076acd6ce99'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params= {'APPID':app_key, 'q':city, 'units':'metric'}
    response= requests.get(url, params=params, proxies=proxies)
    weather = response.json()
    label['text']= format_response(weather)
    
def format_response(weather):
    try:
        city= weather['name']
        country= weather['sys']['country']
        description= weather['weather'][0]['description']
        description =description.capitalize()
        temp= weather['main']['temp']
        humidity= weather['main']['humidity']
        mi_temp= weather['main']['temp_min']
        ma_temp= weather['main']['temp_max']
        wind_speed = weather['wind']['speed']
        timeprint = time.strftime('%H:%M:%S')
        final_output = 'City: %s \nCountry: %s \nDescription: %s \nTemperature: %s°С \nHumidity: %s \nMinimum Temperature: %s°С \nMaximum Temperature: %s°С \nWind speed: %sm/s \nTime: %s' % (city, country, description, temp, humidity, mi_temp, ma_temp, wind_speed, timeprint)
    except:
        final_output= 'Problem while accuring data.\nPlease check your entry and try again...'
    return final_output
    

#main_window <Start>
canvas=tk.Canvas(root, height=440, width=440)
canvas.pack()
#backgroung image
bg_image = tk.PhotoImage(file='data/bgimg.png')
bg_label = tk.Label(canvas, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
#main_window <End>

#input frame <Start>
#input frame defenition <start>
input_frame= tk.Frame(canvas,bg= '#fee2f3', bd=5)
input_frame.place(relx=0.5, rely=0.05,relwidth=0.9, relheight=0.1, anchor='n')

#Entry behaviour functions <Start>
def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if entry.get() == 'Enter your location (City, Country)':
       entry.delete(0, "end") # delete all the text in the entry
       entry.insert(0, '') #Insert blank for user input
       entry.config(fg = 'black')
def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Enter your location (City, Country)')
        entry.config(fg = 'grey')
#Entry behaviour functions <End>

#Entry in Entry frame
entry=tk.Entry(input_frame, font=('song ti', 11))
entry.insert(0, 'Enter your location (City, Country)')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.config(fg = 'grey')
entry.place(relx=0.01,rely=0.05,relwidth=0.65, relheight=0.9)

#Button in entry frame
button= tk.Button(input_frame, text="Get Weather",font=('song ti', 10), command=lambda: get_weather(entry.get()))
button.place(relx=0.67,rely=0.05, relwidth=0.32, relheight=0.9)

#input frame <End>

#output frame <Start>
#output frame defenition
output_frame= tk.Frame(canvas,bg= '#fee2f3', bd=10)
output_frame.place(relx=0.5, rely=0.2,relwidth=0.9, relheight=0.7, anchor='n')

#fill the frame with label function
label=tk.Label(output_frame, font=('song ti', 15), justify='left', bd=10, anchor='w')
label.place(relwidth=1, relheight=1)
#output frame <End>

root.mainloop()








