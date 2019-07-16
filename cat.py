class Cat:
    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time
    
    def __str__(self):
        return "{}, {} and {}".format(self.name, self.preferred_food, self.meal_time)

    def eats_at(self):
        if self.meal_time > 12:
            return self.meal_time - 12 + "PM" 
        elif self.meal_time == 12:
            return self.meal_time + "PM"  
        else:
            return self.meal_time + "AM"
    
    def meow(self):
        if self.meal_time > 12:
            return "My name is {} and I eat {} at {} PM".format(self.name, self.preferred_food, self.meal_time - 12)
        elif self.meal_time == 12:
            return "My name is {} and I eat {} at {} PM".format(self.name, self.preferred_food, self.meal_time)
        else:
            return "My name is {} and I eat {} at {} AM".format(self.name, self.preferred_food, self.meal_time)

cora = Cat("Cora", "gravy chicken entree", 11)
mia = Cat("Mia", "salmon", 14)

print(cora.meow())
print(mia.meow())