import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("CALCULATOR")

firstnumber = tk.Label(mainWindow, text='first number')
firstnumber.pack()

firstnumberentry = tk.Entry(mainWindow)
firstnumberentry.pack()

secondnumber = tk.Label(mainWindow, text='second number')
secondnumber.pack()

secondnumberentry = tk.Entry(mainWindow)
secondnumberentry.pack()

operation = tk.Label(mainWindow, text='operation')
operation.pack()

def addition():
  first = int(firstnumberentry.get())
  second = int(secondnumberentry.get())
  result = first + second
  result_label.config(text='operation result is :' + str(result))

def minus():
  first = int(firstnumberentry.get())
  second = int(secondnumberentry.get())
  result = first - second
  result_label.config(text='operation result is :' + str(result))

def multiply():
  first = int(firstnumberentry.get())
  second = int(secondnumberentry.get())
  result = first * second
  result_label.config(text='operation result is :' + str(result))

def divide():
  first = int(firstnumberentry.get())
  second = int(secondnumberentry.get())
  result = first / second
  result_label.config(text='operation result is :' + str(result))

addition_button = tk.Button(mainWindow,text='+', command=lambda : addition())
addition_button.pack()

minus_button = tk.Button(mainWindow,text='-', command=lambda : minus())
minus_button.pack()

multiply_button = tk.Button(mainWindow,text='*', command=lambda : multiply())
multiply_button.pack()

divide_button = tk.Button(mainWindow,text='/', command=lambda : divide(), pady=(10))
divide_button.pack()

result_label=tk.Label(mainWindow,text='Result is :')
result_label.pack()

mainWindow.mainloop()

