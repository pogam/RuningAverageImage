import numpy as np
import scipy.ndimage as ndimage

def runing_mean_neighbor(x):

    def test_func(values):
        return values.sum()

    def padwithzeros(vector, pad_width, iaxis, kwargs):
        vector[:pad_width[0]] = 0
        vector[-pad_width[1]:] = 0
        return vector

    footprint = np.array([[1,1,1],
                          [1,0,1],
                          [1,1,1]])
    nbre_neighbour = np.zeros_like(x)
    nbre_neighbour[:,:] = 8
    nbre_neighbour[0,:] = 5
    nbre_neighbour[-1,:] = 5
    nbre_neighbour[:,0] = 5
    nbre_neighbour[:,-1] = 5
    nbre_neighbour[0,0] = 3
    nbre_neighbour[0,-1] = 3
    nbre_neighbour[-1,-1] = 3
    nbre_neighbour[-1,-1] = 3

    x_padded = np.lib.pad(x, 1, padwithzeros)

    return  ndimage.generic_filter(x_padded, test_func, footprint=footprint)[1:-1,1:-1]/nbre_neighbour


x = np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
print 'input'
print '----'
print x
print ''
print 'runing average'
print '----'
print runing_mean_neighbor(x)
