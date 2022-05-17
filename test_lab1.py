import pytest
import main_lab1
import os.path

def test_create_database(): # Тест на создание БД
    main_lab1.init_db()
    assert os.path.exists(main_lab1.db_name) == True

def test_clients(): #Тест на наличие столбцов в Clients
    assert main_lab1.Clients.name == True
    assert main_lab1.Clients.city == True
    assert main_lab1.Clients.address == True

def test_orders(): #Тест на наличие столбцов в Orders
    assert main_lab1.Orders.clients == True
    assert main_lab1.Orders.amount ==True
    assert main_lab1.Orders.date == True
    assert main_lab1.Orders.description == True

def test_sum_clients(): #Тест на наличие 10 строк в Clients
    main_lab1.fill_db()
    assert len(main_lab1.Clients.select()) > 9

def test_sum_orders(): #Тест на наличие 10 строк в Orders
    assert len(main_lab1.Orders.select()) > 9
