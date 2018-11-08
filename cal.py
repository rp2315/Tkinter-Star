
from tkinter import *

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)      
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op): 
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0
  
    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

sum1 = Calc()
top= Tk()
calc = Frame(top)
calc.grid()

top.title("Calculator")
text_box = Entry(calc, justify = RIGHT, bd = 2, fg = "black")
text_box.grid(row = 0, column = 0, columnspan = 4, pady = 5)
text_box.insert(0, "0")

numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(Button(calc, text = numbers[i], width=3, height=1))
        bttn[i].grid(row = j, column = k, padx = 5, pady = 5)
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

b = Button(calc, text = "0", width=3, height=1)
b["command"] = lambda: sum1.num_press(0)
b.grid(row = 4, column = 0, padx = 5, pady = 5)

b1 = Button(calc, text = chr(247), width=3, height=1)
b1["command"] = lambda: sum1.operation("divide")
b1.grid(row = 1, column = 3, padx = 5, pady = 5)

b2 = Button(calc, text = "EXIT", width=3, height=1)
b2["command"] = top.destroy
b2.grid(row = 5, column = 0, padx = 5, pady = 5)

b3= Button(calc, text = chr(215), width=3, height=1)
b3["command"] = lambda: sum1.operation("times")
b3.grid(row = 2, column = 3, padx = 5, pady = 5)

b4 = Button(calc, text = "-", width=3, height=1)
b4["command"] = lambda: sum1.operation("minus")
b4.grid(row = 3, column = 3, padx = 5, pady = 5)

b5= Button(calc, text = ".", width=3, height=1)
b5["command"] = lambda: sum1.num_press(".")
b5.grid(row = 4, column = 1, padx = 5, pady = 5)

b6 = Button(calc, text = "+", width=3, height=1)
b6["command"] = lambda: sum1.operation("add")
b6.grid(row = 4, column = 3, padx = 5, pady = 5)

b7= Button(calc, text =  chr(177), width=3, height=1)
b7["command"] = sum1.sign
b7.grid(row = 5, column = 3, padx = 5, pady = 5)

b8= Button(calc, text = "C", width=3, height=1)
b8["command"] = sum1.cancel
b8.grid(row = 5, column = 1, padx = 5, pady = 5)

b9 = Button(calc, text = "AC", width=3, height=1)
b9["command"] = sum1.all_cancel
b9.grid(row = 5, column = 2, padx = 5, pady = 5)

b10 = Button(calc, text = "=", width=3, height=1)
b10["command"] = sum1.calc_total
b10.grid(row = 4, column = 2, padx = 5, pady = 5)

top.mainloop()
