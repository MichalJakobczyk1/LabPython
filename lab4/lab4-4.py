import random

#Bird
class Bird:
    def __init__(self, name, color, wingspan):
        self.__name = name
        self.__color = color
        self.__wingspan = wingspan

    def make_sound(self, *args):
        return "Some sound"

    def get_info(self):
        return f" Bird: {self.__name} \n Color: {self.__color} \n Wingspan: {self.__wingspan}"

    def fly(self):
        return f"{self.__name} is flying with a wingspan of {self.__wingspan} cm."

    def build_nest(self):
        return "Building nest"


class Swallow(Bird):
    def make_sound(self):
        return "Trelelele"

    def build_nest(self):
        return "Swallow is building nest"

    def search_companion(self):
        return "Swallow is looking for company"


class Falcon(Bird):
    def __init__(self, name, color, wingspan, flight_speed):
        super().__init__(name, color, wingspan)
        self.__flight_speed = flight_speed

    def make_sound(self):
        return "Skrrreeee"

    def build_nest(self):
        return "Falcon is building nest"

    def attack_prey(self):
        return f"Falcon is attacking prey with: {self.__flight_speed} km/h"


class Parrot(Bird):
    def make_sound(self, message):
        return f"Parrot is trying to repeat after you and after moment make sound: {message}"

    def build_nest(self):
        return "Parrot is building nest"


basic_bird = Bird("bird","black",23)
print(basic_bird.get_info())
print(basic_bird.make_sound())
print(basic_bird.fly())
print(basic_bird.build_nest())
print("\n")

swallow = Swallow("Swallow","white",14)
print(swallow.get_info())
print(swallow.make_sound())
print(swallow.fly())
print(swallow.build_nest())
print(swallow.search_companion())
print("\n")

falcon = Falcon("Falcon","brown", 120, 64)
print(falcon.get_info())
print(falcon.make_sound())
print(falcon.fly())
print(falcon.build_nest())
print(falcon.attack_prey())
print("\n")

parrot = Parrot("Parrot","red", 45)
print(parrot.get_info())
print(parrot.make_sound("Hi ara what's up"))
print(parrot.fly())
print(parrot.build_nest())
print("\n")


#Warrior


class Unit:
    def __init__(self, name, health, energy, attack, defense):
        self.name = name
        self.health = health
        self.energy = energy
        self.attack = attack
        self.defense = defense

    def display_info(self):
        return (f"This is {self.name} unit with "
                f"\n {self.health} health "
                f"\n {self.energy} energy "
                f"\n {self.attack} attack "
                f"\n {self.defense} defense ")

    def attack_unit(self):
        return f"{self.name} attacks with {self.attack} damage"

    def defend_attack(self):
        return f"{self.name} defends attack and gets {self.defense}% reduced damage"


class Warrior(Unit):
    max_armor = 0

    def __init__(self, name, health, energy, attack, defense, armor):
        super().__init__(name, health, energy, attack, defense)
        self.__armor = armor
        Warrior.max_armor = self.__armor

    def defend_attack(self):
        if self.__armor > 1:
            self.__armor -= 1
            return f"{self.name} blocks attack, remaining armor: {self.__armor}/{self.max_armor}"
        elif self.__armor == 1:
            return f"Armor breaks. Now {self.name} defends attack and gets {self.defense}% reduced damage"
        else:
            return f"{self.name} defends attack and gets {self.defense}% reduced damage"


class Berserk(Unit):
    def __init__(self, name, health, energy, attack, defense, *rage):
        super().__init__(name, health, energy, attack, defense)
        self.__rage = 0

    def randomize_with_percentage(self, value):
        random_number = random.uniform(0, 100)

        return random_number < value

    def attack_unit(self):
        print(self.__rage)
        self.__rage += random.randint(0, self.attack)
        result = self.randomize_with_percentage(self.__rage)
        if result:
            return f"{self.name} crits for {self.attack*2} damage!"
        else:
            return f"{self.name} attacks with {self.attack} damage"


class Spell:
    def __init__(self, name, cost, damage):
        self.__name = name
        self.__cost = cost
        self.__damage = damage


class Mage(Unit):
    max_mana = 0

    def __init__(self, name, health, energy, attack, defense, mana):
        super().__init__(name, health, energy, attack, defense)
        self.__mana = mana
        Mage.max_mana = self.__mana

    def cast_spell(self, spell):
        if spell._Spell__cost > self.__mana:
            return f"Not enough mana"
        else:
            self.__mana -= spell._Spell__cost
            return f"{self.name} is casting {spell._Spell__name} for {spell._Spell__damage} damage {self.__mana}/{self.max_mana} remaining"


fireball = Spell("fireball", 15, 60)
ice_spike = Spell("ice spike", 10, 40)
earthquake = Spell("earthquake", 25, 100)

warrior = Warrior("Rodrig", 100, 50, 15, 30, 3)
print(warrior.display_info())
print(warrior.attack_unit())
print(warrior.defend_attack())
print(warrior.defend_attack())
print(warrior.defend_attack())
print("\n")

berserk = Berserk("Olaf", 70, 80, 30, 12)
print(berserk.display_info())
print(berserk.attack_unit())
print(berserk.attack_unit())
print(berserk.attack_unit())
print(berserk.attack_unit())
print(berserk.attack_unit())
print(berserk.defend_attack())
print("\n")

mage = Mage("Gandalf", 50, 30, 30, 5, 100)
print(mage.display_info())
print(mage.attack_unit())
print(mage.cast_spell(fireball))
print(mage.cast_spell(ice_spike))
print(mage.cast_spell(earthquake))
print(mage.cast_spell(earthquake))
print(mage.cast_spell(earthquake))
print(mage.cast_spell(earthquake))

