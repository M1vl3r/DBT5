from Models.Model import Model


class sellers(Model):

    def get6(self):
        start_date = input("Введите начальную дату ")
        end_date = input("Введите конечную дату ")
        return super().get6(start_date, end_date)

    def get10(self):
        start_date = input("Введите начальную дату ")
        end_date = input("Введите конечную дату ")
        return super().get6(start_date, end_date)