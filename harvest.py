############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        
        self.pairings = []
        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        
        self.pairings.append(pairing)
        
    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
       


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    Mel1 = MelonType('musk', '1998', 'green', True, True, 'MuskMelon')
    Mel1.add_pairing('mint')

    Mel2 = MelonType('cas', '2003', 'orange', False, False, 'Casaba')
    Mel2.add_pairing('mint')
    Mel2.add_pairing('strawberries')

    Mel3 = MelonType('cren', '1996', 'green', False, False, 'Crenshaw')
    Mel3.add_pairing('proscuitto')

    Mel4 = MelonType('yw', '2013', 'yellow', False, True, 'Yellow Watermelon')
    Mel4.add_pairing('ice cream')

    all_melon_types.extend([Mel1, Mel2, Mel3, Mel4])

    return all_melon_types



def print_pairing_info(melon_types):  #list of objects
    """Prints information about each melon type's pairings."""
    for melon in melon_types:       #iterating over that list of object
        print(f'{melon.name} pairs with {melon.pairings}m)    '   #object should have attribute of pairings

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 

# mel = MelonType('yw',2013, 'yellow', False, True)
# mel.pairing('strawberry')
