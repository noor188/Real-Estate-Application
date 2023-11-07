from property import Property
from validation import getValidInput

class House(Property):
    '''Represents a house. It advertise the number of stories, whether it has a garage,
    and whether the yard is fenced'''

    validGarage = ('attached', 'detached', 'none')
    validFenced = ('yes', 'no')

    def __init__(self, numStories = '', garage= '', fenced= '', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.numStories = numStories

    def display(self):
        '''Calls Properties display method using super to ensure the 
        property class is properly initiaized'''
        super().display()
        print('HOUSE DETAILS')
        print('# of stories: {}'.format(self.numStories))
        print('garage: {}'.format(self.garage))
        print('fenced yard: {}'.format(self.fenced))

    def promptInit():
        '''Gets dictionary values from the parent class, and then adds some values of its own. Number of stories, garage, and fenced Yard'''
        parentInit = Property.promptInit()
        numStories = input('How many stories? ')
        fenced = getValidInput('Is the yard fenced? ', House.validFenced)
        garage = getValidInput('Is there a garage? ', House.validGarage)

        parentInit.update({
            'numStories': numStories,
            'fenced': fenced,
            'garage': garage
        })
        return parentInit
    promptInit = staticmethod(promptInit)