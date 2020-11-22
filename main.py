from collections import namedtuple
from weasyprint import HTML, Document
import datetime as dt
import os


class Input:
    __slots__ = ('id', 'created_at', 'delivery_method', 'article', 'product_name', 'count')

    def __init__(self, id, created_at, delivery_method, article, product_name, count):
        self.id = id
        self.created_at = created_at
        self.delivery_method = delivery_method
        self.article = article
        self.product_name = product_name
        self.count = count
    """метод возвращения словаря"""
    def lists(self):
        return {
            'Номер заказа': self.id,
            'Дата': self.created_at,
            'Способ доставки': self.delivery_method,
            'артикул': self.article,
            'наименование': self.product_name,
            'количество': self.count
        }


class InputProduct:
    """Дополнительный класс для отдачи только артикула, имя, и количества"""
    __slots__ = ('article', 'product_name', 'count')

    def __init__(self, article, product_name, count):
        self.article = article
        self.product_name = product_name
        self.count = count

    def lists(self):
        return {
            'артикул': self.article,
            'наименование': self.product_name,
            'количество': self.count
        }


class File_create(object):
    """Тут создаем файл"""
    def __init__(self, name_html, order_product):
        self.name_html = name_html
        self.order_product = order_product

    def file_name(self):
        with open(f'{self.name_html}.html', 'a') as file: # создаем файл либо перезаписываем
            for x, y in self.order_product.items(): # достаем значения словаря
                file.write(f' <p>{x} - {y}</p> \n')
        # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{name_html}.html') # удаляем старый файл
        # os.remove(path)


class OrderPackagePrinter(object):
    """Создаем pdf"""
    def __init__(self, order):
        self.order = order

    def call(self):
        file_weas = HTML(filename=f'{name_html}.html').write_pdf(f'{name_html}.pdf')


def count_input():
    """метод обработки дополнительных товаров"""
    answer = input('Есть ли еще товары, напишите Да или Нет: ').lower()
    if answer == 'да':
        a = int(input('Сколько у Вас товаров: '))
        a_count = a
        while True:
            if a_count > 0:
                article = int(input('Артикул: '))
                product_name = input('Наименование: ').split()
                count = int(input('Количество: '))
                c = InputProduct(article=article, product_name=product_name, count=count)
                d = File_create(name_html, c.lists())
                d.file_name()
            a_count -= 1
            if a_count <= 0:
                OrderPackagePrinter(name_html).call()
                break
    elif answer == 'нет':
        OrderPackagePrinter(name_html).call()
    else:
        OrderPackagePrinter(name_html).call()


if __name__ == '__main__':
    id = int(input('Введите id: '))
    delivery_method = input('Введите способ доставки: ')
    created_at = dt.datetime.now().strftime("%d-%m-%Y")
    article = int(input('Артикул: '))
    product_name = input('Наименование: ').split()
    count = int(input('Количество: '))
    order_product = Input(id, created_at, delivery_method, article, product_name, count)
    name_html = input('Введите имя файла для html документа без расширения: ')
    a = File_create(name_html, order_product.lists())
    a.file_name()
    count_input()
