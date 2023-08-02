
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from tkinter import ttk
from io import StringIO
import os
from pathlib import Path

# Get the absolute path to the current file
file_path = os.path.abspath(__file__)

# Get the directory containing the current file
output_path = os.path.dirname(file_path)

# Set the assets path to the "assets/frame0" directory inside the output path
assets_path = Path(output_path) / "Required files/assets/frame0"


def relative_to_assets(path: str) -> Path:
    return assets_path / Path(path)


def callbisection():
    window.destroy()
    os.system('python BS.py')


def callRF():
    window.destroy()
    os.system('python RF.py')


def callnp():
    window.destroy()
    os.system('python np.py')


def callji():
    window.destroy()
    os.system('python JI.py')


def callGS():
    window.destroy()
    os.system('python GS.py')


def callem():
    window.destroy()
    os.system('python em.py')


window = Tk()

window.geometry("992x662+500+200")
window.configure(bg="#020000")
window.title('Home')


canvas = Canvas(
    window,
    bg="#020000",
    height=662,
    width=992,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"), )
image_1 = canvas.create_image(
    160,
    200,

    image=image_image_1,

)


image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    500.0,
    128.0,

    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=callRF,
    relief="flat"
)
button_1.place(
    x=399.0,
    y=250.0,
    width=179.0,
    height=76.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=callnp,
    relief="flat"
)
button_2.place(
    x=698.0,
    y=250.0,
    width=179.0,
    height=76.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=callem,
    relief="flat"
)
button_3.place(
    x=698.0,
    y=486.0,
    width=179.0,
    height=76.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=callGS,
    relief="flat"
)
button_4.place(
    x=399.0,
    y=486.0,
    width=179.0,
    height=76.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=callji,
    relief="flat"
)
button_5.place(
    x=104.0,
    y=486.0,
    width=179.0,
    height=76.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=callbisection,
    relief="flat"
)
button_6.place(
    x=104.0,
    y=250.0,
    width=179.0,
    height=76.0
)
window.resizable(False, False)
window.mainloop()
