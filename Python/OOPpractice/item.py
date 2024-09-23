import csv


class Item:
    pay_rate = 0.8  # 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # run validations for received args
        assert price >= 0, "Price should be positive"
        assert quantity >= 0, "Quantity should be positive"

        # assigning value
        self.__name = name
        self.price = price
        self.quantity = quantity

        # appending objects/instances in list
        Item.all.append(self)

    @property
    def name(self):
        """to make name read only"""
        return self.__name

    @name.setter
    def name(self, value):
        """This will enable to rename the name attribute. @property method will no longer work."""
        self.__name = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open(r'D:\DataScience\Python\items.csv', "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            price = float(item.get('Price'))  # Use 0 as default value if 'Price' is missing
            quantity = int(item.get('Quantity'))  # Use 0 as default value if 'Quantity' is missing

            Item(
                name=item.get('Name'),
                price=price,
                quantity=quantity,
            )

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate