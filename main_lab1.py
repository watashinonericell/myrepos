from peewee import *
from sys import argv
import datetime
import random
import os.path
import pytest

db_name = 'database.db'
db = SqliteDatabase(db_name)


class BaseModel(Model):
    class Meta:
        database = db


class Clients(BaseModel):
    name = CharField()
    city = CharField()
    address = CharField()


class Orders(BaseModel):
    clients = ForeignKeyField(Clients, backref='client')
    date = DateTimeField()
    amount = IntegerField()
    description = CharField()


def init_db():
    # Создание или удаление базы данных
    if os.path.exists(db_name) == True:
        os.remove(db_name)
        print('* База данных удалена! *')
    db.create_tables([Clients, Orders], safe=True)
    print('* База данных создана! *')

def fill_db():
        clients_number = 10
        print('*Заполнение базы данных*')
        clients_list = []
        name_list = ["Олег", "Алина", "Юрий", "Елизавета", "Александр", "Дарья", "Даниил", "Евгения", "Валерия", "Анастасия"]
        city_list = ["Москва", "Москва", "Рязань", "Иванова", "Рязань", "Москва", "Москва", "Сургут", "Сургут", "Сургут"]
        address_list = ["Энергетиков 22", "Энергетиков 23", "Быстринская 22", "Университетская 12", "Мира 56", "Ленина 14", "проспект Победы 9", "Пушкина 12", "Есенина 50", "Карла Маркса 38"]

        for i in range(clients_number):
            clients_list.append({'name': name_list[random.randint(
                0, len(name_list) - 1)], 'city': city_list[random.randint(0, len(city_list) - 1)],
                                 'address': address_list[random.randint(0, len(address_list) - 1)]})

        orders_list = []
        orders_list_dis = ["Книга", "Краски", "Пряжа", "Куртка", "Корм для кошек", "Подушка", "Плакат", "Клавиатура", "Видеокарта", "Кружка", "Тетрадь"]

        for i in range(len(clients_list)):
            orders_list.append({'clients': i + 1,
                                'date': str(random.randint(2019, 2021)) + '-' + str(random.randint(1, 12)) + '-' + str(
                                    random.randint(1, 28)) + '\t' + str(random.randint(0, 23)) + ':' + str(
                                    random.randint(0, 59)) + ':' + str(random.randint(0, 59)),
                                'amount': random.randint(1, 50), 'description': orders_list_dis[random.randint(0, 10)]})

        Clients.insert_many(clients_list).execute()
        Orders.insert_many(orders_list).execute()
        print('*База данных заполнена!*')

def print_clients():
    print('\n******************TABLE CLIENTS******************\n')
    print('\nNAME\t\tCITY\t\tADDRESS')
    query = Clients.select().order_by(Clients.id)
    for row in query:
        print(row.name, row.city, row.address, sep='\t\t', end='\n')

def print_orders():
    print('\n*********************************TABLE ORDERS*********************************\n')
    print('\nID CLIENTS\t\tDATE\t\t\tAMOUNT\t\tDESCRIPTION')
    query = Orders.select().order_by(Orders.id)
    for row in query:
        print(row.clients.name, row.date, row.amount, row.description, sep='\t\t', end='\n')

def show_db(n):
    if n == 'Clients':
        print_clients()
    elif n == 'Orders':
        print_orders()
    elif n == 'all':
        print_clients()
        print_orders()

if __name__ == "__main__":
    if len(argv) <= 1 :
        print(
            "Создание базы данных db:\tinit\nЗаполнение базы данных db:\tfill\nВывод таблицы db:\t\tshow\nСтарт:\t\t\t\tstart")
    else:
        if argv[1] == 'init':
            init_db()
        if argv[1] == 'fill':
            fill_db()
        if argv[1] == 'show':
            if len(argv) <= 2:
                print("Укажите таблицу, которую нужно вывести:\tClients, Orders, all")
            else:
                show_db(argv[2])
        if argv[1] == 'start':
            init_db()
            fill_db()
            show_db('all')