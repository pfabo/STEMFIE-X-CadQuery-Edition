#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:03:35 2024

@author: pf

Pulley and Pulley_Holder

"""
from lib.base import *
from lib.components import *
from lib.beams import *
from lib.hole import Hole_List, Hole



class Pulley(Stemfie_X):
    '''
    dt    - 1,2 .. typ kladky 
            1 - mala kladka bez pomocnych dier
            2 - kladka s 4 dierami
            3 - kladka s odlahcenim
    holes - True/False .. vypln kladky dierami
    fill  - True/False .. odlahcenie kladky
    thick - hrubka kladky
    
    '''
    def __init__(self, dt, holes=True, fill=False, thick=0.8, beams=3):
        Stemfie_X.__init__(self)  
        
        if dt<1: dt = 1
        
        d1 = dt*self.BU - 0.5
        d2 = d1-2.5
        h  = thick*self.BU
        
        p1 = BU_Component()
        p1.obj = (p1.obj
            .circle(d1)
            .workplane(offset=h/2)
            .circle(d2)
            .loft(combine = True)
        )
        
        p2 = BU_Component()
        p2.obj = (p2.obj
            .circle(d2)
            .workplane(offset=h/2)
            .circle(d1)
            .loft(combine = True)
            .translate([0,0,h/2])
        )
        self.U([p1,p2])
        self.T([0,0,-h/2])
        
        # specifikacia podla priemerov kladiek
        hole_grid = []
        if dt == 1 or dt==2:
            hh = Hole(1).BU_Tz(-1/2)
            self.D(hh)
        
        if dt == 2:
            N = 8
            dp = np.pi*2/N
            
            for i in range(N):
                dx = self.BU*np.cos(dp*i)
                dy = self.BU*np.sin(dp*i)
                hole_grid.append([dx,dy])
                
            hr = BU_Component()
            hr.obj = hr.obj.pushPoints(hole_grid) 
            hr.obj = hr.obj.circle(self.HR)
            hr.obj = hr.obj.extrude(10)
            hr.BU_Tz(-1/2)
            self.D(hr)
        
        if dt >= 3:
            # vnutorny kruh
            p3 = BU_Component()
            p3.obj = (p3.obj
            .circle(d2-3.5)
            .extrude(h)
            .translate([0,0,-h/2])
            )
            self.D(p3) 
            
            if beams==3:
                b1 = Beam_Block([dt+dt-1,1,thick], holes = [False,False, True], center=True)
                b2 = Beam_Block([dt+dt-1,1,thick], holes = [False,False, True], center=True).Rz(-60)
                b3 = Beam_Block([dt+dt-1,1,thick], holes = [False,False, True], center=True).Rz( 60)
                self.U([b1, b2, b3])
            else:
                b1 = Beam_Block([dt+dt-1,1,thick], holes = [False,False, True], center=True)
                b2 = Beam_Block([dt+dt-1,1,thick], holes = [False,False, True], center=True).Rz()
                b3 = Beam_Block([dt+dt-1,1,thick], holes = [False,False, True], center=True).Rz( 45)
                b4 = Beam_Block([dt+dt-1,1,thick], holes = [False,False, True], center=True).Rz(-45)
                self.U([b1, b2, b3, b4])
        
            self.obj = self.obj.edges("|Z").fillet(dt-2)


class Pulley_Holder_1(Stemfie_X):
    '''
    Base - 1 BU Block
    '''
    def __init__(self, height):
        Stemfie_X.__init__(self)

        h = height*self.BU
        p2 = Beam_Block([1, 1, 1/2], [False,False,False])
        
        p1 = BU_Component()
        p1.obj = (p1.obj
            .moveTo(  0,  0)
            .lineTo( self.BU,  0)
            .lineTo( self.BU,  h)
            .threePointArc( [5, 5+h], [0, h] ) # absolutne suradnice
            .close()
            .extrude(self.BU/2)
            )
        hr = []
        for i in range(height):
            hr.append([1/2,i+1])
        h1 = Hole_List(hr)
        p1.D(h1)
        p1.Rx().BU_Ty(1/2)
        self.U([p1,p2])
        h2 = Hole(3/4).BU_Txy([1/2, 1/2])        
        self.D(h2)


class Pulley_Holder_2(Stemfie_X):
    '''
    Base - 1 BU Block
    '''
    def __init__(self, height):
        Stemfie_X.__init__(self)
        
        h = height*self.BU
        p2 = Beam_Block([2, 1, 1/2], [False,False,False])
        
        p1 = BU_Component()
        p1.obj = (p1.obj
            .moveTo(  0,  0)
            .lineTo( self.BU*2,  0)
            .lineTo( self.BU*2,       self.BU*height)
            .lineTo( self.BU*(2-1/2), self.BU*(height+1/2) ) 
            .lineTo( self.BU*(  1/2), self.BU*(height+1/2) )
            .lineTo( self.BU*(    0), self.BU*(height)     )   
            .close()
            .extrude(self.BU/2)
            )
        h1 = Hole(2).BU_Txy(1, height )    # diera pre hriadel
        p1.D(h1)
        if height > 1:
            hr = []
            for i in range(height):
                hr.append([1/2, i])
                hr.append([1/2+1, i])
            h2 = Hole_List(hr)
            p1.D(h2)
        p1.Rx().BU_Ty(1/2)
        self.U([p1,p2])
        h2 = Hole_List( [ [1/2,1/2], [1/2+1, 1/2] ], 3/4)#.BU_Txy([1/2, 1/2])        
        self.D(h2)
        
        
#-----------------------------------------------------------------------
