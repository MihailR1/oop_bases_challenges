"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""


class PrintLoggerMixin:
    def log(self, message: str):
        print(message)


class Product(PrintLoggerMixin):
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self):
        self.log(f'LOG: Get info for product {self.title} with price {self.price}')
        return f'Product {self.title} with price {self.price}'


class PremiumProduct(Product):
    def increase_price(self):
        self.log(f'LOG: Increase_price for product {self.title} with old price {self.price}')
        self.price *= 1.2

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info} (Premium)'


class DiscountedProduct(Product):
    def decrease_price(self):
        self.log(f'LOG: Decrease_price for product {self.title} with old price {self.price}')
        self.price /= 1.2

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info} (Discounted)'


if __name__ == '__main__':
    premium_product = PremiumProduct('milk', 130)
    discount_product = DiscountedProduct('tomato', 50)
    premium_product.get_info()
    premium_product.increase_price()
    discount_product.get_info()
    discount_product.decrease_price()
