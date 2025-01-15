# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:56:29 2021

@author: anthony.krzysko
"""
from xray_scattering_tools.get_detector_objects import get_detector_objects_from_folder
import matplotlib.pyplot as plt
from matplotlib import cm

directory_in_str = r"C:\Users\Anthony.Krzysko\Documents\2021-1128_compton_exp_11IDC\data\2021-1207_sample_B_comp_4"
obj_list = get_detector_objects_from_folder(directory_in_str, "point", angle=89.3)
color_scheme = cm.get_cmap('rainbow', len(obj_list)+1)

y_value_choice = "norm_to_wings_intensity"
x_value_choice = "momentum_array"
label_choice = "alias"

for obj in obj_list: 
    if obj.meta_data["scan_name"] == "sample_B_donut_pt_J":
        obj.meta_data["alias"] = "A"           
    elif obj.meta_data["scan_name"] == "sample_B_donut_pt_K":
        obj.meta_data["alias"] = "B"
    elif obj.meta_data["scan_name"] == "sample_B_donut_pt_L_2":
        obj.meta_data["alias"] = "C"
    elif obj.meta_data["scan_name"] == "sample_B_donut_pt_I":
        obj.meta_data["alias"] = "D"
        
fig = plt.figure(figsize=(10,8))
ax = plt.axes()   
ax.set_xlabel("p$_z$ (a.u.)", fontsize=24)
ax.set_ylabel("Intensity", fontsize=24)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

i= 1
for obj in obj_list:
    x = obj.data_values[x_value_choice]
    y = obj.data_values[y_value_choice]
    label_value = obj.meta_data[label_choice]
    ax.plot(x, y, label=label_value, color=color_scheme(i))
    i+=1
    
ax.legend(frameon=False, fontsize=14)    
plt.xlim([-6, 6])
plt.ylim([0, 0.06])