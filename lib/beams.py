#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:58:15 2024

@author: pf
"""

from lib.base import *
from lib.components import *
from lib.hole import Hole_Grid

class Beam_Block(Stemfie_X):
    '''
        b = Beam_Block([x,y,z])
        b = Beam_Block(x)        
    '''
    
    def __init__(self, dim=[1,1,1], holes = [True, True, True], center=False):
        Stemfie_X.__init__(self)
        
        if isinstance(dim, list):
            x,y,z = dim
        else:
            x = dim
            y = 1
            z = 1
        
        xx = x*self.BU
        yy = y*self.BU
        zz = z*self.BU
        
        self.obj = self.obj.box(xx,yy,zz)
        self.obj = self.obj.translate([xx/2, yy/2, zz/2])
        
        if holes[0] == True:        # x-holes
            hx = Hole_Grid(z,y,x, 1/2, 1/2).Ry(-90).BU_Tx(x)
            self.D(hx)
        
        if holes[1] == True:        # y-holes
            hy = Hole_Grid(x,z,y, 1/2, 1/2).Rx(90).BU_Ty(y)
            self.D(hy)
        
        if holes[2] == True:        # z-holes
            hz = Hole_Grid(x,y,z, 1/2, 1/2)
            self.D(hz)
            
        if center == True:
            self.BU_T([-x/2, -y/2, -z/2])
            
