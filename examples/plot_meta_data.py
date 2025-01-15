# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 12:37:15 2021

@author: anthony.krzysko
"""

from xray_scattering_tools.get_detector_objects import get_detector_objects_from_folder
from xray_scattering_tools.get_detector_objects import get_dataframe_from_objects_list
import matplotlib.pyplot as plt
import numpy as np

directory_in_str = r"C:\Users\Anthony.Krzysko\Documents\2021-1128_compton_exp_11IDC\data\2021-1202_sample_B_donut_2"

obj_list = get_detector_objects_from_folder(directory_in_str, "point", angle=89)
meta_data_choice = "total_counts"
meta_data_choice = "compton_cps"
#meta_data_choice = "s_parameter"
y_list = []
x_values = np.linspace(0, len(obj_list) + 1, num=len(obj_list))
number_items = []

i= 1
for obj in obj_list:
    y_list.append(obj.meta_data[meta_data_choice])
    number_items.append(i)
    i=+1
 
x = x_values
#x = number_items
y = y_list
    
fig = plt.figure(figsize=(10,6))
ax = plt.axes()   
ax.plot(x, y, "o", color="red")
print(f"x values: {x_values}")
print(f" y values: {y_list}")