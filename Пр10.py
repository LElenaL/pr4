import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename


window = Tk() #назначаем главный управляющую функцию окна
window.title("Леонтьева Елена Евгеньевна") #Устанавливаем заголовок окна 
window.geometry('800x600') #Устанавливаем размер окна
window.resizable(width=False, height=False) #Запрещаем изменять размер

tab_control = ttk.Notebook(window) #Добавляем функцию управления вкладками

#Присваеваем каждой переменной свою вкладку

calc_tab = ttk.Frame(tab_control)
box_tab = ttk.Frame(tab_control)
text_tab = ttk.Frame(tab_control)
#Добавляем вкладки в функцию управления
tab_control.add(calc_tab,text=f'{"Калькулятор": ^85s}')
tab_control.add(box_tab,text=f'{"Чекбоксы ": ^85s}')
tab_control.add(text_tab,text=f'{"Текст ": ^85s}')

#region кальулятор
textEntry = StringVar() # Эта переменная отвечает за текст в поле ответа

# Это функция, где мы будем производить вычисления
def solve():
    if comboExample.get() == "": #Если значение выпадающего списка ПУСТО, то в поле ответа запишется ошибка
        textEntry.set("err")
    elif comboExample.get() == "+": #ИначеЕсли значение выпадающего списка +, то в поле ответа запишется
                                    #значение из поля_1 + значение из поля_2. Далее по аналогии
        try:
            textEntry.set(float(par_1_textbox.get())+float(par_2_textbox.get())) #Тут мы получаем значнеие из поля 1 и 2 и складываем их
        except:
            textEntry.set("err") #Трай эксцепт нужен в случае не правильного ввода данных, напрмер не числа а строки
    elif comboExample.get() == "*":
        try:
            textEntry.set(float(par_1_textbox.get()) * float(par_2_textbox.get()))
        except:
            textEntry.set("err")
    elif comboExample.get() == "/":
        try:
            textEntry.set(float(par_1_textbox.get()) / float(par_2_textbox.get()))
        except:
            textEntry.set("err")
    elif comboExample.get() == "-":
        try:
            textEntry.set(float(par_1_textbox.get()) - float(par_2_textbox.get()))
        except:
            textEntry.set("err")
    else:
        textEntry.set("0")
    return None

par_1_textbox = Entry(calc_tab,width=20) #Объявляем поле ввода, указываем на какую именно вкладку и его размер
par_1_textbox.grid(column=0, row=0) #Рисуем поле в нулевой колонке, нулевой строки

#Объявляем выпадающий список, указываем на какую именно вкладку и его размер
comboExample = ttk.Combobox(calc_tab, values=["+", "-", "*", "/"],width=20)
comboExample.grid(column=1,row=0)#Рисуем поле в первой колонке, нулевой строки

#Аналогично с первым полем
par_2_textbox = Entry(calc_tab,width=20)
par_2_textbox.grid(column=2, row=0)
#Тоже самое
result_textbox = Entry(calc_tab,width=20,textvariable = textEntry)
result_textbox.grid(column=3, row=0)

#Объявляем кнопочку, указываем вкладку, называем кнопку РЕШИТЬ и назначаем ей нашу функцию solve
btn_solve = Button(calc_tab, width=20,text="Решить", command=solve)
btn_solve.grid(column=4, row=0)
#endregion
#region выбор
#Аналогично предыдущей функции, вызывает окошко, в котором пишется твой выбор, в зависимости от выбранного чекбокса
def check():
    if r_var.get() == 0:
        tkinter.messagebox.showinfo("Ваш выбор","Вы выбрали первый вариант!")
    elif r_var.get() == 1:
        tkinter.messagebox.showinfo("Ваш выбор","Вы выбрали второй вариант!")
    elif r_var.get() == 2:
        tkinter.messagebox.showinfo("Ваш выбор","Вы выбрали третий вариант!")
    else:
        tkinter.messagebox.showinfo("Ваш выбор","Вы не выбрали вариант.")


    return None
r_var = IntVar()#Переменная, которая будет изменяться в зависимости от выбранного чекбокса
r_var.set(0)#Переменная изначально равна нулю

#Объявляем чекбокс, указываем на какую именно вкладку, указываем какую переменную будет изменять этот чекбокс,
#указываем какое значение будет назначено, в случае его выбора
first_check = Radiobutton(box_tab,text="Первый вариант",variable=r_var, value=0)
first_check.grid(column=0, row=0)

#Аналогично, только значние = 1
second_check = Radiobutton(box_tab,text="Второй вариант",variable=r_var, value=1)
second_check.grid(column=1, row=0)

#Аналогично, только значние = 2
third_check = Radiobutton(box_tab,text="Третий вариант",variable=r_var, value=2)
third_check.grid(column=2, row=0)
#Объявляем кнопку, указываем вкладку, называем кнопку УЗНАТЬ и назначаем ей нашу функцию check
btn_choice = Button(box_tab, text="узнать", command=check)
btn_choice.grid(column=3, row=0)
#endregion
#region текст

def enter_text():
    filename = askopenfilename() #Объявим переменную и вызовем окно выбор файла, оно вернёт нам путь файла
    text_box.delete(1.0,tkinter.END)#Очищаем наше поле текста
    f = open(filename,encoding='utf-8')#Открываем наш файл
    for line in f:#читаем каждую линию
        text_box.insert(tkinter.END, line)#заносим каждую линию в поле текста
    return None

#Объявляем наше поле текста, указываем вкладку, его размер и врап = ворд (это способ переноса текста по словам)
text_box = Text(text_tab,width=100, height=30,wrap = WORD)
text_box.grid(column=0, row=2)

#Объявляем кнопку, указываем вкладку, называем кнопку ЗАГРУЗИТЬ и назначаем ей нашу функцию enter_text
btn_choice = Button(text_tab, text="Загрузить", command=enter_text)
btn_choice.grid(column=0, row=0)
#endregion



#Рисуем наш табконтрол (это виджет с вкалдками, который мы объявили вверху),
# и обозначаем fill='both' (Это значит заполнить полностью все пространство)
tab_control.pack(expand=1,fill='both')

#запустить наше окно
window.mainloop()