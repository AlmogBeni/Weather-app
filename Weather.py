# Importing the good stuff.
from tkinter import *
import requests
import json
from datetime import datetime
 
# . Initializing the screen display.
root =Tk()
root.geometry("400x400") #size of the window by default
root.resizable(0,0) #to make the window size fixed
#title of our window
root.title("Weather App")
 
# - Functions to fetch and display weather info
city_value = StringVar()
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

city_value = StringVar()
 
def showWeather():
# ! Entering the api key to integrate the website with the program.
    api_key = "4b09cfd51d84596a0a3856fa259ecdb9"
 
    # Get city name from user from the input field (later in the code)
    city_name=city_value.get()
 
    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    # Get the response from fetched url
    response = requests.get(weather_url)
 
    # changing response from json to python readable 
    weather_info = response.json()
    tfield.delete("1.0", "end")
 
# .As per API documentation, if the cod is 200, it means that weather data was successfully fetched
    if weather_info['cod'] == 200:
        kelvin = 273
 
# - Storing the fetched values of weather of a city
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
 
# * Assigning values to our weather varaible, to display as output
         
        weather = f"\nWeather of: {city_name}\ntemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly enter valid city name."

    tfield.insert(INSERT, weather)
  
# : Front-end part (UI) 
city_head= Label(root, text = 'Enter City Name', font = 'Georgia 10 bold').pack(pady=10)
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Georgia 10 bold').pack() 
Button(root, command = showWeather, text = "Check Weather", font="Georgia 10 bold", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
weather_now = Label(root, text = "The Weather is:", font = 'Georgia 12 bold').pack(pady=10)
tfield = Text(root, width=46, height=10)
tfield.pack()
Label(root,text ="Made By - Almog Beni", font = 'Georgia 10 bold', width = '20').pack(side = 'bottom')

# / Running main program. 
root.mainloop()