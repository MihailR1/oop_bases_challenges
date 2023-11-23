"""
У нас есть базовый класс продукта, а так же есть миксин для продуктов питания, но нет класса для продуктов питания.

Задания:
    1. Нужно создать класс FoodProduct, который будет наследовать от классов Product и FoodProductMixin.
    2. У класса FoodProduct переопределить метод get_product_info, таким образом, чтобы если продукт премиальный, то в скобках
       в конце добавлялось слово Premium.
       Например: Product title: Avocado, price: 12 (Premium)'
    3. Создать экземпляр класс FoodProduct с ценой меньше 10 и вызвать у него метод get_product_info.
    4. Создать экземпляр класс FoodProduct с ценой больше 10 и вызвать у него метод get_product_info.
"""


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_product_info(self):
        return f'Product title: {self.title}, price: {self.price}'


class FoodProductMixin:
    def is_premium_food(self):
        return self.price > 10


class FoodProduct(Product, FoodProductMixin):
    def get_product_info(self):
        if self.is_premium_food():
            return super().get_product_info() + f' (Premium)'
        return super().get_product_info()


if __name__ == '__main__':
    food_prod_1 = FoodProduct('milk', 9)
    food_prod_2 = FoodProduct('tomato', 240)
    print(food_prod_1.get_product_info())
    print(food_prod_2.get_product_info())
