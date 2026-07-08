from Address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address=to_address
        self.from_address=from_address
        self.cost=cost
        self.track=track 

    def get_info(self):
        print(f"Отправление {self.track} из {self.from_address.get_index()}, {self.from_address.get_city()}, {self.from_address.get_street()}, {self.from_address.get_home()} - {self.from_address.get_flat()} в {self.to_address.get_index()}, {self.to_address.get_city()}, {self.to_address.get_street()}, {self.to_address.get_home()} - {self.to_address.get_flat()}. Стоимость {self.cost} рублей.")
