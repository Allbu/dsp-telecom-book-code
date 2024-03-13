import numpy as np
import matplotlib.pyplot as plt
import sincRec_fuction as sR

def rectpuls(t, width):
    """Generates a rectangular pulse with specified width."""
    return np.where(np.abs(t) <= width / 2, 1, 0)

## Define variables
Ts=0.2 #sampling interval (in seconds)
Fs=1/Ts #sampling frequency (5 Hz)
oversampling_factor = 200 #oversampling factor
textra = 0 #one extra time (1 second) for visualizing sincs
pulse_width = 0.2 #support of the rects in seconds
graph_overlay = True #allows you to plot overlapping graphs
## Generate signal xn sampled at Fs
n= np.arange(-3,3+1)
xn=np.array([0, 0, 0, 1, -3, 3, 0]) #signal with only three non-zero samples
## Generate oversampled version of xn
oversampled_Ts = Ts/oversampling_factor #new value of Ts
oversampled_n = np.arange(n[0]*oversampling_factor,n[-1]*oversampling_factor+1)
oversampled_t = oversampled_n*oversampled_Ts #time in seconds

oversampled_xn = rectpuls(oversampled_t,pulse_width) - \
                3*rectpuls(oversampled_t-Ts,pulse_width) + \
                3*rectpuls(oversampled_t-2*Ts,pulse_width) #define the signal
## Reconstruct signal from samples stored at xn and compare with 
## the "ground truth" oversampled_xn
a=sR.ak_sinc_reconstruction(n,xn,Ts,oversampled_n,oversampled_xn,textra,graph_overlay)
