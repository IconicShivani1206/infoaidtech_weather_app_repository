from timezonefinder import TimezoneFinder
import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
from geopy.geocoders import Nominatim
from datetime import *
import requests 
import pytz
from PIL import Image, ImageTk
from tkvideo import tkvideo
a=Tk()
a.title("Weather App")
a.geometry("1000x700")
my_label = Label(a)
my_label.pack()
player = tkvideo("bg vdo.mp4", my_label, loop = 1, size = (1000,300))
player.play()


print("Trigger kyu nahi ho raha hai?")


def getWeather():
    ct=entry.get()    
    geolocator=Nominatim(user_agent="geopapiExcercises")
    loc=geolocator.geocode(ct)
    obj=TimezoneFinder()
    loc = geolocator.geocode(ct)
    result = obj.timezone_at(lng=loc.longitude, lat=loc.latitude)
    print(result)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I: %M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT TIME")

    #weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+ct+"&appid=cbc36cfaaabff4e0790850395c1f66b8"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind= json_data['wind']['speed']

    
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    t.config(text=(temp,"°"))
     
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)

#Searchbox
si=PhotoImage(file="searchbox.png")
im=Label(image=si)
im.place(x=20,y=20)
entry =Entry(a,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
entry.place(x=50,y=40)
entry.focus()

icon=PhotoImage(file="s_icon.png")
ic=Button(image=icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
ic.place(x=400,y=34)

# #logo
Logo=PhotoImage(file="logo.png")
l=Label(image=Logo)
l.place(x=700,y=300)

# box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.place(x=5,y=300)

#Bottom
bot=PhotoImage(file="bottom.png")
l=Label(image=bot)
l.place(y=600)

#time
name=Label(a,font=("arial",15,"bold"))
name.place(x=30,y=550)
clock=Label(a,font=("Helvetica",20,"bold"))
clock.place(x=40,y=600)

l1=Label(a,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
l1.place(x=40,y=320)

l2=Label(a,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
l2.place(x=170,y=320)

l3=Label(a,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
l3.place(x=350,y=320)

l4=Label(a,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
l4.place(x=570,y=320)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=500)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=600)


w=Label(text="...",font=("arial",20,'bold'),bg="#1ab5ef")
w.place(x=40,y=350)

h=Label(text="...",font=("arial",20,'bold'),bg="#1ab5ef")
h.place(x=200,y=350)

d=Label(text="...",font=("arial",20,'bold'),bg="#1ab5ef")
d.place(x=370,y=350)

p=Label(text="...",font=("arial",20,'bold'),bg="#1ab5ef")
p.place(x=590,y=350)

a.mainloop()