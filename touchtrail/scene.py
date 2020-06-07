"""This module manages all the components of a computer vision scene.

Classes are used to manage all the people and things in a scene. Every scene has
a place as well, which is managed by the Place class.

    Typical usage example:

    scene = Scene()
    scene.describe()
"""
__all__ = []

class Object():
    """A generic computer vision object.

    Attributes:
        width (float):  Width of the bounding box as a ratio of the overall
        image width.
        height (float): Height of the bounding box as a ratio of the overall
        image height.
        top (float): Top coordinate of the bounding box as a ratio of overall
        image height.
        left (float): Left coordinate of the bounding box as a ratio of overall
        image width.
    """

    def __init__(self, width, height, left, top):
        self.width = width
        self.height = height
        self.left = left
        self.top = top

    def is_touching(self, other):
        """Determines if two objects have come into contact by calculating
        overlap between two bouding boxes. Assumes coordinate system starts
        at top left.

        Collision Examples:
                                                     __________________
                               ___________          |                  |
         _________            |           |         |    _____   G     |
        |         |           |     C     |         |   |     |        |
        |    A    |___________|__         |         |   |  F  |        |
        |_________|              |________|         |   |_____|        |
                |                |                  |__________________|
                |       B        |
            ____|            ____|____       ___________
           |    |___________|         |     |          _|________
           |     |          |    D    |     |    H    |    I     |
           |  E  |          |_________|     |         |__________|
           |_____|                          |___________|

        Args:
            other (Object): The Object to compare.

        Returns:
            True if this object overlaps with other, else False.
        """
        right = self.left + self.width
        bottom = self.top + self.height
        other_right = other.left + other.width
        other_bottom = other.top + other.height

        return (right < other.left or self.left > other_right or
                bottom < other.top or self.top > other_bottom)

class Person(Object):
    """Maintains properties for a person object."""

    def __init__(self, bounding_box):
        super().__init__(bounding_box)


class Place():
    """Maintains properties about the location of a scene."""
    pass


class Thing(Object):
    """Maintains properties for things that are objects."""
    pass

class Scene():
    """Maintains a coherent scene narrative consisting of locations, paths,
    collisions, and Person-Thing contacts."""
    pass
