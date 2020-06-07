"""This module manages all the components of a computer vision scene.

Classes are used to manage all the people and things in a scene. Every scene has
a place as well, which is managed by the Place class.

    Typical usage example:

    scene = Scene()
    scene.describe()
"""
from dataclasses import dataclass

@dataclass
class BoundingBox():
    """Store the properties for a computer vision bounding box.

    Attributes:
        X (float):  Width of the bounding box as a ratio of the overall image
        width.
        Y (float): Height of the bounding box as a ratio of the overall image
        height.
        top (float): Top coordinate of the bounding box as a ratio of overall
        image height.
        left (float): Left coordinate of the bounding box as a ratio of overall
        image width.
    """
    X: float
    Y: float
    top: float
    left: float

class Object():
    """A generic computer vision object."""

    def __init__(self, bounding_box):
        self.bounding_box = bounding_box

    def is_touching(self, other):
        """Calculates if two objects have come into contact."""
        raise NotImplemented

class Person(Object):
    """Maintains properties for a person object."""
    pass


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
