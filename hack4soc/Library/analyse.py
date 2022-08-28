# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 07:21:10 2022

@author: Neelesh Thonse Rao
"""

import csv
import  matplotlib.pyplot as plt

with open("quiz.csv", "r") as f:
    head = ["TimeStamp", "Score", "Username"]
    r = csv.DictReader(f, fieldnames=head)
    
    d, final = {}, {}
    
    count = 0
    for i in r:
        if count == 0:
            count += 1
            continue
        
        d[i['Username']] = int(i['Score'])
        
    
    
    #del d['Enter your username']  
    #print(d)
    x_coor = list(d.keys())
    y_coor = list(d.values())
    
    
    plt.bar(x_coor, y_coor, width=0.6,color=['red','black'])
    plt.title("Student Performance")
    plt.xlabel("Name of Student")
    plt.ylabel("Marks out of 6")
    plt.show()
    
        
        