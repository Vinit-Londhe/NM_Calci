from pathlib import Path
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sys


file_path = os.path.abspath(__file__)


output_path = os.path.dirname(file_path)


assets_path = Path(output_path) / "Required files/assetsEM/frame0"


def relative_to_assets(path: str) -> Path:
    return assets_path / Path(path)


def home():
    window.destroy()
    os.system('python mainframe.py')


def EM(func, x0, y0, xn, p):
    sys.stdout = open("result.txt", "w")

    def f(x, y):
        r = eval(func)
        return r

    def euler(x0, y0, xn, n):

        # Calculating step size
        h = (xn-x0)/n

        print('x0\ty0\tslope\tyn')
        print('------------------------------')
        for i in range(n):
            slope = f(x0, y0)
            yn = y0 + h * slope
            print('%.4f\t%.4f\t%0.4f\t%.4f' % (x0, y0, slope, yn))
            print('\n')
            y0 = yn
            x0 = x0+h

        print('\nAt x=%.4f, y=%.4f' % (xn, yn))

    # Inputs
    x0 = float(x0)
    y0 = float(y0)
    xn = float(xn)
    step = int(p)
    euler(x0, y0, xn, step)
    sys.stdout.close()
    os.system('python result.py')


def test():
    func = entry_1.get()
    x0 = float(entry_2.get())
    y0 = float(entry_3.get())
    xn = float(entry_5.get())
    n = int(entry_4.get())
    EM(func, x0, y0, xn, n)


window = Tk()

window.geometry("919x555+300+100")
window.configure(bg="#333131")
window.title('Eulars Method')


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
    555.0,
    29.0,
    anchor="nw",
    text="Enter Function f(x,y)",
    fill="#FFFFFF",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    599.0,
    350.0,
    anchor="nw",
    text="No. of steps",
    fill="#FFFFFF",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    599.0,
    240.0,
    anchor="nw",
    text="          Xn",
    fill="#FFFFFF",
    font=("Inter SemiBold", 24 * -1)
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
    x=577.0,
    y=467.0,
    width=175.0,
    height=47.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    671.0,
    91.5,
    image=entry_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=550.0,
    y=70.0,
    width=242.0,
    height=41.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=home,
    relief="flat",
    bg="#333131"
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
    228.0,
    277.0,
    image=image_image_1
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    577.0,
    212.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=545.0,
    y=190.0,
    width=64.0,
    height=43.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    669.0,
    300.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=637.0,
    y=278.0,
    width=64.0,
    height=43.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    669.0,
    410.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=637.0,
    y=388.0,
    width=64.0,
    height=43.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    758.0,
    212.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=726.0,
    y=190.0,
    width=64.0,
    height=43.0
)

canvas.create_text(
    562.0,
    153.0,
    anchor="nw",
    text="X0",
    fill="#FFFFFF",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    743.0,
    153.0,
    anchor="nw",
    text="Y0",
    fill="#FFFFFF",
    font=("Inter SemiBold", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
