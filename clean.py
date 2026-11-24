# Reflection
# 1.
# 2.
# 3.

print(f"-----Exercise 1-----")
import pandas as pd

df = pd.read_csv("data/messy_sales.csv")

df.info()
print(df.isnull().sum())
# 1. Missing values across columns: Customer ID has 7.54% missing (362 of 4,800), Region has 2.31% missing (111), Quantity Sold has 1.96% missing (94), Order ID has 0.65% missing (31), and Order Date has 0.52% missing (25).
# 2. Unit Price is stored as text (str) instead of a number (float): 
#    Prices should be numeric (float or int) so you can calculate totals or averages.
# 3. Order Date is stored as text (str) instead of a date.

print(f" -----Exercise 2-----")
df.columns = df.columns.str.lower().str.replace(" ", "_")
print(df.columns.tolist())

print(f" -----Exercise 3-----")
print("Shape before:", df.shape)

# Drop rows missing order_id or order_date.
# order_id uniquely identifies each transaction, 
# and order_date is needed to analyze sales over time.
df = df.dropna(subset=["order_id", "order_date"])

# Fill missing quantity_sold with the column mean.
# This keeps those rows available for other analyses while keeping 
# the overall average quantity unchanged.
df["quantity_sold"] = df["quantity_sold"].fillna(df["quantity_sold"].mean())

print("Shape after:", df.shape)
print(df.isnull().sum())

print(f" -----Exercise 4-----")
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
print("Dates that became NaT:", df["order_date"].isna().sum())

df["unit_price"] = (
    df["unit_price"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["quantity_sold"] = df["quantity_sold"].astype(int)

df["revenue"] = (df["unit_price"] * df["quantity_sold"]).round(2)

print(df.dtypes)

print(f" -----Exercise 5-----")
print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Shape after:", df.shape)

print(f" -----Exercise 6-----")
print(df.describe())

# Suspicious Statistic 1: minimum revenue is -3268.00. These are likely returns, which are
# real money that went back to customers, so I keep them.

# Suspicious Statistic 2: maximum revenue is 59994.00, far above the 75th percentile. 
# It comes from quantity_sold = 9999 at $6.00, a placeholder and not a real order.

# Drop quantity_sold of 9999: it's a placeholder someone typed, not a real order. 
# Keeping it would inflate revenue and skew averages and totals.
df = df[df["quantity_sold"] != 9999]

print("Shape after:", df.shape)