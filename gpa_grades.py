#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:56:18 2021

@author: nishi
"""


creds= []
grades = []
gradenum = []

def classn():

    num = int(input("How many classes?"))
    i = 0
    sum1=0
    while (i < num):
        credam = int(input("Enter Class credit: "))
        creds.append(credam)
        i = i +1
        sum1 = sum1 + credam

    y = 0
    while (y <num):
        grade = input("Enter Your Grade For Each Class in Order (Letter Form): ")
        grades.append(grade)
        y = y + 1
    total= 0
    total = float(total)
    for element in grades:
        if element == "A+":
            total = total + 4.3
            gradenum.append(4.3)
        elif element == "A":
            total = total + 4.0
            gradenum.append(4.0)
        elif element == "A-":
            total = total + 3.7
            gradenum.append(3.7)
        elif element == "B+":
            total = total + 3.3
            gradenum.append(3.3)
        elif element == "B":
            total = total + 3.0
            gradenum.append(3.0)
        elif element == "B-":
            total = total + 2.7
            gradenum.append(2.7)
        elif element == "C+":
            total = total + 2.3
            gradenum.append(2.3)
        elif element == "C":
            total = total + 2.0
            gradenum.append(2.0)
        elif element == "C-":
            total = total + 1.7
            gradenum.append(1.7)
        elif element == "D":
            total = total + 1.3 
            gradenum.append(1.3)
    x=0
    tot=0

    while (x<num):
        t = creds[x]* gradenum[x]
        tot = float(tot) + float(t)
        x=x+1
        
    gpa = tot / sum1
    print(float(gpa))



    

classn()