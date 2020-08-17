import tkinter as tk

root = tk.Tk()

root.title("Pythagorean Theorem")

canvas1 = tk.Canvas(root, width=600, height=320, bg="LightSteelBlue4")
canvas1.pack()

title = tk.Label(root, text='Calculate the Unknown Side')
title.config(font=('times new roman', 14))
canvas1.create_window(300, 25, window=title)

note = tk.Label(root, text='Place known values in the appropriate place and leave the remaining empty.')
note.config(font=('times new roman', 10))
canvas1.create_window(300, 60, window=note)

label1 = tk.Label(root, text="Side A", font=('arial sans', 8))
canvas1.create_window(100, 100, window=label1)

label2 = tk.Label(root, text="Side B", font=('arial sans', 8))
canvas1.create_window(300, 100, window=label2)

label3 = tk.Label(root, text="Hypotnuse", font=('arial sans', 8))
canvas1.create_window(500, 100, window=label3)

entry1 = tk.Entry(root)
canvas1.create_window(100, 140, window=entry1)

entry2 = tk.Entry(root)
canvas1.create_window(300, 140, window=entry2)

entry3 = tk.Entry(root)
canvas1.create_window(500, 140, window=entry3)

counter = 0

def upClick():
    global counter

    counter = counter + 1

    counterLabel.configure(text=counter)

def downClick():
    global counter

    if counter == 0:
        counter = counter + 0
        counterLabel.configure(text=counter)
    else:
        counter = counter - 1
        counterLabel.configure(text=counter)

def solve():
    global counter
    global box

    a = entry1.get()
    b = entry2.get()
    c = entry3.get()
    # calculations
    if not entry3.get():
        a = float(a)
        b = float(b)
        answer = (((a ** 2) + (b ** 2)) ** 0.5)
    elif not entry2.get():
        a = float(a)
        c = float(c)
        answer = (((c ** 2) - (a ** 2)) ** 0.5)
    else:
        b = float(b)
        c = float(c)
        answer = (((c ** 2) - (b ** 2)) ** 0.5)

    solved = tk.Label(root, text=float(round(answer, counter)))
    box = canvas1.create_window(300, 230, window=solved)


def clear():
    global i
    canvas1.delete(box)



button1 = tk.Button(text="Solve the triangle", command=solve, bg="red", fg="white", font=('arial sans', 8, 'bold'))
canvas1.create_window(300, 180, window=button1)

clearButton = tk.Button(text="Clear answer", command=clear, bg="red", fg="white", font=("arial sans", 8, "bold"))
canvas1.create_window(420, 180, window=clearButton)

decimalCount = tk.Label(text="How many decimal places should there be?", font=('arial sans', 8))
canvas1.create_window(300, 260, window=decimalCount)

counterLabel = tk.Label(root, text=counter)
canvas1.create_window(300, 295, window=counterLabel)

upButton = tk.Button(root, text="Increase", command=upClick)
canvas1.create_window(350, 285, window=upButton)

downButton = tk.Button(root, text="Decrease", command=downClick)
canvas1.create_window(350, 310, window=downButton)



root.mainloop()
