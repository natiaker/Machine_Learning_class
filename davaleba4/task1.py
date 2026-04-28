# 1. გამოიყენეთ sales_dirty.xlsx ფაილი.  გაყიდვების მონაცემების ფაილში გაასუფთავეთ Region, Units_Sold, Unit_Price,
# Revenue და Salesperson სვეტები, მოაშორეთ ზედმეტი გამოტოვებები, გაასწორეთ რეგისტრი, იპოვეთ ცარიელი და არასწორი
# მნიშვნელობები, გადააკეთეთ რიცხვითი სვეტები სწორ ტიპებად, შეამოწმეთ არის თუ არა Revenue = Units_Sold × Unit_Price,
# საჭიროების შემთხვევაში ჩაასწორეთ, შემდეგ pandas-ის გამოყენებით გამოთვალეთ რეგიონების მიხედვით ჯამური გაყიდვები და
# პროდუქტების მიხედვით საშუალო შემოსავალი, ხოლო matplotlib-ით ააგეთ რეგიონების მიხედვით სვეტოვანი დიაგრამა და
# პროდუქტების მიხედვით ხაზოვანი ან სვეტოვანი დიაგრამა.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data/sales_dirty.xlsx", header=2)

print(df.to_string())

text_cols = ['Region', 'Product', 'Salesperson']
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()

num_cols = ['Units_Sold', 'Unit_Price', 'Revenue']
for col in num_cols:
    df[col] = df[col].astype(str).str.replace(r'[^\d.]', '', regex=True)
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna(subset=['Units_Sold', 'Unit_Price'])

df['Calculated_Revenue'] = df['Units_Sold'] * df['Unit_Price']
mask = df['Revenue'] != df['Calculated_Revenue']

df.loc[mask, 'Revenue'] = df.loc[mask, 'Calculated_Revenue']

df = df.drop(columns=['Calculated_Revenue'])


print("\n============ Sales Clean ============")
print(df.to_string())

print("\n=== Total Sales by Region ===")
region_sales = df.groupby('Region')['Revenue'].sum()
print(region_sales)

print("\n=== Average Revenue by Product ===")
product_avg = df.groupby('Product')['Revenue'].mean()
print(product_avg)

# რეგიონები - სვეტოვანი დიაგრამა
region_sales.plot(kind='bar')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# პროდუქტები - სვეტოვანი დიაგრამა
product_avg.plot(kind='bar')
plt.title('Average Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


