import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("Zomato-data-.csv")
print(df.head())
df.info()

# 1. Clean and convert 'rate' to float
def handleRate(rate):
    if pd.isna(rate) or rate == 'NEW' or rate == '-':
        return np.nan
    rate = str(rate).split("/")[0]
    return float(rate)

df["rate"] = df["rate"].apply(handleRate)

print("\nTop 5 Most Frequent Ratings:")
print(df["rate"].value_counts().head(5))

# 2. Restaurant types plot
sns.countplot(x=df['listed_in(type)'])
plt.xlabel("Type of Restaurants")
plt.xticks(rotation=45)
plt.show()

# 3. Overall rate distribution plot
sns.boxplot(x=df['rate'])
plt.show()

# 4. Group votes by restaurant type
grouped_data = df.groupby("listed_in(type)")['votes'].sum()
print("\nTotal Votes by Restaurant Type:")
print(grouped_data.head())

# 5. Restaurant with maximum votes
max_votes = df['votes'].max()
restaurant_with_max_votes = df.loc[df['votes'] == max_votes]
print("\nRestaurant with maximum votes:")
print(restaurant_with_max_votes[['name', 'votes']])

# 6. Online order countplot (Added plt.show() here)
sns.countplot(x=df['online_order'])
plt.title("Online Orders Count")
plt.show()

# 7. Online order vs Rating comparison
plt.figure(figsize=(6, 6))
sns.boxplot(x='online_order', y='rate', data=df)
plt.title("Rating by Online Order Availability")
plt.show()