class Car:
    """
    A class to represent a car.
    
    Attributes:
    make : The make of the car.
    model : The model of the car.
    year : The year of manufacture.
    """
    
    def init(self, make, model, year):
        """
        Initializes the Car object with make, model, and year.
        
        :param make: The make of the car 
        :param model: The model of the car 
        :param year: The year of manufacture
        """
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        """
        Prints the car's make, model, and year.
        """
        print(f"Car Information: {self.year} {self.make} {self.model}")

