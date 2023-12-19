import mysql.connector

def execute_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='auction_company',
            user='root',
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def show_auctions_within_date_range(connection, start_date, end_date):
    query = f"SELECT AuctionName, AuctionDate, Location FROM Auctions WHERE AuctionDate BETWEEN '{start_date}' AND '{end_date}';"
    result = execute_query(connection, query)
    print("Результат запроса:")
    print(result)

def add_auction(connection, auction_name, auction_date, location):
    query = f"INSERT INTO Auctions (AuctionName, AuctionDate, Location) VALUES ('{auction_name}', '{auction_date}', '{location}');"
    execute_query(connection, query)
    print("Аукцион добавлен успешно.")

def show_total_income_by_auction(connection):
    query = "SELECT AuctionName, SUM(SalePrice) AS TotalIncome FROM Lots JOIN Auctions USING(AuctionID) WHERE SaleDate IS NOT NULL GROUP BY AuctionID ORDER BY TotalIncome DESC;"
    result = execute_query(connection, query)
    print("Результат запроса:")
    print(result)

def show_sold_items_within_date_range(connection, start_date, end_date):
    query = f"SELECT * FROM Lots WHERE SaleDate BETWEEN '{start_date}' AND '{end_date}';"
    result = execute_query(connection, query)
    print("Результат запроса:")
    print(result)

def add_sale(connection, auction_id, lot_number, sale_price, sale_date):
    query = f"UPDATE Lots SET SalePrice = {sale_price}, SaleDate = '{sale_date}' WHERE AuctionID = {auction_id} AND LotNumber = {lot_number};"
    execute_query(connection, query)
    print("Информация о продаже добавлена успешно.")

def show_sellers_total_income_within_date_range(connection, start_date, end_date):
    query = f"SELECT SellerName, SUM(SalePrice) AS TotalIncome FROM Lots JOIN Sellers USING(SellerID) WHERE SaleDate IS NOT NULL AND SaleDate BETWEEN '{start_date}' AND '{end_date}' GROUP BY SellerID ORDER BY TotalIncome DESC;"
    result = execute_query(connection, query)
    print("Результат запроса:")
    print(result)

def show_buyers_within_date_range(connection, start_date, end_date):
    query = f"SELECT DISTINCT BuyerName FROM Lots WHERE SaleDate IS NOT NULL AND SaleDate BETWEEN '{start_date}' AND '{end_date}';"
    result = execute_query(connection, query)
    print("Результат запроса:")
    print(result)

def add_auction_record(connection, auction_name, auction_date, location):
    query = f"INSERT INTO Auctions (AuctionName, AuctionDate, Location) VALUES ('{auction_name}', '{auction_date}', '{location}');"
    execute_query(connection, query)
    print("Запись о проведенном аукционе добавлена успешно.")

def show_auctions_by_location(connection, location):
    query = f"SELECT * FROM Auctions WHERE Location = '{location}';"
    result = execute_query(connection, query)
    print("Результат запроса:")
    print(result)

def show_sellers_participated_in_auctions_within_date_range(connection, start_date, end_date):
    query = f"SELECT DISTINCT SellerName FROM Lots WHERE SaleDate BETWEEN '{start_date}' AND '{end_date}';"
    result = execute_query(connection, query)
    print("Результат запроса:")
    print(result)

def add_or_update_seller(connection, seller_name, seller_info):
    query = f"INSERT INTO Sellers (SellerName, SellerInfo) VALUES ('{seller_name}', '{seller_info}') ON DUPLICATE KEY UPDATE SellerInfo = '{seller_info}';"
    execute_query(connection, query)
    print("Продавец добавлен или обновлен успешно.")

def show_buyers_with_purchase_count_within_date_range(connection, start_date, end_date):
    query = f"SELECT BuyerName, COUNT(*) AS PurchaseCount FROM Lots WHERE SaleDate IS NOT NULL AND SaleDate BETWEEN '{start_date}' AND '{end_date}' GROUP BY BuyerID ORDER BY PurchaseCount DESC;"
    result = execute_query(connection, query)
    print("Результат запроса:")
    print(result)

# Подключаемся к базе данных
connection = connect_to_database()

if not connection:
    print("Не удалось подключиться к базе данных.")
else:
    try:
        # Запрос номера задания
        task_number = int(input("Введите номер задания (1-12): "))

        # Выполнение соответствующего действия
        if task_number == 1:
            start_date = input("Введите начальную дату (гггг-мм-дд): ")
            end_date = input("Введите конечную дату (гггг-мм-дд): ")
            show_auctions_within_date_range(connection, start_date, end_date)
        elif task_number == 2:
            auction_name = input("Введите название аукциона: ")
            auction_date = input("Введите дату аукциона (гггг-мм-дд): ")
            location = input("Введите место проведения аукциона: ")
            add_auction(connection, auction_name, auction_date, location)
        elif task_number == 3:
            show_total_income_by_auction(connection)
        elif task_number == 4:
            start_date = input("Введите начальную дату (гггг-мм-дд): ")
            end_date = input("Введите конечную дату (гггг-мм-дд): ")
            show_sold_items_within_date_range(connection, start_date, end_date)
        elif task_number == 5:
            auction_id = int(input("Введите ID аукциона: "))
            lot_number = int(input("Введите номер лота: "))
            sale_price = float(input("Введите цену продажи: "))
            sale_date = input("Введите дату продажи (гггг-мм-дд): ")
            add_sale(connection, auction_id, lot_number, sale_price, sale_date)
        elif task_number == 6:
            start_date = input("Введите начальную дату (гггг-мм-дд): ")
            end_date = input("Введите конечную дату (гггг-мм-дд): ")
            show_sellers_total_income_within_date_range(connection, start_date, end_date)
        elif task_number == 7:
            start_date = input("Введите начальную дату (гггг-мм-дд): ")
            end_date = input("Введите конечную дату (гггг-мм-дд): ")
            show_buyers_within_date_range(connection, start_date, end_date)
        elif task_number == 8:
            auction_name = input("Введите название аукциона: ")
            auction_date = input("Введите дату аукциона (гггг-мм-дд): ")
            location = input("Введите место проведения аукциона: ")
            add_auction_record(connection, auction_name, auction_date, location)
        elif task_number == 9:
            location = input("Введите место проведения аукциона: ")
            show_auctions_by_location(connection, location)
        elif task_number == 10:
            start_date = input("Введите начальную дату (гггг-мм-дд): ")
            end_date = input("Введите конечную дату (гггг-мм-дд): ")
            show_sellers_participated_in_auctions_within_date_range(connection, start_date, end_date)
        elif task_number == 11:
            seller_name = input("Введите имя продавца: ")
            seller_info = input("Введите информацию о продавце: ")
            add_or_update_seller(connection, seller_name, seller_info)
        elif task_number == 12:
            start_date = input("Введите начальную дату (гггг-мм-дд): ")
            end_date = input("Введите конечную дату (гггг-мм-дд): ")
            show_buyers_with_purchase_count_within_date_range(connection, start_date, end_date)
        else:
            print("Некорректный номер задания. Введите число от 1 до 12.")
    finally:
        # Закрываем соединение с базой данных
        connection.close()
