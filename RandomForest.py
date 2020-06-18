# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:02:11 2020

@author: Acer
"""

! curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
! sudo apt-get install git-lfs
! git lfs install
! git clone https://github.com/neheller/kits19.git

%cd kits19
! python -m starter_code.get_imaging

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score 

#Komórka z opracowaniem danych do wrzucenia do lasu losowego
from starter_code.utils import load_case
import numpy as np

""""
Dane:
1. Wczytać case'a
2. get_data
3. Zmniejszyć obrazy
4. Dodać do jakiegoś dataframe XD
"""

for i in range(10, 13):
  volume, segmentation = load_case(i)
  vol = volume.get_fdata()
  seg = segmentation.get_fdata()

  nsamples, nx, ny = vol.shape
  vol = vol.reshape(nsamples, nx*ny)

  nsamples, nx, ny = seg.shape
  seg = seg.reshape(nsamples, nx*ny)

  if i==10:
    X=vol
    y=seg
  X=np.concatenate((X, vol))
  y=np.concatenate((y, seg))

#podział danych na zbiór testowy i treningowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# obiekt klasyfikatora – liczba drzew = 5
clf = RandomForestClassifier(n_estimators=5)
clf.fit(X_train, y_train)   # trenowanie klasyfikatora
y_pred = clf.predict(X_train)

nsamples = y_test.shape[0]
y_test = y_test.reshape(nsamples, nx, ny)
y_pred_test = y_pred_test.reshape(nsamples, nx, ny)

for i in range(nsamples):
  plt.figure(figsize=(14,7))
  plt.subplot(1, 2, 1)
  plt.imshow(y_test[i],cmap='gray')
  plt.axis('off')
  plt.title("True Mask")

  plt.subplot(1, 2, 2)
  plt.imshow(y_pred_test[i],cmap='gray')
  plt.axis('off')
  plt.title("Mask Prediction")
