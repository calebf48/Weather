import requests
from tkinter import *
import json
from datetime import datetime

#Initialize tkinter window
root = Tk()
root.geometry("400x400") #Size of window by default
root.resizable(0,0) #Fixed window size
root.title("Weather App") #Title of window

city_value = StringVar()

def showWeather(): 
#Openweathermap API key
    api_key = '6b08f1018c3408c190f43c0e50e025c9'

    city_name = city_value.get()

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    response = requests.get(url)

    data = response.json()

    tfield.delete("1.0", "end") #to clear the text field for every new output

    if response.status_code == 200:
        temp = round((data['main']['temp'] - 273.15) * 1.8 + 32)
        feels_like_temp = round((data['main']['feels_like'] - 273.15) * 1.8 + 32)
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed'] * 3.6
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        timezone = data['timezone']
        cloudy = data['clouds']['all']
        desc = data['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        weather = f"\nCurrent weather in {city_name}:\nTemperature (Farenheit): {temp}°\nFeels like (Farenheit): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {desc}"
    else: 
        weather = f"\n\tWeather for '{city_name}' not found!\n\tPlease enter a valid city name."

    tfield.insert(INSERT, weather) #Send value in text field to display output

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

city_head = Label(root, text = 'Enter city name', font = 'Arial 12 bold').pack(pady = 10) #Generate label heading
inp_city = Entry(root, textvariable = city_value, width = 24, font = 'Arial 14 bold').pack() #Entry field

Button(root, command = showWeather, text = "Get weather", font = "Arial 10", bg = 'lightblue', fg = 'black', activebackground = "teal", padx = 5, pady = 5).pack(pady = 20)

weather_now = Label(root, text = "Current weather: ", font = 'Arial 12 bold').pack(pady = 10)

tfield = Text(root, width = 46, height = 10)
tfield.pack()

root.mainloop()