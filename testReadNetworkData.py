import numpy as np
import ReadNetworkData as rd
filename='TestSystem.txt'

#read in the data from the file...

bus_data , load_data , gen_data , line_data , tran_data , mva_base , bus_to_ind , ind_to_bus = \
    rd.read_network_data_from_file(filename)

print(type(bus_data))
