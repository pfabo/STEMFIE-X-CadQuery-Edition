#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import pi, sin, cos
from lib.base import *
from lib.components import *
from lib.beams import *
from lib.holes import Hole_List, Hole


class Fence_Base(Stemfie_X):
    def __init__(self, width=2, mode=1, height=1/4):   
        r'''
        size - sirka 2/4 BU
        
        mode 1      /\/\/\
                    \/\/\/
        
        mode 2      \/\/\/
                    /\/\/\
        '''
        Stemfie_X.__init__(self)     

        d = [ [0,0], [1/4, 0], [1, 3/4], [1,1], [3/4, 1], [0, 1/4] ]
        b1 = BU_Polyline(d, height)
        if mode==2:
            b1.BU_Tx(-1)
            
        b2 = b1.MKy()
        b4 = Beam_Block([2,1,height], [False, False, True]).BU_Ty(-1).BU_Tx(-1)
        b1.U([b2, b4]).BU_Ty(-1)
        
        if width==4:
            b3 = b1.MKx()
            b1.U(b3)
            b4 = Beam_Block([2,1,height]).BU_Ty(1).BU_Tx(-1)
            b5 = b4.MKx()
            b1.U([b4,b5])
        
        self.obj = b1.obj


class Fence(Stemfie_X):
    def __init__(self, length=1, width=2, mode=1, height=1/4):   
        Stemfie_X.__init__(self) 
        
        for i in range(length):
            q = Fence_Base(width, mode, height).BU_Tx(i*2)
            self.U(q)
        

