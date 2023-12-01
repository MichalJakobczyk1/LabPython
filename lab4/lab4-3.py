class Employee:
    def __init__(self, name, profession, salary):
        self.name = name
        self.profession = profession
        self.salary = salary

    def get_info(self):
        return f" Name: {self.name} \n Profession: {self.profession} \n Salary: {self.salary}"

    def change_prof(self, new_prof):
        self.profession = new_prof

    def increase_salary(self, amount):
        self.salary += amount


class Monster:
    def __init__(self, name, health, defense):
        self.name = name
        self.health = health
        self.defense = defense

    def get_info(self):
        return f" Name: {self.name} \n Health: {self.health} \n Defense: {self.defense}"

    def defend_attack(self, damage):
        max_health = self.health
        self.health -= (damage - self.defense)
        print(f"After attack monster has: {self.health}/{max_health}")

    def heal_monster(self, *amount):
        print(f"Monster will be regenerating for {amount} seconds")
        for i in amount:
            self.health += i
        print("Monster is fully regenerated")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
        
class Refrigerator:
    def __init__(self, capacity, brand, products=[]):
        self.capacity = capacity
        self.brand = brand
        self.products = products

    def add_product(self, product):
        if len(self.products) < self.capacity:
            self.products.append(product)
        else:
            print("Refrigerator is full")

    def delete_product(self, product):
        if len(self.products) > 0:
            self.products.remove(product)
        else:
            print("Refrigerator is empty")

    def show_inside(self):
        if len(self.products) > 0:
            print("Refrigerator products are:")
            for p in self.products:
                print(f"{p.name} - {p.price} PLN")
        else:
            print("Refrigerator is empty")


emp = Employee("Jan","spawacz",5000)
print(emp.get_info())
emp.change_prof("tynkarz")
emp.increase_salary(500)
print(emp.get_info())
print("\n")

mon = Monster("Bruxa",70,12)
mon.get_info()
mon.defend_attack(20)
mon.heal_monster(8)
print("\n")

eggs = Product("eggs",12)
apple = Product("apple",4)
banana = Product("banana",5)
ham = Product("ham",10)
ref = Refrigerator(3,"Beko",[eggs,apple,banana])
ref.show_inside()
ref.delete_product(eggs)
ref.show_inside()
ref.add_product(eggs)
ref.add_product(ham)
ref.delete_product(apple)
ref.delete_product(banana)
ref.delete_product(eggs)
ref.delete_product(eggs)
ref.show_inside()

