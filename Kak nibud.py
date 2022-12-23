from tkinter import *

root = Tk()

check = True #переменная проверки, кто ходит
class Field:

    def __init__(self, win, row, column, state):
        self.frame = Frame(win)
        self.frame.grid(row=row, column=column, padx=10, pady=10)
        self.ID = column #айдишник фрейма
        # Словарь кнопок
        self.btn_dict, btn_key = {}, 0

        # Словарь букв для поля
        letters = {1: 'А', 2: 'Б', 3: 'В', 4: 'Г', 5: 'Д', 6: 'Е', 7: 'Ж', 8: 'З', 9: 'И', 10: 'К'}

        for row in range(11):
            for column in range(11):
                if row == 0:
                    if column >= 1:
                        # Выводим буквы по горизонтали
                        Label(self.frame, text=f'{column}').grid(row=row, column=column)
                else:
                    if column == 0:
                        # Заполняем буквы по вертикали
                        Label(self.frame, text=f'{letters[row]}').grid(row=row, column=column)
                    else:
                        # Создаём кнопку и помещаем её в словарь
                        self.btn_dict[btn_key] = Button(self.frame, width=4, height=2, state=state, command=lambda btn=btn_key: self.attack(self.btn_dict[btn]))
                        self.btn_dict[btn_key].grid(row=row, column=column)
                        btn_key += 1

    # Обработчик кнопки для пройденной атаки
    def attack(self, btn):
        global check
        btn_key = 0
        btn['text'] = '*'
        btn['state'] = 'disabled'
        print(self.ID)
        if check and self.ID == 1:
            print("Test")
            for row in range(1, 11):
                for column in range(1, 11):
                    f1.btn_dict[btn_key]["state"] = "active"
                    self.btn_dict[btn_key]["state"] = "disabled"
                    btn_key += 1
            check = False
        elif check == False and self.ID == 0:
            print("Test")
            for row in range(1, 11):
                for column in range(1, 11):
                    f2.btn_dict[btn_key]["state"] = "active"
                    self.btn_dict[btn_key]["state"] = "disabled"
                    btn_key += 1
            check = True
        #else:
            #print("Test Not")
            #check = True


f1, f2 = Field(root, 0, 0, "disabled"), Field(root, 0, 1, "active")

root.mainloop()
