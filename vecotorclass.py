class Vector:
    """
       Represent a vector in a multidimensional space.
    """
    def __init__(self,d):
        self.coords = [0]*d
        print(self.coords)
    def __len__(self):
        return len(self.coords) 
    def __getitems__(self,J):
        """ Return J element from Vector"""
        return self.coords[J]

Vect = Vector(4)
print(Vect.__len__())
print(Vect.__getitems__(2))
