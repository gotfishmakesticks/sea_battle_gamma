from tkinter import *
check = True
class Field:

    def __init__(self, win, row, column, state):
        frame = Frame(win)
        frame.grid(row=row, column=column, padx=10, pady=10)

        # Словарь кнопок
        btn_dict, btn_key = {}, 0

        # Словарь букв для поля
        letters = {1: 'А', 2: 'Б', 3: 'В', 4: 'Г', 5: 'Д', 6: 'Е', 7: 'Ж', 8: 'З', 9: 'И', 10: 'К'}

        for row in range(11):
            for column in range(11):
                if row == 0:
                    if column >= 1:
                        # Выводим буквы по горизонтали
                        Label(frame, text=f'{column}').grid(row=row, column=column)
                else:
                    if column == 0:
                        # Заполняем буквы по вертикали
                        Label(frame, text=f'{letters[row]}').grid(row=row, column=column)
                    else:
                        # Создаём кнопку и помещаем её в словарь
                        btn_dict[btn_key] = Button(frame, width=4, height=2, state=state, command=lambda btn=btn_key: self.attack(btn_dict[btn]))
                        btn_dict[btn_key].grid(row=row, column=column)
                        btn_key += 1

    # Обработчик кнопки для пройденной атаки
    def attack(self, btn):
        global check
        btn['text'] = '*'
        btn['state'] = 'disabled'
        if check:
            check = False
        else:
            check = True
