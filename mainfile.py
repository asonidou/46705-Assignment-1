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
    Z = np.zeros(N,dtype=complex)
    Y = np.zeros(N,dtype=complex)
    b = np.zeros(N,dtype=complex)
    Bus_nr = np.zeros(N)
    fb = np.zeros(N)
    tb = np.zeros(N)

    for line in line_data:
        (FROM_BUS, TO_BUS, ID, R, X, B, MVA_rating, X2, X0) = line
        from_idx = bus_to_ind[FROM_BUS]
        to_idx = bus_to_ind[TO_BUS]
        Z = R
        Y = 1/Z
        Ybus[from_idx,to_idx] += -Y
        Ybus[from_idx,from_idx] += Y + 


    for tran in tran_data:
        (FROM_BUS, TO_BUS, ID, R, X, n, ANG1, FROM_CON, TO_CON, MVA_rating, X2, X0) = tran
        from_idx = bus_to_ind[FROM_BUS]
        to_idx = bus_to_ind[TO_BUS]
        ....



    for l in range(N):
        Z[l] = 1j*line_data[l][4]+line_data[l][3]
        Y[l] = 1/Z[l]
        b[l] = 1j*line_data[l][5]/2
        Bus_nr[l] = bus_data[l][0]
        fb[l] = line_data[l][0]  # Store value and its original index
        tb[l] = line_data[l][1]

    #Bus addmitance Matrix Ybus

    for r in range(N):
        for c in range(N):
            from_idx = np.where(fb == Bus_nr[r])[0]
            to_idx = np.where(tb == Bus_nr[r])[0] 
            
            # Off-diagonal elements (mutual admittance)
            Ybus[fb, tb] -= Y[r]
            Ybus[tb, fb] -= Y[r]
            
            # Diagonal elements (self-admittance)
            Ybus[fb, fb] += Y[r] + 1j * b[r] / 2
            Ybus[tb, tb] += Y[r] + 1j * b[r] / 2


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