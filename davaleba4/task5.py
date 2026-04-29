# 5.	გამოიყენეთ air_quality_dirty.xlsx ფაილი. ჰაერის ხარისხის ფაილში გაასუფთავეთ PM2.5, PM10, Temperature, Humidity
# და AQI_Category სვეტები, იპოვეთ გამოტოვებული და არარეალური მნიშვნელობები, მაგალითად უარყოფითი დაბინძურების მაჩვენებლები
# ან 100%-ზე მეტი ტენიანობა, მოაწესრიგეთ კატეგორიების სახელები, შემდეგ pandas-ით გამოთვალეთ სადგურების მიხედვით საშუალო
# PM2.5 და PM10, იპოვეთ ყველაზე დაბინძურებული დღეები და სადგურები, ხოლო matplotlib-ით ააგეთ დროის მიხედვით PM2.5-ის
# ხაზოვანი გრაფიკი და სადგურების მიხედვით საშუალო დაბინძურების სვეტოვანი დიაგრამა.


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data/air_quality_dirty.xlsx', header=2)
print(df.to_string())

cols_to_numeric = ['PM2.5', 'PM10', 'Temperature', 'Humidity']
for col in cols_to_numeric:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# არარეალური მნიშვნელობების გაფილტვრა
# PM2.5 და PM10 უნდა იყოს 0-ზე მეტი; Humidity უნდა იყოს 0-დან 100-მდე
df = df[(df['PM2.5'] >= 0) & (df['PM10'] >= 0)]
df = df[(df['Humidity'] >= 0) & (df['Humidity'] <= 100)]

df['AQI_Category'] = df['AQI_Category'].astype(str).str.strip().str.title()

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])


station_stats = df.groupby('Station')[['PM2.5', 'PM10']].mean()
most_polluted_days = df.sort_values(by='PM2.5', ascending=False).head(5)

print("--- საშუალო მაჩვენებლები სადგურების მიხედვით ---")
print(station_stats)
print("\n--- ყველაზე დაბინძურებული 5 დღე ---")
print(most_polluted_days[['Date', 'Station', 'PM2.5']])


plt.figure(figsize=(12, 6))
# დავაჯგუფოთ დღეების მიხედვით საშუალო მნიშვნელობისთვის
daily_pm25 = df.groupby('Date')['PM2.5'].mean()
daily_pm25.plot(kind='line', marker='o', color='red')
plt.title('PM2.5 კონცენტრაციის ცვლილება დროის მიხედვით')
plt.xlabel('თარიღი')
plt.ylabel('PM2.5 (avg)')
plt.grid(True)
plt.show()

# სადგურების მიხედვით საშუალო დაბინძურების სვეტოვანი დიაგრამა
station_stats.plot(kind='bar', figsize=(10, 6))
plt.title('საშუალო დაბინძურება სადგურების მიხედვით')
plt.ylabel('კონცენტრაცია')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

