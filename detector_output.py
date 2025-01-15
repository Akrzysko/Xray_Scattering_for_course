# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:47:37 2021

@author: anthony.krzysko
"""
from xray_scattering_tools.compton_calculations import ComptonExp
import xray_scattering_tools.support_functions as xRaySup
import scipy
import numpy as np

class DetectorOutput():
    def __init__(self, file_path, incident_energy, angle, scan_name="default", alias="none", x_pos=0, y_pos=0, z_pos=0, is_compton_type=False):
        
        # meta data types that should be stored with the 
        # data and accessed in dictionary
        self.file_path = file_path
        self.incident_energy = incident_energy
        self.angle = angle
        self.scan_name = scan_name
        self.alias = alias
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
        
    
        self.meta_data = {
            "file_path": self.file_path,
            "incident_energy": self.incident_energy,
            "angle": self.angle,
            "scan_name": self.scan_name,
            "alias": self.alias
            }
        self.data_values = {}
         
    def get_compton_calculations(self, intensity_array):
        self.compton_calculations = ComptonExp(self.meta_data["incident_energy"], self.meta_data["angle"], self.data_values["calibrated_energy"])
        self.meta_data["compton_energy"] = round(self.compton_calculations.get_compton_energy(), 2)
        self.data_values["momentum_array"] = self.compton_calculations.get_momentum_arr()
        # self.data_values["momentum_array_compton"], self.data_values["raw_intensity_compton"], self.meta_data["total_counts_compton"]  = xRaySup.snip_x_and_y_values(self.data_values["momentum_array"], self.data_values["raw_intensity"], -5, 5)
        self.data_values["norm_to_wings_intensity"] =  self.compton_calculations.norm_to_wings(intensity_array)
        s_values = self.compton_calculations.s_parameter(x=self.data_values["momentum_array"], y=intensity_array)
        self.meta_data["s_parameter"] = round(s_values[0], 5)
        self.meta_data["uncertainty_s_param"] = round(s_values[1], 5)
        self.middle_s_sum = s_values[2][0]
        self.other_s_sum = s_values[2][1]
        # self.meta_data["s_parameter"], self.meta_data["uncertainty_s_param"] = self.compton_calculations.s_parameter(x=self.data_values["momentum_array"], y=self.data_values["raw_intensity"])
        # popt_voigt, pcov_gauss = scipy.optimize.curve_fit(self.compton_calculations._1voigt, self.data_values["momentum_array_compton"], self.data_values["raw_intensity_compton"], p0=[0.4, 0, 0.5, 0.2, 0, 0.5])
        # perr_voigt = np.sqrt(np.diag(pcov_gauss))
        # self.data_values["raw_intensity_compton_fit"] = self.compton_calculations._1voigt(self.data_values["momentum_array_compton"], popt_voigt[0], popt_voigt[1], popt_voigt[2], popt_voigt[3], popt_voigt[4], popt_voigt[5])
        
    def string_slicer(self, my_str, sub_string):
        index = my_str.find(sub_string)
        if index !=-1 :
            return my_str[index:] 
        else :
            raise Exception('Sub string not found!')
            
    def cut_out_str(self, str_in, preceding_str, trailing_str):
        cut_str = str_in.split(preceding_str)[1].split(trailing_str)[0]
        return cut_str
    
    def recalculate_count_rate(self, count_time):
        self.meta_data["count_time"] = count_time
        self.data_values["cps_intensity"] = self.data_values["raw_intensity"] / self.meta_data["count_time"]
        self.meta_data["total_count_rate"] = round(self.meta_data["total_counts"] / self.meta_data ["count_time"], 2)
    
    def get_ratio_regions(self, x, y, low_x_1, high_x_1, low_x_2, high_x_2):
        isolated_regions = xRaySup.isolate_regions_of_plot(x,  y, low_x_1,  high_x_1, low_x_2,  high_x_2)
        self.meta_data["peak_ratio"] = isolated_regions["ratio"]
        self.meta_data["lower_x_1"] = low_x_1
        self.meta_data["high_x_1"] = high_x_1
        self.meta_data["lower_x_2"] = low_x_2
        self.meta_data["high_x_2"] = high_x_2
        self.data_values["isolated_x_1"], self.data_values["isolated_y_1"], self.meta_data["region_1_sum"] = isolated_regions["region_1"]
        self.data_values["isolated_x_2"], self.data_values["isolated_y_2"], self.meta_data["region_2_sum"] = isolated_regions["region_2"]
        
    def subtract_background(self, non_background_intensity, background_intensity):
        self.data_values["background_subtracted_intensity"] = non_background_intensity - background_intensity
        self.get_compton_calculations(self.data_values["background_subtracted_intensity"])
    
    
        
            
                
                
                

