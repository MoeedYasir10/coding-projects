from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.title("currency convertor")
screen.geometry("1200x700")

def convertCurrency():
    username = NameText.get('1.0', END)
    choosenCurrency = currency.get(currency.curselection())
    amount = int(AmountText.get('1.0', END))
    convertTo = convertListBox.get(convertListBox.curselection())
    answear = 0

    if (choosenCurrency == 'Dollars'):
        if (convertTo == 'Dollars'):
            answear = amount
        elif (convertTo == 'Pound'):
            answear = amount * 0.74
        elif (convertTo == 'Euro'):
            answear = amount * 0.86
        elif (convertTo == 'INR'):
            answear = amount * 86.01
        elif (convertTo == 'PKR'):
            answear = amount * 284.63
        elif (convertTo == 'Yen'):
            answear = amount * 147.35
        elif (convertTo == 'AED'):
            answear  = amount * 3.67
    elif (choosenCurrency == 'Pound'):
        if (convertTo == 'Dollars'):
            answear = amount * 1.35
        elif (convertTo == 'Pound'):
            answear = amount
        elif (convertTo == 'Euro'):
            answear = amount * 1.15
        elif (convertTo == 'INR'):
            answear = amount * 115.88
        elif (convertTo == 'PKR'):
            answear = amount * 384.26
        elif (convertTo == 'Yen'):
            answear = amount * 198.56
        elif (convertTo == 'AED'):
            answear = amount * 4.95
    elif (choosenCurrency == 'Euro'):
        if (convertTo == 'Dollars'):
            answear = amount * 1.17
        elif (convertTo == 'Pound'):
            answear = amount * 0.87
        elif (convertTo == 'Euro'):
            answear = amount
        elif (convertTo == 'INR'):
            answear = amount * 100.48
        elif (convertTo == 'PKR'):
            answear = amount * 332.87
        elif (convertTo == 'Yen'):
            answear = amount * 172.21
        elif (convertTo == 'AED'):
            answear = amount * 4.29
    elif (choosenCurrency == 'INR'):
        if (convertTo == 'Dollars'):
            answear = amount * 0.012
        elif (convertTo == 'Pound'):
            answear = amount * 0.0087
        elif (convertTo == 'Euro'):
            answear = amount * 0.0100
        elif (convertTo == 'INR'):
            answear = amount * 1
        elif (convertTo == 'PKR'):
            answear = amount * 3.31
        elif (convertTo == 'Yen'):
            answear = amount * 1.73
        elif (convertTo == 'AED'):
            answear = amount * 0.043
    elif (choosenCurrency == 'PKR'):
        if (convertTo == 'Dollars'):
            answear = amount * 0.0035
        elif (convertTo == 'Pound'):
            answear = amount * 0.0026
        elif (convertTo == 'Euro'):
            answear = amount * 0.0030
        elif (convertTo == 'INR'):
            answear = amount * 0.30
        elif (convertTo == 'PKR'):
            answear = amount * 1
        elif (convertTo == 'Yen'):
            answear = amount * 0.52
        elif (convertTo == 'AED'):
            answear = amount * 0.0129
    elif (choosenCurrency == 'Yen'):
        if (convertTo == 'Dollars'):
            answear = amount * 0.0067
        elif (convertTo == 'Pound'):
            answear = amount * 0.0050
        elif (convertTo == 'Euro'):
            answear = amount * 0.0058
        elif (convertTo == 'INR'):
            answear = amount * 0.58
        elif (convertTo == 'PKR'):
            answear = amount * 1.92
        elif (convertTo == 'YEN'):
            answear = amount * 1
        elif (convertTo == 'AED'):
            answear = amount * 0.025
    elif (currencyChoosen == 'AED'):
        if (convertTo == 'Dollars'):
            answear = amount * 0.27
        elif (convertTo == 'Pound'):
            answear = amount * 0.20
        elif (convertTo == 'Euro'):
            answear = amount * 0.23
        elif (convertTo == 'INR'):
            answear = amount * 23.46
        elif (convertTo == 'PKR'):
            answear = amount * 77.57
        elif (convertTo == 'YEN'):
            answear = amount * 40.45
        elif (convertTo == 'AED'):
            answear = amount * 1
    messagebox.showinfo(title = 'answear', message = username + ' ' + str(amount) + ' ' + choosenCurrency + ' = ' + str(answear) + ' ' + convertTo)


NameLabel = Label(screen, text = 'Name')
NameLabel.place(x = 50, y = 50)
NameText = Text(screen, width = 20, height = 2)
NameText.place(x = 200, y = 50)
currencyChoosen = Label(screen, text = 'choose currency')
currencyChoosen.place(x = 50, y = 100)

currency = Listbox(screen, exportselection = False)
currency.insert(0, 'Dollars')
currency.insert(1, 'Pound')
currency.insert(2, 'Euro')
currency.insert(3, 'INR')
currency.insert(4, 'PKR')
currency.insert(5, 'Yen')
currency.insert(6, 'AED')
currency.place(x = 200, y = 100)
Amount = Label(screen, text = 'Amount')
Amount.place(x = 50, y = 300)
AmountText = Text(screen, width = 20, height = 2)
AmountText.place(x = 200, y = 300)
ConvertLabel = Label(screen, text = 'Convert')
ConvertLabel.place(x = 50, y = 350 )

convertListBox = Listbox(screen, exportselection=False)
convertListBox.insert(0, 'Dollars')
convertListBox.insert(1, 'Pound')
convertListBox.insert(2, 'Euro')
convertListBox.insert(3, 'INR')
convertListBox.insert(4, 'PKR')
convertListBox.insert(5, 'Yen')
convertListBox.insert(6, 'AED')
convertListBox.place(x = 200, y = 350)
ConvertButton = Button(screen, text = 'Convert', command = convertCurrency)
ConvertButton.place(x = 400, y = 550)
currencyPhoto = PhotoImage(file = 'Assets/currencyImage.png')
labelphoto = Label(screen, image = currencyPhoto)
labelphoto.place(x = 500, y = 100)

screen.mainloop()