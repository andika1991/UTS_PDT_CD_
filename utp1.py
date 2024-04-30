import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/andika1991/UTS_PDT_CD_/main/avocado.csv")
df.head()

total_volume = df["Total Volume"].sum()
median_volume = df["Total Volume"].median()
mean_volume = df["Total Volume"].mean()

total_bags = df["Total Bags"].sum()
median_bags = df["Total Bags"].median()
mean_bags = df["Total Bags"].mean()

mean_avg_price = df["AveragePrice"].mean()
median_avg_price = df["AveragePrice"].median()
