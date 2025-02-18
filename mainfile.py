#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 08:33:55 2025

@author: alexandrasonidou
"""

import numpy as np
import ReadNetworkData as rd
filename='TestSystem.txt'
bus_data , load_data , gen_data , line_data , tran_data , mva_base , bus_to_ind , ind_to_bus = \
    rd.read_network_data_from_file(filename)
def LoadNetworkData (filename):
    global Ybus , Sbus , V0, buscode, ref, pq_index, ps_index, Y_fr, Y_to, bf_f, br_t, br_v_ind, br_Y, S_LD, \
        ind_to_bus, bus_to_ind, MVA_base, bus_labels, br_MVA , Gen_MVA, 
        br_id, br_Ymat, bus_kv, p_gen_max, q_gen_min, q_gen_max, v_min, v_max
