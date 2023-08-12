from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):
        # applying super class
        super().__init__(
            name, price, quantity
        )

        # run validations for received args
        assert broken_phone >= 0, "Broken phones should be in positive"

        # assigning value
        self.broken_phone = broken_phone

        # appending objects/instances in list
        Item.all.append(self)

        # Updating phone if it doesn't contain broken phone value
        Phone.all.append(self)