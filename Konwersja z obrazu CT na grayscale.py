# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:48:14 2020

@author: Mejbi
"""

#Wczesniej należy wczytać wszystkie obrazy danego pacjenta przy pomocy funkcji "load_case" z pliku "utils.py" 
#w folderze "starter_code"

import numpy as np
import matplotlib.pyplot as plt
from skimage import color

DEFAULT_HU_MAX = 512
DEFAULT_HU_MIN = -512

#Zmodyfikowane funkcje z pliku "visualize.py"

def hu_to_grayscale(volume, hu_min, hu_max):
    
    if hu_min is not None or hu_max is not None:
        volume = np.clip(volume, hu_min, hu_max)

    mxval = np.max(volume)
    mnval = np.min(volume)
    im_volume = (volume - mnval)/max(mxval - mnval, 1e-3)

    im_volume = 255*im_volume
    return np.stack((im_volume, im_volume, im_volume), axis=-1)



def visualize(vol, hu_min=DEFAULT_HU_MIN, hu_max=DEFAULT_HU_MAX):

    vol = vol.get_data()

    viz_ims = hu_to_grayscale(vol, hu_min, hu_max)

    for i in range(viz_ims.shape[0]):
        
        x = color.rgb2gray(viz_ims[i])
        
        #Sprawdzenie, czy wszystkie obrazy są w skali szarosci
        plt.figure(i)
        plt.imshow(x,cmap='gray')
        plt.axis('off')

