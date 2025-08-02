import sys
import math
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QDialog, QMessageBox, QGridLayout
)
from PyQt5.QtCore import Qt

# --- Calculation Functions ---
def sum_(num1, num2): return num1 + num2
def sub(num1, num2): return num1 - num2
def mul(num1, num2): return num1 * num2
def div(num1, num2): return num1 / num2
def power(num1, num2): return math.pow(num1, num2)
def sqrt(num1): return math.sqrt(num1)
def sin(num1): return math.sin(num1)
def cos(num1): return math.cos(num1)
def tan(num1): return math.tan(num1)
def cot(num1): return 1 / math.tan(num1)
def sec(num1): return 1 / math.cos(num1)
def cosec(num1): return 1 / math.sin(num1)
def area_of_circle(radius): return math.pi * radius * radius
def area_of_triangle(base, height): return 0.5 * base * height
def area_of_rectangle(length, breadth): return length * breadth
def area_of_square(side): return side * side
def area_of_parallelogram(base, height): return base * height
def area_of_trapezium(base1, base2, height): return 0.5 * (base1 + base2) * height
def area_of_rhombus(diagonal1, diagonal2): return 0.5 * diagonal1 * diagonal2
def area_of_pentagon(side): return (5 * side ** 2) / (4 * math.tan(math.pi / 5))
def area_of_hexagon(side): return (3 * math.sqrt(3) * side ** 2) / 2
def area_of_octagon(side): return 2 * (1 + math.sqrt(2)) * side ** 2
def area_of_circle_arc(radius, angle): return math.pi * radius ** 2 * (angle / 360)
def area_of_ellipse(a, b): return math.pi * a * b
def perimeter_of_circle(radius): return 2 * math.pi * radius
def perimeter_of_triangle(side1, side2, side3): return side1 + side2 + side3
def perimeter_of_rectangle(length, breadth): return 2 * (length + breadth)
def perimeter_of_square(side): return 4 * side
def perimeter_of_trapezoid(a, b, c, d): return a + b + c + d
def perimeter_of_rhombus(side): return 4 * side
def perimeter_of_pentagon(side): return 5 * side
def perimeter_of_hexagon(side): return 6 * side
def perimeter_of_octagon(side): return 8 * side
def perimeter_of_circle_arc(radius, angle): arc_length = 2 * math.pi * radius * (angle / 360); return arc_length + 2 * radius
def perimeter_of_ellipse(a, b): h = ((a - b) ** 2) / ((a + b) ** 2); return math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

# --- Standard Calculator Dialog ---
class StandardCalculator(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Standard Calculator")
        self.setFixedSize(350, 420)
        layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("font-size: 20px;")
        layout.addWidget(self.display)
        grid = QGridLayout()
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]
        for (text, row, col) in buttons:
            btn = QPushButton(text)
            btn.setFixedSize(70, 50)
            btn.setStyleSheet("font-size: 16px;")
            if text == '=':
                btn.clicked.connect(self.calculate)
            elif text == 'C':
                btn.clicked.connect(self.clear)
                grid.addWidget(btn, row, col, 1, 4)
                continue
            else:
                btn.clicked.connect(lambda _, t=text: self.display.setText(self.display.text() + t))
            grid.addWidget(btn, row, col)
        layout.addLayout(grid)
        self.setLayout(layout)
    def clear(self):
        self.display.clear()
    def calculate(self):
        try:
            result = str(eval(self.display.text()))
            self.display.setText(result)
        except:
            self.display.setText("Error")

# --- Geometry Calculator Dialog ---
class GeometryCalculator(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Geometry Calculator")
        self.setFixedSize(400, 600)
        layout = QVBoxLayout()
        label = QLabel("Select a shape:")
        label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(label)
        shapes = [
            ("Square", self.square),
            ("Circle", self.circle),
            ("Rectangle", self.rectangle),
            ("Triangle", self.triangle),
            ("Parallelogram", self.parallelogram),
            ("Trapezium", self.trapezium),
            ("Rhombus", self.rhombus),
            ("Pentagon", self.pentagon),
            ("Hexagon", self.hexagon),
            ("Octagon", self.octagon),
            ("Circle Arc", self.circle_arc),
            ("Ellipse", self.ellipse)
        ]
        for name, func in shapes:
            btn = QPushButton(name)
            btn.setFixedHeight(40)
            btn.setStyleSheet("font-size: 15px;")
            btn.clicked.connect(func)
            layout.addWidget(btn)
        self.setLayout(layout)
    def show_result(self, area, perimeter):
        QMessageBox.information(self, "Result", f"Area: {area}\nPerimeter: {perimeter}")
    def get_value(self, prompt):
        dlg = QDialog(self)
        dlg.setWindowTitle(prompt)
        vbox = QVBoxLayout()
        label = QLabel(prompt)
        edit = QLineEdit()
        vbox.addWidget(label)
        vbox.addWidget(edit)
        btn = QPushButton("OK")
        btn.clicked.connect(dlg.accept)
        vbox.addWidget(btn)
        dlg.setLayout(vbox)
        if dlg.exec_() == QDialog.Accepted:
            try:
                return float(edit.text())
            except:
                return None
        return None
    def get_values(self, prompts):
        dlg = QDialog(self)
        dlg.setWindowTitle("Input Values")
        vbox = QVBoxLayout()
        edits = []
        for prompt in prompts:
            label = QLabel(prompt)
            edit = QLineEdit()
            vbox.addWidget(label)
            vbox.addWidget(edit)
            edits.append(edit)
        btn = QPushButton("OK")
        btn.clicked.connect(dlg.accept)
        vbox.addWidget(btn)
        dlg.setLayout(vbox)
        if dlg.exec_() == QDialog.Accepted:
            try:
                return [float(e.text()) for e in edits]
            except:
                return None
        return None
    def square(self):
        side = self.get_value("Side:")
        if side is not None:
            area = area_of_square(side)
            perimeter = perimeter_of_square(side)
            self.show_result(area, perimeter)
    def circle(self):
        radius = self.get_value("Radius:")
        if radius is not None:
            area = area_of_circle(radius)
            perimeter = perimeter_of_circle(radius)
            self.show_result(area, perimeter)
    def rectangle(self):
        vals = self.get_values(["Length:", "Width:"])
        if vals:
            area = area_of_rectangle(vals[0], vals[1])
            perimeter = perimeter_of_rectangle(vals[0], vals[1])
            self.show_result(area, perimeter)
    def triangle(self):
        vals = self.get_values(["Base:", "Height:", "Side 1:", "Side 2:", "Side 3:"])
        if vals:
            area = area_of_triangle(vals[0], vals[1])
            perimeter = perimeter_of_triangle(vals[2], vals[3], vals[4])
            self.show_result(area, perimeter)
    def parallelogram(self):
        vals = self.get_values(["Base:", "Height:", "Side:"])
        if vals:
            area = area_of_parallelogram(vals[0], vals[1])
            perimeter = 2 * (vals[0] + vals[2])
            self.show_result(area, perimeter)
    def trapezium(self):
        vals = self.get_values(["Base 1:", "Base 2:", "Height:", "Side 1:", "Side 2:"])
        if vals:
            area = area_of_trapezium(vals[0], vals[1], vals[2])
            perimeter = vals[0] + vals[1] + vals[3] + vals[4]
            self.show_result(area, perimeter)
    def rhombus(self):
        vals = self.get_values(["Diagonal 1:", "Diagonal 2:", "Side:"])
        if vals:
            area = area_of_rhombus(vals[0], vals[1])
            perimeter = perimeter_of_rhombus(vals[2])
            self.show_result(area, perimeter)
    def pentagon(self):
        side = self.get_value("Side:")
        if side is not None:
            area = area_of_pentagon(side)
            perimeter = perimeter_of_pentagon(side)
            self.show_result(area, perimeter)
    def hexagon(self):
        side = self.get_value("Side:")
        if side is not None:
            area = area_of_hexagon(side)
            perimeter = perimeter_of_hexagon(side)
            self.show_result(area, perimeter)
    def octagon(self):
        side = self.get_value("Side:")
        if side is not None:
            area = area_of_octagon(side)
            perimeter = perimeter_of_octagon(side)
            self.show_result(area, perimeter)
    def circle_arc(self):
        vals = self.get_values(["Radius:", "Angle (degrees):"])
        if vals:
            area = area_of_circle_arc(vals[0], vals[1])
            perimeter = perimeter_of_circle_arc(vals[0], vals[1])
            self.show_result(area, perimeter)
    def ellipse(self):
        vals = self.get_values(["a (semi-major axis):", "b (semi-minor axis):"])
        if vals:
            area = area_of_ellipse(vals[0], vals[1])
            perimeter = perimeter_of_ellipse(vals[0], vals[1])
            self.show_result(area, perimeter)

# --- Main Window ---
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator Type Selection")
        self.setFixedSize(370, 220)
        self.setStyleSheet("background: #f0f4f7;")
        layout = QVBoxLayout()
        label = QLabel("Select calculator type:")
        label.setStyleSheet("font-size: 16pt; font-weight: bold;")
        layout.addWidget(label)
        btn_std = QPushButton("Standard Calculator")
        btn_std.setStyleSheet("font-size: 14pt; background: #2196f3; color: white; height: 40px;")
        btn_std.clicked.connect(self.open_standard)
        layout.addWidget(btn_std)
        btn_geo = QPushButton("Geometry Calculator")
        btn_geo.setStyleSheet("font-size: 14pt; background: #009688; color: white; height: 40px;")
        btn_geo.clicked.connect(self.open_geometry)
        layout.addWidget(btn_geo)
        self.setLayout(layout)
    def open_standard(self):
        dlg = StandardCalculator()
        dlg.exec_()
    def open_geometry(self):
        dlg = GeometryCalculator()
        dlg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
