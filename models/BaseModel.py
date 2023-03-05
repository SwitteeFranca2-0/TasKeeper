#!/usr/bin/python3
"""Basemodel for TaskKeeper"""
import uuid
from datetime import datetime


class Task():
    """Base model for the task object"""
    __deleted_tasks = {}
    __no_instances = 0

    def __init__(self, *args, **kwargs):
        """Instansiates the task object"""
        Task.__no_instances += 1
        if not kwargs:
            self.id = str(uuid.uuid1())
            self.name = args[0]
            if len(args) >= 2 and args[1] != 1 and args[1] != 0:
                raise ValueError('Please, status must be either 0 or 1')
            if len(args) >= 2:
                self.status = args[1]
            else:
                self.status = 0
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
                if k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] = datetime.fromisoformat(v)

    def __str__(self):
        """String representation of this object"""
        cls = self.__class__.__name__
        date = datetime.isocalendar(self.created_at)
        date = 'Day: ' + str(date[2]) + ' of Week: ' + str(date[1]) + ' of Year: ' + str(date[0])
        return "[{}].\n\tName of task: {}\n\tId: {}\n\tStatus: {}\n\tTime Created: {}".format(cls, self.name, self.id, self.status, date)
    
    def save(self):
        """Saves changed information"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()
    
    def to_dict(self):
        """Return a dictionary of the object instances"""
        dict = {}
        dict.update(self.__dict__)
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = datetime.isoformat(self.__dict__['created_at'])
        dict['updated_at'] = datetime.isoformat(self.__dict__['updated_at'])
        return dict





        