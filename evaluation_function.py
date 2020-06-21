# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:17:39 2020

@author: Lociel
"""

# Ewaluacja funkcje
# Ewaluacja nerki
# Ewaluacja nowotworu
# Ewaluacja wartosci S

# predicted - wartości maski uzyskane za pomocą RF
# actual - wartości maski zapisane w segmentation

def confusion_matrix_kidney(predicted,actual):
  numrows,numcols = predicted.shape
  TPk=0
  FPk=0
  FNk=0
  
  for x in range(numrows):
    for y in range(numcols):
      if predicted[x,y]==actual[x,y] and predicted[x,y]!=0:
        TPk+=1
      if predicted[x,y]!=actual[x,y] and predicted[x,y]!=0:
        FPk+=1
      if predicted[x,y]!=actual[x,y] and predicted[x,y]==0:
        FNk+=1

  return TPk,FPk,FNk

def confusion_matrix_tumor(predicted,actual):
  numrows,numcols = predicted.shape
  TPt=0
  FPt=0
  FNt=0

  for x in range(numrows):
    for y in range(numcols):
      if predicted[x,y]==actual[x,y] and predicted[x,y]==2:
        TPt+=1
      if predicted[x,y]!=actual[x,y] and predicted[x,y]==2:
        FPt+=1
      if predicted[x,y]!=actual[x,y] and predicted[x,y]!=2:
        FNt+=1

  return TPt,FPt,FNt

def evaluation_kidney(predicted,actual):
  TPk,FPk,FNk = confusion_matrix_kidney(predicted,actual)
  
  # Założenie wyjątku, kiedy maska nie zawiera ani nerki ani nowotworu
  a=(1 in actual)
  b=(1 in predicted)
  c=(2 in actual)
  d=(2 in predicted)
  
  if a==True or b==True or c==True or d==True:
    S = ((2*TPk)/(2*TPk+FPk+FNk))
  else:
    S=1

  return S

def evaluation_tumor(predicted,actual):
  TPt,FPt,FNt = confusion_matrix_tumor(predicted,actual)
  
  # Założenie wyjątku, kiedy maska nie zawiera nowotworu
  c=(2 in actual)
  d=(2 in predicted)
  
  if c==True or d==True:  
    S = (2*TPt)/(2*TPt+FPt+FNt)
  else:
    S=1

  return S

def evaluation(predicted,actual):

  S = (1/2)*(evaluation_tumor(predicted,actual)+evaluation_kidney(predicted,actual))

  return S
