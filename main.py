from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def get_base_currency(event=None):  # получаем данные из первого бокса
    base_currency = base_combobox.get()
    # print(base_currency)
    return base_currency


def get_quote_currency(event=None): # получаем данные из второго бокса
    quote_currency = quote_combobox.get()
    # print(quote_currency)
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
            print(value_1) # показали результат значения ключа
            print(value_2)
            mb.showinfo(title='Результат', message=f'1 {base_currency} равен {value_2}')
        except Exception as e:
            print(e)



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

but_result = ttk.Button(text='Получить курс валюты', command=exchange)
but_result.grid()

window.mainloop()