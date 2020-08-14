# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 18:46:14 2020

@author: gauri
"""
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("general_data.csv")
print("Mean: ", dataset["MonthlyIncome"].mean())
print("Median: ",dataset["MonthlyIncome"].median())
print("Mode: ", dataset["MonthlyIncome"].mode())
print("Skewness: ",dataset["MonthlyIncome"].skew())
print("Kurtoisis: ",dataset["MonthlyIncome"].kurt())
print("Standard Deviation", dataset["MonthlyIncome"].std())
print("Summary/ description: ",dataset["MonthlyIncome"].describe())


