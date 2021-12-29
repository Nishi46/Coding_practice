#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:55:02 2021

@author: nishi
"""

file1 = open('file_path_project.txt','r')
lines_f1 = file1.readlines()
res = ""
for line in lines_f1:
    path = line.split("-> ")[-1]
    name = line.split("/")[-1]
    file2 = open('path_seperated.txt','a')
    res = path.rstrip()+" "+name
    file2.write(res)
    file2.close()

