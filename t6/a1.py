class Account:
    def __init__(self, name, starting_balance, transaction_history=[]):
        """
        Конструктор для создания банковского аккаунта.
        :param name: имя владельца аккаунта
        :param starting_balance: стартовый баланс аккаунта
        :param transaction_history: начальная история операций (по умолчанию пустая)
        """
        self.name = name
        self.starting_balance = starting_balance
        self.transaction_history = transaction_history

    def deposit(self, amount):
        """
        Метод для пополнения банковского аккаунта.
        :param amount: сумма, которую нужно положить на счёт
        :return: новый баланс аккаунта после пополнения
        """
        self.transaction_history.append({'type': 'deposit', 'amount': amount})
        return self.starting_balance + amount

    def withdraw(self, amount):
        """
        Метод для снятия денег с банковского аккаунта.
        :param amount: сумма, которую нужно снять со счёта
        :return: новый баланс аккаунта после снятия
        """
        self.transaction_history.append({'type': 'withdrawal', 'amount': amount})
        return self.starting_balance - amount

    def get_balance(self):
        """
        Метод для получения текущего баланса аккаунта.
        :return: текущий баланс
        """
        return self.starting_balance + sum([transaction['amount'] for transaction in self.transaction_history if transaction['type'] == 'deposit']) - sum([transaction['amount'] for transaction in self.transaction_history if transaction['type'] == 'withdrawal'])

    def get_transaction_history(self):
        """
        Метод для получения истории операций.
        :return: список операций
        """
        return self.transaction_history

    def save_transaction_history(self, filename):
        """
        Метод для сохранения истории операций во внешний файл.
        :param filename: имя файла для сохранения
        """
        with open(filename, 'w') as file:
            for transaction in self.transaction_history:
                file.write(f"{transaction['type']} {transaction['amount']}\n")

    def load_transaction_history(self, filename):
        """
        Метод для загрузки истории операций из внешнего файла.
        :param filename: имя файла для загрузки
        """
        self.transaction_history = []
        with open(filename, 'r') as file:
            for line in file:
                transaction_type, amount = line.strip().split()
                self.transaction_history.append({'type': transaction_type, 'amount': float(amount)})

# Пример использования класса Account

# Создаём аккаунт
my_account = Account('John Doe', 1000)

# Пополняем счёт
my_account.deposit(500)

# Выводим баланс
print(my_account.get_balance())  # 1500

# Проводим операцию снятия
my_account.withdraw(200)

# Выводим баланс после снятия
print(my_account.get_balance())  # 1300

# Сохраняем историю операций в файл
my_account.save_transaction_history('transaction_history.txt')

# Загружаем историю операций из файла
my_account.load_transaction_history('transaction_history.txt')

# Выводим историю операций
for transaction in my_account.get_transaction_history():
    print(transaction)
