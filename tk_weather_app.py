from tkinter import *
from tkinter import messagebox
from datetime import datetime
import requests
import time
import os

api=os.environ.get("api")
root=Tk()
root.geometry("400x450")
root.configure(bg="#b2cfca")
entry=Entry(root,width=20,bg="white",font=("Verdana",15),fg="blue",borderwidth=5,justify = CENTER)
entry.pack(pady=80)
label = Label(root, text=" ", font=("Verdana", 15), fg="gray",bg="#b2cfca")
label_2=Label(root,text=" ",font=("Verdana",15),bg="#b2cfca")

# create timer for app
def timer():
    new_time = time.strftime("%H:%M:%S")
    label_2.config(text=new_time,fg="red")
    label_2.after(1000,timer)
timer()

def delete(): # delete something in entry widget
    entry.delete(0,END)

# get api request
def info_get():
     try:
        city=entry.get()
        req = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
        req_json=requests.get(req).json()
        #convert unix timestamp to datetime
        def unix_format(unix):
            value = datetime.fromtimestamp(unix)
            current_time = f"{value:%H:%M:%S}"
            return current_time
        sunrise = req_json["sys"]["sunrise"] #unix time
        sunset = req_json["sys"]["sunset"]  # unix time
        temp = req_json["main"]["temp"]
        weather_main = req_json["weather"][0]["main"]
        weather_desc = req_json["weather"][0]["description"]
        info_all=f"{city.upper() }\n\nSunrise \t{unix_format(sunrise)}" + f"\nSunset \t{unix_format(sunset)}\n" \
            f"Temp :\t{temp} C \n{weather_main} / {weather_desc}\n"
        label.config(text=info_all,justify="left",pady=15)
     except Exception:
        messagebox.showinfo("Information","Please write correct country name") # shows info if input incorrect city
# show message when exit app
def confirm():
    answer = messagebox.askyesno(title='confirmation',message='Are you sure you want to exit ?')
    if answer:
        root.destroy()
def main():
    exit=Button(root,text="Exit",command=confirm,width=8)
    clear=Button(root,text="Clear",command=delete,width=8)
    search=Button(root,text="Search",command=info_get,width=8)
    label_3=Label(root,text="Weather App",font=("Verdana",15),bg="#b2cfca")
    label_3.place(x=100,y=20)
    label_2.place(x=250,y=20)
    exit.place(x=70,y=130)
    clear.place(x=150,y=130)
    search.place(x=230,y=130)
    label.place(x=50,y=220)
    root.mainloop()

if __name__=="__main__":
    main()







