# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 08:47:25 2022

@author: anthony.krzysko
"""
import numpy as np

mc2 = 0.511e3
def compton_energy(E_1, phi_deg):
    phi = phi_deg*np.pi/180
    E_compton = E_1/(1+(E_1/mc2)*(1-np.cos(phi)))
    return E_compton

def momentum_resolution_per_E1(E_1, phi_deg):
    phi = phi_deg*np.pi/180
    E_c = compton_energy(E_1, phi_deg)
    
    dpz_dE1 = 137.036 / (E_1 * (np.sqrt(1+(E_1/E_c)**2 - 2*(E_1/E_c)*np.cos(phi))))
    return dpz_dE1
    
def incident_energy_momentum_resolution(E_1, phi_deg, E_1_spread):
    dpz_dE1 = momentum_resolution_per_E1(E_1, phi_deg)
    incident_E_term = E_1_spread * dpz_dE1
    return incident_E_term

def momentum_resolution_per_E2(E_1, phi_deg):
    phi = phi_deg*np.pi/180
    E_c = compton_energy(E_1, phi_deg)
    E_c_norm=E_c/E_1
    dpz_dE2=137/(E_c*np.sqrt(1+E_c_norm**2-2*E_c_norm*np.cos(phi)))
    return dpz_dE2

def detector_momentum_resolution(E_1, phi_deg, detector_resolution):
    dpz_dE2 = momentum_resolution_per_E2(E_1, phi_deg)
    detector_term = detector_resolution * dpz_dE2
    return detector_term

def momentum_resolution_per_phi(E_1, phi_deg):
    phi = phi_deg*np.pi/180
    E_c = compton_energy(E_1, phi_deg)
    dpz_dE2 = momentum_resolution_per_E2(E_1, phi_deg)
    dpz_dphi = dpz_dE2*(E_c*E_c/mc2)*np.sin(phi)
    return dpz_dphi 

def angular_spread(slit_size, slit_distance):
    two_theta =  np.arctan(2 * slit_size / slit_distance)
    two_theta_deg = two_theta * (180  / np.pi )
    return two_theta, two_theta_deg

def angular_momentum_resolution(E_1, phi_deg, slit_size, slit_distance):
    dpz_dphi = momentum_resolution_per_phi(E_1, phi_deg)
    del_E = angular_spread(slit_size, slit_distance)
    geometric_term = del_E[0] * dpz_dphi
    return geometric_term

def total_momentum_resolution(E_1, E_1_spread, detector_resolution, phi_deg, slit_size, slit_distance):
    E1_term = incident_energy_momentum_resolution(E_1, phi_deg, E_1_spread)
    detector_term = detector_momentum_resolution(E_1, phi_deg, detector_resolution)
    geometric_term = angular_momentum_resolution(E_1, phi_deg, slit_size, slit_distance)
    momentum_res = np.sqrt(E1_term**2 + detector_term**2 + geometric_term**2)
    return momentum_res
    
# print(total_momentum_resolution(105.7, 105.7 *5e-03, 0.5, 90, 1, 200))