#   Code is copied from 'Pythons Class Development kit' - video to learn more about Python class methods:
#   https://youtu.be/HTLu2DFOdTg?list=FLJpj9JO97RXNeiS1yV47URg
import math


class Circle(object):
    """An advanced circle analytic toolkit"""
    __slots__ = ['diameter']
    version = '0.1'  # class variable

    def __init__(self, radius):
        self.radius = radius  # instance variable, only variables that are unique to the instance.

    @property   # convert dotted access to method calls
    def radius(self):
        """radius of a circle"""
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    def area(self):
        """perform quadrature on a shape of uniform radius"""
        p = self.__perimeter() # class local reference
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    @classmethod  # alternative constructor
    def from_bbd(cls, bbd):
        """Construct a circle from a bounding box diagonal"""
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    @staticmethod
    def angle_to_grade(self, angle):
        """Convert angle in degree to percentage grade"""
        return math.tan(math.radians(angle)) * 100.0

#   Important lessons
#   Supply the customer with alternative constructors
#   You can expose the attributes
#   Instance variables are only variables that are unique to the instance
#   Python does not use get or set, you can add property later
