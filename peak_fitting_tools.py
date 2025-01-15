# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:29:46 2021

@author: Anthony.Krzysko
"""
import numpy as np
import scipy
guesses=[0.4, 0, 0.5, 0.2, 0, 0.5]
class PeakFitting():
    def __init__(self, x, y, guesses):
        self.x = x
        self.y = y
        self.guesses = guesses
        
        # self.fit_to_gauss(self._1gaussian, self.x, self.y, self.guesses)
        self.fit_to_voigt(self._1gaussian, self.x, self.y, self.guesses)
    
    
    def fit_to_voigt(self, curve_definition, x, y, guesses): 
        popt_voigt, pcov_gauss = scipy.optimize.curve_fit(self._1voigt,x, y, p0=guesses)
        perr_voigt = np.sqrt(np.diag(pcov_gauss))
        self.fitted_y= self._1voigt(x, popt_voigt[0], popt_voigt[1], popt_voigt[2], popt_voigt[3], popt_voigt[4], popt_voigt[5])
        print(popt_voigt)
        print(popt_voigt)
    
    def fit_to_gauss(self, curve_definition, x, y, guesses):
        popt_gauss, pcov_gauss = scipy.optimize.curve_fit(self._1gaussian, x, y , p0=guesses)
        perr_gauss = np.sqrt(np.diag(pcov_gauss))
        self.fitted_y = self._1gaussian(x, popt_gauss[0], popt_gauss[1], popt_gauss[2])
        print(perr_gauss)
    
    
    
    def _1gaussian(self, x, amp1,cen1,sigma1): 
        x = self.x
        
        return amp1*(1/(sigma1*(np.sqrt(2*np.pi))))*(np.exp((-1.0/2.0)*(((x-cen1)/sigma1)**2)))    
    
    
    def _1voigt(self, x, ampG1, cenG1, sigmaG1, ampL1, cenL1, widL1):
        x = self.x
        return (ampG1*(1/(sigmaG1*(np.sqrt(2*np.pi))))*(np.exp(-((x-cenG1)**2)/((2*sigmaG1)**2)))) +\
                  ((ampL1*widL1**2/((x-cenL1)**2+widL1**2)) )        
                  
                  
        