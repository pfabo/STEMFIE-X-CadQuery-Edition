#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import pi, sin, cos
from lib.base import *
from lib.components import *
from lib.beams import *
from lib.hole import Hole_List, Hole


class Wheel(Stemfie_X):
    def __init__(self, r, h=1/4, d=1/2, beams=3 ):  
        Stemfie_X.__init__(self)  
        
        self.r = r if r in [1,2,3] else 1
        self.d = d if d>=1/4  else 1/2
        self.beams = beams if beams in [3,4] else 3
        self.h = h if h>=1/4  else 1/4
        
        if r==1:
            self.wheel_1()
            
        if r==2:
            self.wheel_2()
            
        if r==3:
            self.wheel_3()
        
        
    def wheel_1(self):
        hole_grid = []
        
        w1 = BU_Cylinder(2 * self.r + 1, self.h)
        
        N = 8
        dp = pi*2/N
        # pozicie dier    
        for i in range(N):
            dx = self.BU*cos(dp*i) 
            dy = self.BU*sin(dp*i)
            hole_grid.append([dx,dy])
        
        # diery ...
        hr = BU_Component()
        hr.obj = hr.obj.pushPoints(hole_grid) 
        hr.obj = hr.obj.circle(self.HR)
        hr.obj = hr.obj.extrude(self.BU * self.h)
        hr.obj = hr.obj.translate([0,0,-self.h/2*self.BU])
        w1.D(hr)
        
        w1.BU_Tz(self.h/2)
       
        # upevnenie osi
        dd = BU_Cylinder(1, self.d).BU_Tz(self.h+self.d/2)
        w1.U(dd)
        self.obj = w1.obj
        
    
    def wheel_2(self):
        hole_grid = []        
        w1 = BU_Cylinder(2 * self.r + 1, self.h)
        
        N = 8
        dp = pi*2/N
        for i in range(N):
            dx = self.BU*cos(dp*i) 
            dy = self.BU*sin(dp*i)
            hole_grid.append([dx,dy])
        
        N = 16
        dp = pi*2/N
        for i in range(N):
                dx = 2*self.BU*cos(dp*i) 
                dy = 2*self.BU*sin(dp*i)
                hole_grid.append([dx,dy])
                
        hr = BU_Component()
        hr.obj = hr.obj.pushPoints(hole_grid) 
        hr.obj = hr.obj.circle(self.HR)
        hr.obj = hr.obj.extrude(self.BU * self.h)
        hr.obj = hr.obj.translate([0,0,-self.h/2*self.BU])
        w1.D(hr)
        
        
    def wheel_3(self):
        hole_grid = []
        w1 = BU_Cylinder(2 * self.r + 1, self.h)
        c2 = BU_Cylinder(2*self.r, self.h)
        w1.D(c2)
        
        dt = self.r
        if self.beams==3:
            b1 = Beam_Block([dt+dt+1-1/4, 1, self.h], holes = [False,False,False], center=True)
            b2 = Beam_Block([dt+dt+1-1/4, 1, self.h], holes = [False,False,False], center=True).Rz(-60)
            b3 = Beam_Block([dt+dt+1-1/4, 1, self.h], holes = [False,False,False], center=True).Rz( 60)
            w1.U([b1, b2, b3])
        else:
            b1 = Beam_Block([dt+dt+1-1/4 ,1, self.h], holes = [False,False,False], center=True)
            b2 = Beam_Block([dt+dt+1-1/4 ,1, self.h], holes = [False,False,False], center=True).Rz()
            b3 = Beam_Block([dt+dt+1-1/4 ,1, self.h], holes = [False,False,False], center=True).Rz( 45)
            b4 = Beam_Block([dt+dt+1-1/4 ,1, self.h], holes = [False,False,False], center=True).Rz(-45)
            w1.U([b1, b2, b3, b4])
        
        N = 2 * self.beams
        dp = pi*2/N
        hole_grid.append([0,0])
        for j in range(1,4):
            for i in range(N):
                dx = self.BU*j*cos(dp*i) 
                dy = self.BU*j*sin(dp*i)
                hole_grid.append([dx,dy])
            
        hr = BU_Component()
        hr.obj = hr.obj.pushPoints(hole_grid) 
        hr.obj = hr.obj.circle(self.HR)
        hr.obj = hr.obj.extrude(self.BU * self.h)
        hr.obj = hr.obj.translate([0,0,-self.h/2*self.BU])
        w1.D(hr)
        
        if self.beams == 3:
            ff = 3
        else:
            ff = 2
        w1.obj = w1.obj.edges("|Z").fillet(ff)
        
        
        ''' 
        
        if r==3:
            w1 = BU_Cylinder(r+1/2, h)
            
            c2 = BU_Cylinder(r, h)
            w1.D(c2)
            
            dt = r+1-1/4
            if beams==3:
                b1 = Beam_Block([dt+dt-1,1,h], holes = [False,False,False], center=True)
                b2 = Beam_Block([dt+dt-1,1,h], holes = [False,False,False], center=True).Rz(-60)
                b3 = Beam_Block([dt+dt-1,1,h], holes = [False,False,False], center=True).Rz( 60)
                w1.U([b1, b2, b3])
                      
            else:
                b1 = Beam_Block([dt+dt-1,1,h], holes = [False,False,False], center=True)
                b2 = Beam_Block([dt+dt-1,1,h], holes = [False,False,False], center=True).Rz()
                b3 = Beam_Block([dt+dt-1,1,h], holes = [False,False,False], center=True).Rz( 45)
                b4 = Beam_Block([dt+dt-1,1,h], holes = [False,False,False], center=True).Rz(-45)
                w1.U([b1, b2, b3, b4])
   
                
            N = 2*beams
            dp = pi*2/N
            hole_grid.append([0,0])
            for j in range(1,4):
                for i in range(N):
                    dx = self.BU*j*cos(dp*i) 
                    dy = self.BU*j*sin(dp*i)
                    hole_grid.append([dx,dy])
                
            hr = BU_Component()
            hr.obj = hr.obj.pushPoints(hole_grid) 
            hr.obj = hr.obj.circle(self.HR)
            hr.obj = hr.obj.extrude(self.BU*h)
            hr.obj = hr.obj.translate([0,0,-h/2*self.BU])
            w1.D(hr)
            
            w1.obj = w1.obj.edges("|Z").fillet(dt-2)
        '''
        
        
        w1.BU_Tz(self.h/2)
       
        dd = BU_Cylinder(1, self.d).BU_Tz(self.h+self.d/2)
        w1.U(dd)
        
        self.obj = w1.obj
        
        
