# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:28:23 2020

@author: suyogya
"""


import glassdoor_scrapper as sc
import pandas as pd

path = "C:/Users/suyogya/Documents/Github Backup/Glassdoor_Salary_Project/chromedriver"

dataframe = sc.get_jobs("data scientist",15,False,path,2)


# start stop and step variables 
start, stop, step = 0, 5, 1
 
# converting to string data type 
dataframe["Salary Estimate"]= dataframe["Salary Estimate"].astype(str) 
  
# slicing till 2nd last element 
dataframe["Salary Estimate (int)"]= dataframe["Salary Estimate"].str.slice(start, stop, step) 