"""
Jesus Zeno SIE 508 Assignment 4
This is a modification of the third assignment.
We will make an abstract parent property class that will have certain attributes. House and apartment
will be children classes of property. There are Purchase and Rental classes. HousePurchase, HouseRental,
ApartmentPurchase, and ApartmentRental will be child classes of multiple inheritance from a combination
of House OR Apartment AND Purchase OR Rental.
"""

from abc import ABC, abstractmethod

# Parent abstract class to House and Apartment
class Property(ABC):
    @abstractmethod
    # Abstract method to display all the object instance variables
    def display(self):
        pass

    @abstractmethod
    # More specific abstract method to display object instance variables for a specific Real Estate Agent.
    def displayPropertyForAgent(self):
        pass


# Here we are making the House class which is a child of the property class.
class House(Property):
    def __init__(self, property_name="", square_feet="", num_bedrooms="",
                                 num_bathrooms="", address="", num_stories="", garage="",
                                 fenced_yard="", **kwargs):
        super().__init__(**kwargs)  # Passes on any unused kwargs into next (child) class.
        # Initialize all the protected object variables in the appropriate data type.
        self._property_name = property_name
        self._square_feet = int(square_feet)
        self._num_bedrooms = int(num_bedrooms)
        self._num_bathrooms = float(num_bathrooms)
        self._address = address
        self._num_stories = int(num_stories)
        self._garage = str(garage)
        self._fenced_yard = str(fenced_yard)
        # Check which kwargs are left
        # print("kwargs in initialize house property: ", kwargs)

    # Display all house attributes.
    def display(self):
        print("\nInfo for property: {}".format(self._property_name))
        print("Square feet: {}sqft".format(self._square_feet))
        print("Number of bedrooms: {}".format(self._num_bedrooms))
        print("Number of bathrooms: {}".format(self._num_bathrooms))
        print("Address: {}".format(self._address))
        print("Number of stories in the house: {}".format(self._num_stories))
        print("Garage status: {}".format(self._garage))
        print("Fence status: {}".format(self._fenced_yard))

    # More specific method to display house object instance variables for a specific Real Estate Agent
    # object.
    def displayPropertyForAgent(self):
        print(self._property_name)
        print("Property type: House")
        print("Address:\n{}".format(self._address))

# Here we are making an Apartment class which is a child of the property class.
class Apartment(Property):
    def __init__(self, property_name="", square_feet="", num_bedrooms="", num_bathrooms="", address="",
                 balcony="", laundry="", **kwargs):
        super().__init__(**kwargs)  # Passes on any unused kwargs into next (child) class.
        # Initialize all the protected object variables in the appropriate data type.
        self._property_name = property_name
        self._square_feet = int(square_feet)
        self._num_bedrooms = int(num_bedrooms)
        self._num_bathrooms = float(num_bathrooms)
        self._address = address
        self._balcony = str(balcony)
        self._laundry = str(laundry)
        # Check which kwargs are left
        # print("kwargs in initialize apartment property: ", kwargs)

    # Display all apartment attributes.
    def display(self):
        print("\nInfo for property: {}".format(self._property_name))
        print("Square feet: {}sqft".format(self._square_feet))
        print("Number of bedrooms: {}".format(self._num_bedrooms))
        print("Number of bathrooms: {}".format(self._num_bathrooms))
        print("Address: {}".format(self._address))
        print("Balcony status: {}".format(self._balcony))
        print("Laundry room status: {}".format(self._laundry))

    # More specific method to display apartment object instance variables for a specific Real Estate Agent.
    def displayPropertyForAgent(self):
        print(self._property_name)
        print("Property type: Apartment")
        print("Address:\n{}".format(self._address))


# Here we are making a purchase class. This tells us the cost of the property and its taxes. This class
# will act as a parent class to HousePurchase and ApartmentPurchase classes.
class Purchase:
    def __init__(self, price="", taxes="", **kwargs):
        super().__init__(**kwargs)  # Passes on any unused kwargs into next (child) class.
        # Initialize all the protected object variables in the appropriate data type.
        self._price = int(price)
        self._taxes = int(taxes)
        # Check which kwargs are left
        # print("kwargs in Purchase: ", kwargs)

    # Display method to show the purchase price and taxes for the property.
    def display_purchase_price(self):
        print("Price of property: $", self._price)
        print("Taxes for property: $", self._taxes)

# Here we are making a Rental class. This tells us the cost of the rental property. This will act as
# a parent class to the ApartmentRental and ApartmentPurchase classes.
class Rental:
    def __init__(self, rent="", **kwargs):
        super().__init__(**kwargs)  # Passes on any unused kwargs into next (child) class.
        # Initialize all the protected object variables in the appropriate data type.
        self._rent = float(rent)
        # Check which kwargs are left
        # print("kwargs in Rent: ", kwargs)

    # Method to display rent of property
    def display_rental_price(self):
        print("Rent of property: $", self._rent)


"""Multiple inheritance time. The classes below will inherit from a combination of House OR Apartment
AND Purchase OR Rental"""

# Multiple inheritance of House and purchase classes
class HousePurchase(House, Purchase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Passes on any unused kwargs into next (child) class.
        # Check which kwargs are left
        # print("kwargs in house purchase: ", kwargs)

    # A method to print the House property type (purchase), price, taxes, and address for agent.
    def displayHousePurchaseForAgent(self):
        # Use super to call parent methods.
        super().displayPropertyForAgent()
        super().display_purchase_price()

# Multiple inheritance of House and Rental classes
class HouseRental(House, Rental):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Passes on any unused kwargs into next (child) class.
        # Check which kwargs are left
        # print("kwargs in house rental: ", kwargs)

    # A method to print the House property type (rental), rent, and address for agent.
    def displayHouseRentalForAgent(self):
        # Use super to call parent methods.
        super().displayPropertyForAgent()
        super().display_rental_price()


# Multiple inheritance of House and purchase classes
class ApartmentPurchase(Apartment, Purchase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Passes on any unused kwargs into next (child) class.
        # Check which kwargs are left
        # print("kwargs in apartment purchase: ", kwargs)

    # A method to print the Apartment property type (purchase), price, taxes, and address for agent.
    def displayApartmentPurchaseForAgent(self):
        # Use super to call parent methods.
        super().displayPropertyForAgent()
        super().display_purchase_price()


# Multiple inheritance of House and Rental classes
class ApartmentRental(Apartment, Rental):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Passes on any unused kwargs into next (child) class.
        # Check which kwargs are left
        # print("kwargs in apartment rental: ", kwargs)

    # A method to print the Apartment property type (rental), rent, and address for agent.
    def displayApartmentRentalForAgent(self):
        # Use super to call parent methods.
        super().displayPropertyForAgent()
        super().display_rental_price()
