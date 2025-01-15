# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 08:36:59 2021

@author: anthony.krzysko
"""
from xray_scattering_tools.detector_output import DetectorOutput
import numpy as np
import pandas as pd
import ntpath

class TESOutput(DetectorOutput):
    def __init__(self, file_path, incident_energy, angle, scan_name="default", is_compton_type=True, count_time=1, date_exp = "NA") : 
        DetectorOutput.__init__(self, file_path, incident_energy, angle, scan_name)
        self.meta_data["detector_type"] = "TES"
        self.meta_data["scan_name"] = self.path_leaf(self.file_path)
        self.meta_data["count_time"] = count_time
        self.meta_data["date_exp"] = date_exp
        self.tes_file_import()
        # print(self.data_values["raw_intensity"])
        # print(self.data_values["calibrated_energy"])
        # print(self.meta_data["total_counts"])
        self.get_compton_calculations(self.data_values["raw_intensity"])
        
    def tes_file_import(self):
        self.original_data_df = pd.read_csv(self.file_path, header=1)
        self.meta_data["num_channels"] = self.original_data_df.shape[0]
        self.data_values["channels"] = np.linspace(1, self.meta_data["num_channels"], self.meta_data["num_channels"])
        self.data_values["calibrated_energy"] =  self.original_data_df["# Energy (eV)"] / 1000
        self.data_values["raw_intensity"]  = self.original_data_df["Counts"]
        self.data_values["cps_intensity"] = self.data_values["raw_intensity"] / self.meta_data["count_time"]
        self.meta_data["total_counts"] = round(self.original_data_df["Counts"].sum())
        self.meta_data["total_count_rate"] = round( self.meta_data["total_counts"] / self.meta_data ["count_time"], 2)
    
    def path_leaf(self, path):
       head, tail = ntpath.split(path)
       return tail or ntpath.basename(head)
        