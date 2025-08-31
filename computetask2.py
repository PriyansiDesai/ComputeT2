""" Objective: 
 Explore and clean the raw UFC fighters dataset.
 Transform physical attributes (height, weight, reach) into consistent formats.
 Handle missing values, duplicates, and outliers.
 Visualize patterns in fighter performance: wins, losses, KO ratio, submission attempts.
 Analyze relationships between physical attributes, fighting style, and performance.
 Generate insights about which attributes may influence fight outcomes. """

# Loaded all libraries and downloaded dataset file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("ufc-fighters-statistics.csv")

# Exloring the dataset to understand its structure, check for missing values, and inspecting unique categories in important features 
print("Shape of dataset (rows, columns):", df.shape)
print("Column names in the dataset:\n", df.columns)
print("\nSummary statistics for numerical features:\n", df.describe())
print("\nMissing values in each column:\n", df.isnull().sum())
if 'Stance' in df.columns:
    print("\nUnique values in 'Stance' column:\n", df['Stance'].unique())

#Now many columns have missing values; so I will be a filling numeric ones with median, categorical with mode, adding 'No nickname' for missing nicknames, and removing duplicates
df['height_cm'] = df['height_cm'].fillna(df['height_cm'].median())
df['weight_in_kg'] = df['weight_in_kg'].fillna(df['weight_in_kg'].median())
df['reach_in_cm'] = df['reach_in_cm'].fillna(df['reach_in_cm'].median())
df['stance'] = df['stance'].fillna(df['stance'].mode()[0])
df['nickname'] = df['nickname'].fillna('No nickname')
df = df.drop_duplicates()
print(df.isnull().sum())
print("Number of duplicate rows:", df.duplicated().sum())

# Visualizing distributions of key numeric features and spotting outliers
numeric_cols = ['height_cm', 'weight_in_kg', 'reach_in_cm', 'wins', 'losses', 'draws']

for col in numeric_cols:
    plt.figure(figsize=(8,4))
    plt.subplot(1,2,1)
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f'Histogram of {col}')
    plt.subplot(1,2,2)
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.tight_layout()
    plt.show()

# Visualizing categorical features
categorical_cols = ['stance']
for col in categorical_cols:
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x=col)
    plt.title(f'Count of each category in {col}')
    plt.show()

# Exploring relationships between features to see which attributes affect fighter performance, checking correlations between numeric columns, how stance relates to wins/losses, and trends in height/weight vs wins
# Correlation heatmap to see how fighter attributes relate to wins, losses, draws
plt.figure(figsize=(12,8))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation between numeric features")
plt.show()

# Comparing average wins by stance
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='stance', y='wins')
plt.title("Average wins by stance")
plt.show()

# Similarly, average losses by stance
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='stance', y='losses')
plt.title("Average losses by stance")
plt.show()

# Scatter plots to see trends
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x='height_cm', y='wins')
plt.title("Height vs Wins")
plt.show()
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x='weight_in_kg', y='wins')
plt.title("Weight vs Wins")
plt.show()