#  advanced calcutaor
import math
from math import pi as pi
import tkinter as tk
from tkinter import messagebox

def sum(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def power(num1,num2):
    return math.pow(num1,num2)

def sqrt(num1):
    return math.sqrt(num1)

def sin(num1):
    return math.sin(num1)

def cos(num1):
    return math.cos(num1)

def tan(num1):
    return math.tan(num1)

def cot(num1):
    return math.cot(num1)

def sec(num1):
    return math.sec(num1)

def cosec(num1):
    return math.cosec(num1)

def area_of_circle(radius):
    return math.pi*radius*radius

def area_of_triangle(base,height):
    return 0.5*base*height

def area_of_rectangle(length,breadth):
    return length*breadth

def area_of_square(side):
    return side*side

def area_of_parallelogram(base,height):
    return base*height

def area_of_trapezium(base1,base2,height):
    return 0.5*(base1+base2)*height

def area_of_rhombus(diagonal1,diagonal2):
    return 0.5*diagonal1*diagonal2

def area_of_pentagon(side):
    return 0.5*side*side

def area_of_hexagon(side):
    return 0.5*side*side

def  area_of_octagon(side):
    return 0.5*side*side

def  area_of_circel_arc(radius,angle):
    return 0.5*radius*radius*angle

def  area_of_ellipse(a,b):
    return pi*a*b


def perimeter_of_circle(radius):
    return 2*pi*radius

def perimeter_of_triangle(side1,side2,side3):
    return side1+side2+side3

def perimeter_of_rectangle(length,breadth):
    return 2*(length+breadth)

def perimeter_of_square(side):
    return 4*side

def perimeter_of_trapezoid(a, b, c, d):
    return a + b + c + d

def perimeter_of_rhombus(side):
    return 4*side

def perimeter_of_pentagon(side):
    return 5*side

def perimeter_of_hexagon(side):
    return 6*side

def perimeter_of_octagon(side):
    return 8*side

def perimeter_of_circel_arc(radius,angle):
    return 2*pi*radius*angle/360

def perimeter_of_ellipse(a,b):
    return 2*pi*a*pi*b

def open_standard_calculator():
    win = tk.Toplevel(root)
    win.title("Standard Calculator")
    win.geometry("350x420")
    win.configure(bg="#f0f4f7")

    # Make the window resizable
    win.rowconfigure(tuple(range(6)), weight=1)
    win.columnconfigure(tuple(range(4)), weight=1)

    expression = tk.StringVar()
    entry = tk.Entry(
        win, textvariable=expression, font=("Segoe UI", 20), bd=10,
        insertwidth=2, borderwidth=4, justify='right'
    )
    entry.grid(row=0, column=0, columnspan=4, pady=15, padx=10, sticky="nsew")

    def btn_click(item):
        current = expression.get()
        expression.set(current + str(item))

    def btn_clear():
        expression.set("")

    def btn_equal():
        try:
            result = str(eval(expression.get()))
            expression.set(result)
        except:
            expression.set("Error")

    # Button layout
    buttons = [
        ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
        ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
        ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
        ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
        ('C',5,0)
    ]

    for (text, row, col) in buttons:
        if text == '=':
            tk.Button(
                win, text=text, font=("Segoe UI", 14),
                bg="#4caf50", fg="white", bd=0, activebackground="#388e3c",
                command=btn_equal
            ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        elif text == 'C':
            tk.Button(
                win, text=text, font=("Segoe UI", 14),
                bg="#f44336", fg="white", bd=0, activebackground="#b71c1c",
                command=btn_clear
            ).grid(row=row, column=col, columnspan=4, padx=5, pady=10, sticky="nsew")
            # Make the clear row expand for all columns
            for c in range(4):
                win.columnconfigure(c, weight=1)
        else:
            tk.Button(
                win, text=text, font=("Segoe UI", 14),
                bg="#e0e0e0", bd=0, activebackground="#bdbdbd",
                command=lambda t=text: btn_click(t)
            ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

def open_geometry_calculator():
    win = tk.Toplevel(root)
    win.title("Geometry Calculator")

    def open_square():
        top = tk.Toplevel(win)
        top.title("Square")
        top.configure(bg="#f0f4f7")
        tk.Label(top, text="Side:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry.pack(pady=4, padx=10)
        def calc():
            try:
                side = float(entry.get())
                area = area_of_square(side)
                perimeter = perimeter_of_square(side)
                messagebox.showinfo("Result", f"Area: {area}\nPerimeter: {perimeter}")
            except:
                messagebox.showerror("Error", "Invalid input")
        tk.Button(top, text="Calculate", font=("Segoe UI", 12), bg="#4caf50", fg="white", bd=0, activebackground="#388e3c", command=calc).pack(pady=10)

    def open_circle():
        top = tk.Toplevel(win)
        top.title("Circle")
        top.configure(bg="#f0f4f7")
        tk.Label(top, text="Radius:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry.pack(pady=4, padx=10)
        def calc():
            try:
                radius = float(entry.get())
                area = area_of_circle(radius)
                perimeter = perimeter_of_circle(radius)
                messagebox.showinfo("Result", f"Area: {area}\nPerimeter: {perimeter}")
            except:
                messagebox.showerror("Error", "Invalid input")
        tk.Button(top, text="Calculate", font=("Segoe UI", 12), bg="#4caf50", fg="white", bd=0, activebackground="#388e3c", command=calc).pack(pady=10)

    def open_rectangle():
        top = tk.Toplevel(win)
        top.title("Rectangle")
        top.configure(bg="#f0f4f7")
        tk.Label(top, text="Length:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry1 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry1.pack(pady=4, padx=10)
        tk.Label(top, text="Width:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry2 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry2.pack(pady=4, padx=10)
        def calc():
            try:
                length = float(entry1.get())
                width = float(entry2.get())
                area = area_of_rectangle(length, width)
                perimeter = perimeter_of_rectangle(length, width)
                messagebox.showinfo("Result", f"Area: {area}\nPerimeter: {perimeter}")
            except:
                messagebox.showerror("Error", "Invalid input")
        tk.Button(top, text="Calculate", font=("Segoe UI", 12), bg="#4caf50", fg="white", bd=0, activebackground="#388e3c", command=calc).pack(pady=10)

    def open_triangle():
        top = tk.Toplevel(win)
        top.title("Triangle")
        top.configure(bg="#f0f4f7")
        tk.Label(top, text="Base:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry1 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry1.pack(pady=4, padx=10)
        tk.Label(top, text="Height:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry2 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry2.pack(pady=4, padx=10)
        tk.Label(top, text="Side 1:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry3 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry3.pack(pady=4, padx=10)
        tk.Label(top, text="Side 2:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry4 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry4.pack(pady=4, padx=10)
        tk.Label(top, text="Side 3:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry5 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry5.pack(pady=4, padx=10)
        def calc():
            try:
                base = float(entry1.get())
                height = float(entry2.get())
                s1 = float(entry3.get())
                s2 = float(entry4.get())
                s3 = float(entry5.get())
                area = area_of_triangle(base, height)
                perimeter = perimeter_of_triangle(s1, s2, s3)
                messagebox.showinfo("Result", f"Area: {area}\nPerimeter: {perimeter}")
            except:
                messagebox.showerror("Error", "Invalid input")
        tk.Button(top, text="Calculate", font=("Segoe UI", 12), bg="#4caf50", fg="white", bd=0, activebackground="#388e3c", command=calc).pack(pady=10)

    def open_parallelogram():
        top = tk.Toplevel(win)
        top.title("Parallelogram")
        top.configure(bg="#f0f4f7")
        tk.Label(top, text="Base:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry1 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry1.pack(pady=4, padx=10)
        tk.Label(top, text="Height:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry2 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry2.pack(pady=4, padx=10)
        tk.Label(top, text="Side:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry3 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry3.pack(pady=4, padx=10)
        def calc():
            try:
                base = float(entry1.get())
                height = float(entry2.get())
                side = float(entry3.get())
                area = area_of_parallelogram(base, height)
                perimeter = 2 * (base + side)
                messagebox.showinfo("Result", f"Area: {area}\nPerimeter: {perimeter}")
            except:
                messagebox.showerror("Error", "Invalid input")
        tk.Button(top, text="Calculate", font=("Segoe UI", 12), bg="#4caf50", fg="white", bd=0, activebackground="#388e3c", command=calc).pack(pady=10)

    def open_trapezium():
        top = tk.Toplevel(win)
        top.title("Trapezium")
        top.configure(bg="#f0f4f7")
        tk.Label(top, text="Base 1:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry1 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry1.pack(pady=4, padx=10)
        tk.Label(top, text="Base 2:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry2 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry2.pack(pady=4, padx=10)
        tk.Label(top, text="Height:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry3 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry3.pack(pady=4, padx=10)
        tk.Label(top, text="Side 1:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry4 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry4.pack(pady=4, padx=10)
        tk.Label(top, text="Side 2:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry5 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry5.pack(pady=4, padx=10)
        def calc():
            try:
                base1 = float(entry1.get())
                base2 = float(entry2.get())
                height = float(entry3.get())
                side1 = float(entry4.get())
                side2 = float(entry5.get())
                area = area_of_trapezium(base1, base2, height)
                perimeter = base1 + base2 + side1 + side2
                messagebox.showinfo("Result", f"Area: {area}\nPerimeter: {perimeter}")
            except:
                messagebox.showerror("Error", "Invalid input")
        tk.Button(top, text="Calculate", font=("Segoe UI", 12), bg="#4caf50", fg="white", bd=0, activebackground="#388e3c", command=calc).pack(pady=10)

    def open_rhombus():
        top = tk.Toplevel(win)
        top.title("Rhombus")
        top.configure(bg="#f0f4f7")
        tk.Label(top, text="Diagonal 1:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry1 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry1.pack(pady=4, padx=10)
        tk.Label(top, text="Diagonal 2:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry2 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry2.pack(pady=4, padx=10)
        tk.Label(top, text="Side:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry3 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry3.pack(pady=4, padx=10)
        def calc():
            try:
                d1 = float(entry1.get())
                d2 = float(entry2.get())
                side = float(entry3.get())
                area = area_of_rhombus(d1, d2)
                perimeter = perimeter_of_rhombus(side)
                messagebox.showinfo("Result", f"Area: {area}\nPerimeter: {perimeter}")
            except:
                messagebox.showerror("Error", "Invalid input")
        tk.Button(top, text="Calculate", font=("Segoe UI", 12), bg="#4caf50", fg="white", bd=0, activebackground="#388e3c", command=calc).pack(pady=10)

    def open_pentagon():
        top = tk.Toplevel(win)
        top.title("Pentagon")
        top.configure(bg="#f0f4f7")
        tk.Label(top, text="Side:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry.pack(pady=4, padx=10)
        def calc():
            try:
                side = float(entry.get())
                area = area_of_pentagon(side)
                perimeter = perimeter_of_pentagon(side)
                messagebox.showinfo("Result", f"Area: {area}\nPerimeter: {perimeter}")
            except:
                messagebox.showerror("Error", "Invalid input")
        tk.Button(top, text="Calculate", font=("Segoe UI", 12), bg="#4caf50", fg="white", bd=0, activebackground="#388e3c", command=calc).pack(pady=10)

    def open_hexagon():
        top = tk.Toplevel(win)
        top.title("Hexagon")
        top.configure(bg="#f0f4f7")
        tk.Label(top, text="Side:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry.pack(pady=4, padx=10)
        def calc():
            try:
                side = float(entry.get())
                area = area_of_hexagon(side)
                perimeter = perimeter_of_hexagon(side)
                messagebox.showinfo("Result", f"Area: {area}\nPerimeter: {perimeter}")
            except:
                messagebox.showerror("Error", "Invalid input")
        tk.Button(top, text="Calculate", font=("Segoe UI", 12), bg="#4caf50", fg="white", bd=0, activebackground="#388e3c", command=calc).pack(pady=10)

    def open_octagon():
        top = tk.Toplevel(win)
        top.title("Octagon")
        top.configure(bg="#f0f4f7")
        tk.Label(top, text="Side:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry.pack(pady=4, padx=10)
        def calc():
            try:
                side = float(entry.get())
                area = area_of_octagon(side)
                perimeter = perimeter_of_octagon(side)
                messagebox.showinfo("Result", f"Area: {area}\nPerimeter: {perimeter}")
            except:
                messagebox.showerror("Error", "Invalid input")
        tk.Button(top, text="Calculate", font=("Segoe UI", 12), bg="#4caf50", fg="white", bd=0, activebackground="#388e3c", command=calc).pack(pady=10)

    def open_circle_arc():
        top = tk.Toplevel(win)
        top.title("Circle Arc")
        top.configure(bg="#f0f4f7")
        tk.Label(top, text="Radius:", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry1 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry1.pack(pady=4, padx=10)
        tk.Label(top, text="Angle (degrees):", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry2 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry2.pack(pady=4, padx=10)
        def calc():
            try:
                radius = float(entry1.get())
                angle = float(entry2.get())
                area = area_of_circel_arc(radius, angle)
                perimeter = perimeter_of_circel_arc(radius, angle)
                messagebox.showinfo("Result", f"Area: {area}\nPerimeter: {perimeter}")
            except:
                messagebox.showerror("Error", "Invalid input")
        tk.Button(top, text="Calculate", font=("Segoe UI", 12), bg="#4caf50", fg="white", bd=0, activebackground="#388e3c", command=calc).pack(pady=10)

    def open_ellipse():
        top = tk.Toplevel(win)
        top.title("Ellipse")
        top.configure(bg="#f0f4f7")
        tk.Label(top, text="a (semi-major axis):", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry1 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry1.pack(pady=4, padx=10)
        tk.Label(top, text="b (semi-minor axis):", font=("Segoe UI", 12), bg="#f0f4f7").pack(pady=8)
        entry2 = tk.Entry(top, font=("Segoe UI", 12), bd=2, relief="groove")
        entry2.pack(pady=4, padx=10)
        def calc():
            try:
                a = float(entry1.get())
                b = float(entry2.get())
                area = area_of_ellipse(a, b)
                perimeter = perimeter_of_ellipse(a, b)
                messagebox.showinfo("Result", f"Area: {area}\nPerimeter: {perimeter}")
            except:
                messagebox.showerror("Error", "Invalid input")
        tk.Button(top, text="Calculate", font=("Segoe UI", 12), bg="#4caf50", fg="white", bd=0, activebackground="#388e3c", command=calc).pack(pady=10)


    tk.Label(win, text="Select a shape:", font=("Segoe UI", 16, "bold"), bg="#f0f4f7", fg="#333").pack(pady=18)

    button_style = {
        "width": 22, "height": 2, "font": ("Segoe UI", 12),
        "bg": "#e0e0e0", "fg": "#222", "bd": 0,
        "activebackground": "#bdbdbd", "activeforeground": "#222",
        "cursor": "hand2"
    }

    tk.Button(win, text="Square", command=open_square, **button_style).pack(pady=4)
    tk.Button(win, text="Circle", command=open_circle, **button_style).pack(pady=4)
    tk.Button(win, text="Rectangle", command=open_rectangle, **button_style).pack(pady=4)
    tk.Button(win, text="Triangle", command=open_triangle, **button_style).pack(pady=4)
    tk.Button(win, text="Parallelogram", command=open_parallelogram, **button_style).pack(pady=4)
    tk.Button(win, text="Trapezium", command=open_trapezium, **button_style).pack(pady=4)
    tk.Button(win, text="Rhombus", command=open_rhombus, **button_style).pack(pady=4)
    tk.Button(win, text="Pentagon", command=open_pentagon, **button_style).pack(pady=4)
    tk.Button(win, text="Hexagon", command=open_hexagon, **button_style).pack(pady=4)
    tk.Button(win, text="Octagon", command=open_octagon, **button_style).pack(pady=4)
    tk.Button(win, text="Circle Arc", command=open_circle_arc, **button_style).pack(pady=4)
    tk.Button(win, text="Ellipse", command=open_ellipse, **button_style).pack(pady=4)

root = tk.Tk()
root.title("Calculator Type Selection")
root.geometry("370x220")
root.configure(bg="#f0f4f7")

tk.Label(root, text="Select calculator type:", font=("Segoe UI", 16, "bold"), bg="#f0f4f7").pack(pady=20)
tk.Button(
    root, text="Standard Calculator", font=("Segoe UI", 14), width=22, height=2,
    bg="#2196f3", fg="white", bd=0, activebackground="#1976d2", activeforeground="white",
    command=open_standard_calculator
).pack(pady=8)
tk.Button(
    root, text="Geometry Calculator", font=("Segoe UI", 14), width=22, height=2,
    bg="#009688", fg="white", bd=0, activebackground="#00695c", activeforeground="white",
    command=open_geometry_calculator
).pack(pady=8)
root.mainloop()