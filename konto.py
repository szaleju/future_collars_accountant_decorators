from sys import argv
from manager import Manager, FileManager

manager = Manager()
file_manager = FileManager()


@manager.assign("saldo", 2)
def balance_update(manager, amount, comment):
    if manager.balance + int(amount) >= 0:
        manager.balance += int(amount)


@manager.assign("zakup", 3)
def buy(manager, product_name, price, amount):
    if manager.balance - int(price)*int(amount) >= 0:
        manager.balance -= int(price)*int(amount)
        if product_name not in manager.stock:
            manager.stock[product_name] = int(amount)
        else:
            manager.stock[product_name] += int(amount)
    else:
        print("Brak wystarczającej ilość gotówki.")


@manager.assign("sprzedaz", 3)
def sell(manager, product_name, price, amount):
    if product_name not in manager.stock:
        print("Brak produktu w magazynie!")
    elif manager.stock[product_name] >= int(amount):
        manager.stock[product_name] -= int(amount)
        manager.balance += int(price)*int(amount)
    else:
        print("Brak wystarczającej ilości")


file_manager.open_file()
file_manager.file_process(manager)
print("Stan konta: ", manager.balance)