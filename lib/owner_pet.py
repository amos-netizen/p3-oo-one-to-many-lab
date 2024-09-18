class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
            self._pets.append(pet)
        else:
            raise Exception("Can only add instances of Pet")

    def pets(self):
        return self._pets

    def get_sorted_pets(self):
        # Sort pets alphabetically by name
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    all = []
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

        # Automatically add the pet to the owner's list of pets, if an owner is provided
        if owner:
            owner.add_pet(self)
