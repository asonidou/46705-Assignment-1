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
    Ybus = np.zeros((N,N),dtype=complex)
    print(line_data)

    # Continue with your code here and create the needed data types...
    # sweep over the bus_data,load_data,gen_data,line_data, tran_data to fill in appropriate values

    # Line Impedances => Line Admittances and susceptance
    Za=1j*line_data[0][4]+line_data[0][3];  Ya=1/Za;  b_a= 1j*line_data[0][5]/2
    Zb=1j*line_data[1][4]+line_data[1][3];  Yb=1/Zb;  b_b= 1j*line_data[1][5]/2
    Zc=1j*line_data[2][4]+line_data[2][3]; Yc=1/Zc;  b_c= 1j*line_data[2][5]/2

    # N = 3 #number of busses

    #Bus addmitance Matrix
    Ybus=np.array([[Ya+Yc+b_a+b_c ,-Ya           ,-Yc           ],\
                   [-Ya           , Ya+Yb+b_a+b_b,-Yb           ],\
                  [-Yc           ,-Yb           ,  Yb+Yc+b_b+b_c]])
    
    Sbus = np.array([0,1,-(1.6+1j*0.1)]) # Apparent power specification
    SLD = np.array([0,0, (1.6+1j*0.1)]) # Loads at each buss (used when displaying results
    V0 = np.ones(N,dtype=np.complex)# Inital guess for V vector
    buscode = np.array([3,2,1]) # Bustype vector
    pq_index = np.where(buscode== 1)[0] # Find indices for all PQ-busses
    pv_index = np.where(buscode== 2)[0] # Find indices for all PV-busses
    ref = np.where(buscode== 3)[0] # Find index for ref bus

    # Create Branch Matrices
    n_br= 3; n_bus = N # number of brances, number of busses

    # Create the two branch admittance matrices
    Y_from=np.zeros((n_br,n_bus),dtype=np.complex)
    Y_to=np.zeros((n_br,n_bus),dtype=np.complex)

    br_f=np.array([1,1,2])-1 # The from busses (python indices start at 0)
    br_t=np.array([2,3,3])-1 # The to busses
    br_Y=np.array([Ya,Yc,Yb]) # The series admittance of each branch
    br_B=np.array([b_a,b_c,b_b]) # Half the branch susceptance

    for k in range(0,len(br_f)):# Fill in the matrices
        Y_from[k,br_f[k]] = br_Y[k]+br_B[k]
        Y_from[k,br_t[k]] = -br_Y[k]
        Y_to[k,br_f[k]]   = -br_Y[k]
        Y_to[k,br_t[k]]   = br_Y[k]+br_B[k]

    return

# calling the function
LoadNetworkData (filename)