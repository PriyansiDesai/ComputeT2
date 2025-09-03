import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("UFC Fighters Data Analysis")

# Load dataset
df = pd.read_csv("ufc-fighters-statistics.csv")

st.subheader("Dataset Overview")
st.write("Shape:", df.shape)
st.write(df.head())

st.subheader("Missing Values")
st.write(df.isnull().sum())

# Fill missing values
df['height_cm'] = df['height_cm'].fillna(df['height_cm'].median())
df['weight_in_kg'] = df['weight_in_kg'].fillna(df['weight_in_kg'].median())
df['reach_in_cm'] = df['reach_in_cm'].fillna(df['reach_in_cm'].median())
df['stance'] = df['stance'].fillna(df['stance'].mode()[0])
df['nickname'] = df['nickname'].fillna('No nickname')
df = df.drop_duplicates()

st.subheader("Data after cleaning")
st.write(df.head())

# Numeric distributions
numeric_cols = ['height_cm', 'weight_in_kg', 'reach_in_cm', 'wins', 'losses', 'draws']
for col in numeric_cols:
    fig, ax = plt.subplots(1,2, figsize=(12,4))
    sns.histplot(df[col], kde=True, bins=30, ax=ax[0])
    ax[0].set_title(f'Histogram of {col}')
    sns.boxplot(x=df[col], ax=ax[1])
    ax[1].set_title(f'Boxplot of {col}')
    st.pyplot(fig)

# Categorical distributions
categorical_cols = ['stance']
for col in categorical_cols:
    fig, ax = plt.subplots(figsize=(6,4))
    sns.countplot(data=df, x=col, ax=ax)
    ax.set_title(f'Count of each category in {col}')
    st.pyplot(fig)

# Correlation heatmap
fig, ax = plt.subplots(figsize=(12,8))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
ax.set_title("Correlation between numeric features")
st.pyplot(fig)

# Average wins/losses by stance
for metric in ['wins','losses']:
    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(data=df, x='stance', y=metric, ax=ax)
    ax.set_title(f"Average {metric} by stance")
    st.pyplot(fig)

# Scatter plots
for col in ['height_cm', 'weight_in_kg']:
    fig, ax = plt.subplots(figsize=(6,4))
    sns.scatterplot(data=df, x=col, y='wins', ax=ax)
    ax.set_title(f"{col} vs Wins")
    st.pyplot(fig)
