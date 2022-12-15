import tkinter as tk


# Создание формы
root = tk.Tk()
root.title('Sea Battle')
root.resizable(width=False, height=False)

# Создание поля для расположения элементов
frame_main = tk.Frame(root)
frame_main.grid()

# Словарь букв для поля
letters = {1: 'А', 2: 'Б', 3: 'В', 4: 'Г', 5: 'Д', 6: 'Е', 7: 'Ж', 8: 'З', 9: 'И', 10: 'К'}



'''Создание поля с кнопками и буквами'''

# Обработчик кнопки для пройденной атаки
check = True
def attack(btn, dict1, dict2):
    global check
    btn['text'] = '*'
    btn['state'] = 'disabled'
    for key, value in dict1.items():
        dict1[key]['state'] = 'disabled'
    for key, value in dict2.items():
        if dict2[key]['text'] != '*':
            dict2[key]['state'] = 'disabled'
        else:
            dict2[key]['state'] = 'active'

'''Поле пользователя (то есть то, на котором располагаются корабли пользователя)'''

# Место для расположения элементов
frame_user = tk.Frame(frame_main, padx=3, pady=3)
frame_user.grid(row=0, column=0)

# Список кнопок (если не сработает, то меняю на словарь... Пока работает, но если понадобиться обработчик, то придётся использовать словарь)
btn_user_dict, btn_user_key = {}, 0

# Генирируем поле
for row in range(11):
    for column in range(11):
        if row == 0:
            if column >= 1:
                # Выводим буквы по горизонтали
                tk.Label(frame_user, text=f'{column}').grid(row=row, column=column)
        else:
            if column == 0:
                # Выводм буквы по вертикали
                tk.Label(frame_user, text=f'{letters[row]}').grid(row=row, column=column)
            else:
                # Создаём кнопку в списке
                btn_user_dict[btn_user_key] = tk.Button(frame_user, width=4, height=2, state="disabled", command=lambda btn=btn_user_key, dict1=btn_user_dict, dict2=btn_bot_dict: attack(btn_user_dict[btn], dict1, dict2))
                btn_user_dict[btn_user_key].grid(row=row, column=column)
                btn_user_key += 1


'''Поле бота (то есть то, которое нужно атаковать)'''

# Место для расположения элементов
frame_bot = tk.Frame(frame_main)
frame_bot.grid(row=0, column=1)

# Словарь кнопок
btn_bot_dict, btn_bot_key = {}, 0

# Генирируем поле
for row in range(11):
    for column in range(11):
        if row == 0:
            if column >= 1:
                # Выводим буквы по горизонтали
                tk.Label(frame_bot, text=f'{column}').grid(row=row, column=column)
        else:
            if column == 0:
                # Заполняем буквы по вертикали
                tk.Label(frame_bot, text=f'{letters[row]}').grid(row=row, column=column)
            else:
                # Создаём кнопку и помещаем её в словарь
                btn_bot_dict[btn_bot_key] = tk.Button(frame_bot, width=4, height=2, command=lambda btn=btn_bot_key: attack(btn_bot_dict[btn]))
                btn_bot_dict[btn_bot_key].grid(row=row, column=column)
                btn_bot_key += 1


'''Состояние игры'''

# Блокировка раблокировка полей
while True:
    amount = 0
    if check == True:
        for key, value in btn_bot_dict.items():
            if btn_bot_dict[key]['text'] != '*':
                btn_bot_dict[key]['state'] = 'disabled'
            else:
                amount += 1
        for key, value in btn_user_dict.items():
            if btn_user_dict[key]['text'] != '*':
                btn_user_dict[key]['state'] = 'active'
        if amount == 100:
            break
    else:
        for key, value in btn_bot_dict.items():
            if btn_bot_dict[key]['text'] != '*':
                btn_bot_dict[key]['state'] = 'active'
        for key, value in btn_user_dict.items():
            if btn_user_dict[key]['text'] != '*':
                btn_user_dict[key]['state'] = 'disabled'
        if amount == 100:
            break


root.mainloop()
