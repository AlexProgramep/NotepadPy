import tkinter
import tkinter.font as tkFont
from datetime import datetime
from tkinter import VERTICAL, Scrollbar, BooleanVar
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.simpledialog import askinteger, askstring
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
             ('Text Document', '*.txt')]
    out = asksaveasfile(mode='w', filetypes=files)
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Помилка", message="Помилка збереження файлу")


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
    newwindow = tkinter.Toplevel(root)
    newwindow.geometry("700x700")
    newwindow.iconbitmap("python_icon.ico")
    newtext = tkinter.Text(newwindow, width=400, height=400, wrap="word")
    scrollb = Scrollbar(newwindow, orient=VERTICAL, command=text.yview)
    scrollb.pack(side="right", fill="y")
    newtext.configure(yscrollcommand=scrollb.set)

    newtext.pack()

    menubar = tkinter.Menu(newwindow)
    filemenu = tkinter.Menu(menubar)
    filemenu.add_command(label="Новий", command=new_file)
    filemenu.add_command(label="Відкрити", command=open_file)
    filemenu.add_command(label="Нове вікно", command=open_win)
    filemenu.add_command(label="Очистити поле", command=clear_file)
    filemenu.add_command(label="Зберегти", command=save_file)
    filemenu.add_command(label="Зберегти", command=save_file)
    filemenu.add_command(label="Зберегти як", command=save_as)
    filemenu.add_command(label="Час та дата", command=currenttime)

    fontmenu.add_command(label="Розмір", command=fontsize)
    fontmenu.add_command(label="Стиль шрифту", command=fontname)
    fontmenu.add_command(label="Назва стилів", command=font_names)
    fontmenu.add_checkbutton(label="Звичайний шрифт", onvalue=0, offvalue=1, variable=bool_bold, command=fontnormal)
    fontmenu.add_checkbutton(label="Жирний шрифт", onvalue=1, offvalue=0, variable=bool_bold, command=fontbold)
    fontmenu.add_checkbutton(label="Не нахилений", onvalue=0, offvalue=1, variable=bool_slant, command=fontroman)
    fontmenu.add_checkbutton(label="нахилений", onvalue=1, offvalue=0, variable=bool_slant, command=fontitalic)
    fontmenu.add_checkbutton(label="Нижнє підкреслення(є)", onvalue=1, offvalue=0, variable=bool_underline,
                             command=underline_on)
    fontmenu.add_checkbutton(label="Нижнє підкреслення (нема)", onvalue=0, offvalue=1, variable=bool_underline,
                             command=underline_off)
    fontmenu.add_checkbutton(label="Закреслити(так)", onvalue=1, offvalue=0, variable=bool_overstrike,
                             command=overstrike_on)
    fontmenu.add_checkbutton(label="Закреслити(нi)", onvalue=0, offvalue=1, variable=bool_overstrike,
                             command=overstrike_off)

    menubar.add_cascade(label="Файл", menu=filemenu)
    menubar.add_cascade(label="Информация", command=info)
    menubar.add_cascade(label="Шрифт", menu=fontmenu)
    newwindow.config(menu=menubar)


def currenttime():
    now = datetime.now()
    current_time = "{}:{}   {}.{}.{}".format(now.hour, now.minute, now.day, now.month, now.year)
    text.insert('1.0', current_time)


def fontsize():
    size_number = askinteger('Розмір шрифту', 'Оберіть розмір шрифту')
    fontExample.configure(size=size_number)


def fontnormal():
    fontExample.configure(weight="normal")


def fontbold():
    fontExample.configure(weight="bold")


def fontroman():
    fontExample.configure(slant="roman")


def fontitalic():
    fontExample.configure(slant="italic")


def underline_on():
    fontExample.configure(underline=True)


def underline_off():
    fontExample.configure(underline=False)


def overstrike_on():
    fontExample.configure(overstrike=True)


def overstrike_off():
    fontExample.configure(overstrike=False)


def fontname():
    font_name = askstring('Назва шрифту', 'Введіть коректну назву шрифту (можете переглянути назву ')
    fontExample.configure(family=font_name)

def font_names():
    newwindow = tkinter.Toplevel(root)
    newwindow.geometry("500x500")
    newwindow.iconbitmap("python_icon.ico")
    newtext = tkinter.Text(newwindow, width=400, height=400, wrap="word")
    scrollb = Scrollbar(newwindow, orient=VERTICAL, command=text.yview)
    scrollb.pack(side="right", fill="y")
    newtext.configure(yscrollcommand=scrollb.set)
    for n in tkFont.families()[::-1]:
        newtext.insert('1.0', f"{n} \n")

    newtext.pack()


def info():
    messagebox.showinfo("Інформація",
                        'Блокнот на Python.\n Зберігає файли у форматі ".txt" ')


root = tkinter.Tk()
root.title("БлокнотPY")
root.geometry("800x800+500+100")
root.iconbitmap("python_icon.ico")

bool_bold = BooleanVar()
bool_slant = BooleanVar()
bool_underline = BooleanVar()
bool_overstrike = BooleanVar()

text = tkinter.Text(root, width=400, height=400, wrap="word")
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
fontExample = tkFont.Font()
text.configure(yscrollcommand=scrollb.set, font=fontExample)
text.pack()

menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar)
fontmenu = tkinter.Menu(menubar)

filemenu.add_command(label="Новий", command=new_file)
filemenu.add_command(label="Відкрити", command=open_file)
filemenu.add_command(label="Нове вікно", command=open_win)
filemenu.add_command(label="Очистити поле", command=clear_file)
filemenu.add_command(label="Зберегти", command=save_file)
filemenu.add_command(label="Зберегти", command=save_file)
filemenu.add_command(label="Зберегти як", command=save_as)
filemenu.add_command(label="Час та дата", command=currenttime)

fontmenu.add_command(label="Розмір", command=fontsize)
fontmenu.add_command(label="Стиль шрифту", command=fontname)
fontmenu.add_command(label="Назва стилів", command=font_names)
fontmenu.add_checkbutton(label="Звичайний шрифт", onvalue=0, offvalue=1, variable=bool_bold, command=fontnormal)
fontmenu.add_checkbutton(label="Жирний шрифт", onvalue=1, offvalue=0, variable=bool_bold, command=fontbold)
fontmenu.add_checkbutton(label="Не нахилений", onvalue=0, offvalue=1, variable=bool_slant, command=fontroman)
fontmenu.add_checkbutton(label="нахилений", onvalue=1, offvalue=0, variable=bool_slant, command=fontitalic)
fontmenu.add_checkbutton(label="Нижнє підкреслення(є)", onvalue=1, offvalue=0, variable=bool_underline,
                         command=underline_on)
fontmenu.add_checkbutton(label="Нижнє підкреслення (нема)", onvalue=0, offvalue=1, variable=bool_underline,
                         command=underline_off)
fontmenu.add_checkbutton(label="Закреслити(так)", onvalue=1, offvalue=0, variable=bool_overstrike, command=overstrike_on)
fontmenu.add_checkbutton(label="Закреслити(нi)", onvalue=0, offvalue=1, variable=bool_overstrike,
                         command=overstrike_off)

menubar.add_cascade(label="Файл", menu=filemenu)
menubar.add_cascade(label="Информацiя", command=info)
menubar.add_cascade(label="Шрифт", menu=fontmenu)
root.config(menu=menubar)

root.mainloop()
