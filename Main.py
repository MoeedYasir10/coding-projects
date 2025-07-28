from tkinter import *

window = Tk()
window.title('Calculator')
window.geometry('540x600')

def clearText():
    screenLabel.configure(text="")

def clickZero():
    Text = screenLabel.cget('text')
    Text = Text + '0'
    screenLabel.configure(text = Text)

def clickOne():
    Text = screenLabel.cget('text')
    Text = Text + '1'
    screenLabel.configure(text = Text)

def clickTwo():
    Text = screenLabel.cget('text')
    Text = Text + '2'
    screenLabel.configure(text = Text)

def clickThree():
    Text = screenLabel.cget('text')
    Text = Text + '3'
    screenLabel.configure(text = Text)

def clickFour():
    Text = screenLabel.cget('text')
    Text = Text + '4'
    screenLabel.configure(text = Text)

def clickFive():
    Text = screenLabel.cget('text')
    Text = Text + '5'
    screenLabel.configure(text = Text)

def clickSix():
    Text = screenLabel.cget('text')
    Text = Text + '6'
    screenLabel.configure(text = Text)

def clickSeven():
    Text = screenLabel.cget('text')
    Text = Text + '7'
    screenLabel.configure(text = Text)

def clickEight():
    Text = screenLabel.cget('text')
    Text = Text + '8'
    screenLabel.configure(text = Text)

def clickNine():
    Text = screenLabel.cget('text')
    Text = Text + '9'
    screenLabel.configure(text = Text)

def clickDot():
    Text = screenLabel.cget('text')
    Text = Text + '.'
    screenLabel.configure(text = Text)

def clickPlus():
    Text = screenLabel.cget('text')
    screenLabel.configure(text = '')
    LblNum1.configure(text = Text)
    LblOp.configure(text = '+')

def clickMinus():
    Text = screenLabel.cget('text')
    screenLabel.configure(text = '')
    LblNum1.configure(text = Text)
    LblOp.configure(text = '-')


def clickTimes():
    Text = screenLabel.cget('text')
    screenLabel.configure(text='')
    LblNum1.configure(text=Text)
    LblOp.configure(text='X')


def clickDivide():
    Text = screenLabel.cget('text')
    screenLabel.configure(text='')
    LblNum1.configure(text=Text)
    LblOp.configure(text='/')

def clickEquals():
    Text = screenLabel.cget('text')
    screenLabel.configure(text = '')
    Num1 = LblNum1.cget('text')
    operator = LblOp.cget('text')
    N1 = float(Num1)
    N2 = float(Text)

def clickPercentage():
    Text = screenLabel.cget('text')
    screenLabel.configure(text = '')
    N1 = float(Text)
    result = N1 / 100
    screenLabel.configure(text = str(result))

def clickC():
    LblNum1.configure(text = '')
    LblOp.configure(text = '')
    screenLabel.configure(text = '')


    if (operator == '+'):
        result = N1 + N2
        screenLabel.configure(text = str(result))
    elif(operator == '-'):
        result = N1 - N2
        screenLabel.configure(text = str(result))
    elif (operator == 'X'):
        result = N1 * N2
        screenLabel.configure(text = str(result))
    elif (operator == '/'):
        result = N1 / N2
        screenLabel.configure(text = str(result))


LblNum1 = Label(window, text = '')
LblOp = Label(window, text = '')


screenLabel = Label(window, text = '', width = 60, height = 5, bg = 'black', fg = 'white')
screenLabel.place(x = 0, y = 0)
button01 = Button(window, text = 'AC', width = 10, height = 5,  command = clearText)
button01.place(x = 0, y = 100)
button02 = Button(window, text = 'C', width = 10, height = 5, command = clickC)
button02.place(x = 135, y = 100)
button03 = Button(window, text = '%', width = 10, height = 5, command = clickPercentage)
button03.place(x = 270, y = 100)
button04 = Button(window, text = '/', width = 10, height = 5, command=clickDivide)
button04.place(x = 405, y = 100)
button05 = Button(window, text = '7', width = 10, height = 5, command = clickSeven)
button05.place(x = 0, y = 200)
button06 = Button(window, text = '8', width = 10, height = 5,  command = clickEight)
button06.place(x = 135, y = 200)
button07 = Button(window, text = '9', width = 10, height = 5,  command = clickNine)
button07.place(x = 270, y = 200)
button08 = Button(window, text = 'X', width = 10, height = 5, command = clickTimes)
button08.place(x = 405, y = 200)
button09 = Button(window, text = '4', width = 10, height = 5, command = clickFour)
button09.place(x =  0, y = 300)
button10 = Button(window, text = '5', width = 10, height = 5, command = clickFive)
button10.place(x = 135, y = 300)
button10 = Button(window, text = '6', width = 10, height = 5, command = clickSix)
button10.place(x = 270, y = 300)
button11 = Button(window, text = '-', width = 10, height = 5, command = clickMinus)
button11.place(x = 405, y = 300)
button12 = Button(window, text = '1', width = 10, height = 5, command = clickOne)
button12.place(x = 0, y = 400)
button13 = Button(window, text = '2', width = 10, height = 5, command = clickTwo)
button13.place(x = 135, y = 400)
button14 = Button(window, text = '3', width = 10, height = 5, command = clickThree)
button14.place(x = 270, y = 400)
button15 = Button(window, text = '+', width = 10, height = 5, command = clickPlus)
button15.place(x = 405, y = 400)
button16 = Button(window, text = '0', width = 20, height = 5, command=clickZero)
button16.place(x = 0, y = 500)
button17 = Button(window, text = '.' ,width = 10, height = 5 , command = clickDot)
button17.place(x = 225, y = 500)
button18 = Button(window, text = '=', width = 10, height = 5, command = clickEquals)
button18.place(x = 360, y = 500)
window.mainloop()