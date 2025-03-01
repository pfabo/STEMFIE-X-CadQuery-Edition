#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:58:15 2024

@author: pf

Base Stemfie-X class
"""

import numpy as np
import copy as cp

import cadquery as cq
from cadquery import exporters

BU = 10        # Basic Unit
HR = 1.95      # Hole Radius


class Stemfie_X_Base():
    def __init__(self): 
        self.BU = BU 
        self.HR = HR 


class Stemfie_X(Stemfie_X_Base):

    def __init__(self): 
        Stemfie_X_Base.__init__(self)
        self.obj = cq.Workplane("XY" , origin=(0,0,0))
        

    #---------------------------------------------------------------------
    # translate operations
    #---------------------------------------------------------------------
    def Tx(self, n=10):
        self.obj = self.obj.translate([n,0,0])
        return self
    
    
    def Ty(self, n=10):
        self.obj = self.obj.translate([0,n,0])
        return self
    
    
    def Tz(self, n=10):
        self.obj = self.obj.translate([0,0,n])
        return self
    
    
    def T(self, t):
        # t - list [x,y,z] or [x,y]
        if len(t)==2:
            t.append(0)
        self.obj = self.obj.translate(t)
        return self
        
    
    def BU_T(self, t):
        # t - list [x,y,z] or [x,y]
        if len(t)==2:
            t.append(0)
        
        [x,y,z] = np.array(t)*self.BU
        self.obj = self.obj.translate([x,y,z])
        return self
    
    
    def BU_Tx(self, n=1):
        self.obj = self.obj.translate([n*self.BU,0,0])
        return self
    
    
    def BU_Ty(self, n=1):
        self.obj = self.obj.translate([0,n*self.BU,0])
        return self
    
    
    def BU_Tz(self, n=1):
        self.obj = self.obj.translate([0,0,n*self.BU])
        return self
    
    
    def BU_Txy(self, c1, c2=None):
        '''
        BU_Txy([x,y])
        BU_Txy(x,y)
        '''
        if c2==None:
            self.BU_T(c1)
        else:
            self.BU_T([c1,c2])
        return self
    
    
    def Rx(self, angle=90):
        self.obj=self.obj.rotate([0,0,0], [1,0,0], angle)
        return self
    
    
    def Ry(self, angle=90):
        self.obj=self.obj.rotate([0,0,0], [0,1,0], angle)
        return self
    
    
    def Rz(self, angle=90):
        self.obj=self.obj.rotate([0,0,0], [0,0,1], angle)
        return self
    
    #---------------------------------------------------------------------
    # boolean operations
    #---------------------------------------------------------------------
    def D(self, comp):
        # difference
        if isinstance(comp, list):
            for c in comp:
                self.obj=self.obj.cut(c.obj)
        else:
            self.obj=self.obj.cut(comp.obj)
        return self
    
    
    def I(self, comp):
        # intersection
        if isinstance(comp, list):
            for c in comp:
                self.obj=self.obj.intersect(c.obj)
        else:
            self.obj=self.obj.intersect(comp.obj)
        return self
    
    
    def U(self, comp):
        # union
        if isinstance(comp, list):
            for c in comp:
                self.obj=self.obj.union(c.obj)
        else:
            self.obj=self.obj.union(comp.obj)
        return self
    
    #---------------------------------------------------------------------
    # mirror 
    # mirror with copy
    #---------------------------------------------------------------------
    
    def Mx(self):
        self.obj=self.obj.mirror(mirrorPlane="XZ", basePointVector=(0, 0, 0))
        return self
    
    def My(self):
        self.obj=self.obj.mirror(mirrorPlane="YZ", basePointVector=(0, 0, 0))
        return self
    
    def Mz(self):
        self.obj=self.obj.mirror(mirrorPlane="XY", basePointVector=(0, 0, 0))
        return self
    
    def MKx(self):
        temp = cp.copy(self)
        self.obj=self.obj.mirror(mirrorPlane="XZ", basePointVector=(0, 0, 0))
        self.U(temp)
        return self
    
    def MKy(self):
        temp = cp.copy(self)
        self.obj=self.obj.mirror(mirrorPlane="YZ", basePointVector=(0, 0, 0))
        self.U(temp)
        return self
        
    def MKz(self):
        temp = cp.copy(self)
        self.obj=self.obj.mirror(mirrorPlane="XY", basePointVector=(0, 0, 0))
        self.U(temp)
        return self
    
    #---------------------------------------------------------------------
    # utils
    #---------------------------------------------------------------------
    
    def copy(self):
        return cp.copy(self)
    
    def export_stl(self, file_name):
        if file_name.endswith('.stl') == False: 
            file_name = file_name + '.stl'
        self.obj.export(file_name)
        return self
        
    def export_step(self, file_name):
        if file_name.endswith('.step') == False: 
            file_name = file_name + '.step'
        self.obj.export(file_name)
        return self

    

        

