# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:37:07 2021

@author: anthony.krzysko
"""
import numpy as np
from xray_scattering_tools.support_functions import snip_x_and_y_values

class ComptonExp():
    def __init__(self, incident_energy, angle_deg, calibrated_energy):
        
        self.E_1 = incident_energy
        self.angle = angle_deg 
        self.calibrated_energy = calibrated_energy 
        self.mc2 = 0.511e3
        self.mass_e =9.11e-31 #kg
        self.c_light = 299792458 # m / s
        self.m_c = self.mass_e * self.c_light
        self.me_rest = 511 #kev
        self.m_c2 = self.me_rest * (self.c_light**2)
        self.phi = self.angle*(np.pi/180)
        
        
    def get_compton_energy(self):
        self.compton_energy = self.E_1/(1+(self.E_1/self.mc2)*(1-np.cos(self.phi)))
        # print(self.compton_energy)
        return self.compton_energy
    
    def get_momentum_arr(self):
        self.E_2 = np.asarray(self.calibrated_energy)
        self.momentum_arr = self.m_c*((self.E_2 - self.E_1+(self.E_1*self.E_2/self.me_rest)*(1-np.cos(self.phi)))/np.sqrt(self.E_1**2+self.E_2**2 - 2*self.E_1*self.E_2*np.cos(self.phi))/(1.99285191410e-24))
        # print(self.momentum_arr)
        return self.momentum_arr
    
    def s_parameter(self, x, y, Li_cont=0.5, total_cont=1.5):
       Li_x, Li_y, Li_sum =  snip_x_and_y_values(x, y, -1 * Li_cont, Li_cont)
       # print(Li_x)
       # print(Li_y)
       # print(Li_sum)
       total_x_pos, total_y_pos, total_sum_pos =  snip_x_and_y_values(x, y, Li_cont, total_cont)
       total_x_neg, total_y_neg, total_sum_neg =  snip_x_and_y_values(x, y, -1 * total_cont,-1 * Li_cont)
       # print(Li_x)
       # print(total_x_pos)
       #print(total_y_neg)
       other_cont = total_sum_pos + total_sum_neg
       s_param = Li_sum / other_cont
       sum_values = [Li_sum, other_cont]
       
       error_Li_cont = np.sqrt(Li_sum)
       error_other_cont = np.sqrt(other_cont)
       
       uncertainty_s = s_param * np.sqrt((error_Li_cont/Li_sum)**2 + (error_other_cont/other_cont)**2)
       
       return s_param, uncertainty_s, sum_values
   
    

    def norm_to_wings(self, intensity_array):
        lower_index = np.where(self.momentum_arr  > -6)
        upper_index = np.where(self.momentum_arr > -2)
        
        wing_lower = int(lower_index[0][0])
        wing_upper = int(upper_index[0][0]) + 1

        
        sum_intensity = np.sum(intensity_array[wing_lower:wing_upper]) *2
        norm_intensity_shoulder_arr =  (intensity_array  / sum_intensity)
        return norm_intensity_shoulder_arr
   

    def _1voigt(self, x, ampG1, cenG1, sigmaG1, ampL1, cenL1, widL1):
        return (ampG1*(1/(sigmaG1*(np.sqrt(2*np.pi))))*(np.exp(-((x-cenG1)**2)/((2*sigmaG1)**2)))) +\
                  ((ampL1*widL1**2/((x-cenL1)**2+widL1**2)) )
        
    
    