import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from tkinter import ttk
from io import StringIO
import os
from pathlib import Path
from sympy import *
from sympy import symbols, parse_expr, diff
import sys
# Get the absolute path to the current file
file_path = os.path.abspath(__file__)

# Get the directory containing the current file
output_path = os.path.dirname(file_path)

# Set the assets path to the "assets/frame0" directory inside the output path
assets_path = Path(output_path) / "Required files/assetsnp/frame0"


def relative_to_assets(path: str) -> Path:
    return assets_path / Path(path)


def NP(func, x0, t, n):
    sys.stdout = open("result.txt", "w")

    def newton_raphson(func, x0, e, N):

        # Define the function and its derivative
        x = symbols('x')
        f = parse_expr(func)
        df = f.diff(x)

        # Print the table header
        print("Iteration\tx\t\tf(x)")
        print(" " * 25)

        # Iteratively improve the estimate of the root
        for i in range(1, N+1):
            x1 = x0 - f.evalf(subs={x: x0}) / df.evalf(subs={x: x0})

            # Print the current iteration
            print("%d\t%f\t\t%f" % (i, x1, f.evalf(subs={x: x1})))

            # Check if the tolerance has been reached
            if abs(f.evalf(subs={x: x1})) < e:
                print("\nRoot found with tolerance %e: %f" % (e, x1))
                return x1

            # Update the current estimate
            x0 = x1

        # If the maximum number of iterations is reached, print a warning message
        print("\nWarning: maximum number of iterations (%d) reached without finding a root with tolerance %e" % (N, e))

    # Test the function with the function x**2 - 3, initial guess 1, tolerance 1e-8, and maximum number of iterations 10
    newton_raphson(func, x0, t, n)
    sys.stdout.close()
    window.destroy()
    os.system('python result.py')


def test():
    f = entry_4.get()
    x0 = float(entry_2.get())
    ns = int(entry_3.get())
    t = float(entry_1.get())
    NP(f, x0, t, ns)


def home():
    window.destroy()
    os.system('python mainframe.py')


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
    578.0,
    29.0,
    anchor="nw",
    text="Enter Function",
    fill="#FFFFFF",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    649.0,
    141.0,
    anchor="nw",
    text="X0",
    fill="#FFFFFF",
    font=("Inter SemiBold", 26 * -1)
)

canvas.create_text(
    589.0,
    363.0,
    anchor="nw",
    text="Tolerable Error",
    fill="#FFFFFF",
    font=("Inter SemiBold", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    674.5,
    418.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=583.0,
    y=396.0,
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
    663.0,
    193.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=638.0,
    y=172.0,
    width=50.0,
    height=41.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    663.0,
    312.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=638.0,
    y=291.0,
    width=50.0,
    height=41.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    663.0,
    94.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=542.0,
    y=71.0,
    width=242.0,
    height=45.0
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
    214.0,
    277.0,
    image=image_image_1
)

canvas.create_text(
    589.0,
    255.0,
    anchor="nw",
    text="No. of steps",
    fill="#FFFFFF",
    font=("Inter SemiBold", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
