# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:28:10 2020

@author: Lociel
"""

# przykładowe sprawdzenie działania klasyfikacji RF
# case o indeksie 10

from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

volume, segmentation = load_case(10)
vol = volume.get_fdata()
seg = segmentation.get_fdata()

nsamples, nx, ny = vol.shape
vol = vol.reshape(nsamples, nx*ny)

nsamples, nx, ny = seg.shape
seg = seg.reshape(nsamples, nx*ny)

X_train, X_test, y_train, y_test = train_test_split(vol, seg, test_size=0.22)

# obiekt klasyfikatora – liczba drzew = 7 
clf = RandomForestClassifier(n_estimators=7)
clf.fit(X_train, y_train)   # trenowanie klasyfikatora
y_pred = clf.predict(X_train)

y_pred_test = clf.predict(X_test)

nsamples = y_test.shape[0]
y_test = y_test.reshape(nsamples, nx, ny)
y_pred_test = y_pred_test.reshape(nsamples, nx, ny)

for i in range(nsamples):
  print(i)

  plt.figure(figsize=(14,7))
  plt.subplot(1, 2, 1)
  plt.imshow(y_test[i],cmap='gray')
  plt.axis('off')
  plt.title("True Mask")

  plt.subplot(1, 2, 2)
  plt.imshow(y_pred_test[i],cmap='gray')
  plt.axis('off')
  plt.title("Mask Prediction")