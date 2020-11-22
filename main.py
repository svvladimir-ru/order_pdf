from collections import namedtuple
from weasyprint import HTML, Document
import datetime as dt


class OrderPackagePrinter(object):

    def __init__(self, order):
        self.order = order

    def call(self):
        name_html = input('Введите имя файла для html документа без расширения: ')
        with open(f'{name_html}.html', 'a') as file: # создаем файл либо перезаписываем
            file.write('<div>')
            for x, y in order.items(): # достаем значения словаря
                file.write(f' <p>{x} - {y}</p> \n')
            file.write('</div> \n')
        name = input('Введите имя файла без расширения: ')
        file_weas = HTML(filename=f'{name_html}.html').write_pdf(f'{name}.pdf') # создаем файл
        # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{name_html}.html') # удаляем старый файл
        # os.remove(path)


if __name__ == '__main__':
    id = int(input('Введите id: '))
    delivery_method = input('Введите способ доставки: ')
    created_at = dt.datetime.now().strftime("%d-%m-%Y")
    article = int(input('Артикул: '))
    product_n = input('Наименование: ').split()
    count = int(input('Количество: '))
    product_one = namedtuple('product', ['article_number', 'product_name', 'quantity'])
    product = product_one(article, product_n, count)
    order = {
        'Номер заказа': id,
        'Дата заказа': created_at,
        'Способ доставки': delivery_method,
        'Артикул': product[0],
        'Наименование товара': product[1],
        'Количество': product[2],

    }

    a = OrderPackagePrinter(order)
    a.call()

