from tkinter import *
from tkinter import messagebox
root = Tk()

check = True #переменная проверки, кто ходит

f1ships, f2ships = [], []
buttonlist = []
xslist = ["*", "X", "XX"]
shipcount = [0, 0]

class Ship:
    global f1ships, f2ships
    def __init__(self, field, x, y, size, rotation):

        self.field = field
        self.x = x
        self.y = y
        self.size = size
        self.rotation = rotation

        btn_key = (y - 1) * 10 + x - 1
        if field == f1 and rotation != "null":
            f1ships.append([self, [], [], rotation, size])
            shipcount[0] += 1
            ID = len(f1ships)-1
        else:
            f2ships.append([self, [], [], rotation, size])
            shipcount[1] += 1
            ID = len(f2ships)-1
        match(rotation):
            case "east":
                for row in range(x, x + size):
                    field.btn_dict[btn_key]["text"] = "S" + str(row - x + 1)
                    btn_key += 1
                    if field == f1:
                        f1ships[ID][1].append(row)
                        f1ships[ID][2].append(y)
                    else:
                        f2ships[ID][1].append(row)
                        f2ships[ID][2].append(y)
            case "south":
                for column in range(y, y + size):
                    field.btn_dict[btn_key]["text"] = "S" + str(column - y + 1)
                    btn_key += 10
                    if field == f1:
                        f1ships[ID][1].append(x)
                        f1ships[ID][2].append(column)
                    else:
                        f2ships[ID][1].append(x)
                        f2ships[ID][2].append(column)
            case "null":
                pass
            case other:
                raise ValueError

    def checkforx(self):

        match(self.rotation):
            case "east":
                xs = 0
                btn_key = (self.y - 1) * 10 + self.x - 1
                for row in range(self.x, self.x + self.size):
                    if self.field.btn_dict[btn_key]["text"] == "X":
                        xs += 1
                    btn_key += 1
                if xs == self.size:
                    for row in range(self.x, self.x + self.size):
                        self.field.btn_dict[btn_key - 1]["text"] = "XX"
                        btn_key -= 1
                    if self.field == f1:
                        shipcount[0] -= 1
                        print(shipcount)
                        if shipcount[0] == 0:
                            messagebox.showinfo("", "Победа 2 игрока")
                            for i in range(100):
                                self.field.btn_dict[i]["state"] = "disabled"
                                f2.btn_dict[i]["state"] = "disabled"
                    else:
                        shipcount[1] -= 1
                        print(shipcount)
                        if shipcount[1] == 0:
                            messagebox.showinfo("", "Победа 1 игрока")
                            for i in range(100):
                                self.field.btn_dict[i]["state"] = "disabled"
                                f2.btn_dict[i]["state"] = "disabled"
            case "south":
                xs = 0
                btn_key = (self.y - 1) * 10 + self.x - 1
                for row in range(self.y, self.y + self.size):
                    if self.field.btn_dict[btn_key]["text"] == "X":
                        xs += 1
                    btn_key += 10
                if xs == self.size:
                    for row in range(self.y, self.y + self.size):
                        self.field.btn_dict[btn_key - 10]["text"] = "XX"
                        btn_key -= 10
                    if self.field == f1:
                        shipcount[0] -= 1
                        print(shipcount)
                        if shipcount[0] == 0:
                            messagebox.showinfo("", "Победа 2 игрока")
                            for i in range(100):
                                self.field.btn_dict[i]["state"] = "disabled"
                                f1.btn_dict[i]["state"] = "disabled"
                    else:
                        shipcount[1] -= 1
                        print(shipcount)
                        if shipcount[1] == 0:
                            messagebox.showinfo("", "Победа 1 игрока")
                            for i in range(100):
                                self.field.btn_dict[i]["state"] = "disabled"
                                f1.btn_dict[i]["state"] = "disabled"

class Field:

    def __init__(self, win, row, column, state):
        global buttonlist
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
                        x = btn_key % 10 + 1
                        y = btn_key // 10 + 1
                        self.btn_dict[btn_key] = Button(self.frame, width=4, height=2, state=state, command=lambda btn=btn_key: self.attack(self.btn_dict[btn], x, y))
                        self.btn_dict[btn_key].grid(row=row, column=column)
                        buttonlist.append([self.ID, self.btn_dict[btn_key], x, y, btn_key])
                        btn_key += 1

    # Обработчик кнопки для пройденной атаки
    def attack(self, btn, x, y):
        global check
        global xslist
        btn_key = 0
        if btn["text"] == "":
            btn['text'] = '*'
            btn['state'] = 'disabled'
        else:
            btn["text"] = "X"
            btn["state"] = "disabled"

        shipid = nullship
        for i in range(len(buttonlist)):
            if buttonlist[i][1] == btn:
                x = buttonlist[i][2]
                y = buttonlist[i][3]
                btn_key = buttonlist[i][4]

        if check and self.ID == 1:
            cringe = 0
            for row in range(0, 100):
                if not (f1.btn_dict[cringe]["text"] in xslist):
                    f1.btn_dict[cringe]["state"] = "active"
                self.btn_dict[cringe]["state"] = "disabled"
                cringe += 1
            for i in range(len(f2ships)):
                for xx in range(len(f2ships[i][1])):
                    for yy in range(len(f2ships[i][2])):

                        if x == f2ships[i][1][xx] and y == f2ships[i][2][yy]:
                            shipid = f2ships[i][0]
                            shipid.checkforx()
            check = False
        elif check is False and self.ID == 0:
            cringe = 0
            for row in range(0, 100):
                if not (f2.btn_dict[cringe]["text"] in xslist):
                    f2.btn_dict[cringe]["state"] = "active"
                self.btn_dict[cringe]["state"] = "disabled"
                cringe += 1
            for i in range(len(f1ships)):
                for xx in range(len(f1ships[i][1])):
                    for yy in range(len(f1ships[i][2])):
                        if x == f1ships[i][1][xx] and y == f1ships[i][2][yy]:
                            shipid = f1ships[i][0]
                            shipid.checkforx()
            check = True


f1, f2 = Field(root, 0, 0, "disabled"), Field(root, 0, 1, "active")

nullship = Ship(f1, -1, -1, -1, "null")

p1 = Ship(f1, 1, 1, 1, "east")
p2 = Ship(f1, 10, 1, 1, "east")
p3 = Ship(f1, 1, 10, 1, "east")
p4 = Ship(f1, 10, 10, 1, "east")

p5 = Ship(f1, 3, 1, 2, "south")
p6 = Ship(f1, 10, 3, 2, "south")
p7 = Ship(f1, 1, 8, 2, "east")

p8 = Ship(f1, 5, 1, 3, "south")
p9 = Ship(f1, 1, 4, 3, "east")

p10 = Ship(f1, 4, 9, 4, "east")


q1 = Ship(f2, 1, 1, 1, "east")
q2 = Ship(f2, 3, 10, 1, "east")
q3 = Ship(f2, 5, 6, 1, "east")
q4 = Ship(f2, 9, 3, 1, "east")

q5 = Ship(f2, 1, 7, 2, "south")
q6 = Ship(f2, 7, 1, 2, "east")
q7 = Ship(f2, 5, 10, 2, "east")

q8 = Ship(f2, 3, 2, 3, "south")
q9 = Ship(f2, 5, 4, 3, "east")

q10 = Ship(f2, 10, 5, 4, "south")

shipcount[1] -= 1
print(shipcount)

root.mainloop()
