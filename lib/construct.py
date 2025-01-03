#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:37:59 2024

@author: pf
"""
from lib.base import Stemfie_X, np, Stemfie_X_Base
import cadquery as cq

class Construct(Stemfie_X_Base):
    """
    Simplified version of the cq.Assembly class
    """
    
    def __init__(self, name):
        Stemfie_X_Base.__init__(self)
        self.name = name
        self.obj = cq.Assembly(loc=cq.Location(cq.Vector(0, 0, 0)) )
        
    
    def add(self, cmp, color="gray90", loc=[0,0,0,], angle = [0,0,0] ):
        """
        Parameters
        ----------
        cmp : Stemfie_X object
            DESCRIPTION.
        loc : list, optional
            Position in BU units. The default is [0,0,0,].
        angle : list, optional
            Rotation in degrees. The default is [0,0,0].
        color : string, optional
            Color name string. The default is "gray90".
            Color names:
            https://cadquery.readthedocs.io/en/latest/assy.html#assembly-colors

        Returns
        -------
        None.

        """
        x,y,z = np.array(loc)*self.BU
        #self.obj.add(cmp.obj, loc=cq.Location(cq.Vector(x, y, z), tuple(angle) ), color=cq.Color(color) )
        self.obj.add(cmp.obj, color=cq.Color(color), loc=cq.Location(cq.Vector(x, y, z)) )
    
    
    def export_step(self):
        cq.exporters.export(self.obj, self.name +'.step')
        
    def export_stl(self):
        cq.exporters.export(self.obj, self.name +'.stl')
        
    def display(self):
        # display object in Jupyter Notebook
        display(self.obj)
        
    
        
        
