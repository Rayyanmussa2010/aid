# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:24:48 2021

@author: DELL
"""
from tkinter import *

from tkinter import filedialog
from PIL import ImageTk, Image
root=Tk()
root.title("Walking on canvas using functions")
root.geometry("600x600")

label=Label(root, text="Enter your color")
label.place(relx=0.5, rely=0.9, anchor=CENTER)

input=Entry(root)
input.insert(0, "black")
input.place(relx=0.7, rely=0.9, anchor=CENTER)

canvas=Canvas(root, width=590, height=510, bg="white")
canvas.pack()
artist =ImageTk.PhotoImage(Image.open ("start_point1.png"))
myimage=canvas.create_image(50, 50, image=artist)

direction=""
oldx=50
oldy=50
newx=50
newy=50

def right_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx+5
    direction="right"
    draw(direction, oldx, oldy, newx, newy)

def left_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx-5
    direction="left"
    draw(direction, oldx, oldy, newx, newy)

def up_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newy=newy-5
    direction="up"
    draw(direction, oldx, oldy, newx, newy)

def down_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newy=newy+5
    direction="down"
    draw(direction, oldx, oldy, newx, newy)

def draw(direction, oldx, oldy, newx, newy):
    fill_color=input.get()
    if(direction=="right"):
        right_line=canvas.create_line(oldx, oldy, newx, newy, width=3, fill=fill_color)
    
    if(direction=="left"):
        right_line=canvas.create_line(oldx, oldy, newx, newy, width=3, fill=fill_color)
    
    if(direction=="up"):
        right_line=canvas.create_line(oldx, oldy, newx, newy, width=3, fill=fill_color)
    
    if(direction=="down"):
        right_line=canvas.create_line(oldx, oldy, newx, newy, width=3, fill=fill_color)


root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)


























root.mainloop()