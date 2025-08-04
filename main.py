from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def get_base_currency(event=None):  # получаем данные из первого бокса
    base_currency = base_combobox.get()
    return base_currency


def get_quote_currency(event=None): # получаем данные из второго бокса
    quote_currency = quote_combobox.get()
    return quote_currency


def exchange(): # получаем данные из API при нажатии кнопки
    base_currency = get_base_currency() # получили из первой функции get
    quote_currency = get_quote_currency() # получили из второй функции get
    if base_currency and quote_currency:
        try:
            url = f'https://api.coingecko.com/api/v3/simple/price?vs_currencies={quote_currency}&ids={base_currency}'
            response = requests.get(url)
            response.raise_for_status()
            data = response.json() # получили файл в формате json в виде словаря
            value_1 = list(data.values())[0]  # берём первое значение всего словаря
            value_2 = list(value_1.values())[0]  # берём первое значение внутреннего словаря
            formatted_value = f'{value_2:,}'.replace(',', ' ')
            mb.showinfo(title='Результат', message=f'1 {currencies[base_currency]} равен {formatted_value} {vs_currencies[quote_currency]}')
        except Exception as e:
            print(e)
    else:
        mb.showerror(title='Ошибка', message='Не выбрана валюта')


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
window.title('Курс обмена криптовалют')
# размер окна и параметры его отображения(посередине экрана)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
width_position = screenwidth // 2 - 150
height_position = screenheight // 2 - 150
window.geometry(f'300x300+{width_position}+{height_position}')

label_base = ttk.Label(text='Базовая криптовалюта')
label_base.grid(row=1, column=1,padx=80, pady=20)
base_combobox = ttk.Combobox(window, values=list(currencies.keys()))
base_combobox.grid(row=2,column=1,padx=80, pady=20)
base_combobox.bind('<<ComboboxSelected>>', get_base_currency)

label_quote = ttk.Label(text='Целевая валюта')
label_quote.grid(row=3,column=1,padx=80, pady=20)
quote_combobox = ttk.Combobox(window, values=list(vs_currencies.keys()))
quote_combobox.grid(row=4,column=1,padx=80, pady=20)
quote_combobox.bind('<<ComboboxSelected>>', get_quote_currency)

but_result = ttk.Button(text='Получить курс обмена', command=exchange)
but_result.grid(row=5,column=1,padx=80, pady=20)


window.mainloop()