
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import os

from pathlib import Path
from tkinter import Scrollbar
from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

file_path = os.path.abspath(__file__)


output_path = os.path.dirname(file_path)


assets_path = Path(output_path) / "Required files/assetsR/frame0"


def relative_to_assets(path: str) -> Path:
    return assets_path / Path(path)


def home():
    window.destroy()
    os.system('python mainframe.py')


window = Tk()

window.geometry("919x555+300+100")
window.configure(bg="#333111")
window.title('Result')


canvas = Canvas(
    window,
    bg="#333131",
    height=555,
    width=919,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=home,
    relief="flat",
    bg="#333131"
)
button_1.place(
    x=14.0,
    y=17.0,
    width=43.0,
    height=34.0,

)

canvas.create_text(
    426.0,
    17.0,
    anchor="nw",
    text="Result",
    fill="#69C04B",
    font=("Inter Bold", 28 * -1),

)

kkh = h ok
