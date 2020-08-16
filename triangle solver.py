import tkinter as tk

root = tk.Tk()

root.title("Pythagorean Theorem")

canvas1 = tk.Canvas(root, width=600, height=300, bg="LightSteelBlue4")
canvas1.pack()

title = tk.Label(root, text='Calculate the Unknown Side')
title.config(font=('times new roman', 14))
canvas1.create_window(300, 25, window=title)

note = tk.Label(root, text='For the unknown value, place a 0.')
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


def solve():
    a = float(entry1.get())
    b = float(entry2.get())
    c = float(entry3.get())

    # calculations
    if c == 0:
        answer = (((a ** 2) + (b ** 2)) ** 0.5)
    elif b == 0:
        answer = (((c ** 2) - (a ** 2)) ** 0.5)
    else:
        answer = (((c ** 2) - (b ** 2)) ** 0.5)

    solved = tk.Label(root, text=float(answer))
    canvas1.create_window(300, 230, window=solved)


button1 = tk.Button(text="Solve the triangle.", command=solve, bg="red", fg="white", font=('arial sans', 8, 'bold'))
canvas1.create_window(300, 180, window=button1)

root.mainloop()
