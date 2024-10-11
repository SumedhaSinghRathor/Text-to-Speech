import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text to Speech")
root.geometry("900x450+100+100")
root.resizable(False, False)
root.configure(bg="#8ACE00")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    
    voices = engine.getProperty('voices')

    def setVoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if (speed == 'Fast'):
            engine.setProperty('rate', 250)
            setVoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setVoice()
        else:
            engine.setProperty('rate', 60)
            setVoice()

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    
    voices = engine.getProperty('voices')

    def setVoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if (text):
        if (speed == 'Fast'):
            engine.setProperty('rate', 250)
            setVoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setVoice()
        else:
            engine.setProperty('rate', 60)
            setVoice()

#icon
image_icon = PhotoImage(file="Asset 1.png")
root.iconphoto(False, image_icon)

#TopFrame
Top_frame = Frame(root, bg="white", width = 900, height = 100)
Top_frame.place(x = 0, y = 0)

Logo = PhotoImage(file = "mic.png")
Label(Top_frame, image = Logo, bg = "white").place(x = 10, y = 5)

Label(Top_frame, text = "TEXT TO SPEECH", font = "arial 20 bold", bg = "white", fg = "black").place(x = 100, y = 30)


text_area = Text(root, font = "Roboto 20", bg = "white", relief = GROOVE, wrap = WORD)
text_area.place(x = 10, y = 110, width = 500, height = 250)

Label(root, text = "VOICE", font = "arial 15 bold", bg = "#8ACE00", fg = "black").place(x = 580, y = 140)
Label(root, text = "SPEED", font = "arial 15 bold", bg = "#8ACE00", fg = "black").place(x = 760, y = 140)

gender_combobox = Combobox(root, values = ['Male', 'Female'], font = "arial 14", state = 'r', width = 10)
gender_combobox.place(x = 550, y = 180)
gender_combobox.set('Female')

speed_combobox = Combobox(root, values = ['Fast', 'Normal', 'Slow'], font = "arial 14", state = 'r', width = 10)
speed_combobox.place(x = 730, y = 180)
speed_combobox.set('Normal')

btn = Button(root, text = "Speak", font = "arial 14 bold", width = 10, command = speaknow)
btn.place(x = 550, y = 250)

save = Button(root, text = "Save", font = "arial 14 bold", width = 10, command = download)
save.place(x = 730, y = 250)


root.mainloop()
