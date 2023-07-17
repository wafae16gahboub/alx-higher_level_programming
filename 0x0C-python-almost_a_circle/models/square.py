#!/usr/bin/python3
"""Write the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """[summary]

    Args:
        Rectangle ([type]): [description]
    """
    def __init__(self, size, x=0, y=0, id=None):
        """[summary]

        Args:
            size ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding the __str__ method so that it returns a new string"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """getter

        Returns:
            [int]: [private instance attribute]
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter should assign width and height with the same value

        The setter should have the same value validation as the
        Rectangle for width and height

        __setattr__(self, name, value)
        super().__setattr__(name, value)

        (name) - The name of the attribute.
        (value) - The value we want to assign to the attribute.
        """
        super().__setattr__('width', value)
        super().__setattr__('heigth', value)

    def update(self, *args, **kwargs):
        """method that assigns attributes"""
        attr = ['id', 'size', 'x', 'y']
        if args is None or not args:
            for key, val in kwargs.items():
                setattr(self, key, val)
        else:
            for n in range(len(args)):
                setattr(self, attr[n], args[n])

    def to_dictionary(self):
        """method that returns the dictionary representation
        of a Square"""
        return dict(id=self.id, x=self.x, y=self.y,
                    size=self.size)
