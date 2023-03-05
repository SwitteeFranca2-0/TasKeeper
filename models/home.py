#!/usr/bin/python3
"""Class fro home tasks"""

from models.BaseModel import Task

class Home(Task):
    """Defining the home task"""
    def __init__(self, *args, **kwargs):
        """Inheriting from basemodel"""
        super().__init__(*args, **kwargs)
        user_id = ""
