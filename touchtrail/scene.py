"""This module manages all the components of a computer vision scene.

Classes are used to manage all the people and things in a scene. Every scene has
a place as well, which is managed by the Place class.

    Typical usage example:

    scene = Scene()
    scene.describe()
"""

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
        overlap between two bouding boxes.

        Args:
            other (Object): The Object to compare.

        Returns:
            True if this object overlaps with other, else False.
        """
        raise NotImplemented

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
