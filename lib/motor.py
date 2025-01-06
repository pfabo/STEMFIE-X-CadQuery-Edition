#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:03:35 2024

@author: pf

Motor_D25           Motor diam. 25mm with gerabox

Motor_D25_Holder    Mounting block for Motor_D25

"""

from lib.base import *
from lib.components import *
from lib.beams import *
from lib.hole import Hole_List, Hole
from lib.construct import *

from numpy import array

class Motor_D25(Stemfie_X):
    def __init__(self, scr=False, FC=False):   
        Stemfie_X.__init__(self)     

        offs = 0.1 # mm
        # motor body
        h1 = 51.2 / self.BU   # mm
        r1 = (25/2 + offs) / self.BU
        c1 = BU_Cylinder(r1, h1, hole=False)
        
        # odsadenie motora
        r2 = (7/2 + offs) / self.BU   # mm
        h2 = 2.7 / self.BU
        c2 = BU_Cylinder(r2, h2, hole=False)
        
        # axe
        r3 = 4 / 2 / self.BU
        h3 = 10 / self.BU
        c3 = BU_Cylinder(r3, h3, hole=False)

        # mounting holes
        dr = (19.50+14.40)/2 /2/self.BU
        rx = 3/2/self.BU
        mh = BU_Cylinder(rx, 1, hole=False)
            
        # assembly object -> create FreeCAD STEP
        #---------------------------------------------------------------
        if FC==True:
            motor = Construct('motor')
            
            motor.add(c2, color="blue", loc=[0,0, h1/2+h2/2] )
            
            if scr==True:
                motor.add(mh, color="orange", loc=[0,dr, h1/2+h3/2] )
                motor.add(mh, color="orange", loc=[0,-dr, h1/2+h3/2] )
            else:
                mh.BU_Ty(dr).MKx().BU_Tz(h1/2) 
                c1.D(mh)
                
            motor.add(c1, color="lightblue")  
            motor.add(c3, color="gray", loc=[0,0, h1/2+h2+h3/2] )
            self.obj = motor.obj
        
        else:
            # create cadquery object
            #---------------------------------------------------------------
            c2.BU_Tz(h1/2+h2/2)
            c3.BU_Tz(h1/2+h2+h3/2)
            c1.U([c2,c3])
            if scr==True:
                mh.BU_Ty(dr).MKx().BU_Tz(h1/2+h3/2)
                c1.U(mh)
            else:
                mh.BU_Ty(dr).MKx().BU_Tz(h1/2) 
                c1.D(mh)
            self.obj = c1.obj


class Motor_D25_Holder(Stemfie_X):
    def __init__(self):   
        Stemfie_X.__init__(self)          
        
        m1 = Motor_D25(scr = True)
        m1.Ry().BU_Tz(2).BU_Ty(1+1/2).BU_Tx(-1-3/4-1/16)

        bb = Beam_Block([1,3,4], [False, False, False])
        s1 = array([ [0,0], [0,1], [0,2] ]) + [1/2, 1/2]
        h1 = Hole_List(s1)
        h2 = Hole_List(s1)
        bb.D(h1)
        bb.D(h1.BU_Tz(3))

        bb.D(h2.Ry().BU_Tz(1))
        bb.D(h2.BU_Tz(3))

        s2 = array([ [0,0], [0,3]]) + [1/2, 1/2]
        h3 = Hole_List(s2).Rx().BU_Ty(1)
        bb.D(h3)
        bb.D(h3.BU_Ty(2))
        bb.D(m1)
        self.obj = bb.obj
