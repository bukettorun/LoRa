import random
import math
import numpy
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import transpose
from parameters import *
import distance
import transmission_funcs
import pandas as pd
import xlsxwriter

#flag=input("Available simulator versions: 1, 2, 3. Please select the version to be run: ")
#print(flag)
number_of_masts = 9
position_of_masts = numpy.zeros((number_of_masts,3),float)

for i in range(len(position_of_masts)):
    for j in range(len(position_of_masts[0])):
        if j==0:
            #x coordinate of the mast
            position_of_masts[i][j]=i*250
        elif j==1:
            #y coordinate of the mast
            position_of_masts[i][j]=2
        elif j==2:
            #z coordinate of the mast 
            position_of_masts[i][j]=2

#print("The positions of the masts:")
#print(position_of_masts)

number_of_transmissions = int(Path_Length/(speed_of_train*transmission_period))
print(number_of_transmissions)
positions_of_train = numpy.zeros((number_of_transmissions,3),int)


for i in range(len(positions_of_train)):
    for j in range(len(positions_of_train[0])):
        if j==0:
            positions_of_train[i][j]=(i+1)*speed_of_train*transmission_period
        elif j==1:
            positions_of_train[i][j]=0
        elif j==2:
            #positions_of_train[i][j]=random.choice([1.8, 2, 2.5])
            positions_of_train[i][j]=2

#print("position of the train:")
#print(positions_of_train)

distance_between_nodes= [random.uniform(25,50), random.uniform(50,75), random.uniform(75,100)]
#distance between the main node and the other nodes
total_journey_time= Path_Length/speed_of_train
#total amount of time during journey
 
#the version choice is left to the user
if flag==1:
    #simulator version1
    positions_of_train=positions_of_train
elif flag==2:
    #simulator version 2
    positions_of_train_v2 = numpy.zeros((4*len(positions_of_train),3),float)
    for i in range(len(positions_of_train_v2)):
        for j in range(len(positions_of_train_v2[0])):
            if j==0:
                if i%4==0:
                    positions_of_train_v2[i][j]=positions_of_train[int(i/4)][j]-75
                elif i%4==1:
                    positions_of_train_v2[i][j]=positions_of_train[int(i/4)][j]-50
                elif i%4==2:
                    positions_of_train_v2[i][j]=positions_of_train[int(i/4)][j]-25
                elif i%4==3:
                    positions_of_train_v2[i][j]=positions_of_train[int(i/4)][j]
            elif j==1:
                positions_of_train_v2[i][j]=0
            elif j==2:
                positions_of_train_v2[i][j]=random.choice([1.8, 2, 2.5])

    positions_of_train=positions_of_train_v2
elif flag==3.1:
    #simulator version 3.1
    positions_of_train=positions_of_train

    number_of_transmissions_in_train = int(total_journey_time/transmission_period_in_train)
    transmissions_in_train = numpy.zeros((number_of_transmissions_in_train,3),float)

    for i in range(len(transmissions_in_train)):
        for j in range(len(transmissions_in_train[0])):
            transmissions_in_train[i][j]= distance_between_nodes[j]
    
    #print(transmissions_in_train)

    path_loss_matrix_in_train = transmission_funcs.path_loss_train(transmissions_in_train)
    #print(path_loss_matrix_in_train)


    received_power_matrix_in_train = transmission_funcs.received_power_train(path_loss_matrix_in_train)
    #print(received_power_matrix_in_train)

    BLER_matrix_in_train = transmission_funcs.BLER_func(received_power_matrix_in_train,Pr_sensitivity_train,"802.15.4")
    #print(BLER_matrix_in_train)
elif flag==3.2:
    #simulator version 3.2
    positions_of_train=positions_of_train

    number_of_transmissions_in_train = int(total_journey_time/transmission_period_in_train)
    transmissions_in_train = numpy.zeros((number_of_transmissions_in_train,3),float)

    for i in range(len(transmissions_in_train)):
        for j in range(len(transmissions_in_train[0])):
            transmissions_in_train[i][j]= random.uniform(25, 50)
            # the distance between 

    #print(transmissions_in_train)

    path_loss_matrix_in_train = transmission_funcs.path_loss_train(transmissions_in_train)
    #print("path loss for IEEE 802.15.4")
    #print(path_loss_matrix_in_train)


    received_power_matrix_in_train = transmission_funcs.received_power_train(path_loss_matrix_in_train)
    #print("received powers for IEEE 802.15.4")
    #print(received_power_matrix_in_train)

    BLER_matrix_in_train = transmission_funcs.BLER_func(received_power_matrix_in_train,Pr_sensitivity_train,"802.15.4")
    #print("Bler for IEEE 802.15.4")
    #print(BLER_matrix_in_train)
    


#print("where the packet is sent from:")
#print(positions_of_train)
#print(flag)

distance_matrix = distance.distance(positions_of_train,position_of_masts)
#print("distances between the tranmission point and each masts:")
#print(distance_matrix)

path_loss_matrix, path_loss_ideal_matrix=transmission_funcs.path_loss(distance_matrix)
#print("path loss for each path:")
#print(path_loss_matrix)



received_power_matrix=transmission_funcs.received_power(path_loss_matrix)
#print("received powers at each mast")
#print(received_power_matrix)
received_power_ideal_matrix=transmission_funcs.received_power(path_loss_ideal_matrix)

BLER_matrix=transmission_funcs.BLER_func(received_power_matrix,Pr_sensitivity,"LoRa")
#print("BLER values for each packet at each mast:")
#print(BLER_matrix)



trend = numpy.zeros(len(positions_of_train))
print(positions_of_train)
for i in range(len(positions_of_train)):
    trend [i] = positions_of_train[i][0]

results = numpy.zeros(len(received_power_matrix))
results_ideal = numpy.zeros(len(received_power_ideal_matrix))
for i in range(len(received_power_matrix)):
    results [i] = received_power_matrix[i][0]
    results_ideal [i] = received_power_ideal_matrix[i][0] 

#results_ideal= [-113.82936573 -114.88365638 -115.85351121 -116.75145758 -117.58742643 -118.36942366 -119.10400428 -119.7965727 -120.45169283 -121.07320215 -121.6643818 -122.22805471 -122.76666719 -123.28235301 -123.77698456 -124.25221665 -124.70950822 -125.15016488 -125.57536158 -125.98613755 -126.38344726 -126.7681379 -127.14099197 -127.50271609 -127.85395228]
#print("RSSI")
#print(numpy.transpose(results))
#print("distances")
#print(trend)



workbook = xlsxwriter.Workbook("Results.xlsx")
worksheet = workbook.add_worksheet()
row=1
col=0

worksheet.write(0, 0, "Distance")
worksheet.write(0, 1, "RSSI (σ=0)")
worksheet.write(0, 2, "RSSI (σ=9.6)")

for x,y,z in zip(trend,results_ideal,results):
        worksheet.write(row, col, x)
        worksheet.write(row, col+1, y)
        worksheet.write(row, col+2, z)
        row += 1

workbook.close()


yellowcurve,=plt.plot(trend, results)
bluecurve,=plt.plot(trend, results_ideal)
plt.legend([yellowcurve,bluecurve],["σ = 9.6","σ = 0"])

for i in range(len(results)):
    sim=plt.scatter( trend[i],results[i], color = "blue",marker="*")
    sim=plt.scatter( trend[i],results_ideal[i], color = "orange",marker=".")
    

plt.xlabel("distance [m]")
plt.ylabel("RSSI [dBm]")
plt.show()


