from rental import Rental
from house import House

class HouseRental(Rental, House):
    '''Represents a rented house. It entends Rental and House classes'''

    def promptInit():
        '''Gets dictionary values from the parent classes (Rental and House)'''
        init = House.promptInit()
        init.update(Rental.promptInit())
        return init
    
    promptInit = staticmethod(promptInit)  
