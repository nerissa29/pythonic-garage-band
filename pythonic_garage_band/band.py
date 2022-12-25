class Band:
    members = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.__class__.members.append(self)

    def __str__(self):
        results = ""
        members = []
        for member in self.members:
            results += member.__str__()

    def __repr__(self):
        return f"{self.name}"

    # def instruments(self):
    #     instruments = []
    #     for ins in self.
    #     instruments.append(self.get_instrument)

    def play_solos(self, grp):
        for member in grp.members:
            print(f"{member.instrument}, {member}")

    def band_data(grp, nirvana_data):
        for group in nirvana_data:
            if group.members['instrument'] == "guitar":
                grp.members.append(
                    Guitarist(group['name'], group['instrument']))
                continue
            elif group.members['instrument'] == "bass":
                grp.members.append(
                    Bassist(group['name'], group['instrument']))
                continue
            elif group.members['instrument'] == "drums":
                grp.members.append(
                    Drummer(group['name'], group['instrument']))
                continue


# base class
class Musician:
    def __init__(self, name):
        self.name = name


# derived class
class Guitarist(Musician):
    # def __init__(self, name, instrument):
    def __init__(self, name):

        super().__init__(name)
        self.name = name
        # self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    # def __init__(self, name, instrument):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        # self.instrument = instrument


    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    # def __init__(self, name, instrument):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        # self.instrument = instrument


    def __str__(self):
        return  f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"


nirvana_data = {
    "name": "Nirvana",
    "members": [
        {"name": "Kurt Cobain", "instrument": "Guitar"},
        {"name": "Krist Novoselic", "instrument": "Bass"},
        {"name": "Dave Grohl", "instrument": "Drums"},
    ],
    }















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
