# Pusula Data Science Intern Case Study

**Name:** Bircan Balkı  
**Email:** bircanbalki@gmail.com  

##  Dataset
- **File:** Talent_Academy_Case_DT_2025.xlsx  
- **Observations:** 2235  
- **Features:** 13  
- **Target Variable:** `TedaviSuresi`  

### Columns
- `HastaNo`: Anonymized patient ID  
- `Yas`: Age  
- `Cinsiyet`: Gender  
- `KanGrubu`: Blood type  
- `Uyruk`: Nationality  
- `KronikHastalik`: Chronic conditions  
- `Bolum`: Department/Clinic  
- `Alerji`: Allergies  
- `Tanilar`: Diagnoses  
- `TedaviAdi`: Treatment name  
- `TedaviSuresi`: Treatment duration (target)  
- `UygulamaYerleri`: Application sites  
- `UygulamaSuresi`: Application duration  

---
##  Tasks

### 1. Exploratory Data Analysis (EDA)
- Checked dataset structure, shape, and data types  
- Summary statistics (numerical & categorical)  
- Missing value analysis  
- Visualizations:
  - Histograms  
  - Boxplots (outlier detection)  
  - Correlation heatmap  
  - Countplots for categorical variables  

### 2. Data Preprocessing
- Handled missing values:
  - **KNNImputer** for numerical features  
  - **SimpleImputer** (most frequent) for categorical features  
- Encoded categorical variables:
  - **LabelEncoder** for binary categorical variables  
  - **OneHotEncoder** for multi-class categorical variables  
- Normalized numerical variables using **StandardScaler**  
- Final **cleaned dataset** saved as: `cleaned_dataset.csv`  

---

##  How to Run

1. Clone this repository:  
   ```bash
   git clone https://github.com/bircanbalki/Pusula_Bircan_Balki.git
   cd Pusula_Bircan_Balki
