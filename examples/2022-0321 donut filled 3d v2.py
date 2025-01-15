# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:56:29 2021

@author: anthony.krzysko
"""
from xray_scattering_tools.get_detector_objects import get_detector_objects_from_folder
import matplotlib.pyplot as plt
from matplotlib import cm

directory_in_str = r"C:\Users\Anthony.Krzysko\Documents\2022-0302_compton_xrd_11IDC\Data\organized\3d_plotting_2"
obj_list = get_detector_objects_from_folder(directory_in_str, "point", angle=87)
color_scheme = cm.get_cmap('rainbow', len(obj_list)+1)

s_parameter_list = []
s_parameter_uncert_list = []
hxx_positions = []
h2y_positions = []
z_positions = []

for obj in obj_list: 
    if obj.meta_data["scan_name"] == "sample_C_pt_A":
        obj.meta_data["hxx"] = 0 
        obj.meta_data["h2y"] = 0
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_G":
        obj.meta_data["hxx"] = -1 
        obj.meta_data["h2y"] = 0
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_F":
        obj.meta_data["hxx"] = -2
        obj.meta_data["h2y"] = 0
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_E":
        obj.meta_data["hxx"] = -3
        obj.meta_data["h2y"] = 0
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_D":
        obj.meta_data["hxx"] = -4
        obj.meta_data["h2y"] = 0
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_C":
        obj.meta_data["hxx"] = -5
        obj.meta_data["h2y"] = 0
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_FF":
        obj.meta_data["hxx"] = -6
        obj.meta_data["h2y"] = 0
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_H_mid":
        obj.meta_data["hxx"] = 2
        obj.meta_data["h2y"] = 0
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])  
    elif obj.meta_data["scan_name"] == "sample_C_pt_I":
        obj.meta_data["hxx"] = 3
        obj.meta_data["h2y"] = 0
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])   
    elif obj.meta_data["scan_name"] == "sample_C_pt_J":
        obj.meta_data["hxx"] = 4
        obj.meta_data["h2y"] = 0
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])  
    elif obj.meta_data["scan_name"] == "sample_C_pt_K":
        obj.meta_data["hxx"] = 5
        obj.meta_data["h2y"] = 0
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
# the h2y -2      
    elif obj.meta_data["scan_name"] == "sample_C_pt_V":
        obj.meta_data["hxx"] = 0
        obj.meta_data["h2y"] = -2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_EE":
        obj.meta_data["hxx"] = 1
        obj.meta_data["h2y"] = -2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_L":
        obj.meta_data["hxx"] = -2
        obj.meta_data["h2y"] = -2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_M":
        obj.meta_data["hxx"] = -3
        obj.meta_data["h2y"] = -2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_N":
        obj.meta_data["hxx"] = -4
        obj.meta_data["h2y"] = -2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_U":
        obj.meta_data["hxx"] = -1
        obj.meta_data["h2y"] = -2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_O":
        obj.meta_data["hxx"] = 2
        obj.meta_data["h2y"] = -2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_P":
        obj.meta_data["hxx"] = 3
        obj.meta_data["h2y"] = -2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_Q":
        obj.meta_data["hxx"] = 4
        obj.meta_data["h2y"] = -2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
# h2y 2
    elif obj.meta_data["scan_name"] == "sample_C_pt_Z":
        obj.meta_data["hxx"] = 0
        obj.meta_data["h2y"] = 2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_Y":
        obj.meta_data["hxx"] = -1
        obj.meta_data["h2y"] = 2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_X":
        obj.meta_data["hxx"] = -2
        obj.meta_data["h2y"] = 2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_W":
        obj.meta_data["hxx"] = -3
        obj.meta_data["h2y"] = 2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_R":
        obj.meta_data["hxx"] = -4
        obj.meta_data["h2y"] = 2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_T":
        obj.meta_data["hxx"] = -5
        obj.meta_data["h2y"] = 2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_S":
        obj.meta_data["hxx"] = -6
        obj.meta_data["h2y"] = 2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_AA":
        obj.meta_data["hxx"] = 1
        obj.meta_data["h2y"] = 2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_BB":
        obj.meta_data["hxx"] = 2
        obj.meta_data["h2y"] = 2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_CC":
        obj.meta_data["hxx"] = 3
        obj.meta_data["h2y"] = 2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "sample_C_pt_DD":
        obj.meta_data["hxx"] = 4
        obj.meta_data["h2y"] = 2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
    elif obj.meta_data["scan_name"] == "point_RR_half_1":
        obj.meta_data["hxx"] = 6
        obj.meta_data["h2y"] = 2
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
        s_parameter_uncert_list.append(obj.meta_data["uncertainty_s_param"])
# hxx -4
    elif obj.meta_data["scan_name"] == "sample_D_pt_JJ":
        obj.meta_data["hxx"] = -4
        obj.meta_data["h2y"] = 3
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"]+0.2)
    elif obj.meta_data["scan_name"] == "sample_D_pt_KK":
        obj.meta_data["hxx"] = -4
        obj.meta_data["h2y"] = 1
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
    elif obj.meta_data["scan_name"] == "sample_D_pt_LL":
        obj.meta_data["hxx"] = -4
        obj.meta_data["h2y"] = -1
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
# hxx 4
    elif obj.meta_data["scan_name"] == "sample_D_pt_MM":
        obj.meta_data["hxx"] = 4
        obj.meta_data["h2y"] = 3
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"] +0.2)
    elif obj.meta_data["scan_name"] == "sample_D_pt_NN":
        obj.meta_data["hxx"] = 4
        obj.meta_data["h2y"] = 1
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
    elif obj.meta_data["scan_name"] == "sample_D_pt_OO":
        obj.meta_data["hxx"] = 4
        obj.meta_data["h2y"] = -1
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
# hxx 2
    elif obj.meta_data["scan_name"] == "sample_D_pt_YY":
        obj.meta_data["hxx"] = 2
        obj.meta_data["h2y"] = 1
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
    elif obj.meta_data["scan_name"] == "sample_D_pt_ZZ":
        obj.meta_data["hxx"] = 2
        obj.meta_data["h2y"] = -1
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
# edges
    elif obj.meta_data["scan_name"] == "sample_D_pt_SS":
        obj.meta_data["hxx"] = 6
        obj.meta_data["h2y"] = 1
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
    elif obj.meta_data["scan_name"] == "sample_D_pt_TT":
        obj.meta_data["hxx"] = 6
        obj.meta_data["h2y"] = -1
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
    elif obj.meta_data["scan_name"] == "sample_D_pt_UU":
        obj.meta_data["hxx"] = -6
        obj.meta_data["h2y"] = -1
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
    elif obj.meta_data["scan_name"] == "sample_D_pt_VV":
        obj.meta_data["hxx"] = -6
        obj.meta_data["h2y"] = 1
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
# uppper edges
    elif obj.meta_data["scan_name"] == "sample_D_pt_PP":
        obj.meta_data["hxx"] = -2
        obj.meta_data["h2y"] = 3
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"] +0.2)
    elif obj.meta_data["scan_name"] == "sample_D_pt_QQ":
        obj.meta_data["hxx"] = 2
        obj.meta_data["h2y"] = 3
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"] + 0.2)
# upper and lower corner
    elif obj.meta_data["scan_name"] == "sample_D_pt_HH":
        obj.meta_data["hxx"] =0
        obj.meta_data["h2y"] = 3
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
    elif obj.meta_data["scan_name"] == "sample_D_pt_II":
        obj.meta_data["hxx"] =0
        obj.meta_data["h2y"] = -3
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])
    elif obj.meta_data["scan_name"] == "sample_B_0p27_h2y_n5_long":
        obj.meta_data["hxx"] =0
        obj.meta_data["h2y"] = 4
        obj.meta_data["z_pos"] = 0
        hxx_positions.append(obj.meta_data["hxx"])
        h2y_positions.append(obj.meta_data["h2y"])
        z_positions.append(obj.meta_data["z_pos"])
        s_parameter_list.append(obj.meta_data["s_parameter"])


# plot the stuff
plt.style.use('seaborn-poster')

fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')
plt.show()

s_parameter_list = [1 if value >= 0.94 else value for value in s_parameter_list]
# s_parameter_list = [0.7 if value <= 0.78 else value for value in s_parameter_list]


x = hxx_positions
y = h2y_positions
z = z_positions
c = s_parameter_list

ax.scatter(x, y, z, c=c, cmap='Blues', depthshade=False, s=5000)

ax.set_xlabel('x (mm)', labelpad=20)
ax.set_ylabel('y (mm)', labelpad=20)
ax.set_zlabel('z', labelpad=20)