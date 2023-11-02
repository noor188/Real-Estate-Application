
class Property:
    '''Repreent a property. Store square footage, number of bedrooms, 
       and number of bathrooms.'''

    def __init__(self, squareFeet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.squareFeet = squareFeet
        self.numBedrooms = beds
        self.numBaths = baths

    def display(self):
        '''Displays the characteristics of the property.'''
        print()
        print('PROPERTY DETAILS')
        print('================')
        print('square footage: {0}\nbedrooms: {1}\nbathrooms: {2}'.format(self.squareFeet, self.numBedrooms, self.numBaths))
        print()
    
    def promptInit():
        '''Uses a dict constructor to create a dictionary of values that can be
        passed into __init__. The value for each key is prompted with a call to input.'''
        return dict(squareFeet = input('Enter the square feet: '),
                    beds = input('Enter number of bedrooms: '),
                    baths = input('Enter number of baths: '))
    
    promptInit = staticmethod(promptInit)


    
