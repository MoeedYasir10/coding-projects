from tkinter import *

screen = Tk()
screen.title('Todo List')
screen.geometry('400x600')

def todo_list():
    readTask = TaskText.get('1.0', END)
    Time = TimeText.get('1.0', END)
    Day = DayDropdown.get(DayDropdown.curselection())
    Label = DisplayLabel.cget('text')
    message = readTask + ' ' + Day + ', ' + Time
    Label = Label + message + '\n'
    DisplayLabel.config(text = Label)


TaskLabel = Label(screen, text = 'Task')
TaskLabel.place(x = 10, y = 10)
TaskText = Text(screen, width = 20, height = 2)
TaskText.place(x = 50, y = 10 )
TimeLabel = Label(screen, text = 'Time')
TimeLabel.place(x = 10, y = 50)
TimeText = Text(screen, width = 20, height = 2)
TimeText.place(x = 50 , y = 50)
DayLabel = Label(screen, text = 'Day')
DayLabel.place(x = 10, y = 100)
DayDropdown = Listbox(screen, exportselection = False)
DayDropdown.place(x = 50, y = 100)
DayDropdown.insert(0, 'Sunday')
DayDropdown.insert(1, 'Monday')
DayDropdown.insert(2, 'Tuesday')
DayDropdown.insert(3, 'Wednesday')
DayDropdown.insert(4, 'Thursday')
DayDropdown.insert(5, 'Friday')
DayDropdown.insert(6, 'Saturday')
DisplayLabel = Label(screen, width = 20)
DisplayLabel.place(x = 10, y = 390)
addButton = Button(screen, text = 'Add', command = todo_list)
addButton.place(x = 10, y = 350)


screen.mainloop()