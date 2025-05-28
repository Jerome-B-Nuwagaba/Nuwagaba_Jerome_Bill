class Country:
    def show(self):
        print("Method from class Country")

class District(Country):
    def show(self):
        print("Method from class District")

class Division(Country):
    def show(self):
        print("Method from class Division")

class Village(District, Division):
    pass

x = Village()
x.show()

# Check the method resolution order
print(Village.__mro__)
