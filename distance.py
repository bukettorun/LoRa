import numpy
import math

def distance(positions, masts):
    distance_matrix = numpy.zeros((len(positions),len(masts)),float)

    for i in range(len(distance_matrix)):
        for j in range(len(distance_matrix[0])):
            lst=list(numpy.array(positions[i])-numpy.array(masts[j]))
            distance_matrix[i][j]=math.sqrt(lst[0]**2+lst[1]**2+lst[2]**2)

    return distance_matrix
    