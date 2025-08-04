from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

window = Tk()
window.title('Курсы криптовалют')
# размер окна и параметры его отображения(посередине экрана)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
width_position = screenwidth // 2 - 200
height_position = screenheight // 2 - 230
window.geometry(f'400x460+{width_position}+{height_position}')


label_base = ttk.Label(text='Базовая валюта').grid()
base_combobox = ttk.Combobox(window, values=)
base_combobox.grid()
base_combobox.bind('<<ComboboxSelected>>')


label_quote = ttk.Label(text='Целевая валюта').grid()
quote_combobox = ttk.Combobox(window, values=)
quote_combobox.grid()
quote_combobox.bind('<<ComboboxSelected>>')

but_result = ttk.Button(text='Получить курс валюты')