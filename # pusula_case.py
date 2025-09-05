# pusula_case.py
# Author: Bircan Balkı
# mail: bircanbalki@gmail.com 

import pandas as pd 
import numpy as np
import matplotlib as plt
import seaborn as sns

from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler

# ======================
# 1. DATA LOADING
# ======================
df= pd.read_excel("C:\Users\birca\Documents\GitHub\Talent_Academy_Case_DT_2025.xlsx")
print ("Dataset Shape: ", df.shape)
print ("\nColumns: ", df.columns.tolist())
print ("\nInfo: ")
print (df.info())
print ("\nFirst Rows:\n ", df.head())
# ======================
# 2. EXPLORATORY DATA ANALYSIS (EDA)
# ======================

# Genel istatistikler
print("\nDescriptive Statistics:\n ", df.describe(include="all"))
# Eksik Değer Kontrolü
print("\nMissing Values:\n ", df.isnull().sum())
