from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()


        categories_list = [
            {'name': 'ТВ', 'description': 'Различные Телевизоры, Проекторы, Экраны'},
            {'name': 'Телефоны,', 'description': 'Телефоны, Смартфоны,Радиотелефоны'},
            {'name': 'Аудио', 'description': 'Колонки, Наушники, Саундбары'},
        ]
        categories_for_create = []

        for category_item in categories_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categories_for_create)

        product_list = [{ "name": "SULSUMG", "description": "Идеальное изображение",
                          "category": Category.objects.get(name="ТВ"),
                          "price_for_purchase": 15000, "creation_date": "2023-06-01",
                          "last_change_date": "2023-08-01"}
                        ]


        products_to_create = []

        for product_item in product_list:
            products_to_create.append(
                Product(**product_item)
            )
        Product.objects.bulk_create(products_to_create)

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена новыми данными.'))