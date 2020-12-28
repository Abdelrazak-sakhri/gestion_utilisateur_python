#Import librairies
import tkinter
from tkinter import *
import webbrowser

#Screen
tuto = tkinter.Tk()
tuto.title("Initiation TKinter")
tuto.geometry("1280x620")
mainmenu = tkinter.Menu(tuto)

#Label
l1 = Label(text = "Tuto release beta", font="ARIAL", bg="yellow")
l1.pack(pady = 200)

#Def
def open():
    webbrowser.open_new("https://www.youtube.com/watch?v=8nYUFJIuIpg")

def exit():
    quit()

def textfunny():
    l1 = Label(text = "Tuto initiation Tkinter")
    l1.pack()

#Boutons
button1 = Button(text = "YouTube", command = (open))
button1.pack()

button2 = Button(text = "Exit", command = (exit))
button2.pack()

#Menu
first = tkinter.Menu(mainmenu)
first.add_radiobutton(label = "Click Me !", command= (textfunny))

#MainMenu
mainmenu.add_cascade(label = "Funny", menu = first)


