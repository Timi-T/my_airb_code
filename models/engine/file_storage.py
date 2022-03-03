#!/usr/bin/python3
"""
file strorage module
"""


import json


class FileStorage():
    """class to control file operations
    """
    __file_path = 'storage_file.json'
    __objects = {}

    def all(self):
        """function to get all the current objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """function to add a newly created object to the previous objects"""
        name = obj.__class__.__name__
        i_d = obj.id
        obj_key = name + '.' + i_d
        (FileStorage.__objects)[obj_key] = obj

    def save(self):
        """function to save json representation of all objects to a file"""
        new_dict = {}
        for obj_key, obj_value in FileStorage.__objects.items():
            new_dict[obj_key] = obj_value.to_dict()
        new_dict_to_json = json.dumps(new_dict)
        with open(FileStorage.__file_path, 'w', encoding='UTF-8') as f:
            f.write(new_dict_to_json)

    def reload(self):
        """function to load dictionaries from a json file and make objects"""


        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review


        try:
            FileStorage.__objects = {}
            with open(FileStorage.__file_path, 'r', encoding='UTF-8') as f:
                all_objects = f.read()
            all_objects_as_dict = json.loads(all_objects)
            for obj_key, obj_value in all_objects_as_dict.items():
                if (obj_value['__class__'] == "User"):
                    FileStorage.__objects[obj_key] = User(**obj_value)
                elif (obj_value['__class__'] == "BaseModel"):
                    FileStorage.__objects[obj_key] = BaseModel(**obj_value)
                elif (obj_value['__class__'] == "State"):
                    FileStorage.__objects[obj_key] = State(**obj_value)
                elif (obj_value['__class__'] == "City"):
                    FileStorage.__objects[obj_key] = City(**obj_value)
                elif (obj_value['__class__'] == "Amenity"):
                    FileStorage.__objects[obj_key] = Amenity(**obj_value)
                elif (obj_value['__class__'] == "Place"):
                    FileStorage.__objects[obj_key] = Place(**obj_value)
                elif (obj_value['__class__'] == "Review"):
                    FileStorage.__objects[obj_key] = Review(**obj_value)
        except FileNotFoundError:
            pass
