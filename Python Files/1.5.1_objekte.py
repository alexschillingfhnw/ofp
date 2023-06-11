class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

my_dog = Dog("Goodie", 10)
print(my_dog.name)                  # Output: "Goodie"
my_dog.bark()                       # Output: "Woof!"