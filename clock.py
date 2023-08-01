from tkinter import *
import time

def digital():
    d=time.strftime("%H:%M:%S:%p")
    clock.config(text=d)
    clock.after(200,digital)

root=Tk()
root.title("Sudharshan's Digital Clock")
clock=Label(root,font=("Liquid Crystal",100,"bold"))
clock.grid(row=2,column=1)
digital()
root.mainloop()
