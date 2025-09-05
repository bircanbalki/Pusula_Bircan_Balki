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
df= pd.read_excel(r"C:\Users\birca\Documents\GitHub\Talent_Academy_Case_DT_2025.xlsx")
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
#Histogramlar
df.hist(bins=30, figsize=(15,10))
plt.suptitle("Numerical Features Histogram" , fontsize=16)
plt.show()
#Boxplot (numeric outlier kontolü için)
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    plt.figure(figsize=(6,3))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot - {col}")
    plt.show()
# Heatmap (numeric correlation)
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

#Kategorik değişkenler için countplot
categorical_cols = df.select_dtypes(include=["object"]).columns
for col in categorical_cols:
    plt.figure(figsize=(8, 3))
    sns.countplot(y=df[col],order=df[col].value_counts().index)
    plt.title(f"Countplot - {col}")
    plt.show()
# ======================
# 3. DATA PREPROCESSING
# ======================  

#---Eksik Değerler----
#for numeric Columns to KNNImputer
num_imputer=KNNImputer(n_neighbors=5)
