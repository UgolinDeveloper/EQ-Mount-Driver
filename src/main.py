# + ------------------------------------------------- + #
# | File    : main.py                                 | #
# | Author  : UgolinDeveloper / Matthieu              | #
# | Date    : 09/11/20                                | #
# + ------------------------------------------------- + #

# Import modules / files.
import tkinter
import tkinter.font as font
import turtle
import datetime

"""
TODO
> Console
> Catch error
> UTC
"""


###################################
#          WINDOWS PARAM          #
###################################


# Customize main window.
ROOT = tkinter.Tk()
ROOT.title('PILOTE DE MONTURE EQ')
ROOT.resizable(width=False, height=False)
ROOT.geometry('+15+15')
MAIN_WINDOW = tkinter.Canvas(
    master=ROOT, height=700, width=900)
MAIN_WINDOW.pack(side=tkinter.RIGHT, expand=1)


###################################
#           GLOBAL VARS           #
###################################


# Initialize global constants.
RADIUS = 200
TANGLE = [0, 0, 0]
CURSOR = turtle.RawTurtle(MAIN_WINDOW)
FONT_TEXT = font.Font(family="Helvetica", size=11)
CONSOLE_TEXT = font.Font(family="Helvetica", size=8)


###################################
#       GET / SET FUNCTIONS       #
###################################


def _get_pos(target):  # Get cursor position.
    print(target.pos())


def _set_pos(target, x: int, y: int):  # Set cursor position.
    target.setposition(x, y)


####################################
#          MAIN FUNCTIONS          #
####################################


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def create_dot():
    CURSOR.up()
    CURSOR.forward(RADIUS)
    CURSOR.down()
    CURSOR.dot()
    CURSOR.up()
    CURSOR.goto(0, 0)
    CURSOR.down()


def draw_cricle():
    # Set position to write circle.
    CURSOR.up()
    CURSOR.goto(x=0, y=-200)
    CURSOR.down()

    # Draw circle.
    CURSOR.circle(RADIUS)

    # Set position to center.
    CURSOR.up()
    _set_pos(CURSOR, 0, 0)
    CURSOR.left(90)


def hours():
    hours = hours_entry.get()
    hours = int(hours)
    if hours <= 23:
        hours_angle = hours*15
        TANGLE[0] = hours_angle
    else:
        tkinter.messagebox.showerror(
            title='Hours value error!', message="Please provid a good value.")


def minutes():
    minutes = minutes_entry.get()
    minutes = int(minutes)
    if minutes <= 59:
        minutes_angle = minutes*0.25
        TANGLE[1] = minutes_angle
    else:
        tkinter.messagebox.showerror(
            title='Minutes value error!', message="Please provid a good value.")


def seconds():
    seconds = seconds_entry.get()
    seconds = int(seconds)
    if seconds <= 59:
        seconds_angle = seconds*0.00416666
        TANGLE[2] = seconds_angle
    else:
        tkinter.messagebox.showerror(
            title='Seconds value error!', message="Please provid a good value.")


def angle():
    if len(TANGLE) == 3:
        a = TANGLE[0] + TANGLE[1] + TANGLE[2]
        a = int(a)
        CURSOR.right(a)
        create_dot()
        console_print = tkinter.Label(
            console_frame, text=f"Degrees: {TANGLE}\nRotation: {a}°", font=CONSOLE_TEXT, bg='#2C2F33', fg="White", anchor="e", justify="center")
        console_print.pack()
        CURSOR.left(a)
        console_print.after(10000, lambda: console_print.destroy())
    else:
        tkinter.messagebox.showerror(
            title="Error missing value.", message="You miss to complete a value!")


####################################
#               MENU               #
####################################


# Hours label
hours_label = tkinter.Label(
    ROOT, text="Hours", font=FONT_TEXT)
# Hours entry
hours_entry = tkinter.Entry(ROOT, bg='#2C2F33', fg='white',
                            insertbackground='white')

# Minutes label
minutes_label = tkinter.Label(ROOT, text="Minutes", font=FONT_TEXT)
# Minutres entry
minutes_entry = tkinter.Entry(ROOT, bg='#2C2F33', fg='white',
                              insertbackground='white')

# Seconds label
seconds_label = tkinter.Label(ROOT, text="Seconds", font=FONT_TEXT)
# Seconds entry
seconds_entry = tkinter.Entry(ROOT, bg='#2C2F33', fg='white',
                              insertbackground='white')

# Validation button
validate_button = tkinter.Button(ROOT, text="Validate",
                                 command=combine_funcs(hours, minutes, seconds), font=FONT_TEXT, bg='#00c936')

# Angles button
angle_button = tkinter.Button(
    ROOT, text="Angle", command=angle, font=FONT_TEXT, bg="#7289DA")

# Console label
console_label = tkinter.Label(ROOT, text="Console", font=FONT_TEXT)
# Console
console_frame = tkinter.Frame(ROOT, bg='#2C2F33', width=168, height=300)
console_frame.place(x=0, y=500)

# Pack all entries and button
hours_label.pack()
hours_entry.pack()

minutes_label.pack()
minutes_entry.pack()

seconds_label.pack()
seconds_entry.pack()

validate_button.pack(padx=50, pady=10)
angle_button.pack(padx=50, pady=10)

console_label.pack(padx=50, pady=250)
console_frame.pack_propagate(False)


#####################################
#            RUN WINDOWS            #
#####################################


def _main_root():
    MAIN_WINDOW.pack()
    draw_cricle()
    ROOT.mainloop()


if __name__ == "__main__":
    pass
