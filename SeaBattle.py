import tkinter as tk


# Создание формы
root = tk.Tk()
root.title('Sea Battle')
root.resizable(width=False, height=False)

# Создание поля для расположения элементов
frame_main = tk.Frame(root)
frame_main.grid()

# Словарь букв для поля
letters = {0: ' ', 1: 'А', 2: 'Б', 3: 'В', 4: 'Г', 5: 'Д', 6: 'Е', 7: 'Ж', 8: 'З', 9: 'И', 10: 'К'}



'''Создание поля с кнопками и буквами'''

'''Поле пользователя (то есть то, на котором располагаются корабли пользователя)'''

# Место для расположения элементов
frame_user = tk.Frame(frame_main, padx=3, pady=3)
frame_user.grid(row=0, column=0)

# Список кнопок (если не сработает, то меняю на словарь... Пока работает, но если понадобиться обработчик, то придётся использовать словарь)
btn_user_list = []

# Генирируем поле
for row in range(11):
    for column in range(11):
        if row == 0:
            # Выводим буквы по горизонтали
            tk.Label(frame_user, text=f'{letters[column]}').grid(row=row, column=column)
        else:
            if column == 0:
                # Выводм буквы по вертикали
                tk.Label(frame_user, text=f'{letters[row]}').grid(row=row, column=column)
            else:
                # Создаём кнопку в списке
                btn_user_list.append(tk.Button(frame_user, width=4, height=2, state="disabled").grid(row=row, column=column))


'''Поле бота (то есть то, которое нужно атаковать)'''

# Место для расположения элементов
frame_bot = tk.Frame(frame_main)
frame_bot.grid(row=0, column=1)

# Обработчик кнопки для пройденной атаки
def attack(btn):
    btn['text'] = '*'
    btn['state'] = 'disabled'

# Словарь кнопок
btn_bot_dict, btn_key = {}, 0

# Генирируем поле
for row in range(11):
    for column in range(11):
        if row == 0:
            # Заполяем буквы по горизонтали
            tk.Label(frame_bot, text=f'{letters[column]}').grid(row=row, column=column)
        else:
            if column == 0:
                # Заполняем буквы по вертикали
                tk.Label(frame_bot, text=f'{letters[row]}').grid(row=row, column=column)
            else:
                # Создаём кнопку и помещаем её в словарь
                btn_bot_dict[btn_key] = tk.Button(frame_bot, width=4, height=2, command=lambda btn=btn_key: attack(btn_bot_dict[btn]))
                btn_bot_dict[btn_key].grid(row=row, column=column)
                btn_key += 1

root.mainloop()
