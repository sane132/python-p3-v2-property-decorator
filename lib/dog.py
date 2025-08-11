class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei",
        "Beagle", "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name="", breed="Mutt"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            raise ValueError("Name must be string between 1 and 25 characters.")
        self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in self.approved_breeds:
            raise ValueError("Breed must be in list of approved breeds.")
        self._breed = value
