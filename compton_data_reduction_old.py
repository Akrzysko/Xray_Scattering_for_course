# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:47:25 2021

@author: anthony.krzysko
"""
import numpy as np
import matplotlib.pyplot as plt
from scattering_tools.inelastic_scattering_functions import InelasticScatteringFunctions as ISF
# from scipy.signal import savgol_filter, peak_widths
# need to fix the calibration
# need to make sure this works with all types of data imports
# Some data did not save with their own calibration 
# so a special case (maybe when a value == 0 or something)
# needs to be added so that I can account for that. 
    
class ComptonDataReduction():
    def __init__(self, file_path, incident_energy, norm=True, max_norm=False, angle=90, momentum_plot=False):
        
        self.original_file = open(file_path, "r")
        self.original_data_str = self.original_file.read()
        self.exp_title = file_path.split('\\')[-1].split(".dat")[0]
        self.incident_energy = incident_energy
        self.angle = angle
        self.momentum_plot = momentum_plot
        
        self.num_channels = 2048
        self.channels_arr = np.linspace(1, self.num_channels, self.num_channels)
        self.channels_to_energy(self.channels_arr)
        self.count_time = 1
        
        self.get_intensity_arr()
        self.smooth_intensity()
        self.get_header_info()
        
        self.x_label = "Energy (keV)"
        self.y_label = "Intensity (arbitrary units)"
        self.curve_label = self.exp_title
        self.x1 = self.energy_arr
        self.y1 = self.intensity_arr
        
        # create the compton scattering object 
        # defaults to compton type
        self.scattering_calcs = ISF("compton", self.incident_energy) 
        
        self.get_total_counts()
        self.norm_intensity()
        self.norm_to_max()
        self.get_compton_angle()
        self.pz_calculation(self.incident_energy, self.energy_arr, self.angle)
        # self.pz_calculation(self.incident_energy, self.energy_arr, self.calculated_compton_angle_deg)
        self.norm_to_wings()
        self.full_w_h_m()
        
        
        #self.show_plot()
        
    def get_total_counts(self):
        self.total_counts = np.sum(self.intensity_arr, 0)
        
    
    def show_plot(self, log=False, annotate=False):
        fig, ax1 = plt.subplots()
        ax1.plot(self.x1, self.y1, color="red", label=self.curve_label)
        
        ax1.set_xlabel(self.x_label)
        ax1.set_ylabel(self.y_label)
        plt.legend()
        if annotate == True:
            ax1.annotate(self.annotation_label, xy=(self.compton_result, 1),  
            xycoords='data', xytext=(0.8, 0.5), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center', verticalalignment='center',)
            
        if log == False:
            plt.show()  
        if log == True:
            plt.yscale("log")
            plt.show()
    
    def norm_intensity(self):
        self.norm_intensity_cps_arr = self.intensity_smoothed_arr / self.count_time
        self.y1 = self.norm_intensity_cps_arr
        self.y_label = "Intensity (cps)"
        return self.norm_intensity_cps_arr
    
    # def smooth_intensity(self):
        # self.intensity_smoothed_arr = savgol_filter(self.intensity_arr, 11, 3)
        # default (no smoothing):
        # self.intensity_smoothed_arr = savgol_filter(self.intensity_arr, 1, 0)
    
    # def norm_to_max(self):
    #     self.comp_channel_1 = 1500
    #     self.comp_channel_2 = 1650
    #     lower_index = np.where(self.channels_arr  == self.comp_channel_1)
    #     upper_index = np.where(self.channels_arr == self.comp_channel_2)

    #     comp_lower = int(lower_index[0])
    #     comp_upper = int(upper_index[0])
        
    #     self.compton_max_intensity_cps = np.max(self.norm_intensity_cps_arr[comp_lower:comp_upper])
    #     self.norm_intensity()
    #     self.norm_max_arr = self.norm_intensity_cps_arr / self.compton_max_intensity_cps
    #     self.y1 = self.norm_max_arr
    #     self.y_label = "Intensity (normalized to max)"
    #     return self.norm_max_arr
    
    
    def predict_compton(self, angle, plt=False, show_value=True):
       self.compton_result =  self.scattering_calcs.compton_scattering(angle, show_value)
       
       if plt == True: 
          self.compton_result =  self.scattering_calcs.compton_scattering(self.angle, show_value=False, plt=True)
 #           self.annotation_label = f"Compton peak is predicted\nto be\
 # at {str(round(self.compton_result))} keV\n at {angle} degrees"
 #           self.show_plot(annotate=True)

    # removes everything up to the sub string
    def string_slicer(self, my_str, sub_string):
        index = my_str.find(sub_string)
        if index !=-1 :
            return my_str[index:] 
        else :
            raise Exception('Sub string not found!')
    
    def cut_out_str(self, str_in, preceding_str, trailing_str):
        cut_str = str_in.split(preceding_str)[1].split(trailing_str)[0]
        return cut_str
    
    def channels_to_energy(self, channels):
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
        
        self.energy_arr = np.asarray(self.quad*(channels)**2 + (self.slope * channels) + 
                                     self.offset)
        
        return self.energy_arr   
    
    def show_calibration(self):
        print(f"offset: {self.offset}")
        print(f"slope: {self.slope}")
        print(f"quad: {self.quad}")
    
    def get_header_info(self):
        # example of some header info:
        # DATE:       Nov 08, 2020 11:22:39.**
        # CHANNELS:           2048
        # ROIS:        5
        # REAL_TIME:   39680.8671875
        # LIVE_TIME:   37861.2539062
        self.date_exp = self.cut_out_str(self.original_data_str, "DATE: ", 
                               "CHANNELS")
        self.num_channels = int(self.cut_out_str(self.original_data_str, "CHANNELS:", 
                               "ROIS:"))
        self.channels_arr = np.linspace(1, self.num_channels, self.num_channels)
        self.count_time = float(self.cut_out_str(self.original_data_str, "LIVE_TIME:", "CAL_OFFSET:"))
        
    def get_intensity_arr(self, plt=False, log=False):
        data_sliced_1 = self.string_slicer(self.original_data_str, "DATA:")
        data_sliced_2 = data_sliced_1.replace("DATA:", "")
        self.intensity = [float(i) for i in data_sliced_2.split()]
        self.intensity_arr = np.asarray(self.intensity)
        
        x_label = "Channels"
        y_label = "Intensity (arbitrary units)"
        curve_label = self.exp_title
        
        if plt == True and log == False :
            self.x_label = x_label
            self.y_label = y_label
            self.curve_label = curve_label
            self.x1 = self.channels_arr
            self.y1 = self.data_arr
            self.show_plot()
        
        if plt == True and log == True:
            self.x_label = x_label
            self.y_label = y_label
            self.curve_label = curve_label
            self.x1 = self.channels_arr
            self.y1 = self.data_arr
            self.show_plot(log=True)
    
    def get_compton_angle(self):
        self.predict_compton(self.angle, show_value=False)
    
        
        index_compton_energy_low = np.where(self.energy_arr > (self.compton_result - 2))
        index_compton_energy_high = np.where(self.energy_arr > (self.compton_result + 2))
        # print(index_compton_energy_low[0][0])
        # print(index_compton_energy_high[0][0])
       
        
        # self.comp_channel_1 = 1500
        # self.comp_channel_2 = 1650
        # lower_index = np.where(self.channels_arr  == self.comp_channel_1)
        # upper_index = np.where(self.channels_arr == self.comp_channel_2)

        comp_lower = int(index_compton_energy_low[0][0])
        comp_upper = int(index_compton_energy_high[0][0])
        
        self.compton_max_intensity_cps = np.max(self.norm_intensity_cps_arr[comp_lower:comp_upper])
        
        self.compton_max_index = np.where(self.norm_intensity_cps_arr == self.compton_max_intensity_cps)
      
        self.calculated_compton_energy = self.energy_arr[self.compton_max_index]
        
        c_light = 299792458 # m / s
        m_e =  9.11e-31
        m_c2 = 511 #kev
        h_c = 1240 #eV * nm
        
        E_1 = self.incident_energy
        E_C = self.calculated_compton_energy
        
        # print(E_1)
        # print(E_C)
        
        wave_1 = h_c / E_1
        wave_2 = h_c / E_C 
        
        val = (wave_2 - wave_1)  * m_c2 / h_c
        
        cos_angle = 1 - val
        
        self.calculated_compton_angle = np.arccos(cos_angle)
        
        self.calculated_compton_angle_deg = self.calculated_compton_angle * 180 /np.pi
        
        # print(self.calculated_compton_angle)
        # print(self.calculated_compton_angle_deg)
        
        
            
    def pz_calculation(self, incident_energy, compton_energy, compton_angle):
    
        E_1 = incident_energy
        E_2 = np.asarray(compton_energy)
        
        angle_radians = (np.pi / 180) * compton_angle
        
        # momentum is units of kg * (m/s)
        
        mass_e =9.11e-31 #kg
        c_light = 299792458 # m / s
        
        me_rest = 511 #kev
        
        m_c2 = me_rest * (c_light**2)
        
        m_c = 9.11e-31 * 3e8
        
        
        self.momentum_arr = m_c*((E_2 - E_1+(E_1*E_2/me_rest)*(1-np.cos(angle_radians)))/np.sqrt(E_1**2+E_2**2 - 2*E_1*E_2*np.cos(angle_radians))/(1.99285191410e-24))
        
        self.momentum_arr_trim = self.momentum_arr
        self.intensity_arr_trim = self.intensity_arr
        return self.momentum_arr
    
    def norm_to_wings(self):
        lower_index = np.where(self.momentum_arr  > - 4)
        upper_index = np.where(self.momentum_arr > - 2)
        
        wing_lower = int(lower_index[0][0])
        wing_upper = int(upper_index[0][0]) + 1
        # print(wing_lower, wing_upper)
        
        # this is awkward, you have to scale after norm to match 1 BM plots
        # important otherwise you don't get proper scaling
        # or you don't get proper normalization
        # old scaling value was about 0.115. This must be done post norm
        # so here probably just leave at one, unless there is a good reason
        # to actually scale the values prior to normalization
        self.scale_value = 1
        self.norm_intensity_cps_arr_scaled =  self.norm_intensity_cps_arr / self.scale_value
        
        self.sum_intensity = np.sum(self.norm_intensity_cps_arr_scaled[wing_lower:wing_upper]) *2
        self.norm_intensity_shoulder_arr =  self.norm_intensity_cps_arr_scaled / self.sum_intensity
        
        self.x1 = self.momentum_arr
        self.y1 = self.norm_intensity_shoulder_arr
        self.x_label = "p$_z$ (a.u.)"
        self.y_label = "Intensity (arbitrary units)"
        self.curve_label = self.exp_title
        
        if self.momentum_plot == True:
            self.x1 = self.momentum_arr
            self.y1 = self.intensity_arr
            self.show_plot()
            self.x1 = self.momentum_arr
            self.y1 = self.intensity_arr
            # plt.xlim([-6, 6])
            # plt.ylim([0, np.max(self.norm_intensity_shoulder_arr[self.compton_max_index] + 0.01)])
       
       
    
    def full_w_h_m(self):
        self.half_max = np.max(self.norm_intensity_shoulder_arr) / 2.
        #find when function crosses line half_max (when sign of diff flips)
        #take the 'derivative' of signum(half_max - Y[])
        d = np.sign(self.half_max - self.norm_intensity_shoulder_arr[0:-1]) - np.sign(self.half_max - self.norm_intensity_shoulder_arr[1:])
        #plot(X[0:len(d)],d) #if you are interested
        #find the left and right most indexes
        left_idx = np.where(d > 0)[0]
        right_idx = np.where(d < 0)[-1]
        self.f_w_h_m_compton = self.momentum_arr[right_idx] - self.momentum_arr[left_idx]
        
        # scipy.signal.peak_widths(self.norm_intensity_shoulder_arr, peaks, rel_height=0.5, prominence_data=None, wlen=None)[source]
    
        # return self.momentum_arr[right_idx] - self.momentum_arr[left_idx]
        
      
     
            
            
    


