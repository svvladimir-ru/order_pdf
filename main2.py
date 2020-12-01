from collections import namedtuple
from weasyprint import HTML, Document
import datetime as dt
import os
from typing import Optional

id: int
delivery_method: str
article: int
product_name: str
count: int


class Input:
    """класс для уменьшения занимаемой памяти списка"""
    __slots__ = ('id', 'created_at', 'delivery_method', 'article', 'product_name', 'count')

    def __init__(self, id, created_at, delivery_method, article, product_name, count):
        self.id = id
        self.created_at = created_at
        self.delivery_method = delivery_method
        self.article = article
        self.product_name = product_name
        self.count = count
    """метов возвращения словаря"""
    def lists(self):
        return {
            'Номер заказа': self.id,
            'Дата': self.created_at,
            'Способ доставки': self.delivery_method,
            'Артикул': self.article,
            'Наименование': self.product_name,
            'Количество': self.count
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
            'Артикул': self.article,
            'Наименование': self.product_name,
            'Количество': self.count
        }


class File_create(object):
    """Тут создаем файл"""
    def __init__(self, name_html, order_product):
        self.name_html = name_html
        self.order_product = order_product

    def file_name(self, n):
        with open(f'{self.name_html}.html', 'a') as file: # создаем файл либо перезаписываем
            if self.order_product.get('Номер заказа'):
                a = self.order_product.pop('Номер заказа')
                if self.order_product.get('Дата'):
                    d = self.order_product.pop('Дата')
                    if self.order_product.get('Способ доставки'):
                        c = self.order_product.pop('Способ доставки')
                        file.write(f'<h2>   | Заказ № {a} | Дата: {d} | Способ доставки: {c} | </h2> \n')
                        file.write('___________________________________________________________________________\n')
                        file.write(f'<h3>  №  |     Артикул  |    Наименование   |   Количество   | </h3> \n')
            file.write('<div>\n')

            if self.order_product.get('Артикул'):
                e = self.order_product.pop('Артикул')
                if self.order_product.get('Наименование'):
                    r = self.order_product.pop('Наименование')
                    if self.order_product.get('Количество'):
                        t = self.order_product.pop('Количество')
                        file.write(f'<pre> № {n}  |     {e}     |       {r}     |&nbsp;&nbsp;{t}&nbsp;&nbsp;| </pre> \n')
            file.write('____________________________________________________________________________</div>\n')
        # path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{name_html}.html') # удаляем старый файл
        # os.remove(path)


class OrderPackagePrinter(object):
    """Создаем pdf"""
    def __init__(self, order):
        self.order = order

    def call(self):
        file_weas = HTML(filename=f'{self.order}.html').write_pdf(f'{self.order}.pdf')


def count_input():
    """метод обработки дополнительных товаров"""
    answer = input('Есть ли еще товары, напишите Да или Нет: ').lower()
    if answer == 'да':
        a = int(input('Сколько у Вас товаров: '))
        a_count = a
        count_number = []
        for i in range(2, a+2):
            count_number.append(i)
        while True:
            if a_count > 0:
                article = int(input('Артикул: '))
                product_name = input('Наименование: ')
                count = int(input('Количество: '))
                c = InputProduct(article=article, product_name=product_name, count=count)
                d = File_create(name_html, c.lists())
                one_number = count_number.pop(0)   # вытаскиваем первый номер и передаем его
                d.file_name(one_number)
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
    product_name = input('Наименование: ')
    count = int(input('Количество: '))
    order_product = Input(id, created_at, delivery_method, article, product_name, count)
    name_html = input('Введите имя файла для html документа без расширения: ')
    a = File_create(name_html, order_product.lists())
    a.file_name(1)
    count_input()
    
