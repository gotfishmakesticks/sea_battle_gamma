from tkinter import *
from Field import Field

root = Tk()
f1, f2 = Field(root, 0, 0, "disabled"), Field(root, 0, 1, "active")


check = True

if check:
    for row in range(11):
        for column in range(11):
            if row >= 1 & column>=1:
                global btn_dict
                global btn_key
                # Создаём кнопку и помещаем её в словарь
                # btn_dict[btn_key] = Button(frame, width=4, height=2, state=state, command=lambda btn=btn_key: self.attack(btn_dict[btn]))
                # btn_dict[btn_key].grid(row=row, column=column)
                # btn_key += 1
else:
    f1["state"] = "disabled"
    f2["state"] = "active"
root.mainloop()