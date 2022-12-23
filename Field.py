from tkinter import *


class Field:

    def __init__(self, win, row, column):
        frame = Frame(win)
        frame.grid(row=row, column=column, padx=10, pady=10)

        for row in range(11):
            for column in range(11):
                if row == 0:
                    if column >= 1:
                        # Выводим буквы по горизонтали
                        Label(frame_bot, text=f'{column}').grid(row=row, column=column)
                else:
                    if column == 0:
                        # Заполняем буквы по вертикали
                        Label(frame_bot, text=f'{letters[row]}').grid(row=row, column=column)
                    else:
                        # Создаём кнопку и помещаем её в словарь
                        btn_bot_dict[btn_key] = tk.Button(frame_bot, width=4, height=2, command=lambda btn=btn_key: attack(btn_bot_dict[btn]))
                        btn_bot_dict[btn_key].grid(row=row, column=column)
                        btn_key += 1