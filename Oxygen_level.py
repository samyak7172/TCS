# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

lst = [[],[],[],[]]

for i in range(3):
    for j in range(3):
      lst[i].append(int(input()))
      if (lst[i][-1]) not in range(1,101):print("invalid input")

for i in range(3):
    lst[3].append((lst[2][i]+lst[1][i]+lst[0][i])//3)
    
maximum = max(lst[3])

for i in range(3):
    if lst[3][i]<70:
        print('trainee {0} is unfit'.format(i+1))
    elif lst[3][i] == maximum:
        print("Trainee Number: ",i+1)