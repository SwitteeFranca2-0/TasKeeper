#!/usr/bin/python3
"""User class for TaskKeeper"""

import uuid

class User():
    """Defining the home task"""
    def __init__(self, username, password):
        
        self.username = username
        self.user_id = str(uuid.uuid3())
        self.password = password
    
    
    
    
        
