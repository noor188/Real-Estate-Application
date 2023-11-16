class Purchase:
    '''Represents a purchase. Store the purchase price 
       and estimated annual property taxes.'''
    
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        '''Displays the characteristics of the purchase.'''
        super().display()
        print('PURCHASE DETAILS')
        print('================')
        print('selling price: {}'.format(self.price))
        print('estimated taxes: {}'.format(self.taxes))
    
    def promptInit():
        '''Uses a dict constructor to create a dictionary of values that can be
        passed into __init__. The value for each key is prompted with a call to input.'''
        return dict(
            price = input('What is the selling price?'),
            taxes = input('What are the estimated taxes?')
        )

    promptInit = staticmethod(promptInit)
