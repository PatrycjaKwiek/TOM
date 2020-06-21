# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:45:43 2020

@author: Acer
"""

%cd kits19
from starter_code.utils import load_case
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics

#ładowanie danych treningowych
for i in range(9, 12):
  volume, segmentation = load_case(i)
  vol = volume.get_fdata()
  seg = segmentation.get_fdata()
  
  nsamples, nx, ny = vol.shape
  vol = vol.reshape(nsamples, nx*ny)

  nsamples, nx, ny = seg.shape
  seg = seg.reshape(nsamples, nx*ny)

  if i==9:
    X=vol
    y=seg
  X=np.concatenate((X, vol))
  y=np.concatenate((y, seg))

# obiekt klasyfikatora – liczba drzew = 7
clf = RandomForestClassifier(n_estimators=7, warm_start=True)
clf.fit(X_train, y_train)   # trenowanie klasyfikatora

y_pred = clf.predict(X_train)

#Ładowanie danych testowych
volume, segmentation = load_case(7)
vol1 = volume.get_fdata()
seg1 = segmentation.get_fdata()

nsamples, nx, ny = vol1.shape
vol1 = vol1.reshape(nsamples, nx*ny)

nsamples, nx, ny = seg1.shape
seg1 = seg1.reshape(nsamples, nx*ny)

X_test=vol1
y_test=seg1

#Testowanie modelu
y_pred_test = clf.predict(X_test)

