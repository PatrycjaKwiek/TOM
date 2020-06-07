# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:24:18 2020

@author: Mejbi
"""

#walidacja
#do tej funkcji trzeba dać "segmentation" z "load_case" oraz naszą maskę

def confusion_matrix_kidney(predicted,actual):
  numrows,numcols = predicted.shape
  TPk=0
  FPk=0
  FNk=0

  for x in range(numrows):
    for y in range(numcols):
      if predicted[x,y] != 1:
        predicted[x,y]=0
      if actual[x,y] != 0:
        actual[x,y]=1

  for x in range(numrows):
    for y in range(numcols):
      if predicted[x,y]==actual[x,y] and predicted[x,y]==1:
        TPk+=1
      if predicted[x,y]!=actual[x,y] and predicted[x,y]==1:
        FPk+=1
      if predicted[x,y]!=actual[x,y] and predicted[x,y]==0:
        FNk+=1

  return TPk,FPk,FNk


#nieskończone, bo nie wiemy jak będzie wyglądało "predicted"
def confusion_matrix_tumor(predicted,actual):
  numrows,numcols = predicted.shape
  TPt=0
  FPt=0
  FNt=0

  for x in range(numrows):
    for y in range(numcols):

      if actual[x,y] == 2:
        actual[x,y]=1
      if actual[x,y] !=2:
        actual[x,y]=0

  for x in range(numrows):
    for y in range(numcols):
      if predicted[x,y]==actual[x,y] and predicted[x,y]==1:
        TPt+=1
      if predicted[x,y]!=actual[x,y] and predicted[x,y]==1:
        FPt+=1
      if predicted[x,y]!=actual[x,y] and predicted[x,y]==0:
        FNt+=1

  return TPt,FPt,FNt


def evaluation(predicted_kidney,predicted_tumor,actual):
  TPk,FPk,FNk = confusion_matrix_kidney(predicted_kidney,actual)
  TPt,FPt,FNt = confusion_matrix_tumor(predicted_tumor,actual)

  S = (1/2)*(((2*TPt)/(2*TPt+FPt+FNt))+((2*TPk)/(2*TPk+FPk+FNk)))
  return S