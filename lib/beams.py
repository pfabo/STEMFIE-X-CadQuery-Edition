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

            
class Beam_U_Block(Stemfie_X):
    def __init__(self, x, y, h1=1/4, h2=1/4):        
        if h1 < 1/4: h1 = 1/4
        if h2 < 1/4: h2 = 1/4
        
        if h1 > 1/2: h1 = 1/2
        if h2 > 1/2: h2 = 1/2
        
        b1 = Beam_Block([x, y, h1], [False, False, True])
        b2 = Beam_Block([x, h2, 1], [False, True, False]) 
        b3 = Beam_Block([x, h2, 1], [False, True, False]).BU_Ty(y-h2)  
        b1.U([b2, b3])
        
        hx = Hole_Grid(x, 1, 1).BU_Txy(1/2,1/2) 
        b1.D(hx)
        b1.D(hx.BU_Txy(0,y-1) )
        
        hx = Hole_Grid(x, 1, 1).Rx().BU_T([1/2,1,1/2]) 
        b1.D(hx)
        b1.D(hx.BU_Ty(y-1))        
        
        self.obj = b1.obj
        
class Beam_L_Block(Stemfie_X):
    def __init__(self, x, y, h1=1/4, h2=1/4):        
        if h1 < 1/4: h1 = 1/4
        if h2 < 1/4: h2 = 1/4
        
        if h1 > 1/2: h1 = 1/2
        if h2 > 1/2: h2 = 1/2
        
        b1 = Beam_Block([x, y, h1], [False, False, True])
        b2 = Beam_Block([x, h2, 1], [False, True, False])  
        b1.U(b2)
        
        hx = Hole_Grid(x, 1, 1).BU_Txy(1/2,1/2) 
        b1.D(hx)
        b1.D(hx.BU_Txy(0,y-1) )
              
        self.obj = b1.obj



class Beam_H_Block(Stemfie_X):
    def __init__(self, x, y, h1=1/4, h2=1/4):        
        if h1 < 1/4: h1 = 1/4
        if h2 < 1/4: h2 = 1/4
        
        if h1 > 1/2: h1 = 1/2
        if h2 > 1/2: h2 = 1/2
        
        b1 = Beam_Block([x, y, h1], [False, False, True])
        b2 = Beam_Block([x, h2, 1], [False, True, False]) 
        b3 = Beam_Block([x, h2, 1], [False, True, False]).BU_Ty(y-h2)  
        
        b4 = Beam_Block([y, h2, 1], [False, True, False]).Rz().BU_Tx(h2) 
        b5 = Beam_Block([y, h2, 1], [False, True, False]).Rz().BU_Tx(h2).BU_Tx(x-h2)
        b1.U([b2, b3, b4, b5])
        
        hx = Hole_Grid(x, 1, 1).BU_Txy(1/2,1/2) 
        b1.D(hx)
        b1.D(hx.BU_Txy(0,y-1) )
        
        hx = Hole_Grid(x, 1, 1).Rx().BU_T([1/2,1,1/2]) 
        b1.D(hx)
        b1.D(hx.BU_Ty(y-1))    
        
        hy = Hole_Grid(1, y, 1).BU_T([1/2,1/2,0]) 
        b1.D(hy)
        b1.D(hy.BU_Tx(x-1))
        
        hy = Hole_Grid(1, y, 1).Ry().BU_T([0,1/2,1/2]) 
        b1.D(hy)
        b1.D(hy.BU_Tx(x-1))
        
        self.obj = b1.obj
