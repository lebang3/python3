
from tkinter import*
from tkinter.ttk import*
from time import strftime

top = Tk()
top.title("clock")#tao ten

def clock():
    string=strftime('%H:%M:%S:%p')
    label.config(text=string)
    label.after(1000,clock)

label= Label(top , font= ("digital-7",100), background = "black", foreground="white")
label.pack(anchor='center')
clock()
top.mainloop()#tao vong lap (bat buoc)