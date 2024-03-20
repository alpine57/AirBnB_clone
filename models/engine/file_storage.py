#!/usr/bin/python3

import json
from os.path import exists

class FileStorage:
    def __init__(self):
        self.__objects = {}
        self.__classes = {}

    def all(self):
        """Return the dictionary of objects"""
        return self.__objects

    def classes(self):
        """Return the list of class names"""
        return list(self.__classes.keys())

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        self.__classes[obj.__class__.__name__] = obj.__class__

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_instance = eval(class_name)(**value)
                    self.__objects[key] = obj_instance
                    self.__classes[class_name] = eval(class_name)
        except FileNotFoundError:
            pass

