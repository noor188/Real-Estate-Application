from transactions.purchase import Purchase
from real_estate.apartment import Apartment

class ApartmentPurchase(Purchase, Apartment):
    '''Represents a purchased apartment. It entends Purchase and Apartment classes.'''

    def promptInit():
        '''Get dictionary values form the parent classes (Purchase and Apartment).'''
        init = Apartment.promptInit()
        init.update(Purchase.promptInit())
        return init
    promptInit = staticmethod(promptInit)



            

