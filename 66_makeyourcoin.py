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
class One_Pence(Coin):

    def __init__(self):
        # Dictionary for the data pound class. This is specific for each coin
        data = {
            "original_value": 0.01,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56,
        }
        # Super Class means parent class. It will run the constructor and pass all the data as keyword arguments. **data is used to unpack the data
        super().__init__(**data)


#Child class (inheritance)
class Two_Pence(Coin):

    def __init__(self):
        # Dictionary for the data pound class. This is specific for each coin
        data = {
            "original_value": 0.02,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12,
        }
        # Super Class means parent class. It will run the constructor and pass all the data as keyword arguments. **data is used to unpack the data
        super().__init__(**data)


#Child class (inheritance)
class Five_Pence(Coin):

    def __init__(self):
        # Dictionary for the data pound class. This is specific for each coin
        data = {
            "original_value": 0.05,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 18.0,
            "thickness": 1.77,
            "mass": 3.25,
        }
        # Super Class means parent class. It will run the constructor and pass all the data as keyword arguments. **data is used to unpack the data
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour


#Child class (inheritance)
class Ten_Pence(Coin):

    def __init__(self):
        # Dictionary for the data pound class. This is specific for each coin
        data = {
            "original_value": 0.10,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 24.5,
            "thickness": 1.85,
            "mass": 6.50,
        }
        # Super Class means parent class. It will run the constructor and pass all the data as keyword arguments. **data is used to unpack the data
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour


#Child class (inheritance)
class Twenty_Pence(Coin):

    def __init__(self):
        # Dictionary for the data pound class. This is specific for each coin
        data = {
            "original_value": 0.20,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 21.4,
            "thickness": 1.7,
            "mass": 5.00,
        }
        # Super Class means parent class. It will run the constructor and pass all the data as keyword arguments. **data is used to unpack the data
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour


#Child class (inheritance)
class Fifty_Pence(Coin):

    def __init__(self):
        # Dictionary for the data pound class. This is specific for each coin
        data = {
            "original_value": 0.50,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 27.3,
            "thickness": 1.78,
            "mass": 8.00,
        }
        # Super Class means parent class. It will run the constructor and pass all the data as keyword arguments. **data is used to unpack the data
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour

#Child class (inheritance)
class One_Pound(Coin):

    def __init__(self):
        # Dictionary for the data pound class. This is specific for each coin
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5,
        }
        # Super Class means parent class. It will run the constructor and pass all the data as keyword arguments. **data is used to unpack the data
        super().__init__(**data)


#Child class (inheritance)
class Two_Pound(Coin):

    def __init__(self):
        # Dictionary for the data pound class. This is specific for each coin
        data = {
            "original_value": 2.00,
            "clean_colour": "gold & silver",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 28.4,
            "thickness": 2.50,
            "mass": 12.00,
        }
        # Super Class means parent class. It will run the constructor and pass all the data as keyword arguments. **data is used to unpack the data
        super().__init__(**data)


   







