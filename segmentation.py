import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load Excel file
df = pd.read_excel("online_retail_II.xlsx", engine='openpyxl')

# Show basic info
print("Initial data shape:", df.shape)
print("Columns:", df.columns)

# Drop rows with missing Customer ID
df.dropna(subset=['Customer ID'], inplace=True)

# Remove cancelled invoices (starting with 'C')
df = df[~df['Invoice'].astype(str).str.startswith('C')]

# Calculate TotalPrice
df['TotalPrice'] = df['Quantity'] * df['Price']

# Group by Customer ID
customer_df = df.groupby('Customer ID').agg({
    'Invoice': 'nunique',         # Number of orders
    'Quantity': 'sum',            # Total items bought
    'TotalPrice': 'sum'           # Total money spent
}).rename(columns={
    'Invoice': 'NumOrders',
    'Quantity': 'TotalQuantity',
    'TotalPrice': 'TotalSpent'
}).reset_index()

print("Grouped data preview:")
print(customer_df.head())

# Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(customer_df[['NumOrders', 'TotalQuantity', 'TotalSpent']])

# Elbow Method to find optimal k
inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Plot elbow graph
plt.figure(figsize=(8, 5))
plt.plot(K, inertia, 'bo-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.grid(True)
plt.show()

# Fit KMeans with optimal k (choose based on elbow plot, assume k=4)
kmeans = KMeans(n_clusters=4, random_state=42)
customer_df['Cluster'] = kmeans.fit_predict(scaled_features)

# Plot clusters
plt.figure(figsize=(8, 6))
plt.scatter(customer_df['TotalSpent'], customer_df['NumOrders'],
            c=customer_df['Cluster'], cmap='Set1')
plt.xlabel('Total Spent')
plt.ylabel('Number of Orders')
plt.title('Customer Segmentation Clusters')
plt.grid(True)
plt.show()
