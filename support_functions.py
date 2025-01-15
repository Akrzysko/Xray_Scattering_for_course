# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:44:54 2021

@author: Anthony.Krzysko
"""
import numpy as np


def snip_x_and_y_values(x, y, lower_x=-5, upper_x=5):
    lower_index = np.where(x > lower_x)
    upper_index = np.where(x > upper_x)
     
    new_x = x[lower_index[0][0]:upper_index[0][0]]
    new_y = y[lower_index[0][0]:upper_index[0][0]]
    new_y_sum = new_y.sum()
  
    return new_x, new_y, new_y_sum

def isolate_regions_of_plot(x,  y, low_x_1 = -5,  high_x_1 = 5, low_x_2 = 5,  high_x_2 = 7):
    iso_reg_1_vals = snip_x_and_y_values(x, y, low_x_1, high_x_1)
    iso_reg_2_vals = snip_x_and_y_values(x, y, low_x_2, high_x_2)
    
    ratio = iso_reg_1_vals[-1] / iso_reg_2_vals[-1]
    
    isolated_regions = {
        "region_1": iso_reg_1_vals,
        "region_2": iso_reg_2_vals,
        "ratio": ratio    
        }
    
    
    return isolated_regions
