#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []  # Initializing knowledge as an empty list
        
    def learn(self, knowledge):
        self.knowledge.append(knowledge)