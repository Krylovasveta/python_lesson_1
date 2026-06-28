from Address import Address
from Mailing import Mailing

to_a = Address("220279", "Казань", "Пионерская", "5", "5")
from_a = Address("654321", "Санкт-Петербург", "Пушкина", "20", "15")

m = Mailing(to_a, from_a, 250, "TRK123456")

m.get_info()
