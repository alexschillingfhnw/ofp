class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

class Address:
    def __init__(self, street, house_number, city, postal_code):
        self.street = street
        self.house_number = house_number
        self.city = city
        self.postal_code = postal_code

class Contact:
    def __init__(self, person, address, phone_number):
        self.person = person
        self.address = address
        self.phone_number = phone_number

person1 = Person("Nicko Jorgensson", 2000)
person2 = Person("Marco Odermatt", 1999)
address1 = Address("Bahnhofstrasse", "12", "Aarau", "5000")
address2 = Address("Hauptstrasse", "111", "Erlinsbach", "5018")

person1.add_friend(person2)
person2.add_friend(person1)

contact1 = Contact(person1, address1, "0786564738")
contact2 = Contact(person2, address2, "0798847362")

print(contact1.person.name, "lives in", contact1.address.city)
print(contact2.person.name, "has friend", contact2.person.friends[0].name)

contact2.address.city = "Lenzburg"
contact2.address.postal_code = "5100"

print(contact1.person.name, "now lives in", contact1.address.postal_code, contact1.address.city)
print(contact2.person.name, "now lives in", contact2.address.postal_code, contact2.address.city)
