# Q31. Create a class called "Person" with properties for "name", "age", and "gender". Create an object of this
# class and print out its properties.

class Person:
    def __init__(self, name:str, age:int, gender:str):
        self.name = name
        self.age = age
        self.gender = gender


me = Person('Darshan Baslani', 18, 'male')

print(me.name)
print(me.age)
print(me.gender)