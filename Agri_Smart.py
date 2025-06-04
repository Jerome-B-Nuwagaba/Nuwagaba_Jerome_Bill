import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\LENOVO\Desktop\2.2\datasets\climate_action_data.csv')


df.dtypes
df.isnull().sum()
df.info()
df.duplicated()
df.duplicated().sum()
df = df.drop_duplicates()
df.shape
df.replace('error', np.nan, inplace=True)
df.describe
numeric_cols = ['Soil_Moisture(%)', 'Soil_pH', 'Temperature(C)', 'Humidity(%)', 
                'Fertilizer_Recommended(kg/ha)', 'Irrigation_Recommended(mm)']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    
df = df.dropna(subset=['Date'])
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

df['Crop_Type'] = df['Crop_Type'].fillna('Unknown')

df = df[df['Crop_Type'] != 'Unknown']

crop_moisture = df.groupby('Crop_Type')['Soil_Moisture(%)'].mean().sort_values(ascending=False)

plt.figure(figsize=(15, 10))
plt.subplot(2, 3, 1)
sns.histplot(df['Soil_Moisture(%)'], kde=True)
plt.title(f'Distribution of Soil Moisture')
plt.show()    

plt.figure(figsize=(15, 10))
plt.subplot(2, 3, 2)
sns.histplot(df['Temperature(C)'], kde=True)
plt.title(f'Distribution of Temperature(C)')
plt.show()    

plt.figure(figsize=(15, 10))
plt.subplot(2, 3, 3)
sns.histplot(df['Humidity(%)'], kde=True)
plt.title(f'Distribution of Humidity(%)')
plt.show()    

plt.figure(figsize=(15, 10))
plt.subplot(2, 3, 4)
sns.histplot(df['Soil_pH'], kde=True)
plt.title(f'Distribution of Soil pH')
plt.show()

plt.figure(figsize=(10, 8))
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap of Soil and Environmental Variables')
plt.show()

numeric_cols = ['Soil_Moisture(%)', 'Soil_pH', 'Temperature(C)', 'Humidity(%)', 
                'Fertilizer_Recommended(kg/ha)', 'Irrigation_Recommended(mm)']
fertilizer_corr = df[numeric_cols].corr()['Fertilizer_Recommended(kg/ha)'].sort_values(key=abs, ascending=False)

high_temp_crops = df[df['Temperature(C)'] > 30].groupby('Crop_Type')['Irrigation_Recommended(mm)'].mean()

print(df.dtypes)
print(df.isnull().sum())
print(df.info())
print(df.duplicated().sum())
print(df.shape)
print(df.describe)
print(df.isnull().sum())
print(df.describe())
print("\nAverage soil moisture by crop type:")
print(crop_moisture) #Wheat has the highest average soil moisture
print("\nCorrelation with fertilizer recommendations:") #Soil_pH and Humidity influence fertilizer recommendations the most.
print(fertilizer_corr)
print(high_temp_crops) #Appropriate irrigation adjustments; Increase irrigation by 10-15% to compensate for higher evaporation rates
#Implement more frequent but shorter irrigation cycles to prevent water stress
#Consider mulching to retain soil moisture
#Monitor soil moisture levels more closely during heat waves.

#Insights and Recommendations:
#Crops frequently experiencing temperatures above 30°C are primarily Beans, Maize, and Lettuce.
#The crop type with the highest average soil moisture is Wheat (average 47.2%)
#Since fertilizer recommendations are most strongly correlated with soil moisture (negative correlation), ensure proper irrigation before fertilization
#Implement better data validation at the sensor level to reduce 'error' entries.
#Investigate why some crops are unidentified and standardize crop type recording to eliminate "Unknown" entries

df.to_csv('cleaned_precision_agriculture_data.csv', index=False)