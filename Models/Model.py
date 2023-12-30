from Configuration.Config import connection


class Model:

    def get1(self, start_date, last_date):
        with connection().cursor() as cursor:
            query = (f"SELECT auctions.id, auctions.date_a, auctions.place, items.name_lot "
                     f"FROM auctions "
                     f"JOIN items ON auctions.id = items.auction_id "
                     f"WHERE auctions.date_a "
                     f"BETWEEN '{start_date}' AND '{last_date}'")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def get2(self, id, date_a, place, specifica):
        with connection().cursor() as cursor:
            query = f"INSERT INTO auctions (id, date_a, place, specifica) VALUES ({id}, '{date_a}', '{place}', '{specifica}')"
            cursor.execute(query)
            connection().commit()
            print("Запись добавлена.")
            return cursor.fetchall()
        connection().close()

    def get3(self):
        with connection().cursor() as cursor:
            query = ("SELECT auctions.id, SUM(sells.Price_F) "
                     "FROM auctions "
                     "JOIN items ON auctions.id = items.auction_id "
                     "JOIN sells ON items.id = sells.item_id "
                     "GROUP BY auctions.id "
                     "ORDER BY SUM(sells.Price_F) DESC")
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def get4(self, start_date, end_date):
        with connection().cursor() as cursor:
            query = (f"SELECT items.name_lot "
                     f"FROM auctions "
                     f"INNER JOIN items ON auctions.id = items.auction_id "
                     f"INNER JOIN sells ON items.id = sells.item_id "
                     f"WHERE auctions.date_a BETWEEN '{start_date}' AND '{end_date}'")
            cursor.execute(query)
            return cursor.fetchall()
    connection().close()

    def get5(self, id, item_id, buyer_id, Price_F):
        with connection().cursor() as cursor:
            query = (f"INSERT INTO sells (id ,item_id, buyer_id, Price_F) "
                     f"VALUES ({id}, {item_id}, {buyer_id}, '{Price_F}')")
            cursor.execute(query)
            connection().commit()
            print("Запись добавлена.")
            return cursor.fetchall()
    connection().close()

    def get6(self, start_date, end_date):
        with connection().cursor() as cursor:
            query = (f"SELECT name, surname, SUM(sells.Price_F) AS total_amount "
                     f"FROM sellers "
                     f"INNER JOIN items ON sellers.id = items.seller_id "
                     f"INNER JOIN sells ON items.id = sells.item_id "
                     f"INNER JOIN auctions ON items.auction_id = auctions.id "
                     f"WHERE auctions.date_a BETWEEN {start_date} AND {end_date} "
                     f"GROUP BY sellers.name, sellers.surname")
            cursor.execute(query)
            return cursor.fetchall()
    connection().close()

    def get7(self, start_date, end_date):
        with connection().cursor() as cursor:
            query = (f"SELECT buyers.id, buyers.name, buyers.surname "
                     f"FROM buyers "
                     f"JOIN auctions ON buyers.id = auctions.date_a "
                     f"WHERE auctions.date_a BETWEEN {start_date} AND {end_date}")
            cursor.execute(query)
            return cursor.fetchall()
    connection().close()

    def get8(self, date_a, place):
        with connection().cursor() as cursor:
            query = f"INSERT INTO auctions (date_a, place) VALUES ('{date_a}', '{place}')"
            cursor.execute(query)
            print("Запись добавлена.")
            return cursor.fetchall()
    connection().close()

    def get9(self, place):
        with connection().cursor() as cursor:
            query = (f"SELECT id, date_a, place, specifica FROM auctions "
                     f"WHERE place = '{place}'")
            cursor.execute(query)
            return cursor.fetchall()
    connection().close()

    def get10(self, start_date, end_date):
        with connection().cursor() as cursor:
            query = (f"SELECT DISTINCT sellers.id, sellers.name, sellers.surname "
                     f"FROM sellers "
                     f"JOIN auctions ON sellers.id = auctions.date_a "
                     f"WHERE auction.date_a BETWEEN '{start_date}' AND '{end_date}'")
            cursor.execute(query)
            return cursor.fetchall()
    connection().close()

    def get11(self, seller_name, seller_surname, buyers_name, buyers_surname):
        with connection().cursor() as cursor:
            query = f"INSERT INTO sellers (name, surname) VALUES ('{seller_name}', '{seller_surname}');"
            cursor.execute(query)
            query = f"INSERT INTO buyers (name, surname) VALUES ('{buyers_name}', '{buyers_surname}');"
            cursor.execute(query)
            print("Запись добавлена.")
            return cursor.fetchall()
    connection().close()

