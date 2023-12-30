from Models.auctions import auctions
from Models.sells import sells
from Models.sellers import sellers
from Models.buyers import buyers
from Models.Model import Model

auctions = auctions()
buyers = buyers()
sells = sells()
sellers = sellers()

# 1 запрос
# for row, list in enumerate(auctions.get1()):
#    print(row, list)


# 2 запрос
# auctions.get2()


# 3 Запрос
# for row, list in enumerate(auctions.get3()):
#   print(row, list)


# 4 запрос
# for row, list in enumerate(auctions.get4()):
#    print(row, list)


# 5 запрос
# sells.get5()


# 6 запрос
# for row, list in enumerate(sellers.get6()):
#   print(row, list)


# 7 запрос
# for row, list in enumerate(buyers.get7()):
#   print(row, list)


# 8 запрос
# auctions.get8()


# 9 запрос
# for row, list in enumerate(auctions.get9()):
#  print(row, list)


# 10 запрос
# for row, list in enumerate(sellers.get10()):
#  print(row, list)


# 11 запрос
# buyers.get11()