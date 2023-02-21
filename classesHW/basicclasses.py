#!usr/bin/evn python3

class House():
    """description of the hous"""

    def __init__(self, street, number):
        self.street = street
        self.number = number

    def build(self):
        """completed house"""
        print("Hous in the street" + self.street + "number" + str(self.number) + "finished.")


class BanderaArea(House):
    """hous on the area"""

    def __init__(self, area, street, number):
        super().__init__(street, number)
        self.area = area
AreaHous = BanderaArea("Bandery", 'Shevchenka', 8)
print(AreaHous.street)
