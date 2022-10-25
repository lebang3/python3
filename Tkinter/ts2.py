import tkinter

top = tkinter.Tk()

canvas = tkinter.Canvas(top, bg="blue", height=175, width=250)


coord = 10, 50, 240, 210
arc = canvas.create_arc(coord, start=0, extent=150, fill="red")
canvas.pack()
top.mainloop()