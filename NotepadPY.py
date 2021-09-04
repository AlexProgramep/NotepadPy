import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox

FILE_NAME = tkinter.NONE

def new_file():
	global FILE_NAME
	FILE_NAME = "Untitled"
	text.delete('1.0', tkinter.END)

def save_file():
	data = text.get('1.0', tkinter.END)
	out = open(FILE_NAME, 'w')
	out.write(data)
	out.close()

def save_as():
	files = [('All Files', '*.*'),
			 ('Python Files', '*.py'),
			 ('C++ Files', '*.cpp'),
			 ('Text Document', '*.txt')]
	out = asksaveasfile(mode='w',filetypes = files, defaultextension=files)
	data = text.get('1.0', tkinter.END)
	try:
		out.write(data.rstrip())
	except Exception:
		showerror(title="Error", message="Saving file error")

def open_file():
	global FILE_NAME
	inp = askopenfile(mode="r")
	if inp is None:
		return
	FILE_NAME = inp.name
	data = inp.read()
	text.delete('1.0', tkinter.END)
	text.insert('1.0', data)

def clear_file():
    text.delete('1.0', tkinter.END)

def open_win():
	newWindow = tkinter.Toplevel(root)
	newWindow.geometry("700x700")
	newWindow.iconbitmap("python_icon.ico")
	labelExample = tkinter.Text(newWindow, width=400, height=400, wrap="word")
	scrollb = Scrollbar(newWindow, orient=VERTICAL, command=text.yview)
	scrollb.pack(side="right", fill="y")
	labelExample.configure(yscrollcommand=scrollb.set)

	labelExample.pack()

	menuBar = tkinter.Menu(newWindow)
	fileMenu = tkinter.Menu(menuBar)
	fileMenu.add_command(label="Новый", command=new_file)
	fileMenu.add_command(label="Открыть", command=open_file)
	fileMenu.add_command(label="Новое окно", command=open_win)
	fileMenu.add_command(label="Очистить поле", command=clear_file)
	fileMenu.add_command(label="Сохранить", command=save_file)
	fileMenu.add_command(label="Сохранить как", command=save_as)

	menuBar.add_cascade(label="Файл", menu=fileMenu)
	menuBar.add_cascade(label="Информация", command=info)
	newWindow.config(menu=menuBar)

def info():
	messagebox.showinfo("Информация", 'Блокнот на Python.\n Сохраняет файлы в таких форматах,как: ".py" , ".txt" , ".cpp".')

root = tkinter.Tk()
root.title("БлокнотPY")
root.geometry("800x800+500+100")
root.iconbitmap("python_icon.ico")

text = tkinter.Text(root, width=400, height=400, wrap="word")
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)

text.pack()
menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label="Новый", command=new_file)
fileMenu.add_command(label="Открыть", command=open_file)
fileMenu.add_command(label="Новое окно", command=open_win)
fileMenu.add_command(label="Очистить поле", command=clear_file)
fileMenu.add_command(label="Сохранить", command=save_file)
fileMenu.add_command(label="Сохранить как", command=save_as)

menuBar.add_cascade(label="Файл", menu=fileMenu)
menuBar.add_cascade(label="Информация", command=info)
root.config(menu=menuBar)

root.mainloop()
