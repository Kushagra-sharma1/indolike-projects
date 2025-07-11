📁 Project 1: Amazon Electronics - Sentiment-Based Recommendation System
📌 Objective
To build a product recommendation system based on review sentiments (positive/negative), using Amazon Electronics dataset. Recommendations are generated based on review scores and user-product relationships.

📦 Dataset Description
Source: Amazon Review Data

Columns Used:

Column Number	Description
0	User ID
1	Product ID
2	Rating (1 to 5)
3	Timestamp

Only columns 0, 1, and 2 are used.

Ratings are interpreted as sentiment:

5 = Very Positive

1 or 0 = Negative

🛠️ Technologies
Pandas for data manipulation

Sklearn for nearest neighbor recommendation

Matplotlib for visualization

🔁 Key Steps
Load dataset and assign column names: userId, productId, rating

Label sentiments:

python
Copy
Edit
df['sentiment'] = df['rating'].apply(lambda x: 1 if x == 5 else 0)
Filter top-rated products and active users

Create a user-product matrix

Use cosine similarity or KNN to suggest similar positively reviewed products

📈 Output
Shows related products only if user reviews them positively

Example:

diff
Copy
Edit
Recommended products for product X (based on positive sentiments):
- Product Y
- Product Z
📁 Project 2: Customer Segmentation - Online Retail Dataset
📌 Objective
To segment customers based on their purchasing behavior using K-Means Clustering. Helps businesses:

Personalize offers

Identify loyal vs. low-spending customers

📦 Dataset Description
Source: Online Retail Dataset (Kaggle)
File Used: online_retail_II.xlsx

Column	Description
Invoice	Unique transaction number (starts with 'C' for cancellations)
StockCode	Product code
Description	Product name
Quantity	Number of units bought
InvoiceDate	Date of purchase
Price	Unit price
Customer ID	Unique customer ID
Country	Country of the customer

🛠️ Technologies
Pandas, Matplotlib

Scikit-learn (KMeans, StandardScaler)

openpyxl for reading .xlsx files

🔁 Key Steps
Load Excel file using pd.read_excel(...)

Remove missing values and canceled transactions (Invoice starts with 'C')

Compute:

TotalSpent = Quantity × Price

NumOrders = Total invoices per customer

TotalQuantity = Total items bought

Standardize features using StandardScaler

Use Elbow Method to find optimal k (number of clusters)

Cluster customers using KMeans

📈 Output
Clustered scatter plot: Total Spent vs Number of Orders

Groupings such as:

Cluster 0: High spenders

Cluster 1: Low volume customers

Cluster 2: Frequent but low-cost buyers

