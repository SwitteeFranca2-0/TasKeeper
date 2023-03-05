#!/usr/bin/python3
"""File storage fo rtask objects"""

import json
from models.BaseModel import Task
from models.home import Home
from models.outdoor import Outdoor
from models.school import School
from models.work import Work

class FileStorage():
    """Setting the file storage class for task objects"""
    __file_path = 'tasks.json'
    __objects = {}

    __classes = {
        'Task': Task, 'Home': Home, 'Outdoor': Outdoor,
        'School': School, 'Work': Work
    }
    def all(self, cls=None):
        """Load all the objects from the file storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            objs = {}
            for k, v in FileStorage.__objects.items():
                if k.split('.')[0] == cls.__name__:
                    objs[k] = v
            return objs


    def new(self, obj):
        """adds new obect to the object dictionary"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes the object to json object and saves it to JSON file path"""
        info = {}
        for k,v in FileStorage.__objects.items():
            info[k] = v.to_dict()
        with open (FileStorage.__file_path, 'w') as f:
            json.dump(info, f)
    
    def reload(self):
        """Deserializes the content in the file"""
        classes = {'Task': Task}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
            for k, obj in objs.items():
                cls = obj["__class__"]
                self.new(eval(cls)(**obj))
        except FileNotFoundError:
            pass
    
    def delete(self, obj):
        """Deletes an object from the storage"""
        try:
            cls = FileStorage.__classes[obj.__class__.__name__]
            objs = FileStorage.all(cls)
            key = obj.__class__.__name__ + "." + obj.id 
            del objs[key]
            self.save()
        except KeyError:
            print('Object deletion failed. Invalid input')




            
