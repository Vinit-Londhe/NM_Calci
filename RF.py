

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
assets_path = Path(output_path) / "Required files/assetsRF/frame0"


def relative_to_assets(path: str) -> Path:
    return assets_path / Path(path)


def home():
    window.destroy()
    os.system('python mainframe.py')


def RF(func, x0, x1, e):
    sys.stdout = open("result.txt", "w")

    def f(x):
        f = eval(func)
        return f

    def falsePosition(x0, x1, e):
        step = 1
        print('\n\nFALSE POSITION METHOD IMPLEMENTATION')
        condition = True
        while condition:
            x2 = x0 - (x1-x0) * f(x0)/(f(x1) - f(x0))
            print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' %
                  (step, x2, f(x2)))

            if f(x0) * f(x2) < 0:
                x1 = x2
            else:
                x0 = x2

            step = step + 1
            condition = abs(f(x2)) > e

        print('\nRequired root is: %0.8f' % x2)

    x0 = float(x0)
    x1 = float(x1)
    e = float(e)

    if f(x0) * f(x1) > 0.0:
        print('Given guess values do not bracket the root.')
        print('Try Again with different guess values.')
    else:
        falsePosition(x0, x1, e)
    sys.stdout.close()
    window.destroy()
    os.system("python result.py")


def test():
    f = entry_4.get()
    a = float(entry_3.get())
    b = float(entry_2.get())
    t = float(entry_1.get())
    RF(f, a, b, t)


window = Tk()

window.geometry("919x555+300+100")
window.configure(bg="#333131")


canvas = Canvas(
    window,
    bg="#333131",
    height=555,
    width=919,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    591.0,
    53.0,
    anchor="nw",
    text="Enter Function",
    fill="#FFFFFF",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    565.0,
    206.0,
    anchor="nw",
    text="a",
    fill="#FFFFFF",
    font=("Inter SemiBold", 26 * -1)
)

canvas.create_text(
    764.0,
    207.0,
    anchor="nw",
    text="b",
    fill="#FFFFFF",
    font=("Inter SemiBold", 25 * -1)
)

canvas.create_text(
    589.0,
    335.0,
    anchor="nw",
    text="Tolerable Error",
    fill="#FFFFFF",
    font=("Inter SemiBold", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    675.5,
    402.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=584.0,
    y=380.0,
    width=183.0,
    height=42.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=test,
    relief="flat"
)
button_1.place(
    x=589.0,
    y=471.0,
    width=175.0,
    height=47.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    772.0,
    267.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=747.0,
    y=246.0,
    width=50.0,
    height=41.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    580.0,
    267.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=555.0,
    y=246.0,
    width=50.0,
    height=41.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    676.0,
    136.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=555.0,
    y=113.0,
    width=242.0,
    height=45.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    bg="#333131",
    command=home
)
button_2.place(
    x=865.0,
    y=12.0,
    width=43.0,
    height=34.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    230.0,
    288.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
