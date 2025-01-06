#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:58:15 2024

@author: pf

Basic components in BU units,
"""

from lib.base import *
from lib.hole import *

class BU_Component(Stemfie_X):
    def __init__(self):
        Stemfie_X.__init__(self)
        

class BU_Cube(BU_Component):
    # basic cube
    def __init__(self, dim=[1,1,1], center=True):
        """
        BU_Cube([x,y,x])
        BU_Cube(d)
        """
        BU_Component.__init__(self)
        if type(dim) == list:
            x,y,z = np.array(dim)*self.BU
        else:
            x = y = z = dim*self.BU
            
        self.obj = (self.obj).box(x,y,z)
        if center == False:
            self.Tx(x/2).Ty(y/2).Tz(z/2)


class BU_Cylinder(BU_Component):
    # radius, height in BU units
    def __init__(self, diameter, height, angle=360, hole=True, center=True):
        BU_Component.__init__(self)
        
        r = diameter * self.BU / 2
        h = height * self.BU
        
        self.obj = (self.obj).cylinder(height=h, radius=r, angle=angle)
        
        if hole==True:
            ht = Hole(height).BU_Tz(-height/2)
            self.D(ht)
        if center == False:
            self.Tx(self.BU/2).Ty(self.BU/2).Tz(h/2)


class BU_Polyline(BU_Component):
    # x,y - in BU units
    # hole_list = [ [x1,y1], [x2,y2] ... ]
    def __init__(self, point_list, height=1):
        BU_Component.__init__(self)
        point_list = np.array(point_list)*self.BU
        self.obj = self.obj.polyline(point_list).close()
        self.obj = self.obj.extrude(height*self.BU)
        
        
class BU_Bar(BU_Component):
    def __init__(self, length, center=True):
        BU_Component.__init__(self)
        h = length * self.BU
        self.obj = (self.obj).cylinder(radius=self.HR, height=h)
        
        if center == False:
            self.Tz(h/2)
