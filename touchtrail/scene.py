"""This module manages all the components of a computer vision scene.

Classes are used to manage all the people and things in a scene. Every scene has
a place as well, which is managed by the Place class.

    Typical usage example:

    scene = Scene()
    scene.describe()
"""
from uuid import uuid4

__all__ = ('Person', 'Place', 'Thing', 'Scene')


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
        id (string): Unique random UUID.
    """

    def __init__(self, width, height, left, top, id=None):
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.id = id

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

        ## Return True if there's no gap, else False
        return not (right < other.left or self.left > other_right or
                    bottom < other.top or self.top > other_bottom)


class Person(Object):
    """Maintains properties for a person object."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Place():
    """Maintains properties about the location of a scene."""
    pass


class Thing(Object):
    """Maintains properties for things that are objects."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Scene():
    """Maintains a coherent scene narrative consisting of locations, paths,
    collisions, and Person-Thing contacts.

    Attributes:
        objects (dict): Maps object id to object instance.
    """

    def __init__(self):
        self.objects = {}

    def add(self, obj):
        """Add a new Object to the scene.

        Args:
            obj (Object): The Object to be added to this scene.

        Returns:
            The unique id for given object.
        """

        if obj.id is None:
            ## Object id isn't set
            obj_id = uuid4()

            while obj_id in self.objects:
                ## Handle the very very rare case that the uuid library
                ## generates a duplicate
                obj_id = uuid4()
            obj.id = obj_id
        self.objects[obj.id] = obj

    def step(self, new_positions):
        """Update scene with all the new object positions and sizes.

        Args:
            new_positions (dict): A map of object ids to new objects.
        """
        pass
