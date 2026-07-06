import pandas as pd
import sqlite3
calendar = pd.read_parquet("data/Calendar.parquet")
channel = pd.read_parquet("data/Channel.parquet")
geography = pd.read_parquet("data/Geography.parquet")
product = pd.read_parquet("data/Product.parquet")
subcategory = pd.read_parquet("data/ProductSubcategory.parquet")
category = pd.read_parquet("data/ProductCategory.parquet")
promotion = pd.read_parquet("data/Promotion.parquet")
sales = pd.read_parquet("data/Sales.parquet")
stores = pd.read_parquet("data/Stores.parquet")




tables = {
    "Calendar": calendar,
    "Channel": channel,
    "Geography": geography,
    "Product": product,
    "Subcategory": subcategory,
    "Category": category,
    "Promotion": promotion,
    "Sales": sales,
    "Stores": stores
}


con=sqlite3.connect('retail.db')


# for name, df in tables.items():
#     print("="*50)
#     print(name)
#     print(df.shape)
#     print(df.dtypes)
#     print(df.head())



# for name, df in tables.items():
#     # print(name)
#     # print(df.isnull().sum())
#     print(df.duplicated().sum())



# print(sales["channelKey"].isin(channel["Channel"]).all())

# (sales.merge(product, on="ProductKey", how="left")
# .groupby('ProductName')['SalesAmount']
# .sum()
# .sort_values(ascending=False)
# .head(10)
# )