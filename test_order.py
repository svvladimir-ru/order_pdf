import unittest
import datetime as dt
import os
from main import OrderPackagePrinter, Input, InputProduct, File_create


class FileCreateTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.file_name = 'test_file_name'
        self.id = 1
        self.created_at = dt.datetime.now().strftime("%d-%m-%Y")
        self.delivery_method = 'Самовывоз'
        self.article = 43356
        self.product_name = 'Майка'
        self.count = 1
        # self.file_pdf = OrderPackagePrinter(self.file_name).call()

    def test_file_create(self):
        order = {
            'Номер заказа': self.id,
            'Дата': self.created_at,
            'Способ доставки': self.delivery_method,
            'артикул': self.article,
            'наименование': self.product_name,
            'количество': self.count
        }
        file_test = File_create(self.file_name, order).file_name()
        e = os.path.basename(f'{self.file_name}.html')
        self.assertEqual(e, f'{self.file_name}.html', 'Файл не создан')

    def test_file_pdf_create(self):
        file_test = OrderPackagePrinter(self.file_name).call()
        e = os.path.basename(f'{self.file_name}.pdf')
        self.assertEqual(e, f'{self.file_name}.pdf', 'Файл не создан')
