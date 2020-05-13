import random

#Parent class
class Coin:

    #Constructor
    def __init__(self, rare = False, clean = True, heads = True, **kwargs): #properties, **kwargs pack the data down in dictionary called kwargs
        
        # Loop trough the kwags dictionary
        for key,value in kwargs.items():
            settattr(self,key,value)


        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self): #del is destructor
        print("Coin Spent")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

#Child class (inheritance)
class Pound(Coin):

    def __init__(self):
        # Dictionary for the data pound class. This is specific for each coin
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }
        # Super Class means parent class. It will run the constructor and pass all the data as keyword arguments. **data is used to unpack the data
        super().__init__(**data)


   







