# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:53:23 2015

@author: Administrator
"""

class  Room(object):

    def  __init__(self,  name,  description):
        self.name  =  name
        self.description  =  description
        self.paths  =  {}
        
    def  go(self,  direction):
        return  self.paths.get(direction,  None)

    def  add_paths(self,  paths):
        self.paths.update(paths)

