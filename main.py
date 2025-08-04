from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def get_base_currency(event):
    base_currency = base_combobox.get()
    print(base_currency)
    return base_currency


def get_quote_currency(event):
    quote_currency = quote_combobox.get()
    print(quote_currency)
    return quote_currency


currencies = {
    'bitcoin': 'Биткоин',
    'ethereum': 'Эфириум'
}
vs_currencies = {
    'usd': 'Доллар США',
    'eur': 'Евро',
    'jpy': 'Японская иена',
    'gbp': 'Фунт стерлингов',
    'cad': 'Канадский доллар',
    'chf': 'Швейцарский франк',
    'cny': 'Китайский юань',
    'rub': 'Российский рубль'
}


window = Tk()
window.title('Курсы криптовалют')
# размер окна и параметры его отображения(посередине экрана)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
width_position = screenwidth // 2 - 200
height_position = screenheight // 2 - 230
window.geometry(f'400x460+{width_position}+{height_position}')


label_base = ttk.Label(text='Базовая валюта')
label_base.grid()
base_combobox = ttk.Combobox(window, values=list(currencies.keys()))
base_combobox.grid()
base_combobox.bind('<<ComboboxSelected>>', get_base_currency)


label_quote = ttk.Label(text='Целевая валюта')
label_quote.grid()
quote_combobox = ttk.Combobox(window, values=list(vs_currencies.keys()))
quote_combobox.grid()
quote_combobox.bind('<<ComboboxSelected>>', get_quote_currency)

but_result = ttk.Button(text='Получить курс валюты')