transmission_period = 2
# the amount of time between two subsequent transmissions
Path_Length = 2020
# total length between the first and the last station
speed_of_train=18
# the speed of the train in m/s. 11 m/s = 40 km/h
# the speed of the train in m/s. 8 m/s = 30 km/h
# the speed of the train in m/s. 12.5 m/s = 45 km/h
flag=1
# flag parameter indicates the version of the simulator 
gamma=2.79
# path loss exponent

mu=0
sigma=9.6
#the normal distribution with zero mean sigma square variance
#to account for shadowing
pl_d0=50
# the mean path loss at reference distance d0
d0=1
# reference distance
L_add=0
# fading margin, other losses
G_r=0
# the receiver antenna gain in dBi
G_t=0
# the transmitter antenna gain in dBi
L_r=0
# receiver losses
L_t=0
# transmitter losses(connectors, non-matching circuit etc.)
P_t=14
# transmitter power in dBm
Pr_sensitivity=-127
# receiver sensitivity in dBm
bler=0
# the initial value

#-----------
#parameters related with the IEEE 802.15.4
#"train" added to all parameters to distinguish technologies
frequency_train = 2.4*10**9
gamma_train=5
# path loss exponent

mu_train=0
sigma_train=4
#the normal distribution with zero mean sigma square variance
#to account for shadowing
pl_d0_train=127.41
# the mean path loss at reference distance d0
d0_train=40
# reference distance
L_add_train=0
# fading margin, other losses
G_r_train=0
# the receiver antenna gain in dBi
G_t_train=0
# the transmitter antenna gain in dBi
L_r_train=0
# receiver losses
L_t_train=0
# transmitter losses(connectors, non-matching circuit etc.)
P_t_train=3
# transmitter power in dBm
Pr_sensitivity_train=-130
# receiver sensitivity in dBm
bler=0
# the initial value
#Pr[dB] = Pt[dBm] - L[dB]
# L[dB] = k0 + k1 log(d) + s 
# s is Gaussian(zero mean) with variance sigma^2
# which depends on the environment(Indoor=5)
# k0 = 10log(4*pi/lambda)^2 Path loss at a distance of 1 meter
# k1 = 10 Beta
# Beta is the propagation coefficient 
# payload1= 35 byte
#payload2= 100 byte

#maximum transmit power is equal to 3 dBm 
transmission_period_in_train = 0.5
#düzeltmeyi unutma!!
#min amount of the between two subsequent transmission is 5 ms
# F is the device noise figure
#Rb bit rate=250 kbit/s
#T_sys = T0 + T0*(F-1)
# N0 = k*T_sys/2
# SNR= Pr_train/(2*N0*Rb)
k=1.38*10**-23
# k boltzman constant
# BLER=1-(1-BER)**Nb uzun formülü kullan
#Nb is the number of bits in the payload
#SNR mini bul!

