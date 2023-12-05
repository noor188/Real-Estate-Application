from transactions.rental import Rental
from real_estate.apartment import Apartment

class ApartmentRental(Rental, Apartment):
    '''Represents a rented apartment. It entends Rental and Apartment classes.'''

    def promptInit():
        '''Get dictionary values form the parent classes (Rental and Apartment).'''

        init = Rental.promptInit()
        init.update(Apartment.promptInit())
        return init
    promptInit = staticmethod(promptInit)