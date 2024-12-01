#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:10:45 2024

@author: pf
"""
from lib.base import *

class Holes(Stemfie_X):
    def __init__(self, length=1):
        Stemfie_X.__init__(self)
        self.length = length*self.BU

class Hole(Holes):
    
    def __init__(self, length=1):
        Holes.__init__(self, length)
        self.obj = self.obj.circle(self.HR)
        self.obj = self.obj.extrude(self.length)


class Hole_List(Holes):
    # x,y - in BU units
    # hole_list = [ [x1,y1], [x2,y2] ... ]
    def __init__(self, hole_list, length=1):

        Holes.__init__(self, length)
        hole_list = np.array(hole_list)*self.BU
        
        self.obj = self.obj.pushPoints(hole_list) 
        self.obj = self.obj.circle(self.HR)
        self.obj = self.obj.extrude(self.length)

    
class Hole_Grid(Holes):
    
    def __init__(self, dim_x, dim_y, length=1, offs_x=0, offs_y=0, offs_z=0):
        Holes.__init__(self, length)
        
        if dim_x < 1: dim_x = 1
        if dim_y < 1: dim_y = 1
        
        hole_grid = []
        for i in range(int(dim_x)):
            for j in range(int(dim_y)):
                hole_grid.append([i,j])
        
        hole_grid = np.array(hole_grid)*self.BU
        self.obj = self.obj.pushPoints(hole_grid) 
        self.obj = self.obj.circle(self.HR)
        self.obj = self.obj.extrude(self.length)
        self.BU_Tx(offs_x).BU_Ty(offs_y).BU_Tz(offs_z)


class Hole_Slot(Holes):
    
        def __init__(self, size, height=1/4, center=False):
            Holes.__init__(self, height)
            if size > 1:
                bs = (
                    cq.Sketch()
                    .arc( (                0, 0), self.HR, 0.0, 360.0)
                    .arc( ( (size-1)*self.BU, 0), self.HR, 0.0, 360.0)
                    .hull()
                )
                self.obj = self.obj.placeSketch(bs)
                self.obj = self.obj.extrude(self.length)
