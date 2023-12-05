from .property import Property
from errors.validation import getValidInput

class Apartment(Property):
    '''Represents a property. Indicate if it has a balcony, and if
    laundry is en-suite, coin, or none.'''

    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", 'solarium')

    def __init__(self, balcony ='', laundry='', **kwargs):
        '''Calls propertie's __init__ methid using super to ensure
        property class is properly initialized.'''
        
        super().__init__(**kwargs)
        self.balcony= balcony
        self.laundry = laundry

    def display(self):
        '''Call Properties display method using super to ensure the
        Property class is properly initialized.'''

        super().display()
        print()
        print("APARTMENT DETAILS")
        print('================')
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)
        print()

    def promptInit():
        '''Get dictionary values from the parent class, and then adds some values of its own.
        laundry and balcony'''
        parentInit = Property.promptInit()
        laundry = getValidInput("What laundry facilities does "
                                "the property have? ", Apartment.valid_laundries)
        
        balcony = getValidInput("Does the property have a balcony? ", 
                                Apartment.valid_balconies)
        
        parentInit.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parentInit
    promptInit = staticmethod(promptInit)
        



