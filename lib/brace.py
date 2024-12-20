#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:05:31 2024

@author: pf
"""

import numpy as np

from lib.base import *
from lib.components import *
from lib.hole import Hole_List

class Braces(Stemfie_X):
    def __init__(self):
        Stemfie_X.__init__(self)
    

class Brace(Braces):
    
    def __init__(self, size, height=1/4, holes=True, center=False):
        Braces.__init__(self)
        if size > 1:
            bs = (
                cq.Sketch()
                .arc( (                0, 0), self.BU/2, 0.0, 360.0)
                .arc( ( (size-1)*self.BU, 0), self.BU/2, 0.0, 360.0)
                .hull()
            )
            #self.obj = cq.Workplane("XY")
            self.obj = self.obj.placeSketch(bs)
            self.obj = self.obj.extrude(height*self.BU)
            
            if holes==True:
                h = np.zeros( [size, 2])
                for i in range(size):
                    h[i][0] = i
                
                hole_list = Hole_List(h, height)
                self = self.D(hole_list)
                
            if center==True:
                self.BU_Tx( -(size-1)/2 ).BU_Tz(-height/2)
                
        else:
            self.obj = BU_Cylinder(1, height).obj
            self.BU_Tz(height/2)
            
            if holes==True:
                self.D(Hole(height))
                
            if center==True:
                self.BU_Tz(-height/2)
                

class Brace_Arc(Braces):
    
    def __init__(self, r, angle, height=1/4, holes=3, center=False):
        Braces.__init__(self)
        alpha = np.abs(angle/180*np.pi)
        d = self.BU/2
        r = r*self.BU
        height = height*self.BU
        
        if alpha > np.pi:
            alpha = np.pi
        beta = np.pi-alpha

        if (alpha >= np.pi/2) and (alpha <= np.pi*3/4):
            beta = beta-np.pi
            
        if alpha > np.pi/2*3/4:
            beta = beta-np.pi/2

        dx = np.cos(alpha)
        dy = np.sin(alpha)
        dx2 = np.cos(alpha/2)
        dy2 = np.sin(alpha/2)
        rdx = np.cos(beta)*d
        rdy = np.sin(beta)*d

        self.obj = ( #cq.Workplane("XY")
                self.obj
               .moveTo(r-d, 0)
               .threePointArc( (r, -d), (r+d, 0) )
               .threePointArc( (dx2*(r+d), dy2*(r+d) ), (dx*(r+d), dy*(r+d) ) )
               .threePointArc((dx*r+rdx, dy*r+rdy), (dx*(r-d), dy*(r-d)) )
               .threePointArc( (dx2*(r-d), dy2*(r-d) ), (r-d, 0 ) )
               .close()
               )
        
        if holes > 1:
            gamma = alpha / (holes-1)
            for n in range(holes):
                hx = np.cos(gamma*n)*r
                hy = np.sin(gamma*n)*r
                self.obj = self.obj.moveTo(hx,hy)
                self.obj = self.obj.circle(self.HR)
               
        self.obj = self.obj.extrude(height)
        
        if center==True:
            self.BU_Tz(-height/2)
            

class Brace_Circle(Braces): 
    
    def __init__(self, r, height=1/4, holes=3, center=False):
        Braces.__init__(self)
        if r<1: r = 1
        if holes < 1: holes = 1
        
        d = self.BU/2
        r = r*self.BU
        height = height*self.BU
        
        self.obj = ( #cq.Workplane("XY")
                self.obj
               .moveTo(0, 0)
               .circle(r-d)
               .circle(r+d)
               #.extrude(height)
                )
        
        if holes > 1:
            gamma = np.pi*2/ (holes)
            for n in range(holes):
                hx = np.cos(gamma*n)*r
                hy = np.sin(gamma*n)*r
                self.obj = self.obj.moveTo(hx,hy)
                self.obj = self.obj.circle(self.HR)
               
        self.obj = self.obj.extrude(height) 
        
        if center==True:
            self.BU_Tz(-height/2)
