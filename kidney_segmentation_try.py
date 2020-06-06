# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 12:47:14 2020

@author: Lociel
"""

# Wykorzystanie funkcji wymaga wcześniejszego wczytania obrazów
# Funkcja opiera się na modyfikacji funkcji z pliku Konwersja z obrazu CT na grayscale.py
# Jest to przykład ręcznego wykorzystania funkcji random Walker do wykonania segmentacji nerki
# Wyniki przedstawiono w załączonym pliku kidney_segmentation_try.pdf
# Kolejnym etapem jest zautomatyzowanie modelu, celem wyzanczania centrów oraz wartości beta

import numpy as np
import matplotlib.pyplot as plt
import skimage.segmentation as seg
from skimage import color
from skimage import draw

#funkcja, która wyświetla obrazy
def image_show(image, nrows=1, ncols=1, cmap='gray', **kwargs):
  fig, ax=plt.subplots(nrows=nrows, ncols=ncols, figsize=(10,10))
  ax.imshow(image, cmap='gray')
  ax.axis('off')
  return fig, ax

#funkcja tworząca okręgi
def circle_points(resolution, center, radius):
  radians=np.linspace(0, 2*np.pi, resolution)
  cen=center[1]+radius*np.cos(radians)
  rad=center[0]+radius*np.sin(radians)
  
  return np.array([cen, rad]).T

DEFAULT_HU_MAX = 512
DEFAULT_HU_MIN = -512

#funkcja zapożyczona z pliku Konwersja z obrazu CT na grayscale.py
def hu_to_grayscale(volume, hu_min, hu_max):
    
    if hu_min is not None or hu_max is not None:
        volume = np.clip(volume, hu_min, hu_max)

    mxval = np.max(volume)
    mnval = np.min(volume)
    im_volume = (volume - mnval)/max(mxval - mnval, 1e-3)

    im_volume = 255*im_volume
    return np.stack((im_volume, im_volume, im_volume), axis=-1)

#przykładowe wykorzystanie po zmodyfikowaniu funkcji vizualize
def visualize2(vol, hu_min=DEFAULT_HU_MIN, hu_max=DEFAULT_HU_MAX):
    vol = vol.get_data()
    #konwersacja do formy wizualnej
    viz_ims = hu_to_grayscale(vol, hu_min, hu_max)
    #konkretny przykład
    x = color.rgb2gray(viz_ims[30])
    return(x)

#image to pojedynczy obraz zwrócony na podstawie wybranego przypadku
image=visualize2(volume)

image_show(image)

kidney_labels=np.zeros(image.shape, dtype=np.uint8)

indices=draw.circle_perimeter(300,150,10)
kidney_labels[indices]=1
indices=draw.circle_perimeter(300,350,10)
kidney_labels[indices]=1

points = circle_points(200, [300,150],100)[:-1]
kidney_labels[points[:,1].astype(np.int), points[:,0].astype(np.int)]=2
points = circle_points(200, [300,350],100)[:-1]
kidney_labels[points[:,1].astype(np.int), points[:,0].astype(np.int)]=2

image_show(kidney_labels)

#dobranie parametru beta
kidney_segmented = seg.random_walker(image, kidney_labels, beta=90)

fig, ax = image_show(image)
ax.imshow(kidney_segmented == 1, alpha=0.4)