from tkinter import *
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_title.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_title.config(text="Long Break", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_title.config(text="Short Break", fg=RED)
    else:
        count_down(work_sec)
        timer_title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    min = count // 60
    sec = count % 60

    if sec < 10:
        sec = f"0{sec}"
    
    if min < 10:
        min = f"0{min}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check = ""
        work_sessions = reps//2
        for i in range(work_sessions):
            check += "✓"
        check_marks.config(text=check)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomate_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomate_img)

timer_text = canvas.create_text(100,135,text="00:00", fill="white", font=(FONT_NAME, 33, "bold"))
canvas.grid(column=1,row=1)


timer_title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_title.grid(column=1, row=0)

start=Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0,row=2)

reset=Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2,row=2)

check_marks = Label(text="", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1,row=3)













window.mainloop()







