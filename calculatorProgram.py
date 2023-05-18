from tkinter import*

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total= str(eval(equation_text))
        equation_label.set(total)
        equation_text = total  

    except ZeroDivisionError:
        equation_label.set("Math ERROR")

        equation_text = ""

    except SyntaxError:
        equation_label.set("Syntax ERROR")

        equation_text = ""

def clear():
    global equation_text

    equation_label.set("")

    equation_text = ""


window = Tk()

window.title("Calculator Program")
window.geometry("380x320")


equation_text = ""


equation_label = StringVar()


label = Label(window,textvariable=equation_label,font=("Consolas,25"),bg="light grey",width=25,height=3)
label.pack()


frame = Frame(window)
frame.pack()

button1 = Button(frame,text = 1,height=2,width=9,font=35,command=lambda:button_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame,text = 2,height=2,width=9,font=35,command=lambda:button_press(2))
button2.grid(row=0,column=1)

button3 = Button(frame,text = 3,height=2,width=9,font=35,command=lambda:button_press(3))
button3.grid(row=0,column=2)

button4 = Button(frame,text = 4,height=2,width=9,font=35,command=lambda:button_press(4))
button4.grid(row=1,column=0)

button5 = Button(frame,text = 5,height=2,width=9,font=35,command=lambda:button_press(2))
button5.grid(row=1,column=1)

button6 = Button(frame,text = 6,height=2,width=9,font=35,command=lambda:button_press(6))
button6.grid(row=1,column=2)

button7 = Button(frame,text = 7,height=2,width=9,font=35,command=lambda:button_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame,text = 8,height=2,width=9,font=35,command=lambda:button_press(8))
button8.grid(row=2,column=1)

button9 = Button(frame,text = 9,height=2,width=9,font=35,command=lambda:button_press(9))
button9.grid(row=2,column=2)

button9 = Button(frame,text = 0,height=2,width=9,font=35,command=lambda:button_press(0))
button9.grid(row=3,column=1)

plus = Button(frame,text = "+",height=2,width=9,font=35,command=lambda:button_press("+"))
plus.grid(row=0,column=3)

substract = Button(frame,text = "-",height=2,width=9,font=35,command=lambda:button_press("-"))
substract.grid(row=1,column=3)

multiply = Button(frame,text = "x",height=2,width=9,font=35,command=lambda:button_press("*"))
multiply.grid(row=2,column=3)

division = Button(frame,text = "/",height=2,width=9,font=35,command=lambda:button_press("/"))
division.grid(row=3,column=3)

equals = Button(frame,text = "=",height=2,width=9,font=35,command=equals)
equals.grid(row=3,column=2)

decimal = Button(frame,text = ".",height=2,width=9,font=35,command=lambda:button_press("."))
decimal.grid(row=3,column=0)

clear = Button(window,text = "Clear",height=2,width=9,font=35,command=clear)
clear.pack()





window.mainloop()