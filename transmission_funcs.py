import math
import numpy
import random
from parameters import *

def path_loss(distance):
    path_loss_matrix=numpy.zeros((len(distance),len(distance[0])),float) 
    path_loss_ideal_matrix =numpy.zeros((len(distance),len(distance[0])),float)
    for i in range(len(path_loss_matrix)):
        for j in range(len(path_loss_matrix[0])):
            x=math.log10((distance[i][j])/d0)
            path_loss_matrix[i][j]=pl_d0 + 10*gamma*x + random.gauss(mu, sigma)
            path_loss_ideal_matrix[i][j]=pl_d0 + 10*gamma*x

    return path_loss_matrix,path_loss_ideal_matrix

def path_loss_train(distance):
    path_loss_matrix=numpy.zeros((len(distance),len(distance[0])),float)

    for i in range(len(path_loss_matrix)):
        for j in range(len(path_loss_matrix[0])):
            x=math.log10((distance[i][j])/d0_train)
            path_loss_matrix[i][j]=pl_d0_train + 10*gamma_train*x + random.gauss(mu_train, sigma_train)
            

    return path_loss_matrix

def received_power(path_loss):
    received_power_matrix_t=numpy.zeros((len(path_loss),len(path_loss[0])),float)

    for i in range(len(received_power_matrix_t)):
        for j in range(len(received_power_matrix_t[0])):
            received_power_matrix_t[i][j]=P_t + G_t + G_r - L_t - L_r - L_add - path_loss[i][j]
    
    return received_power_matrix_t

def received_power_train(path_loss):
    received_power_matrix=numpy.zeros((len(path_loss),len(path_loss[0])),float)

    for i in range(len(received_power_matrix)):
        for j in range(len(received_power_matrix[0])):
            received_power_matrix[i][j]=P_t_train + G_t_train + G_r_train - L_t_train - L_r_train - L_add_train - path_loss[i][j]
    
    return received_power_matrix

def BLER_func(received_power,sensitivity,tech):
    BLER_matrix=numpy.zeros((len(received_power),len(received_power[0])),float)
    for i in range(len(BLER_matrix)):
        for j in range(len(BLER_matrix[0])):
            if received_power[i][j] >= sensitivity:
                BLER_matrix[i][j]=1
                bler=1
            else:
                BLER_matrix[i][j]=0
                bler=0
            #if tech == "802.15.4" and flag==3.1:
            #    print("BLER on the main node for the packet sent from node {} for transmission period {}: {}".format(j+1,i+1,bler))
            #elif tech == "802.15.4" and flag==3.2:
            #    print("BLER on the main node for the packet sent from node {} for transmission period {}: {}".format(j+1,i+1,bler))
            #elif tech == "LoRa":    
            #    print("BLER on the {}.masts for the packet sent from {}.position of the train: {}".format(j+1,i+1,bler))
    
    return BLER_matrix
        