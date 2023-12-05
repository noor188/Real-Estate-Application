from errors.validation import getValidInput

class Rental:
    '''Represents a Rental. Store the rent per month,
      whether the property is furnished, and whether utilities are included.'''
    
    def __init__(self, furnished= '', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent      = rent
    
    def display(self):
        '''Display the characteristics of the Rental.'''
        print()
        super().display()
        print('RENTAL DETAILS')
        print('================')
        print('rent: {}'.format(self.rent))
        print('estimated utilities: {}'.format(self.utilities))
        print('furnished: {}'.format(self.furnished))
        print()

    def promptInit():
        '''Uses a dict constructor to create a dictionary of values that can be
        passed into __init__. The value for each key is prompted with a call to input.'''
        return dict(
            rent = input('What is the monthly rent? '),
            utilities = input('What are the estimated utilities? '),
            furnished = getValidInput('Is the property furnished?',
                                     ('yes','no'))
        )
    promptInit = staticmethod(promptInit)
    
