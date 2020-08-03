class Vehicle:
    
    category = "pickup_truck"
    bed_length = "standard"
    doors = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return "%d %s, %s for sale; clean title, priced low." % (self.year, self.make, self.model)


my_truck = Vehicle("Dodge", "Ram", 2000)

print(my_truck)