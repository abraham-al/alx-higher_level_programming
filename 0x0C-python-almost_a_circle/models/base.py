#!/usr/bin/python3
""" new class called base """
import json
import csv


class Base:
    """ define Base with id """

    __nb_objects = 0

    def __init__(self, id=None):
        """ method initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string representation """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation """
        d = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    d.append(obj.to_dictionary())
            f.write(cls.to_json_string(d))

    def from_json_string(json_string):
        """ returns the list of the JSON string repr """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ serializes """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**dictionary) for
                        dictionary in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes and deserializes in CSV"""
        ld = []
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    if cls.__name__ == 'Rectangle':
                        ld.append([
                            obj.id, obj.width, obj.height, obj.x, obj.y])
                    if cls.__name__ == 'Square':
                        ld.append([obj.id, obj.size, obj.x, obj.y])
            writer = csv.writer(f)
            for row in ld:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """serializes and deserializes in CSV """
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                ld = []
                reader = csv.DictReader(f)
                for row in reader:
                    for key, val in row.items():
                        row[key] = int(val)
                ld.append(row)
                return [cls.create(**item) for item in ld]
        except FileNotFoundError:
            return []
