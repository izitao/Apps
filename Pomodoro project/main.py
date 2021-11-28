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
CHECKMARK = "✔"

timer = None
checkmarks_actual = ""
reps = 0


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global checkmarks_actual, reps

    window.after_cancel(timer)
    label_timer.config(text="Timer", fg=GREEN)
    checkmarks_actual = ""
    label_checkmark.config(text=checkmarks_actual)
    canvas.itemconfigure(timer_text, text=f"00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps, checkmarks_actual

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks_actual += CHECKMARK
            label_checkmark.config(text=checkmarks_actual)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#timer label
label_timer = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
label_timer.grid(row=0, column=1)

#start button
button_start = Button(text="Start", font=(FONT_NAME, 10), bg="white", highlightthickness=0, command=start_timer)
button_start.grid(row=2, column=0)

#reset button
button_reset = Button(text="Reset", font=(FONT_NAME, 10), bg="white", highlightthickness=0, command=reset_timer)
button_reset.grid(row=2, column=2)

#checkmark label
label_checkmark = Label(text="", font=(FONT_NAME, 10), fg=GREEN, bg=YELLOW)
label_checkmark.grid(row=3, column=1)

window.mainloop()
