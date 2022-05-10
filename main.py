"""
Jesus Zeno SIE508
This main program uses the class RealEstateAgent along with HousePurchase, HouseRental, ApartmentRental,
ApartmentPurchase. See property file for hierarchical structure of multiple inheritance classes.
Together they make a list of real estate agents and display all the agents as well as the
different aspects about each property. In addition, the program tells us which agent is in charge of
what properties.
"""

from Property import Property, House, Apartment, Purchase, Rental, HousePurchase, HouseRental, \
    ApartmentRental, ApartmentPurchase
from RealEstateAgent import RealEstateAgent

def main():

    # Here wake make the two agent objects Leo Fitz and Agent Coulson
    agent_Fitz = RealEstateAgent("Leo Fitz")
    agent_Coulson = RealEstateAgent("Phil Coulson")

    # Print the current list of real estate agents.
    agent_Coulson.printAgentList()

    # Make the HousePurchase object and display its properties
    house_1 = HousePurchase(property_name="House Purchase 1", square_feet="3000", num_bedrooms="5",
                            num_bathrooms="3.5", address="12 Rich Street", num_stories="2",
                            garage="Yes", fenced_yard="Yes", price="800000", taxes="12000")
    house_1.display()
    house_1.display_purchase_price()

    # Make HouseRental object and display its properties
    house_2 = HouseRental(property_name="House Rental 1", square_feet="2000", num_bedrooms="4",
                          num_bathrooms="2.5", address="12A Rich Street", num_stories="2",
                          garage="Yes", fenced_yard="Yes", rent="1500")
    house_2.display()
    house_2.display_rental_price()

    # Make ApartmentRental object and display its properties
    apartment_1 = ApartmentRental(property_name="Apartment Rental 1", square_feet="1200", num_bedrooms="2",
                                  num_bathrooms="1.5", address="14A Building Place", balcony="Yes",
                                  laundry="Yes", rent="1400")
    apartment_1.display()
    apartment_1.display_rental_price()

    # Make ApartmentPurchase object and display its properties
    apartment_2 = ApartmentPurchase(property_name="Apartment Purchase 1", square_feet="1000", num_bedrooms="2",
                                  num_bathrooms="1.5", address="17A Building Place", balcony="Yes",
                                  laundry="Yes", price="200000", taxes="2000")
    apartment_2.display()
    apartment_2.display_purchase_price()

    # Assign Coulson House 1 and Apartment 1
    agent_Coulson.AddProperty(house_1)
    agent_Coulson.AddProperty(apartment_1)

    # List Coulson's properties that he is in charge of
    agent_Coulson.ListProperties()

    # Assign Fitz house 2 and list the property he is in charge of.
    agent_Fitz.AddProperty(house_2)
    agent_Fitz.AddProperty(apartment_2)
    agent_Fitz.ListProperties()


if __name__ == '__main__':
    main()
