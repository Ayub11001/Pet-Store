import random as rand


class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        return f'Name: {self.name}\nAge: {self.age}\n Species: {self.species}\n'


class Cat(Pet):
    def __init__(self, name, species, age, color, breed):
        super().__init__(name, species, age)
        self.color = color
        self.breed = breed

    def display_info(self):
        return f'Name: {self.name}\nAge: {self.age}\n Species: {self.species}\nColor: {self.color}\nBreed: {self.breed}\n'


class Dog(Pet):
    def __init__(self, name, species, age, color, breed):
        super().__init__(name, species, age)
        self.color = color
        self.breed = breed

    def display_info(self):
        return f'Name: {self.name}\nAge: {self.age}\n Species: {self.species}\nColor: {self.color}\nBreed: {self.breed}\n'


class PetAdoptionCenter:
    def __init__(self):
        self.available_pets = {}
        self.adopted_pets = {}

    pet_count = 0
    pet_care_preferences = ({'Dog': ('Walking', 'Bones', 'Fetch', 'Head-Scratches')},
                            {'Cat': ('Napping', 'Cuddling', 'Chickem', 'Belly-Rubs', 'Chaos-Causing')})

    def display_pet_care_preferences(self, pet):
        pet = pet.lower()

        if pet != "cat" and pet != "dog":
            raise ValueError("Invalid pet")

        index = 0 if pet == "dog" else 1

        return ", ".join(PetAdoptionCenter.pet_care_preferences[index][pet.capitalize()])  # Fixing "capitalize()"

    def generate_pet_ID(self, pet=None):
        if pet is None:
            raise ValueError("No animal provided")

        if not isinstance(pet, (Dog, Cat)):
            raise ValueError("This Pet Adoption Center only supports Cats and Dogs!!")
        pet_id = rand.randint(10000, 99999)

        if isinstance(pet, Cat):
            return f"C{pet_id}"
        elif isinstance(pet, Dog):
            return f"D{pet_id}"

    def get_available_pets(self):
        if not self.available_pets:
            return "No pets currently available for adoption!!!"

        pet_info = "\n\n".join(
            f"Name: {pet.name}\nPet-ID: {pet_id}\nAge: {pet.age}\nSpecies: {pet.species}\nColor: {pet.color}\nBreed: {pet.breed}\n"
            for pet_id, pet in self.available_pets.items()
        )
        return pet_info

    def get_adopted_pets(self):
        if not self.adopted_pets:
            return "No pets adopted yet!"

        pet_info = "\n\n".join(
            f"Name: {pet.name}\nPet-ID: {pet_id}\nAge: {pet.age}\nSpecies: {pet.species}\nColor: {pet.color}\nBreed: {pet.breed}\n"
            for pet_id, pet in self.adopted_pets.items()
        )
        return pet_info

    def get_pet_by_ID(self, pet_id):
        if pet_id not in self.adopted_pets and pet_id not in self.available_pets:
            raise ValueError("Invalid pet-ID entered!!")
        pet = self.available_pets[pet_id] if pet_id in self.available_pets else self.adopted_pets[pet_id]

        return f"Name: {pet.name}\nPet-ID: {pet_id}\nAge: {pet.age}\nSpecies: {pet.species}\nColor: {pet.color}\nBreed: {pet.breed}\n"

    def rehome_pets(self, pet):
        if pet is None:
            raise ValueError("No pet provided!!")
        pet_id = self.generate_pet_ID(pet)
        self.available_pets[pet_id] = pet
        return "Pet you brought has been rehomed!!!"

    def adopt_pet(self, pet_id):
        if pet_id in self.adopted_pets:
            return "Pet of your choice has already been adopted!!"
        elif pet_id not in self.available_pets:
            raise ValueError("Invalid pet-ID entered!!")

        self.adopted_pets[pet_id] = self.available_pets.pop(pet_id)
        PetAdoptionCenter.pet_count += 1
        return f"Congratulations, you have successfully adopted {self.adopted_pets[pet_id].name}"


def main():
    center = PetAdoptionCenter()

    while True:
        print("\n Pet Adoption Center ")
        print("1. Rehome a Pet")
        print("2. View Available Pets")
        print("3. View Adopted Pets")
        print("4. Search Pet by ID")
        print("5. Adopt a Pet")
        print("6. View Pet Care Preferences")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter pet name: ")
            species = input("Enter species (Cat/Dog): ").capitalize()
            age = int(input("Enter pet age: "))
            color = input("Enter pet color: ")
            breed = input("Enter pet breed: ")

            if species == "Cat":
                pet = Cat(name, species, age, color, breed)
            elif species == "Dog":
                pet = Dog(name, species, age, color, breed)
            else:
                print("Invalid species! Only Cats and Dogs are allowed.")
                continue

            print(center.rehome_pets(pet))

        elif choice == "2":
            print(center.get_available_pets())

        elif choice == "3":
            print(center.get_adopted_pets())

        elif choice == "4":
            pet_id = input("Enter Pet ID to search: ")
            try:
                print(center.get_pet_by_ID(pet_id))
            except ValueError as e:
                print(e)

        elif choice == "5":
            pet_id = input("Enter Pet ID to adopt: ")
            print(center.adopt_pet(pet_id))

        elif choice == "6":
            species = input("Enter species (Cat/Dog) to view preferences: ").lower()
            try:
                print(center.display_pet_care_preferences(species))
            except ValueError as e:
                print(e)

        elif choice == "7":
            print("Thank you for using the Pet Adoption Center!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
