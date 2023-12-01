from rental import Rental
from house import House

class HouseRental(Rental, House):
    '''Represents a rented house. It extends Rental and House classes.
    Has neither an __init__ nor display method, both parent classes appropriately call super in these
    methods.'''

    def promptInit():
        '''A static method that does not call super, need to be implemented explicitly.
        Gets dictionary values from the parent classes (Rental and House)'''
        init = House.promptInit()
        init.update(Rental.promptInit())
        return init
    
    promptInit = staticmethod(promptInit)  
