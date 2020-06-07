# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:10:49 2020

@author: Lociel
"""
#dane wczytane jak w poprzednich przypadkach
#próba stwierdzenia obecności nerki za pomocą thresholdu
#jeszcze nie automatyczny dobór parametrów

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

    image = color.rgb2gray(viz_ims[-1])
    threshold=np.zeros(image.shape, dtype=np.uint8)
    threshold[image > 165] = 1
    
    aL, bL=np.histogram(threshold[200:400,50:200])
    tL=(aL[-1]+100)/aL[0]
    
    aR, bR=np.histogram(threshold[200:400,300:350])
    tR=(aR[-1]+100)/aR[0]

    centerRc=330
    centerRr=350
    centerLc=330
    centerLr=170
    
    #konkretny przykład
    for i in range(viz_ims.shape[0]):
      centerRc=centerRc-1
      centerLc=centerLc-1
      centerRr=centerRr-1

      x = color.rgb2gray(viz_ims[i])
      
      thresholdx=np.zeros(x.shape, dtype=np.uint8)
      thresholdx[x > 165] = 1
      axL, bxL=np.histogram(thresholdx[200:512,50:200])
      axR, bxR=np.histogram(thresholdx[200:512,300:400])

      kidney_labels=np.zeros(x.shape, dtype=np.uint8)

      #póki co wartości są wpisane ręcznie, zależy nam, żeby centra były wyznaczane automatycznie wraz z wartością beta

      if tL<axL[-1]/axL[0]:
        indices=draw.circle_perimeter(centerLc,centerLr,10)
        kidney_labels[indices]=1
        points = circle_points(200, [centerLc,centerLr],100)[:-1]
        kidney_labels[points[:,1].astype(np.int), points[:,0].astype(np.int)]=2
      
      if tR<axR[-1]/axR[0]:
        indices=draw.circle_perimeter(centerRc,centerRr,10)
        kidney_labels[indices]=1
        points = circle_points(200, [centerRc,centerRr],100)[:-1]
        kidney_labels[points[:,1].astype(np.int), points[:,0].astype(np.int)]=2
      
      if tR<axR[-1]/axR[0] or tL<axL[-1]/axL[0]:
        kidney_segmented = seg.random_walker(x, kidney_labels, beta=100)

        fig, ax = image_show(x)
        ax.imshow(kidney_segmented == 1, alpha=0.4)

visualize2(volume)