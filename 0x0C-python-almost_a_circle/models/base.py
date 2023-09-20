#!/usr/bin/python3
"""Module for task 1"""
import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="UTF-8") as file:
            if list_objs is None or list_objs == []:
                json.dump([], file)
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dict))
