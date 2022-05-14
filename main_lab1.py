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

class Orders (BaseModel):
    clients = ForeignKeyField(Clients, backref='clients')
    date = DateTimeField()
    amount = IntegerField()
    description = CharField()

def init_db(): #создание базы данных
    if os.path.exists(db_name) == True:
        os.remove(db_name)
        print('*База данных удалена!*')
    db.create_table([Clients, Orders], safe = True)
    print('*База данных создана!*')

def fill_db():
        clients_number = 10
        print('*Заполнение базы данных*')
        clients_list = []
        name_list = ["Олег", "Алина", "Юрий", "Елизавета", "Александр", "Дарья", "Даниил", "Евгения", "Валерия", "Анастасия"]
        city_list = ["Сургут", "Москва", "Тюмень", "Нефтеюганск", "Златоуст", "Иванова", "Электросталь", "Зеленоград", "Рязань", "Уфа"]
        address_list = ["Энергетиков 22", "Энергетиков 23", "Шмитовская 15", "Университетская 12", "Мира 56", "Ленина 14", "Проспект Победы 9", "Пушкина 12", "Есенина 50", "Карла Маркса 38"]

        for i in range(clients_number):
            clients_list.append({'name': name_list[random.randint(0, len(name_list) - 1)],
                             'city': city_list[random.randint(0, len(city_list) - 1)],
                             'address': address_list[random.randint(0, len(address_list) - 1)]})

        orders_list = []
        orders_list_dis = ["Книга", "Краски", "Пряжа", "Куртка", "Корм для кошек", "Подушка", "Плакат", "Клавиатура", "Видеокарта", "Кружка", "Тетрадь"]

        for i in range(len(city_list)):
            orders_list.append({'clients': i+1, 'date':str(random.randint(2019, 2021)) + '-' + str(random.randint(1,12))
                               + '-' + str(random.randint(1,28)) + '\t' + str(random.randint(0,23)) + ':'
                               + str(random.randint(0,59)) + str(random.randint(0,59)), 'amount': random.randint(1,50),
                               'description': orders_list_dis[random.randint(0,10)]})

        Clients.insert_many(city_list).execute()
        Orders.insert_many(orders_list).execute()
        print('*<База данных заполнена!*')