import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\LENOVO\Desktop\2.2\datasets\data.csv')

plt.subplot(2, 2, 1)
sns.histplot(df['Duration'], bins=10, kde=True)
plt.title('Histogram of Duration')
plt.show()

# Histogram of 'Pulse'
plt.subplot(2, 2, 2)
sns.histplot(df['Pulse'], bins=30, kde=True)
plt.title('Pulse Distribution')
plt.show()

plt.subplot(2, 2, 3)
sns.histplot(df['Maxpulse'], bins=30, kde=True)
plt.title('Maxpulse')
plt.show()

plt.subplot(2, 2, 4)
sns.histplot(df['Calories'], bins=30, kde=True)
plt.title('Calories')
plt.show()


