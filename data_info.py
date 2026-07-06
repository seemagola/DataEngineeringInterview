import pandas as pd

df = pd.read_parquet("data/Calendar.parquet")
print('Calendar',df.columns)

df = pd.read_parquet("data/Channel.parquet")
print('Channel',df.columns)

df = pd.read_parquet("data/Geography.parquet")
print('Geography',df.columns)

df = pd.read_parquet("data/Product.parquet")
print('Product',df.columns)

df = pd.read_parquet("data/ProductCategory.parquet")
print('ProductCategory',df.columns)

df = pd.read_parquet("data/ProductSubcategory.parquet")
print('ProductSubcategory',df.columns)

df = pd.read_parquet("data/Promotion.parquet")
print('Promotion',df.columns)

df = pd.read_parquet("data/Sales.parquet")
print('Sales',df.columns)

df = pd.read_parquet("data/Stores.parquet")
print('Stores',df.columns)