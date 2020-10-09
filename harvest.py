############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, pcode, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = pcode
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

    Musk_Melon = MelonType('musk', '1998', 'green', True, True, 'MuskMelon')
    Musk_Melon.add_pairing('mint')

    Casaba = MelonType('cas', '2003', 'orange', False, False, 'Casaba')
    Casaba.add_pairing('mint')
    Casaba.add_pairing('strawberries')

    Crenshaw = MelonType('cren', '1996', 'green', False, False, 'Crenshaw')
    Crenshaw.add_pairing('proscuitto')

    Yellow_Watermelon = MelonType('yw', '2013', 'yellow', False, True, 'Yellow Watermelon')
    Yellow_Watermelon.add_pairing('ice cream')

    all_melon_types.extend([Musk_Melon, Casaba, Crenshaw, Yellow_Watermelon])

    return all_melon_types


def print_pairing_info(melon_types):  #list of objects
    """Prints information about each melon type's pairings."""
    for melon in melon_types:       #iterating over that list of object
        print(f'{melon.name} pairs with: {" ".join(melon.pairings)}')      #object should have attribute of pairings


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_lookup = {}
    for melon in melon_types:
        melon_lookup[melon.code] = melon #this is an object
    return melon_lookup

############
# Part 2   #
############

dictionary = make_melon_type_lookup(make_melon_types())

class Melon(object):
    """A melon in a melon harvest."""
   
    def __init__(self, melon_type, shape_rating, color_rating, field, person): #pass other class into melon_type
        self.type = dictionary[melon_type]    #object from part 1
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.person = person
    
    def is_sellable(shape_rating, color_rating, field):
        '''Returns true if shape rating and color rating are greater than 5 and field not equal to 3.'''
        if field != 3 and shape_rating > 5 and color_rating > 5:
            return True


def make_melons():
    """Returns a list of Melon objects."""
    
    melon1 = Melon('yw', 8, 7, 2, 'Sheila') #use code to look up melon type from other class & print out the description from the other class
    melon1.is_sellable = is_sellable(melon1.shape_rating, melon1.color_rating, melon1.field)

    melon2 = Melon('yw', 3, 4, 2, 'Sheila')
    melon2.is_sellable = is_sellable(melon2.shape_rating, melon2.color_rating, melon2.field)
    
    melon3 = Melon('yw', 9, 8, 3, 'Sheila')
    melon3.is_sellable = is_sellable(melon3.shape_rating, melon3.color_rating, melon3.field)
    
    melon4 = Melon('cas', 10, 6, 35, 'Sheila')
    melon4.is_sellable = is_sellable(melon4.shape_rating, melon4.color_rating, melon4.field)
    
    melon5 = Melon('cren', 8, 9, 35, 'Michael')
    melon5.is_sellable = is_sellable(melon5.shape_rating, melon5.color_rating, melon5.field)
    
    melon6 = Melon('cren', 8, 2, 35, 'Michael')
    melon6.is_sellable = is_sellable(melon6.shape_rating, melon6.color_rating, melon6.field)

    melon7 = Melon('cren', 2, 3, 4, 'Michael')
    melon7.is_sellable = is_sellable(melon7.shape_rating, melon7.color_rating, melon7.field)

    melon8 = Melon('musk', 6, 7, 4, 'Michael')
    melon8.is_sellable = is_sellable(melon8.shape_rating, melon8.color_rating, melon8.field)
    
    melon9 = Melon('yw', 7, 10, 3, 'Sheila')
    melon9.is_sellable = is_sellable(melon9.shape_rating, melon9.color_rating, melon9.field)

    melons = [melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9]    
    return melons


def get_sellability_report(melons):
    """Given a list of melon objects, prints whether each one is sellable."""

    for melon in melons:
        #print(f'{melon} is sellable' if is_sellable(melon) else f'{melon} is not sellable')
        if is_sellable(melon):
            print(f'{melon} is sellable')
        else:
            print(f'{melon} is not sellable')       


make_melons()
get_sellability_report(melons)     