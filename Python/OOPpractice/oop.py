from item import Item
from phone import Phone


phone1 = Phone("samsung", 8000, 5, 0)
phone2 = Phone("apple", 80000, 5, 1)
print(Phone.all)
print(Item.all)
print(phone2.price)
xyz = 0


def sum(x: int, y: int):
    return x + y


x = sum("ding", "ding")
"""
Item.instantiate_from_csv()
print(Item.all)

#Object creation/ instance creation
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(item1.calculate_total_price())

print(Item.pay_rate)
print(item1.pay_rate)

print(Item.__dict__) #This will give me all the attributes at class level
print(item1.__dict__) #This will give me all the attributes at method level

item1.apply_discount()
print(item1.price)
item2.pay_rate = 0.7 #This will apply 30% discount to item 2
item2.apply_discount()
print(item2.price)

for instance in Item.all:
    print(instance.name)

print(Item.all)
"""
