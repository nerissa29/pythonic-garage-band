class Band:
    def __init__(self, name, members):
        self.name = name or []
        self.members = members


# base class
class Musician:
    def __init__(self, name):
        self.name = name


# derived class
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def __str__(self):
        return  f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"






# class DogPack:
#     def __init__(self, dogs=None):
#         self.dogs = dogs or []
#
#     def __str__(self):
#         dog_strings = [str(dog) for dog in self.dogs]
#         # dog_strings = []
#         # for dog in self.dogs:
#         #     dog_strings.append(str(dog))
#         return " ".join(dog_strings)
#
#     def __repr__(self):
#         return f"DogPack({self.dogs})"
#
#
# # base class
# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#
# # derived class
# class Boxer(Dog):
#     def __init__(self, name="unknown", jump=0):
#         self.name = name
#         self.jump = jump
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return f"Boxer('{self.name}')"
#
#     def greet(self):
#         return f"The name's {self.name}. Pleasure."
#
#
#
#
