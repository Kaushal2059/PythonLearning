
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timersss = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timersss)
    tick.config(text="")
    canvas.itemconfig(timer, text="00:00")
    label.config(text="Timer")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN *60
    short_break = SHORT_BREAK_MIN *60
    long_break = LONG_BREAK_MIN *60

    if reps % 8 == 0:
        count_down(long_break)
        label.config(text="Break", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break)
        label.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
       global timersss
       timersss = ( window.after(1000, count_down, count -1 ) )
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        tick.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pamadero")
window.config(padx=100, pady= 50, bg=YELLOW)
 
canvas = Canvas(width=200, height= 224, bg= YELLOW, highlightthickness=0)
image = PhotoImage(file="pamadero_game/tomato.png")
canvas.create_image(100, 110, image = image)
timer = canvas.create_text(102,130, text="00:00", fill= "white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg= GREEN, bg= YELLOW)
label.grid(row= 0, column=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

stop = Button(text="Reset", highlightthickness=0, command=reset_timer)
stop.grid(row= 2,column=2)

tick = Label(fg=GREEN, bg=YELLOW, font=50)
tick.grid(row=3, column=1)


window,mainloop()