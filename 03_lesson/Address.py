class Address:
    def __init__(self, index, city, street, home, flat):
        self.index=index
        self.city=city
        self.street=street
        self.home=home
        self.flat=flat

    def get_index(self):
        return self.index

    def get_city(self):
        return self.city

    def get_street(self):
        return self.street

    def get_home(self):
        return self.home
    
    def get_flat(self):
        return self.flat
    