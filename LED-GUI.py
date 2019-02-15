#Imports
import serial
import os
import gc
from tkinter import *
from colormap import rgb2hex
#to work properly on python 3
#pip install easydev pyserial colormap
#Varibles
COMPort = 'COM1'
window = Tk()
red = IntVar()
blue = IntVar()
green = IntVar()
canvas = Canvas(height=50, width=50)
color = rgb2hex(red.get(), green.get(), blue.get())
#ser = serial.Serial(COMPort, 9600, timeout=0)


#update the color displayed in the box
def update():
    color = rgb2hex(red.get(), green.get(), blue.get())
    #print(color)
    Canvas(height=50, width=50)
    canvas.create_rectangle(0,0,50,50,fill=color)
    canvas.place(x=20, y=25)
    window.after(10, update)
    
def sendData():
    data = rgb2hex(red.get(),green.get(),blue.get())
    print ("Hex Color:", data)
    print("RBG color:(",red.get(),green.get(),blue.get(),")")
    '''
    for x in range (1):
        recieved = ser.read()
        print("Recieved:", recieved.decode('utf8'))
    '''
def listen():
    window.after(500, listen)

def clearTerm():
    os.system('cls')
    gc.collect()
    window.after(1000, clearTerm)

#Frame
window.title("RGB LED Controller")
window.geometry('375x170')



#Red
Scale(window, orient='horizontal',troughcolor="#ff0000", from_=0, to=255, length=200, width=20, variable=red).pack()
#Green
Scale(orient='horizontal',troughcolor="#00ff00" , from_=0, to=255, length=200, width=20, variable=green).pack()
#Blue
Scale(orient='horizontal',troughcolor="#0000ff" , from_=0, to=255, length=200, width=20, variable=blue).pack()
#button
btn = Button(window, text="Print", command=sendData)
btn.place(x=27, y=80)
#current color

#clearTerm()
update()
#listen()
window.mainloop()