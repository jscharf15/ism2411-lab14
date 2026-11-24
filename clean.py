# Reflection
# 1.
# 2.
# 3.

# -----Exercise 1-----
import pandas as pd

df = pd.read_csv("data/messy_sales.csv")

df.info()
print(df.isnull().sum())
# 1. Missing values across columns: Customer ID has 7.54% missing (362 of 4,800), Region has 2.31% missing (111), Quantity Sold has 1.96% missing (94), Order ID has 0.65% missing (31), and Order Date has 0.52% missing (25).
# 2. Unit Price is stored as text (str) instead of a number (float): 
#    Prices should be numeric (float or int) so you can calculate totals or averages.
# 3. Order Date is stored as text (str) instead of a date.

# -----Exercise 2-----
