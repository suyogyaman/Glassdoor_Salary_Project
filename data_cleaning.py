# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 09:57:56 2020

@author: suy
"""

#Importing Libraries
import pandas as pd

#Read csv file
df = pd.read_csv('glassdoor_data_original.csv')

#Drop index column
#df.drop('Unnamed: 0',inplace=True,axis=1)

#to do
#Salary Correction
#Remove the salary without value ( -1 value in our case)
df = df[df['Salary Estimate'] != '-1']
#Remove the bracket ( first )
Salary = df['Salary Estimate'].apply(lambda x : x.split('(')[0])
#Remove the K and dollar sign
minus_Kdollar = Salary.apply(lambda x : x.replace('K','').replace('$',''))

#Divide into min and max and avg salary
df['min_salary'] = minus_Kdollar.apply(lambda x : int(x.split('-')[0]))
df['max_salary'] = minus_Kdollar.apply(lambda x : int(x.split('-')[1]))
df['average_salary'] = (df['min_salary']+df['max_salary'])/2

#Company Name : remove num
df['Company Name'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3],axis=1)

#Location seprating state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[-1])
#check headquaters equals to job state
df['same_state'] = df.apply(lambda x : 1 if x.Location == x.Headquarters else 0 ,axis=1)

#Age of company
df['age_company'] = df['Founded'].apply(lambda x : x if x<0 else 2020 - x)

#Parsing of Job Desp like python,R etc
#for python
df['python_yn'] = df['Job Description'].apply(lambda x : 1 if 'python' in x.lower() else 0 )
df['python_yn'].value_counts()
#r studio
df['r_yn'] = df['Job Description'].apply(lambda x : 1 if 'r studio' in x.lower() else 0 )
df['r_yn'].value_counts()
#spark
df['spark_yn'] = df['Job Description'].apply(lambda x : 1 if 'spark' in x.lower() else 0 )
#aws
df['aws_yn'] = df['Job Description'].apply(lambda x : 1 if 'aws' in x.lower() else 0 )
#sql
df['sql_yn'] = df['Job Description'].apply(lambda x : 1 if 'sql' in x.lower() else 0 )
#excel
df['excel_yn'] = df['Job Description'].apply(lambda x : 1 if 'excel' in x.lower() else 0 )


#Data cleaning completed, lets export to csv
df.to_csv('data_cleaned.csv',index=False)


#d = pd.read_csv('data_cleaned.csv')







