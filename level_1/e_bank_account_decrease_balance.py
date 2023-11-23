"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income

    def decrease_balance(self, income: float):
        new_balance = self.balance - income
        if new_balance >= 0:
            self.balance = new_balance
        else:
            raise ValueError


if __name__ == '__main__':
    bank_acc = BankAccount('Ivan Ivanov', 450.99)
    bank_acc.decrease_balance(380)
    print(bank_acc.balance)
    bank_acc.decrease_balance(100)
