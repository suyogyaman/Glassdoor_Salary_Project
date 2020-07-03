# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:28:23 2020

@author: suyogya
"""

import glassdoor_scrapper as sc
import pandas as pd

path = "C:/Users/suy/Documents/Github Backup/Glassdoor_Salary_Project/chromedriver"

frame = int(input("Enter the number of iterations : \n"))
dataframe = sc.get_jobs("data scientist",frame,False,path,2)

dataframe.to_csv("glassdoor_data.csv",index=False)
