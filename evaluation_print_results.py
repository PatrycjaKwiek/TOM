# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:10:14 2020

@author: Lociel
"""

# Ewaluacja sprawdzenie
# Średnia, odchylenie standardowe, wartosć minimalna i maksymalna dla nerki
# Średnia, odchylenie standardowe, wartosć minimalna i maksymalna dla nowotworu
# Suma, srednia, odchylenie standardowe, wartosć minimalna i maksymalna dla wartosci S

import numpy as np

eval_kidney=np.zeros(y_test.shape)
eval_tumor=np.zeros(y_test.shape)

for i in range(len(y_test)):
    eval_kidney[i]=evaluation_kidney(y_pred_test[i],y_test[i])
    #print(eval_kidney)
    eval_tumor[i]=evaluation_tumor(y_pred_test[i],y_test[i])
    #print(eval_tumor[i])

mean_kidney=np.mean(eval_kidney)
print('mean kidney: ')
print(mean_kidney)
std_kidney=np.std(eval_kidney)
print('std kidney: ')
print(std_kidney)
max_kidney=np.ndarray.max(eval_kidney)
print('max kidney: ')
print(max_kidney)
min_kidney=np.ndarray.min(eval_kidney)
print('min kidney: ')
print(min_kidney)

mean_tumor=np.mean(eval_tumor)
print('mean tumor: ')
print(mean_tumor)
std_tumor=np.std(eval_tumor)
print('std tumor: ')
print(std_tumor)
max_tumor=np.ndarray.max(eval_tumor)
print('max tumor: ')
print(max_tumor)
min_tumor=np.ndarray.min(eval_tumor)
print('min tumor: ')
print(min_tumor)

S=np.zeros(y_test.shape)
sum_S=0

# przypadek jednego case'a w zbiorze testowym
for i in range(len(y_test)):
  S[i]=evaluation(y_pred_test[i],y_test[i])
  sum_S=sum_S+evaluation(y_pred_test[i],y_test[i])

print('S: ')
print(sum_S)
mean_S=np.mean(S)
print('mean S: ')
print(mean_S)
std_S=np.std(S)
print('std S: ')
print(std_S)
max_S=np.ndarray.max(S)
print('max S: ')
print(max_S)
min_S=np.ndarray.min(S)
print('min S: ')
print(min_S)