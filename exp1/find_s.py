import numpy as np 
import pandas as pd
import os 
import csv
num_attributes = 6
a = [] 
print("\n The Given Training Data Set \n")

folder = '/media/sahaj9/Apollo/6 th sem/ml/ml_file/exp1'
file = '/media/sahaj9/Apollo/6 th sem/ml/ml_file/exp1/ws.csv'

with open(file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        a.append (row)
        print(row)
        
type(reader)

print(a[0][:-1])

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes
print(hypothesis)

for j in range(0,num_attributes):
    hypothesis[j] = a[0][j] 
    
hypothesis

hypothesis == a[0][:-1]
print("\n Find S: Finding a Maximally Specific Hypothesis\n") 

for i in range(0,len(a)):
    if a[i][num_attributes]=='Yes':
        for j in range(0,num_attributes):
            print(a[i][j], end=' ')
            if a[i][j]!=hypothesis[j]:
                hypothesis[j]='?'
            else :
                hypothesis[j]= a[i][j] 
    print("\n\nFor Training instance No:{} the hypothesis is ".format(i), hypothesis)

print("\n The Maximally Specific Hypothesis for a given Training Examples :\n")
print(hypothesis)
