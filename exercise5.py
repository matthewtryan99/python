###In class exercise
##Exercise 1
class Person: 
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.count = 0
        self.uniq_count = 0
        self.greeted = []

    def greet(self, other_person):
        print(f'Hello {other_person.name}, I am {self.name}!')
        if other_person.name not in self.greeted:
            self.greeted.append(other_person.name)
            self.uniq_count += 1
        
        self.count += 1
    
    def print_contact_info(self):
        print(f'{self.name}\'s email: {self.email}, {self.name}\'s phone number: {self.phone}')

    def add_friend(self, other_person):
        self.friends.append(other_person)
    
    def num_friends(self):
        return len(self.friends)

    def greeting_count(self):
        return self.count

    def __str__(self):
        return (f'Person: {self.name} {self.email} {self.phone}')

    def uniq_greeting(self):
        return self.uniq_count


sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

matt = Person('Matt', 'matt@website.com', '123-456-7890')

sonny.greet(jordan)
sonny.greet(jordan)
jordan.greet(sonny)

print(sonny.phone, sonny.email)
print(jordan.phone, jordan.email)

sonny.print_contact_info()

sonny.add_friend(jordan)
sonny.add_friend(matt)

print(len(sonny.friends))

print(sonny.num_friends())

print(sonny.greeting_count())
print(sonny.uniq_greeting())

##Exercise 2
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def print_info(self):
#         print(self.make, self.model, self.year)

# car = Vehicle('Nissan', 'Leaf', 2015)
# car.print_info()