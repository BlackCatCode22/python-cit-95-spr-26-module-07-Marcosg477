from datetime import date

class Animal:
    id_count = {
        "hyena": 1,
        "lion": 1,
        "tiger": 1,
        "bear": 1
    }

    def __init__(self, age, sex, species, season, color, weight, origin):
        self.age = age
        self.sex = sex
        self.species = species
        self.season = season
        self.color = color
        self.weight = weight
        self.origin = origin
        self.birth_date = self.gen_birth_date()
        self.unique_id = self.gen_unique_id()
        self.name = ""

    def gen_birth_date(self):
        current_year = 2026
        birth_year = current_year - self.age

        if self.season == "spring":
            return f"{birth_year}-03-21"
        elif self.season == "summer":
            return f"{birth_year}-06-21"
        elif self.season == "fall":
            return f"{birth_year}-09-21"
        elif self.season == "winter":
            return f"{birth_year}-12-21"
        else:
            return f"{birth_year}-01-01"

    def gen_unique_id(self):
        prefix = self.species[:2].capitalize()
        number = Animal.id_count[self.species]
        Animal.id_count[self.species] += 1
        return prefix + str(number).zfill(2)

    def __str__(self):
        return f"{self.unique_id}; {self.name}; birth date: {self.birth_date}; {self.color} color; {self.sex}; {self.weight} pounds; from {self.origin}; arrived 2026-04-26"


class Hyena(Animal):
    pass


class Lion(Animal):
    pass


class Tiger(Animal):
    pass


class Bear(Animal):
    pass


animal_names = {
    "hyena": ["Kamari", "Zuri", "Nala", "Tano"],
    "lion": ["Simba", "Leo", "Mufasa", "Kion"],
    "tiger": ["Rajah", "Shere", "Tora", "Kali"],
    "bear": ["Baloo", "Bruno", "Kodiak", "Yogi"]
}

arriving_animals = [
    "4 female hyena spring tan 70 Tunisia",
    "6 male lion summer gold 420 Kenya",
    "3 female tiger fall orange 260 India",
    "8 male bear winter brown 600 Alaska",
    "5 female hyena summer gray 75 Morocco"
]

zoo = {
    "hyena": [],
    "lion": [],
    "tiger": [],
    "bear": []
}

for line in arriving_animals:
    data = line.split()

    age = int(data[0])
    sex = data[1]
    species = data[2]
    season = data[3]
    color = data[4]
    weight = int(data[5])
    origin = data[6]

    if species == "hyena":
        animal = Hyena(age, sex, species, season, color, weight, origin)
    elif species == "lion":
        animal = Lion(age, sex, species, season, color, weight, origin)
    elif species == "tiger":
        animal = Tiger(age, sex, species, season, color, weight, origin)
    elif species == "bear":
        animal = Bear(age, sex, species, season, color, weight, origin)

    animal.name = animal_names[species].pop(0)
    zoo[species].append(animal)

with open("zooPopulation.txt", "w") as file:
    for habitat in zoo:
        file.write(habitat.capitalize() + " Habitat:\n\n")

        for animal in zoo[habitat]:
            file.write(str(animal) + "\n")

        file.write("\n")

print("zooPopulation.txt created successfully.")