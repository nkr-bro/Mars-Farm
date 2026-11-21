from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QGridLayout,QLabel,QVBoxLayout,QHBoxLayout
import field
import numpy as np
from PySide6.QtCore import Qt
from field import n,water
app = QApplication()
window = QWidget()
window.setWindowTitle("Mars Farm")
window.setObjectName("farmWindow")
window.setStyleSheet("QWidget#farmWindow { background-color: darkolivegreen; }")
button_1 = QPushButton("Dry Sail")
button_2 = QPushButton("Water plot")
button_3 = QPushButton("Next day")
exit_button = QPushButton("Exit")
button_3.setMinimumHeight(64)
button_3.setStyleSheet("font-size: 24px;font-weight: bold;")
rules_label = QLabel(
    "MARS FARM\n\n"
    "Your colony on Mars is running out of food. "
    "Harvest at least 12 plants by the end of Day 10 to save it.\n\n"
    "HOW TO PLAY\n\n"
    "1. Click a plot to water it. You can water up to 3 plots per day.\n\n"
    "2. Press Next Day to make watered plants grow. "
    "You can end the day even if you have water left.\n\n"
    "3. Water the same plot on two different days to harvest one plant.    \n\nThis is my second project, so please go easy on me!"
)

rules_label.setWordWrap(True)
rules_label.setStyleSheet("font-size: 20px; color: white;")
layout = QGridLayout(window)
water_label = QLabel("Water:3")
day_label = QLabel("Day: 1/10")
info_label = QHBoxLayout()
info_label.addWidget(water_label)
info_label.addWidget(day_label)
layout.addLayout(info_label,1,0,1,2)
layout.setRowStretch(0,1)
field_layout = QGridLayout()
layout.addLayout(field_layout, 0,0)
layout.setAlignment(field_layout,Qt.AlignmentFlag.AlignCenter)
field_layout.addWidget(button_1,0,0)
rows,cols = n.shape
plots = []
plots.append(button_1)
for row in range(rows):
    for col in range(cols):
        if row == 0 and col  == 0:
            continue
        else:
            plot = QPushButton("Dry Soil")
            plots.append(plot)
            button_1.setFixedSize(160, 160)
            plot.setFixedSize(160,160)
            field_layout.addWidget(plot,row,col)
            plot.clicked.connect(
                lambda  checket = False,r = row,c = col,button = plot : water_plot(r,c,button)
            )

controls_layout = QVBoxLayout()
controls_layout.addWidget(button_2)
layout.addLayout(controls_layout,0,1)
controls_layout.addWidget(button_3)
controls_layout.addWidget(exit_button)
hint_label = QLabel("Click a plot to water it.")
controls_layout.addWidget(hint_label)
controls_layout.addSpacing(24)
controls_layout.addWidget(rules_label)
controls_layout.addStretch()
water_left = 3
again_button = QPushButton("Play again")
harvest_label = QLabel("Harvest:0/12")
info_label.addWidget(harvest_label)
reult_label = QWidget(window)
result_label = QLabel("Result:")
reult_label.hide()
gh = QVBoxLayout(reult_label)
gh.addStretch()
gh.addWidget(result_label)
gh.addWidget(again_button)
gh.addStretch()
again_button.setStyleSheet("background-color: firebrick;color: white")
watered =False


def water_plot(row,col,button):
    global water_left,watered
    if water[row,col]:
        hint_label.setText("This plot is already watered.")
        return
    if water_left == 0:
        hint_label.setText("No water left. Press Next Day.")
        return
    water_left -= 1
    water_label.setText(f"Water:{water_left}")
    button.setText("watered")
    button.setStyleSheet("background-color: saddlebrown;color: white")
    water[row,col] = True
gh.setAlignment(result_label,Qt.AlignmentFlag.AlignCenter)
day = 1
harvest = 0
def next_day():
    global water_left,watered,day,plots,harvest
    n[water] += 1
    water.fill(False)
    riqe = n >= 2
    h = np.count_nonzero(riqe)
    harvest += h
    n[riqe] = 0
    harvest_label.setText(f"Harvest:{harvest}/12")
    if day == 10:
        if harvest >= 12:
            result_label.setText("You Win !")
        else:
            result_label.setText("You looz")
        for i in plots:
            i.setEnabled(False)
        reult_label.setGeometry(window.rect())
        reult_label.show()
        reult_label.raise_()
        button_3.setEnabled(False)
        return
    day += 1

    day_label.setText(f"Day:{day}/10")
    water_left = 3
    hint_label.setText("Click a plot to water it.")
    water_label.setText(f"Water:{water_left}")
    watered = False
    button_1.setText("Dry Sail")
    button_1.setStyleSheet("border-image: url('assets/dry.png') ; color: white")
    for i in plots:
        i.setText("Dry Soil")
        i.setStyleSheet("background-color: peru ;color: white")
    if n[0,0] == 1:
        button_1.setText("Sprout (1/2)")
    if n[0,1] == 1:
        plots[1].setText("Sprout (1/2)")
    if n[0,2] == 1:
        plots[2].setText("Sprout (1/2)")
    if n[0,3] == 1:
        plots[3].setText("Sprout (1/2)")

    if n[1,0] == 1:
        plots[4].setText("Sprout (1/2)")
    if n[1,1] == 1:
        plots[5].setText("Sprout (1/2)")
    if n[1,2] == 1:
        plots[6].setText("Sprout (1/2)")
    if n[1,3] == 1:
        plots[7].setText("Sprout (1/2)")

    if n[2,0] == 1:
        plots[8].setText("Sprout (1/2)")
    if n[2,1] == 1:
        plots[9].setText("Sprout (1/2)")
    if n[2,2] == 1:
        plots[10].setText("Sprout (1/2)")
    if n[2,3] == 1:
        plots[11].setText("Sprout (1/2)")

    if n[3,0] == 1:
        plots[12].setText("Sprout (1/2)")
    if n[3,1] == 1:
        plots[13].setText("Sprout (1/2)")
    if n[3,2] == 1:
        plots[14].setText("Sprout (1/2)")
    if n[3,3] == 1:
        plots[15].setText("Sprout (1/2)")
exit_button.clicked.connect(window.close)

reult_label.setStyleSheet("font-size: 56px;font-weight: bold;color: white")
def restart_game():
    global day,harvest,plots,water_left
    day = 1
    harvest = 0
    water_left = 3
    hint_label.setText("Click a plot to water it.")
    n.fill(0)
    water.fill(False)
    water_label.setText(f"Water:{water_left}")
    harvest_label.setText(f"Harvest:{harvest}/12")
    day_label.setText(f"Day:{day}/10")
    for i in plots:
        i.setEnabled(True)
        i.setText("Dry Soil")
        i.setStyleSheet("background-color: peru ; color: white")
    button_3.setEnabled(True)
    reult_label.hide()
def water_1_plot():
    water_plot(0,0,button_1)
for label in (water_label,day_label,harvest_label):
    label.setStyleSheet("font-size: 28px; font-weight: bold; color: white;")
again_button.clicked.connect(restart_game)
button_3.clicked.connect(next_day)
button_1.clicked.connect(water_1_plot)
print(n.shape)
window.showFullScreen()
app.exec()