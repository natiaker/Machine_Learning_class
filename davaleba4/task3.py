# 3.	გამოიყენეთ ecommerce_orders_dirty.xlsx ფაილი. ონლაინ შეკვეთების ფაილში გაასუფთავეთ Category, Quantity,
# Unit_Price, Discount_%, Customer_Rating და Returned სვეტები, გაასწორეთ კატეგორიების სახელების ფორმატი, ტექსტური
# რიცხვები გადააქციეთ რიცხვებად, იპოვეთ არარეალური ფასდაკლებები და რეიტინგები, შემდეგ გამოთვალეთ თითოეული შეკვეთის
# საბოლოო ღირებულება ფასდაკლების გათვალისწინებით, pandas-ით დააჯგუფეთ მონაცემები კატეგორიების მიხედვით და დათვალეთ
# საშუალო ფასი, საშუალო რეიტინგი და დაბრუნების რაოდენობა, ხოლო matplotlib-ით ააგეთ კატეგორიების მიხედვით გაყიდვების და
# დაბრუნებების შედარებითი დიაგრამა.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data/ecommerce_orders_dirty.xlsx', header=2)
print(df.to_string())

df['Category'] = df['Category'].astype(str).str.strip().str.title()

df['Returned'] = df['Returned'].astype(str).str.strip().str.lower()
df = df[df['Returned'].isin(['yes', 'no'])]

num_cols = ['Quantity', 'Unit_Price', 'Discount_%', 'Customer_Rating']
for col in num_cols:
    df[col] = df[col].astype(str).str.replace(',', '.', regex=False)
    df[col] = pd.to_numeric(df[col], errors='coerce')


# არარეალური მნიშვნელობები
df.loc[(df['Discount_%'] < 0) | (df['Discount_%'] > 100), 'Discount_%'] = None
df.loc[(df['Customer_Rating'] < 0) | (df['Customer_Rating'] > 5), 'Customer_Rating'] = None
df.loc[df['Quantity'] <= 0, 'Quantity'] = None
df.loc[df['Unit_Price'] <= 0, 'Unit_Price'] = None

df = df.dropna(subset=['Quantity', 'Unit_Price', 'Discount_%', 'Customer_Rating'])

print('\nCleaned data:\n')
print(df.to_string())

# საბოლოო ფასი (discount-ის გათვალისწინებით)
df['Final_Price'] = df['Quantity'] * df['Unit_Price'] * (100 - df['Discount_%'] / 100)

avg_price = df.groupby('Category')['Final_Price'].mean()
avg_rating = df.groupby('Category')['Customer_Rating'].mean()
df['Returned_Flag'] = df['Returned'].map({'yes': 1, 'no': 0})
returns_by_category = df.groupby('Category')['Returned_Flag'].sum()

print(avg_price)
print(avg_rating)
print("returned amount = ", returns_by_category.sum())

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

avg_price.plot(kind='bar', ax=ax[0], title='Average Price by Category')
returns_by_category.plot(kind='bar', ax=ax[1], title='Returns by Category', color='orange')

plt.tight_layout()
plt.show()

