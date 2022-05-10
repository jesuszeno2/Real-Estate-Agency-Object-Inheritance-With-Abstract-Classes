"""
Jesus Zeno SIE508 Assignment 4
This file has only one minor edit from the previous assignment. For loop in ListProperties had the try
except block modified to match the methods of the update property file.
This class holds a list of real estate agents and can print that list. We can also use the methods to
assign certain properties to a specific agent. These properties can then be viewed in relation to the agent.
"""

from Property import Property, House, Apartment

class RealEstateAgent:

    # Make global variable and initiate empty list to use later
    global list_agents
    list_agents = []

    def __init__(self, name):
        # Set initial object instance variables upon instantiation
        self._properties_list = None
        self._properties_names_list = None
        self._name = name
        properties_list = []
        properties_names_list = []
        self._properties_list = properties_list
        self._properties_names_list = properties_names_list
        list_agents.append(self._name)

    # Method to help print the list of real estate agents
    def printAgentList(self):
        print("These are all the real estate agents: {}".format(list_agents))

    # Method to list out all the properties for the real estate agent
    def ListProperties(self):
        print("\n{} is responsible for the following properties:".format(self._name))
        i = 0
        # Use a for loop to iterate through all the properties for the real estate agent. In each iteration,
        # call the agent display method for the specific property type.
        for i in range(len(self._properties_list)):
            # Try except block to account for all combinations of house/apartment with pruchase/rental.
            try:
                self._properties_list[i].displayHousePurchaseForAgent()
            except:
                # print("Error displaying House Purchase for agent")
                try:
                    self._properties_list[i].displayHouseRentalForAgent()
                except:
                    # print("Error displaying House rental for agent")
                    try:
                        self._properties_list[i].displayApartmentPurchaseForAgent()
                    except:
                        # print("Error displaying apartment Purchase for agent")
                        try:
                            self._properties_list[i].displayApartmentRentalForAgent()
                        except:
                            print("Error displaying properties for Agent")
            print()  # just for more appealing spacing.
            i += 1

    # Method to add the property to the list of properties for a specific agent. Note that we are adding
    # the property objects to one list so we can call on their methods later as well as the property names
    # to another list so they are easily displayed.
    def AddProperty(self, property):
        self._properties_list.append(property)
        self._properties_names_list.append(property._property_name)
        print("\n{} has been added to {}'s property list".format(property._property_name, self._name))
        print("{}'s full property list includes:\n{}".format(self._name, self._properties_names_list))
