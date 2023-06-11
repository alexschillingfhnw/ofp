class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last

student1 = Student("Nicko", "Jorgensson")
student2 = Student("Marco", "Odermatt")

print(student1.first)                       # Output: "Nicko"
print(student2.last)                        # Output: "Odermatt"