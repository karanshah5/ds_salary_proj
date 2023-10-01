# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 16:12:53 2023

@author: karan
"""
import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/karan/Documents/ds_salary_proj/chromedriver.exe"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)