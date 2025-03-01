#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:05:31 2024

@author: pf
"""

from numpy import pi,sin,cos,abs

from lib.base import *
from lib.components import *
from lib.holes import Hole_List

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
        '''
        angle - 0...180 deg
        '''

        Braces.__init__(self)
        
        alpha = abs(angle/180*pi)   # deg -> rad 
        
        d = self.BU/2               # brace width
        r = r*self.BU               # radius
        height = height*self.BU
        
        if alpha >= pi:              # angle max  = pi
            alpha = pi
        
        # I.kvadrant
        beta = pi/2+alpha             # end angle
        
        # II kvadrant
        if (alpha > pi/2) and (alpha <= pi*3/4):
            beta = -alpha
        
        if alpha > pi*3/4:
            beta = -(alpha-pi/2)

        dx  = cos(alpha)
        dy  = sin(alpha)
        
        dx2 = cos(alpha/2)
        dy2 = sin(alpha/2)
        
        rdx = cos(beta)*d
        rdy = sin(beta)*d

        self.obj = ( #cq.Workplane("XY")
                self.obj
               .moveTo(r-d, 0)
                
                # pociatocny obluk
               .threePointArc( (r, -d), (r+d, 0) )
                
                # vonkajsi obluk
               .threePointArc( (dx2*(r+d), dy2*(r+d) ), (dx*(r+d), dy*(r+d) ) )
                
                # koncovy obluk
               .threePointArc( (dx*r+rdx, dy*r+rdy), (dx*(r-d), dy*(r-d)) )
                
                # vnutorny obluk
               .threePointArc( (dx2*(r-d), dy2*(r-d) ), (r-d, 0 ) )
            
               .close()
               )
        
        if holes > 1:
            gamma = alpha / (holes-1)
            for n in range(holes):
                hx = cos(gamma*n)*r
                hy = sin(gamma*n)*r
                self.obj = self.obj.moveTo(hx,hy)
                self.obj = self.obj.circle(self.HR)
               
        self.obj = self.obj.extrude(height)
        
        if center==True:
            self.Tz(-height/2)
            

class Brace_Circle(Braces): 
    
    def __init__(self, r, height=1/4, holes=4, center=False):
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
            gamma = pi*2/ (holes)
            for n in range(holes):
                hx = cos(gamma*n)*r
                hy = sin(gamma*n)*r
                self.obj = self.obj.moveTo(hx,hy)
                self.obj = self.obj.circle(self.HR)
               
        self.obj = self.obj.extrude(height) 
        
        if center==True:
            self.BU_Tz(-height/2)
