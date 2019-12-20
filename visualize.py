# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:06:41 2019

@author: user
"""

import opensim
def visualize(osimfile):
#    cwd = 'C:\\Users\\user\\Documents\\GitHub\\Compare_rt'
    model = opensim.Model(osimfile)
    model.setUseVisualizer(True)
    state = model.initSystem()
    model.getVisualizer().show(state)
    
