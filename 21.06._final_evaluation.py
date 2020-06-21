# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:02:51 2020

@author: Mejbi
"""


# Walidacja
# predicted - wartości maski uzyskane za pomocą RF
# actual - wartości maski zapisane w segmentation

# macierz pomyłek dla nerki
def confusion_matrix_kidney(predicted,actual):
  numrows,numcols = predicted.shape
  TPk=0 # prawdziwie pozytywna
  FPk=0 # fałszywie pozytywna
  FNk=0 # fałszywie negatywna
  
  for x in range(numrows):
    for y in range(numcols):
      # sprawdzenie ile pixeli wyznaczonej maski jest zgodne z pixelami maski z segmentation dla samej nerki
      if predicted[x,y]==actual[x,y] and predicted[x,y]!=0:
        TPk+=1
      # sprawdzenie ile pixeli wyznaczonej maski zostało uznane za nerkę, a w rzeczywistosci nią nie było
      if predicted[x,y]!=actual[x,y] and predicted[x,y]!=0:
        FPk+=1
      # sprawdzenie ile pixeli wyznaczonej maski nie zostało uznane za nerkę, a w rzeczywistosci nią było
      if predicted[x,y]!=actual[x,y] and predicted[x,y]==0:
        FNk+=1

  return TPk,FPk,FNk

# macierz pomyłek dla nowotworu
def confusion_matrix_tumor(predicted,actual):
  numrows,numcols = predicted.shape
  TPt=0
  FPt=0
  FNt=0

  for x in range(numrows):
    for y in range(numcols):
      # sprawdzenie ile pixeli wyznaczonej maski jest zgodne z pixelami maski z segmentation dla samego nowotworu
      if predicted[x,y]==actual[x,y] and predicted[x,y]==2:
        TPt+=1
      # sprawdzenie ile pixeli wyznaczonej maski zostało uznane za nowotwór, a w rzeczywistosci nim nie było
      if predicted[x,y]!=actual[x,y] and predicted[x,y]==2:
        FPt+=1
      # sprawdzenie ile pixeli wyznaczonej maski nie zostało uznane za nowotwór, a w rzeczywistosci nim było
      if predicted[x,y]!=actual[x,y] and predicted[x,y]!=2:
        FNt+=1

  return TPt,FPt,FNt

# ewaluacja dla nerki
def evaluation_kidney(predicted,actual):
  TPk,FPk,FNk = confusion_matrix_kidney(predicted,actual)

  # założenie wyjątku, kiedy maska nie zawiera ani nerki ani nowotworu
  a=(1 in actual)
  b=(1 in predicted)
  c=(2 in actual)
  d=(2 in predicted)
  
  # sprawdzenie, czy występuje sytuacja, w której wykryto nerkę lub nowotwór
  if a==True or b==True or c==True or d==True:
    S = ((2*TPk)/(2*TPk+FPk+FNk))
  else:
    S=1

  return S

# ewaluacja dla nowotworu
def evaluation_tumor(predicted,actual):
  TPt,FPt,FNt = confusion_matrix_tumor(predicted,actual)

  # założenie wyjątku, kiedy maska nie zawiera nowotworu
  c=(2 in actual)
  d=(2 in predicted)
  
  # sprawdzenie, czy występuje sytuacja, w której wykryto nowotwór
  if c==True or d==True:  
    S = (2*TPt)/(2*TPt+FPt+FNt)
  else:
    S=1

  return S

# srednia ewaluacji dla nerki i nowotworu
def evaluation(predicted,actual):

  S = (1/2)*(evaluation_tumor(predicted,actual)+evaluation_kidney(predicted,actual))

  return S