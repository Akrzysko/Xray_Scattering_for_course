# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 08:17:28 2021

@author: anthony.krzysko
"""

from xray_scattering_tools.detector_output import DetectorOutput
import numpy as np
import ntpath

class VortexOutput(DetectorOutput):
    def __init__(self, file_path, incident_energy, angle, scan_name="default",
                 is_compton_type=False, count_time=1): 
        DetectorOutput.__init__(self, file_path, incident_energy, angle, 
                                scan_name)
        self.meta_data["detector_type"] = "point"
        self.point_file_import()
        self.get_header_info()

        self.get_calibrated_energy()
        self.get_intensity()
        self.get_compton_calculations(self.data_values["raw_intensity"])
    
    
    def path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
    
    def point_file_import(self):
        self.original_file = open(self.file_path, "r")
        self.original_data_str = self.original_file.read()
        self.meta_data["scan_name"] = self.file_path.split('\\')[-1].split(".txt")[0]
    
    def get_header_info(self):
        self.meta_data["count_time"] = float(self.cut_out_str(self.original_data_str, "LIVE_TIME:", "CAL_OFFSET:"))
        #self.meta_data["count_time_real"] = float(self.cut_out_str(self.original_data_str, "ROI_2_net: ", "LIVE_TIME: "))
        self.meta_data["date_exp"] = self.cut_out_str(self.original_data_str, "DATE: ", 
                       "CHANNELS")    
        self.meta_data["num_channels"] = int(self.cut_out_str(self.original_data_str, "CHANNELS:", 
                               "ROIS:"))    
        self.data_values["channels"] = np.linspace(1, self.meta_data["num_channels"] , self.meta_data["num_channels"] )
    
    
    def get_calibrated_energy(self):
        self.quad = float(self.cut_out_str(self.original_data_str, "CAL_QUAD: ", 
                                "TWO_THETA:"))
        self.slope = float(self.cut_out_str(self.original_data_str, "CAL_SLOPE:", 
                                      "CAL_QUAD:"))
        self.offset = float(self.cut_out_str(self.original_data_str, "CAL_OFFSET: ", 
                                      "CAL_SLOPE:"))
        
        if self.quad == 0 and self.slope == 0:
            # print("Calibration seems off in file, input values manually: ")
            # self.quad = float(input("quad value: "))
            # self.slope = float(input("slope value: "))
            # self.offset = float(input("offset value: "))
            self.quad = -1.9759118e-06
            self.slope = 6.2143926e-02
            self.offset = -5.5145211e+00
        
        self.data_values["calibrated_energy"] = np.asarray(self.quad*(self.data_values["channels"])**2 + (self.slope * self.data_values["channels"]) + 
                                     self.offset)
    def get_intensity(self):
        data_sliced_1 = self.string_slicer(self.original_data_str, "DATA:")
        data_sliced_2 = data_sliced_1.replace("DATA:", "")
        intensity = [float(i) for i in data_sliced_2.split()]
        self.data_values["raw_intensity"] = np.asarray(intensity)
        self.meta_data["total_counts"] = self.data_values["raw_intensity"].sum()
        self.data_values["cps_intensity"] = self.data_values["raw_intensity"] / self.meta_data["count_time"]
        self.meta_data["total_count_rate"] = round( self.meta_data["total_counts"] / self.meta_data ["count_time"], 2)
   

        
   
        
    
        
       