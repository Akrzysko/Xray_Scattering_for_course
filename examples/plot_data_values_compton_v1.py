# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:56:29 2021

@author: anthony.krzysko
"""
from xray_scattering_tools.get_detector_objects import get_detector_objects_from_folder
import matplotlib.pyplot as plt
from matplotlib import cm

directory_in_str = r"C:\Users\Anthony.Krzysko\Documents\2022-0302_compton_xrd_11IDC\Data\organized\h2x_n2_1"
obj_list = get_detector_objects_from_folder(directory_in_str, "point", angle=87)
color_scheme = cm.get_cmap('rainbow', len(obj_list)+1)

y_value_choice = "norm_to_wings_intensity"
x_value_choice = "momentum_array"
label_choice = "alias"
s_parameter_list = []
s_parameter_uncert_list = []
hxx_position_list = []

for obj in obj_list:
    if obj.meta_data["scan_name"] == "sample_C_pt_FF":
        obj.meta_data["hxx"] = -6
        obj.meta_data["alias"] = "-6"
        hxx_position_list.append(obj.meta_data["hxx"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_N":
        obj.meta_data["hxx"] = -4
        obj.meta_data["alias"] = "-4"
        hxx_position_list.append(obj.meta_data["hxx"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_M":
        obj.meta_data["hxx"] = -3
        hxx_position_list.append(obj.meta_data["hxx"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
        obj.meta_data["alias"] = "-3"
    elif obj.meta_data["scan_name"] == "sample_C_pt_L":
        obj.meta_data["hxx"] = -2 
        hxx_position_list.append(obj.meta_data["hxx"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
        obj.meta_data["alias"] = "-2"
    elif obj.meta_data["scan_name"] == "sample_C_pt_U":
        obj.meta_data["hxx"] = -1
        obj.meta_data["alias"] = "-1"
        hxx_position_list.append(obj.meta_data["hxx"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_V":
        obj.meta_data["hxx"] = 0
        obj.meta_data["alias"] = "0"
        hxx_position_list.append(obj.meta_data["hxx"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_EE":
        obj.meta_data["hxx"] = 1  
        obj.meta_data["alias"] = "1"  
        hxx_position_list.append(obj.meta_data["hxx"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_O":
        obj.meta_data["hxx"] = 2
        obj.meta_data["alias"] = "2"
        hxx_position_list.append(obj.meta_data["hxx"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_P":
        obj.meta_data["hxx"] = 3
        obj.meta_data["alias"] = "3"
        hxx_position_list.append(obj.meta_data["hxx"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_Q":
        obj.meta_data["hxx"] = 4
        obj.meta_data["alias"] = "4"
        hxx_position_list.append(obj.meta_data["hxx"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_K":
        obj.meta_data["hxx"] = 5
        obj.meta_data["alias"] = "5"
        hxx_position_list.append(obj.meta_data["hxx"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])

    
    

        
        
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
plt.xlim([-5, 5])
plt.ylim([0, 0.06])