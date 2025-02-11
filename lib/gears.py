#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: pf

STEMFIE-X wrapper above the gears library
https://github.com/meadiode/cq_gears

"""
from lib.base import *
from lib.components import *
from lib.beams import *
from lib.hole import Hole_List, Hole
from lib.construct import *

from lib.cq_gears import *

from numpy import array

class Spur_Gear(Stemfie_X):
    
    def __init__(self, teeth_number=20, width=1/2, bore=HR*2):
        Stemfie_X.__init__(self)  
        module=1.0
        spur_gear = SpurGear(module, teeth_number, width=self.BU*width, bore_d=bore)
        self.obj = cq.Workplane("XY" , origin=(0,0,0))
        self.obj = (self.obj).gear(spur_gear)
        

class Rack_Gear(Stemfie_X):
    
    def __init__(self, length, width=1/2, height=1/2):
        Stemfie_X.__init__(self)  
        module=1.0
        rack_gear = RackGear(module, length=self.BU*length, width=self.BU*width, height=self.BU*height)
        self.obj = cq.Workplane("XY" , origin=(0,0,0))
        self.obj = (self.obj).gear(rack_gear)
