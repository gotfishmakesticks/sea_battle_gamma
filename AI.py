'''Примерная работа ИИ'''

from tkinter import *
import random as rnd

root = Tk()

# класс ИИ
class AI:

    def __init__(self):
        self.rnd_x = rnd.randint(0, 2)
        self.rnd_y = rnd.randint(0, 2)

frame = Frame(root)
frame.grid(row=0, column=0)

# Вызов ИИ
ai = AI()
x, y = ai.rnd_x, ai.rnd_y

# Для попадания
x_bot = [x+1, x-1]
y_bot = [y+1, y-1]


btn_dict = dict()

for i in range(3):
    for j in range(3):
        btn_dict[f'{i}{j}'] = Button(frame, text=f"{i}{j}", width=4, height=2)
        btn_dict[f'{i}{j}'].grid(row=i, column=j)

btn_dict[f'{x}{y}']['state'] = 'disabled'
btn_dict[f'{x}{y}']['text'] = '*'


hurvet = rnd.choice([True, False])
rn = rnd.randint(0, 1)
print(hurvet)
if hurvet == True:
    x = x_bot[rn]
else:
    y = y_bot[rn]

btn_dict[f'{x}{y}']['state'] = 'disabled'
btn_dict[f'{x}{y}']['text'] = '**'

root.mainloop()
