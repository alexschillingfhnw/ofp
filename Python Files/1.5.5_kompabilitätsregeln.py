class Student:
    def __init__(self, first):
        self.first = first

    def say_hello(self):
        print("Hello, my name is {}!".format(self.first))

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")

class Student_Dog_Combination:
    def __init__(self, student, dog):
        self.student = student
        self.dog = dog

    def greet(self):
        self.student.say_hello()
        self.dog.bark()

student1 = Student("Nicko")                         
dog1 = Dog("Goodie")
combo1 = Student_Dog_Combination(student1, dog1)
combo1.greet()                                      # Output: "Hello, my name is Nicko!", "Woof!"

student2 = Student("Marco")
dog2 = Dog("Rolli")
combo2 = Student_Dog_Combination(student2, dog2)
combo2.greet()                                      # Output: "Hello, my name is Marco!", "Woof!"