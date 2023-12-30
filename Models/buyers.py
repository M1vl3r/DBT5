from Models.Model import Model


class buyers(Model):

    def get7(self):
        start_date = input("Введите начальную дату ")
        end_date = input("Введите конечную дату ")
        return super().get7(start_date, end_date)

    def get11(self):
        seller_name = input("Введите имя продавца ")
        seller_surname = input("Введите фамилию продавца ")
        buyers_name = input("Введите имя покупателя ")
        buyers_surname = input("Введите фаимлию покупателя ")
        return super().get11(seller_name, seller_surname, buyers_name, buyers_surname)