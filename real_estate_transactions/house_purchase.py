from purchase import Purchase
from house import House

class HousePurchase(Purchase, House):
    '''Represents a purchased house. It entends Purchase and House classes.'''

    def promptInit():
        '''Get dictionary values form the parent classes (Purchase and House).'''

        init = House.promptInit()
        init.update(Purchase.promptInit())
        return init
    promptInit = staticmethod(promptInit)


