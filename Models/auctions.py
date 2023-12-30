from Models.Model import Model


class auctions(Model):

    def get1(self):
        start_date = input("Введите начальную дату ")
        last_date = input("Введите конечную дату ")
        return super().get1(start_date, last_date)

    def get2(self):
        id = input("Введите id аукциона который хотите добавить ")
        date_a = input("Введите дату аукциона который хотите добавить ")
        place = input("Введите название проведения аукциона ")
        specifica = input("Введите специфику аукциона ")
        return super().get2(id, date_a, place, specifica)

    def get3(self):
        return super().get3()

    def get4(self):
        start_date = input("Введите начальную дату ")
        end_date = input("Введите конечную дату ")
        return super().get4(start_date, end_date)

    def get8(self):
        date_a = input("Введите дату проведения аукциона ")
        place = input("Введите место проведения ацкциона ")
        return super().get8(date_a, place)

    def get9(self):
        place = input("Введите место проведения ацкциона ")
        return super().get9(place)
