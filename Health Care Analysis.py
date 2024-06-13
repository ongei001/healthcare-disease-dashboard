import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('african_healthcare_data.csv')

# Set style for seaborn
sns.set(style="whitegrid")

# Create subplots
fig, axes = plt.subplots(3, 3, figsize=(18, 15))

# Plotting Vaccination Rate Distribution
sns.histplot(df['Vaccination_Rate'], kde=True, ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title('Vaccination Rate Distribution')

# Plotting Malaria Prevalence Distribution
sns.histplot(df['Malaria_Prevalence'], kde=True, ax=axes[0, 1], color='salmon')
axes[0, 1].set_title('Malaria Prevalence Distribution')

# Plotting HIV Prevalence Distribution
sns.histplot(df['HIV_Prevalence'], kde=True, ax=axes[0, 2], color='lightgreen')
axes[0, 2].set_title('HIV Prevalence Distribution')

# Plotting Healthcare Facilities Distribution
sns.histplot(df['Healthcare_Facilities'], kde=True, ax=axes[1, 0], color='orange')
axes[1, 0].set_title('Healthcare Facilities Distribution')

# Plotting Access to Clean Water Distribution
sns.histplot(df['Access_to_Water'], kde=True, ax=axes[1, 1], color='lightblue')
axes[1, 1].set_title('Access to Clean Water Distribution')

# Plotting Access to Sanitation Distribution
sns.histplot(df['Access_to_Sanitation'], kde=True, ax=axes[1, 2], color='pink')
axes[1, 2].set_title('Access to Sanitation Distribution')

# Correlation between Vaccination Rate and Healthcare Facilities
sns.scatterplot(data=df, x='Vaccination_Rate', y='Healthcare_Facilities', ax=axes[2, 0])
axes[2, 0].set_title('Vaccination Rate vs Healthcare Facilities')

# Correlation between Malaria Prevalence and Access to Clean Water
sns.scatterplot(data=df, x='Malaria_Prevalence', y='Access_to_Water', ax=axes[2, 1])
axes[2, 1].set_title('Malaria Prevalence vs Access to Clean Water')

# Correlation between HIV Prevalence and Access to Sanitation
sns.scatterplot(data=df, x='HIV_Prevalence', y='Access_to_Sanitation', ax=axes[2, 2])
axes[2, 2].set_title('HIV Prevalence vs Access to Sanitation')

plt.tight_layout()
plt.show()

# Top 10 Countries with Highest and Lowest Vaccination Rates
top_10_highest_vaccination = df.nlargest(10, 'Vaccination_Rate')[['Country', 'Vaccination_Rate']]
top_10_lowest_vaccination = df.nsmallest(10, 'Vaccination_Rate')[['Country', 'Vaccination_Rate']]

print("Top 10 Countries with Highest Vaccination Rates:")
print(top_10_highest_vaccination)
print("\nTop 10 Countries with Lowest Vaccination Rates:")
print(top_10_lowest_vaccination)
