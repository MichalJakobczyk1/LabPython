class Dog:
    def __init__(self, name, tail):
        self.name = name
        self.tail = tail

    def __len__(self):
        return self.tail

    def __str__(self): # lub __repr__(self)
        return "Jestem pieseczkiem " + self.name

    def __add__(self, other_dog):
        if isinstance(other_dog, Dog):
            combined_name = self.name + "i" + other_dog.name
            combined_tail = self.tail + other_dog.tail
            return Dog(combined_name, combined_tail)
        else:
            raise TypeError("You can't add dog to another object!!!")
        
    def __eq__(self, other_dog):
        if isinstance(other_dog, Dog):
            return self.tail == other_dog.tail # ;-)
        else:
            return False
        

class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.limit:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration

