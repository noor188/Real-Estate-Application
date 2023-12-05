from real_estate_transactions.house_rental import HouseRental
from real_estate_transactions.house_purchase import HousePurchase
from real_estate_transactions.apartment_rental import ApartmentRental
from real_estate_transactions.apartment_purchase import ApartmentPurchase
from errors.validation import getValidInput

class Agent:
    '''Represent the user of the application (Agent). Responsible for creating 
    new listings and displaying existing ones.'''

    typeMap = {
        ('house', 'rental') : HouseRental,
        ('house', 'purchase') : HousePurchase,
        ('apartment', 'rental') : ApartmentPurchase,
        ('apartment', 'purchase') : ApartmentPurchase
    }

    def __init__(self):
        '''Initialize an agent with an empty list.'''
        self.propertyList = []
    
    def displayProperties(self):
        '''Display all the properties characteristics.'''
        for property in self.propertyList:
            property.display()
    
    def addProperty(self):
        '''Add a property. It display a simple menu for querying the type of property and 
        whether property is for purchase or rental. Then extract the correct subclass 
        and prompt for all the details using the promptInit hierarchy.'''
        propertyType = getValidInput('What type of property? ', ('house', 'apartment')).lower()
        paymentType = getValidInput('What payment type? ', ('purchase', 'rental')).lower()
        propertyClass = self.typeMap[(propertyType, paymentType)]
        initArgs = propertyClass.promptInit()
        self.propertyList.append(propertyClass(**initArgs))



        
