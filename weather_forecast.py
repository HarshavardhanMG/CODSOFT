from tkinter import *
import requests
from datetime import datetime
import json

main=Tk()
main.geometry("350x370")
main.resizable(0,0)
main.title("Weather")

input_value=StringVar()
kelvin=273

def time_zone(time):
    local_time=datetime.utcfromtimestamp(time)
    return local_time.time()

def check_weather():
    api_key="2c332195ffef17d3a5ab043f6495f24a"
    input_data=input_value.get()
    weather="http://api.openweathermap.org/data/2.5/weather?q="+input_data+"&appid="+api_key
    reply=requests.get(weather)
    weather_info=reply.json()
    wo.delete("1.0", "end")

    if weather_info["cod"]==200:
        temperature=int(weather_info["main"]["temp"]-kelvin)
        feels_like_temperature=int(weather_info["main"]["feels_like"]-kelvin)
        humidity=weather_info["main"]["humidity"]
        pressure=weather_info["main"]["pressure"]
        cloudy=weather_info["clouds"]["all"]
        description=weather_info["weather"][0]["description"]
        wind_speed=weather_info["wind"]["speed"]*3.6
        sunrise=weather_info["sys"]["sunrise"]
        sunset=weather_info["sys"]["sunset"]
        timezone=weather_info["timezone"]
        sunrise_time=time_zone(sunrise+timezone)
        sunset_time=time_zone(sunset+timezone)

        weather=f"\n Weather at : {input_data}\n Temperature : {temperature}°C\n Feels like : {feels_like_temperature}°C\n Humidity : {humidity}%\n Pressure : {pressure} hPa\n Clouds : {cloudy}%\n Wind Speed : {wind_speed} KPH\n Sunrise : {sunrise_time} AM\n Sunset : {sunset_time} PM\n Timezone : {timezone}\n\n {description}"
    else:
        weather=f" Weather for {input_data} not found!\n Kindly check the name or pincode."

    wo.insert(INSERT, weather)

ht=Label(main, text="Enter the City Name or Pin Code", font="arial 12 bold")
ht.pack(padx=10, pady=10)
ci=Entry(main, width=20, font="arial 15 bold italic", bd=2, relief="sunken", justify="center", textvariable=input_value)
ci.pack()
cw=Button(main, text="Show Weather", font="arial 10 bold", bd=3, relief="raised", background="#89CFF0", activebackground="#5072A7", command=check_weather)
cw.pack(pady=12)
wo=Text(main, width=41, height=14, bd=2, relief="solid")
wo.pack()

main.mainloop()