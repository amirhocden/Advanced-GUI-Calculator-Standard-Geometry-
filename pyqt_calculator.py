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
        self.resize(350, 420)
        self.setStyleSheet("background: #f0f4f7;")
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        # Top bar with fullscreen and borderless buttons
        top_bar = QHBoxLayout()
        top_bar.addStretch()
        self.fullscreen_btn = QPushButton("Full Screen")
        self.fullscreen_btn.setStyleSheet("font-size: 12px; background: #2196f3; color: white; border-radius: 6px; padding: 4px 12px;")
        self.fullscreen_btn.setFixedHeight(28)
        self.fullscreen_btn.clicked.connect(self.toggle_fullscreen)
        self.square_btn = QPushButton("Square")
        self.square_btn.setStyleSheet("font-size: 12px; background: #4caf50; color: white; border-radius: 6px; padding: 4px 12px;")
        self.square_btn.setFixedHeight(28)
        self.square_btn.clicked.connect(self.toggle_borderless)
        top_bar.addWidget(self.fullscreen_btn)
        top_bar.addWidget(self.square_btn)
        layout.addLayout(top_bar)
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMinimumHeight(55)
        self.display.setStyleSheet(
            "font-family: 'Segoe UI'; font-size: 20px; background: #fff; border: 2px solid #e0e0e0; border-radius: 8px; padding-right: 10px;"
        )
        self.display.setSizePolicy(self.display.sizePolicy().Expanding, self.display.sizePolicy().Fixed)
        layout.addWidget(self.display)
        grid = QGridLayout()
        grid.setSpacing(8)
        for i in range(6):
            grid.setRowStretch(i, 1)
        for i in range(4):
            grid.setColumnStretch(i, 1)
        self.std_buttons = []
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]
        for (text, row, col) in buttons:
            btn = QPushButton(text)
            btn.setSizePolicy(btn.sizePolicy().Expanding, btn.sizePolicy().Expanding)
            self.std_buttons.append(btn)
            if text == 'C':
                btn.setMinimumHeight(60)
                btn.setFont(self.font())
                btn.setStyleSheet(
                    "QPushButton { font-family: 'Segoe UI'; font-size: 18px; background: #f44336; color: white; border: none; border-radius: 6px; } "
                    "QPushButton:hover { background: #b71c1c; }"
                )
                btn.clicked.connect(self.clear)
                grid.addWidget(btn, row, col, 1, 4)
                continue
            else:
                btn.setFont(self.font())
                btn.setStyleSheet(self._button_style(text))
                if text == '=':
                    btn.clicked.connect(self.calculate)
                else:
                    btn.clicked.connect(lambda _, t=text: self.display.setText(self.display.text() + t))
                grid.addWidget(btn, row, col)
        layout.addLayout(grid)
        self.setLayout(layout)
        self.setSizeGripEnabled(True)

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
            self.fullscreen_btn.setText("Full Screen")
            self.display.setStyleSheet(
                "font-family: 'Segoe UI'; font-size: 20px; background: #fff; border: 2px solid #e0e0e0; border-radius: 8px; padding-right: 10px;"
            )
            for btn in self.std_buttons:
                if btn.text() == 'C':
                    btn.setStyleSheet(
                        "QPushButton { font-family: 'Segoe UI'; font-size: 18px; background: #f44336; color: white; border: none; border-radius: 6px; } "
                        "QPushButton:hover { background: #b71c1c; }"
                    )
                else:
                    btn.setStyleSheet(self._button_style(btn.text()))
        else:
            self.showFullScreen()
            self.fullscreen_btn.setText("Exit Full Screen")
            self.display.setStyleSheet(
                "font-family: 'Segoe UI'; font-size: 36px; background: #fff; border: 2px solid #e0e0e0; border-radius: 8px; padding-right: 10px;"
            )
            for btn in self.std_buttons:
                if btn.text() == 'C':
                    btn.setStyleSheet(
                        "QPushButton { font-family: 'Segoe UI'; font-size: 32px; background: #f44336; color: white; border: none; border-radius: 6px; } "
                        "QPushButton:hover { background: #b71c1c; }"
                    )
                else:
                    # Use larger font for all other buttons
                    style = self._button_style(btn.text()).replace('font-size: 14px;', 'font-size: 28px;')
                    btn.setStyleSheet(style)

    def toggle_borderless(self):
        if self.windowFlags() & Qt.FramelessWindowHint:
            self.setWindowFlags(self.windowFlags() & ~Qt.FramelessWindowHint)
            self.showNormal()
            self.square_btn.setText("Square")
        else:
            self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
            self.showNormal()
            self.square_btn.setText("Exit Square")

    def _button_style(self, text):
        # Tkinter color mapping, fixed for Qt stylesheet syntax
        if text == '=':
            return (
                "QPushButton { font-family: 'Segoe UI'; font-size: 14px; background: #4caf50; color: white; border: none; border-radius: 6px; } "
                "QPushButton:hover { background: #388e3c; }"
            )
        elif text == 'C':
            return (
                "QPushButton { font-family: 'Segoe UI'; font-size: 14px; background: #f44336; color: white; border: none; border-radius: 6px; } "
                "QPushButton:hover { background: #b71c1c; }"
            )
        elif text in ['/', '*', '-', '+']:
            return (
                "QPushButton { font-family: 'Segoe UI'; font-size: 14px; background: #e0e0e0; color: #222; border: none; border-radius: 6px; } "
                "QPushButton:hover { background: #bdbdbd; }"
            )
        else:
            return (
                "QPushButton { font-family: 'Segoe UI'; font-size: 14px; background: #e0e0e0; color: #222; border: none; border-radius: 6px; } "
                "QPushButton:hover { background: #bdbdbd; }"
            )
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
        self.resize(400, 600)
        self.setStyleSheet("background: #f0f4f7; border-radius: 12px;")
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        # Top bar styled like the rest of the app
        top_bar = QHBoxLayout()
        top_bar.addStretch()
        self.fullscreen_btn = QPushButton("Full Screen")
        self.fullscreen_btn.setStyleSheet("font-size: 12px; background: #2196f3; color: white; border-radius: 6px; padding: 4px 12px;")
        self.fullscreen_btn.setFixedHeight(28)
        self.fullscreen_btn.clicked.connect(self.toggle_fullscreen)
        top_bar.addWidget(self.fullscreen_btn)
        layout.addLayout(top_bar)
        self.label = QLabel("Select a shape:")
        self.label.setStyleSheet("font-size: 20px; font-weight: bold; color: #222; margin-bottom: 8px;")
        layout.addWidget(self.label)

        self.shape_buttons = []
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
            btn.setSizePolicy(btn.sizePolicy().Expanding, btn.sizePolicy().Expanding)
            btn.setMinimumHeight(44)
            btn.setStyleSheet(
                "QPushButton { font-family: 'Segoe UI'; font-size: 16px; background: #e0e0e0; color: #222; border: none; border-radius: 8px; margin-bottom: 6px; padding: 8px 0; } "
                "QPushButton:hover { background: #bdbdbd; }"
            )
            btn.clicked.connect(func)
            layout.addWidget(btn)
            self.shape_buttons.append(btn)
        self.setLayout(layout)
        self.setSizeGripEnabled(True)

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
            self.fullscreen_btn.setText("Full Screen")
            self.label.setStyleSheet("font-size: 20px; font-weight: bold; color: #222; margin-bottom: 8px;")
            for btn in self.shape_buttons:
                btn.setStyleSheet(
                    "QPushButton { font-family: 'Segoe UI'; font-size: 16px; background: #e0e0e0; color: #222; border: none; border-radius: 8px; margin-bottom: 6px; padding: 8px 0; } "
                    "QPushButton:hover { background: #bdbdbd; }"
                )
        else:
            self.showFullScreen()
            self.fullscreen_btn.setText("Exit Full Screen")
            self.label.setStyleSheet("font-size: 36px; font-weight: bold; color: #222; margin-bottom: 12px;")
            for btn in self.shape_buttons:
                btn.setStyleSheet(
                    "QPushButton { font-family: 'Segoe UI'; font-size: 32px; background: #e0e0e0; color: #222; border: none; border-radius: 12px; margin-bottom: 10px; padding: 16px 0; } "
                    "QPushButton:hover { background: #bdbdbd; }"
                )
    def toggle_borderless(self):
        if self.windowFlags() & Qt.FramelessWindowHint:
            self.setWindowFlags(self.windowFlags() & ~Qt.FramelessWindowHint)
            self.square_btn.setText("Square")
        else:
            self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
            self.square_btn.setText("Exit Square")
        self.show()
    def show_result(self, area, perimeter):
        dlg = QDialog(self)
        dlg.setWindowTitle("Result")
        dlg.setStyleSheet("background: #f0f4f7; border-radius: 12px;")
        vbox = QVBoxLayout()
        vbox.setContentsMargins(20, 20, 20, 20)
        vbox.setSpacing(18)
        area_label = QLabel(f"<b>Area:</b> <span style='color:#4caf50; font-size:22px;'>{area}</span>")
        area_label.setStyleSheet("font-size: 20px; margin-bottom: 8px;")
        perimeter_label = QLabel(f"<b>Perimeter:</b> <span style='color:#2196f3; font-size:22px;'>{perimeter}</span>")
        perimeter_label.setStyleSheet("font-size: 20px; margin-bottom: 8px;")
        vbox.addWidget(area_label)
        vbox.addWidget(perimeter_label)
        btn = QPushButton("Close")
        btn.setStyleSheet("font-size: 16px; background: #2196f3; color: white; border-radius: 6px; padding: 8px 24px;")
        btn.clicked.connect(dlg.accept)
        vbox.addWidget(btn)
        dlg.setLayout(vbox)
        dlg.exec_()
    def get_value(self, prompt, formula=None):
        dlg = QDialog(self)
        dlg.setWindowTitle(prompt)
        dlg.setStyleSheet("background: #f0f4f7; border-radius: 12px;")
        vbox = QVBoxLayout()
        vbox.setContentsMargins(16, 16, 16, 16)
        vbox.setSpacing(12)
        if formula:
            formula_label = QLabel(f"<b>Formula:</b> {formula}")
            formula_label.setStyleSheet("font-size: 15px; color: #2196f3; margin-bottom: 8px;")
            vbox.addWidget(formula_label)
        label = QLabel(prompt)
        label.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 6px;")
        edit = QLineEdit()
        edit.setStyleSheet("font-size: 16px; padding: 8px; border-radius: 6px; border: 1px solid #e0e0e0; background: #fff;")
        vbox.addWidget(label)
        vbox.addWidget(edit)
        btn = QPushButton("OK")
        btn.setStyleSheet("font-size: 15px; background: #2196f3; color: white; border-radius: 6px; padding: 6px 18px;")
        btn.clicked.connect(dlg.accept)
        vbox.addWidget(btn)
        dlg.setLayout(vbox)
        if dlg.exec_() == QDialog.Accepted:
            try:
                return float(edit.text())
            except:
                return None
        return None
    def get_values(self, prompts, formula=None):
        dlg = QDialog(self)
        dlg.setWindowTitle("Input Values")
        dlg.setStyleSheet("background: #f0f4f7; border-radius: 12px;")
        vbox = QVBoxLayout()
        vbox.setContentsMargins(16, 16, 16, 16)
        vbox.setSpacing(12)
        edits = []
        if formula:
            formula_label = QLabel(f"<b>Formula:</b> {formula}")
            formula_label.setStyleSheet("font-size: 15px; color: #2196f3; margin-bottom: 8px;")
            vbox.addWidget(formula_label)
        for prompt in prompts:
            label = QLabel(prompt)
            label.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 6px;")
            edit = QLineEdit()
            edit.setStyleSheet("font-size: 16px; padding: 8px; border-radius: 6px; border: 1px solid #e0e0e0; background: #fff;")
            vbox.addWidget(label)
            vbox.addWidget(edit)
            edits.append(edit)
        btn = QPushButton("OK")
        btn.setStyleSheet("font-size: 15px; background: #2196f3; color: white; border-radius: 6px; padding: 6px 18px;")
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
        side = self.get_value("Side:", formula="Area = side², Perimeter = 4 × side")
        if side is not None:
            area = area_of_square(side)
            perimeter = perimeter_of_square(side)
            self.show_result(area, perimeter)
    def circle(self):
        radius = self.get_value("Radius:", formula="Area = π × radius², Perimeter = 2 × π × radius")
        if radius is not None:
            area = area_of_circle(radius)
            perimeter = perimeter_of_circle(radius)
            self.show_result(area, perimeter)
    def rectangle(self):
        vals = self.get_values(["Length:", "Width:"], formula="Area = length × width, Perimeter = 2 × (length + width)")
        if vals:
            area = area_of_rectangle(vals[0], vals[1])
            perimeter = perimeter_of_rectangle(vals[0], vals[1])
            self.show_result(area, perimeter)
    def triangle(self):
        vals = self.get_values(["Base:", "Height:", "Side 1:", "Side 2:", "Side 3:"], formula="Area = ½ × base × height, Perimeter = side1 + side2 + side3")
        if vals:
            area = area_of_triangle(vals[0], vals[1])
            perimeter = perimeter_of_triangle(vals[2], vals[3], vals[4])
            self.show_result(area, perimeter)
    def parallelogram(self):
        vals = self.get_values(["Base:", "Height:", "Side:"], formula="Area = base × height, Perimeter = 2 × (base + side)")
        if vals:
            area = area_of_parallelogram(vals[0], vals[1])
            perimeter = 2 * (vals[0] + vals[2])
            self.show_result(area, perimeter)
    def trapezium(self):
        vals = self.get_values(["Base 1:", "Base 2:", "Height:", "Side 1:", "Side 2:"], formula="Area = ½ × (base1 + base2) × height, Perimeter = base1 + base2 + side1 + side2")
        if vals:
            area = area_of_trapezium(vals[0], vals[1], vals[2])
            perimeter = vals[0] + vals[1] + vals[3] + vals[4]
            self.show_result(area, perimeter)
    def rhombus(self):
        vals = self.get_values(["Diagonal 1:", "Diagonal 2:", "Side:"], formula="Area = ½ × diagonal1 × diagonal2, Perimeter = 4 × side")
        if vals:
            area = area_of_rhombus(vals[0], vals[1])
            perimeter = perimeter_of_rhombus(vals[2])
            self.show_result(area, perimeter)
    def pentagon(self):
        side = self.get_value("Side:", formula="Area = (5 × side²) / (4 × tan(π/5)), Perimeter = 5 × side")
        if side is not None:
            area = area_of_pentagon(side)
            perimeter = perimeter_of_pentagon(side)
            self.show_result(area, perimeter)
    def hexagon(self):
        side = self.get_value("Side:", formula="Area = (3√3 × side²) / 2, Perimeter = 6 × side")
        if side is not None:
            area = area_of_hexagon(side)
            perimeter = perimeter_of_hexagon(side)
            self.show_result(area, perimeter)
    def octagon(self):
        side = self.get_value("Side:", formula="Area = 2 × (1 + √2) × side², Perimeter = 8 × side")
        if side is not None:
            area = area_of_octagon(side)
            perimeter = perimeter_of_octagon(side)
            self.show_result(area, perimeter)
    def circle_arc(self):
        vals = self.get_values(["Radius:", "Angle (degrees):"], formula="Area = π × radius² × (angle/360), Perimeter = arc length + 2 × radius")
        if vals:
            area = area_of_circle_arc(vals[0], vals[1])
            perimeter = perimeter_of_circle_arc(vals[0], vals[1])
            self.show_result(area, perimeter)
    def ellipse(self):
        vals = self.get_values(["a (semi-major axis):", "b (semi-minor axis):"], formula="Area = π × a × b, Perimeter ≈ π × (a + b) × [1 + (3h)/(10 + √(4-3h))]")
        if vals:
            area = area_of_ellipse(vals[0], vals[1])
            perimeter = perimeter_of_ellipse(vals[0], vals[1])
            self.show_result(area, perimeter)

# --- Main Window ---
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator Type Selection")
        self.resize(370, 220)
        self.setStyleSheet("background: #f0f4f7;")
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        # Full screen and borderless buttons
        top_bar = QHBoxLayout()
        top_bar.addStretch()
        self.fullscreen_btn = QPushButton("Full Screen")
        self.fullscreen_btn.setStyleSheet("font-size: 12px; background: #2196f3; color: white; border-radius: 6px; padding: 4px 12px;")
        self.fullscreen_btn.setFixedHeight(28)
        self.fullscreen_btn.clicked.connect(self.toggle_fullscreen)
        self.square_btn = QPushButton("Square")
        self.square_btn.setStyleSheet("font-size: 12px; background: #4caf50; color: white; border-radius: 6px; padding: 4px 12px;")
        self.square_btn.setFixedHeight(28)
        self.square_btn.clicked.connect(self.toggle_borderless)
        top_bar.addWidget(self.fullscreen_btn)
        top_bar.addWidget(self.square_btn)
        layout.addLayout(top_bar)
        label = QLabel("Select calculator type:")
        label.setStyleSheet("font-size: 16pt; font-weight: bold;")
        layout.addWidget(label)
        btn_std = QPushButton("Standard Calculator")
        btn_std.setSizePolicy(btn_std.sizePolicy().Expanding, btn_std.sizePolicy().Expanding)
        btn_std.setMinimumHeight(40)
        btn_std.setStyleSheet("font-size: 14pt; background: #2196f3; color: white; border: none; border-radius: 6px;")
        btn_std.clicked.connect(self.open_standard)
        layout.addWidget(btn_std)
        btn_geo = QPushButton("Geometry Calculator")
        btn_geo.setSizePolicy(btn_geo.sizePolicy().Expanding, btn_geo.sizePolicy().Expanding)
        btn_geo.setMinimumHeight(40)
        btn_geo.setStyleSheet("font-size: 14pt; background: #009688; color: white; border: none; border-radius: 6px;")
        btn_geo.clicked.connect(self.open_geometry)
        layout.addWidget(btn_geo)
        self.setLayout(layout)

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
            self.fullscreen_btn.setText("Full Screen")
        else:
            self.showFullScreen()
            self.fullscreen_btn.setText("Exit Full Screen")

    def toggle_borderless(self):
        if self.windowFlags() & Qt.FramelessWindowHint:
            self.setWindowFlags(self.windowFlags() & ~Qt.FramelessWindowHint)
            self.showNormal()
            self.square_btn.setText("Square")
        else:
            self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
            self.showNormal()
            self.square_btn.setText("Exit Square")

    def open_standard(self):
        self.std_dlg = StandardCalculator()
        self.std_dlg.show()
    def open_geometry(self):
        self.geo_dlg = GeometryCalculator()
        self.geo_dlg.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
