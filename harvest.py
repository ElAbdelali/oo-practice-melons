############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__ (self, code, name, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
       

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        print(f"Code updated to {new_code}")


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", "Muskmelon", 1998, "green", True, True )
    musk.add_pairing("mint")
    
    cas = MelonType("cas", "Casaba", 2003, "orange", False, False)
    cas.add_pairing("mint")
    cas.add_pairing("strawberries")
    
    cren = MelonType("cren", "Crenshaw", 1996, "green", False, False )
    cren.add_pairing("proscuitto")
    
    yw = MelonType("yw", "Yellow Watermelon", 2013, "yellow", False, True)
    yw.add_pairing("ice cream")
    
    all_melon_types.append(cas)
    all_melon_types.append(musk)
    all_melon_types.append(cren)
    all_melon_types.append(yw)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs well with: ")
        for pairing in melon.pairings:
            print(f"- {pairing}")
        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melons_by_typecode = {}
    for melon in melon_types:
        if melon.code not in melons_by_typecode:
            melons_by_typecode[melon.code] = melon
            
    return melons_by_typecode


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    
    #constructor
    def __init__ (self, melon_type, shape_rating, color_rating, harvested_from, harvested_by):
        
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    def is_sellable(self):
        if self.shape_rating and self.color_rating > 5 and self.harvested_from != 3:
            return True
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
