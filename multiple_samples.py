# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 08:25:29 2021

@author: anthony.krzysko
"""
import numpy as np

class MultipleSamples():
    def __init__(self, final_sample_values, initial_sample_values=0, background=0):
        self.final_sample_values = np.asarray(final_sample_values)
        self.initial_sample_values = np.asarray(initial_sample_values)
        self.background = np.asarray(background)
        
        self.background_subtract()
        self.calculate_average()
        self.print_sample_values()
 
    def background_subtract(self):
        self.final_sample_values_bkg_sub = self.final_sample_values - self.background   
        if self.initial_sample_values == 0:
            self.initial_sample_values_bkg_sub = 0
        else:
            self.initial_sample_values_bkg_sub = self.initial_sample_values - self.background
        
        self.net_sample_values = self.final_sample_values_bkg_sub - self.initial_sample_values_bkg_sub
    
    def calculate_average(self, std_num=1):
        self.average_net_sample_values = np.average(self.net_sample_values)
        self.std_net_sample_values = np.std(self.net_sample_values) * std_num
        self.pct_error_net_sample_values = (self.std_net_sample_values / self.average_net_sample_values)*100

    def print_sample_values(self):
        print(f'resulting sample values: {self.net_sample_values}, average: {self.average_net_sample_values} \u00B1 {self.std_net_sample_values} ({self.pct_error_net_sample_values}%) ')
    

initial_w = [
    9453.65,
    9541.35,
    9431.3   
    ]

final_w =[
    12110.34,
    12229.67,
    12159.09
    ]
bkg = 1000
system_volumes = MultipleSamples(final_w, initial_sample_values=0, background=bkg)   