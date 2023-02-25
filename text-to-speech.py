import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

main = Tk()
main.title("Text To Speech")
main.geometry("900x450+200+200")
main.resizable(False, False)

# icon
image_icon = PhotoImage(file="speak.png")
main.iconphoto(False, image_icon)
main.configure(bg="#305065")

engine = pyttsx3.init()


def speak():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty("voices")

    def setvoice():
        if gender == "Male":
            engine.setProperty("voice", voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty("voice", voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty("rate", 250)
            setvoice()
        elif speed == "Normal":
            engine.setProperty("rate", 150)
            setvoice()
        else:
            engine.setProperty("rate", 60)
            setvoice()


def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty("voices")

    def setvoice():
        if gender == "Male":
            engine.setProperty("voice", voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, "text.mp3")
            engine.runAndWait()
        else:
            engine.setProperty("voice", voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, "text.mp3")
            engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty("rate", 250)
            setvoice()
        elif speed == "Normal":
            engine.setProperty("rate", 150)
            setvoice()
        else:
            engine.setProperty("rate", 60)
            setvoice()


# Top Frame
top_frame = Frame(main, bg="white", width=900, height=100)
top_frame.place(x=0, y=0)

Logo = PhotoImage(file="speaker-logo.png")
Label(top_frame, image=Logo, bg="white").place(x=20, y=20)

Label(
    top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg="black"
).place(x=100, y=30)

##

text_area = Text(main, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(main, text="VOICE", font="arial 15 bold", bg="#305065", fg="white").place(
    x=580, y=160
)

Label(main, text="SPEED", font="arial 15 bold", bg="#305065", fg="white").place(
    x=760, y=160
)

gender_combobox = Combobox(
    main, values=["Male", "Female"], font="arial 14", state="r", width=10
)
gender_combobox.place(x=550, y=200)
gender_combobox.set("Male")

speed_combobox = Combobox(
    main, values=["Fast", "Normal", "Slow"], font="arial 14", state="r", width=10
)
speed_combobox.place(x=730, y=200)
speed_combobox.set("Normal")

imageicon2 = PhotoImage(file="speak.png")
btn = Button(
    main,
    text=" Speak",
    compound=LEFT,
    image=image_icon,
    width=130,
    font="arial 14 bold",
    command=speak,
)
btn.place(x=550, y=280)

imageicon2 = PhotoImage(file="download.png")
save = Button(
    main,
    text=" Save",
    compound=LEFT,
    image=imageicon2,
    width=130,
    bg="#39c790",
    font="arial 14 bold",
    command=download,
)
save.place(x=730, y=280)

main.mainloop()
