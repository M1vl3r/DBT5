from Models.Model import Model


class sells(Model):

    def get5(self):
        id = input("Введите id продажи ")
        item_id = input("Введите id товара для продажи ")
        buyer_id = input("Введите id покупателя ")
        Price_F = input("Введите цену продажи товара ")
        return super().get5(id, item_id, buyer_id, Price_F)