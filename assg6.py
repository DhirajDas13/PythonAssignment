# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:43:33 2019

@author: DH319684
"""


import heapq
#Create 3 lists
num1 = int(input('Size of first list : '))
arr1 = list()

for i in range(num1) :
  ele1  = int(input())
  arr1.append(ele1)
print(arr1)

input_list = arr1
number_of_elements = 2
maxarr1= heapq.nlargest(number_of_elements, input_list)
input_list = arr1
number_of_elements = 2
minarr1= heapq.nsmallest(number_of_elements, input_list)

num2 = int(input('Size of second list : '))
arr2 = list()

for i in range(num2) :
  ele2  = int(input())
  arr2.append(ele2)

print(arr2)

input_list = arr2
number_of_elements = 2
maxarr2= heapq.nlargest(number_of_elements, input_list)
input_list = arr2
number_of_elements = 2
minarr2= heapq.nsmallest(number_of_elements, input_list)

num3 = int(input('Size of Third list : '))
arr3 = list()

for i in range(num3) :
  ele3  = int(input())
  arr3.append(ele3)

print(arr3)

input_list = arr3
number_of_elements = 2
maxarr3= heapq.nlargest(number_of_elements, input_list)
input_list = arr3
number_of_elements = 2
minarr3= heapq.nsmallest(number_of_elements, input_list)

#Concatenate all 3 lists in a single list
max_list= maxarr1 + maxarr2 + maxarr3
max_list.sort()
print("Maxlist :", max_list)
avg_max_list= sum(max_list) / float(len(max_list))
print("\nAverage of Maxlist :", avg_max_list)

#Concatenate all 3 lists in a single list
min_list= minarr1 + minarr2 + minarr3
min_list.sort()
print("Minlist :", min_list)
avg_min_list= sum(min_list) / float(len(min_list))
print("\nAverage of Minlist :", avg_min_list)

