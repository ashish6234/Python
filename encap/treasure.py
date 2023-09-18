class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name  # Getter method for name

    def get_age(self):
        return self.__age   # Getter method for age

    def set_name(self, name):
        self.__name = name  # Setter method for name

    def set_age(self, age):
        if age < 0:
            print("Age cannot be negative.")
        else:
            self.__age = age  # Setter method for age

# Create a person
person1 = Person("Alice", 30)

# Try to access the private attributes directly (this will not work)
# Uncomment the lines below to see the errors.
# print(person1.__name)
# print(person1.__age)

# Access and modify the attributes using getter and setter methods
print("Original Name:", person1.get_name())
print("Original Age:", person1.get_age())

person1.set_name("Bob")
person1.set_age(25)

print("Updated Name:", person1.get_name())
print("Updated Age:", person1.get_age())
