#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 08:33:55 2025

@author: alexandrasonidou
"""

import numpy as np
import ReadNetworkData as rd
filename='TestSystem.txt'


def LoadNetworkData (filename):

    global Ybus , Sbus , V0, buscode, ref, pq_index, ps_index, Y_fr, Y_to, bf_f, br_t, br_v_ind, br_Y, S_LD, \
    ind_to_bus, bus_to_ind, MVA_base, bus_labels, br_MVA , Gen_MVA, br_id, br_Ymat, bus_kv, p_gen_max, \
    q_gen_min, q_gen_max, v_min, v_max
    
    bus_data , load_data , gen_data , line_data , tran_data , mva_base , bus_to_ind , ind_to_bus = \
    rd.read_network_data_from_file(filename)

    # Construct the bus admittance matrix from elements in the line_data and trans_data
    # Construct the branch admittance matrices Y_fr and Y_to used to determine the line flows

    MVA_base = mva_base
    N = len(bus_data) #Number of buses
    M_lines = len(line_data)
    M_trans = len(tran_data)
    M_branches = M_lines + M_trans
    Ybus = np . zeros ( ( N , N) ,dtype=complex)

    # Continue with your code here and create the needed data types...
    # sweep over the bus_data,load_data,gen_data,line_data, tran_data to fill in appropriate values

