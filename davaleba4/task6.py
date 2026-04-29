# 1.	გამოიყენეთ library_borrowing_dirty.xlsx ფაილი. ბიბლიოთეკის სესხების ფაილში გაასუფთავეთ Book_Category,
# Days_Overdue, Fine_GEL, Member_Type და Returned სვეტები, გაასწორეთ კატეგორიებისა და წევრის ტიპის არაერთგვაროვანი
# ჩანაწერები, იპოვეთ უარყოფითი ან ცარიელი ვადაგადაცილებები და ჯარიმები, შეამოწმეთ კავშირი Days_Overdue-სა და Fine_GEL-ს
# შორის, შემდეგ pandas-ით გამოთვალეთ ყველაზე მოთხოვნადი კატეგორიები, წევრის ტიპების მიხედვით სესხებების რაოდენობა და
# საშუალო ჯარიმა, ხოლო matplotlib-ით ააგეთ კატეგორიების მიხედვით სესხებების სვეტოვანი დიაგრამა და ვადაგადაცილების
# დღეების ჰისტოგრამა.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data/library_borrowing_dirty.xlsx', header=2)
print(df.to_string())

df['Book_Category'] = df['Book_Category'].astype(str).str.strip().str.title()
df['Member_Type'] = df['Member_Type'].astype(str).str.strip().str.title()
df['Returned'] = df['Returned'].astype(str).str.strip().str.lower()

# ვაქცევთ რიცხვებად, ხოლო შეცდომებსა და ცარიელ უჯრებს - 0-ად
df['Days_Overdue'] = pd.to_numeric(df['Days_Overdue'], errors='coerce').fillna(0)
df['Fine_GEL'] = pd.to_numeric(df['Fine_GEL'], errors='coerce').fillna(0)

# უარყოფითი მნიშვნელობების გასწორება (ვაქცევთ 0-ად, რადგან ვადაგადაცილება ვერ იქნება უარყოფითი)
df.loc[df['Days_Overdue'] < 0, 'Days_Overdue'] = 0


top_categories = df['Book_Category'].value_counts()

member_stats = df.groupby('Member_Type').agg({
    'Book_Category': 'count',
    'Fine_GEL': 'mean'
}).rename(columns={'Book_Category': 'Borrowing_Count', 'Fine_GEL': 'Avg_Fine'})

print("--- ყველაზე მოთხოვნადი კატეგორიები ---")
print(top_categories.head(5))
print("\n--- სტატისტიკა წევრის ტიპის მიხედვით ---")
print(member_stats)

# კავშირი Days_Overdue-სა და Fine_GEL-ს შორის
correlation = df['Days_Overdue'].corr(df['Fine_GEL'])
print(f"\nვადაგადაცილების დღეებსა და ჯარიმას შორის კორელაცია: {correlation:.2f}")

# 4. ვიზუალიზაცია
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# სვეტოვანი დიაგრამა: კატეგორიები
top_categories.plot(kind='bar', ax=axes[0], color='skyblue', edgecolor='black')
axes[0].set_title('სესხებები კატეგორიების მიხედვით')
axes[0].set_ylabel('რაოდენობა')

# ჰისტოგრამა: ვადაგადაცილების დღეები
df[df['Days_Overdue'] > 0]['Days_Overdue'].plot(kind='hist', ax=axes[1], bins=20, color='salmon', edgecolor='black')
axes[1].set_title('ვადაგადაცილების დღეების განაწილება')
axes[1].set_xlabel('დღეები')

# სკატერ პლოტი: კავშირი ჯარიმასა და დღეებს შორის
axes[2].scatter(df['Days_Overdue'], df['Fine_GEL'], alpha=0.5, color='green')
axes[2].set_title('ვადაგადაცილება vs ჯარიმა')
axes[2].set_xlabel('დღეები')
axes[2].set_ylabel('ჯარიმა (GEL)')

plt.tight_layout()
plt.show()


