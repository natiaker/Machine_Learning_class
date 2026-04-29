# 4. გამოიყენეთ employee_attendance_dirty.xlsx ფაილი. თანამშრომელთა დასწრების ფაილში
# გაასუფთავეთ Department, Check_In, Check_Out, Hours_Worked და Status სვეტები, გაასწორეთ
# არაერთგვაროვანი სახელები, დროის ფორმატები და სტატუსები, იპოვეთ ცარიელი ან ლოგიკურად შეუსაბამო
# ჩანაწერები, საჭიროების შემთხვევაში გამოთვალეთ Hours_Worked დროის სხვაობით, შემდეგ pandas-ით დათვალეთ
# თითოეული დეპარტამენტის საშუალო ნამუშევარი საათები, დაგვიანებების რაოდენობა და დასწრების სტატისტიკა,
# ხოლო matplotlib-ით ააგეთ დეპარტამენტების მიხედვით საშუალო სამუშაო საათების სვეტოვანი დიაგრამა და
# სტატუსების განაწილების დიაგრამა.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data/employee_attendance_dirty.xlsx', header=2)
print(df.to_string())

df['Department'] = df['Department'].astype(str).str.strip().str.title()
df['Status'] = df['Status'].astype(str).str.strip().str.title()

df['Check_In'] = pd.to_datetime(df['Check_In'], format='mixed', errors='coerce')
df['Check_Out'] = pd.to_datetime(df['Check_Out'], format='mixed', errors='coerce')

# წავშალოთ ის ჩანაწერები, სადაც დრო არასწორია ან ცარიელია
df = df.dropna(subset=['Check_In', 'Check_Out'])
df = df[df['Check_Out'] > df['Check_In']]

# Hours_Worked
df['Hours_Worked'] = (df['Check_Out'] - df['Check_In']).dt.total_seconds() / 3600

avg_hours_dept = df.groupby('Department')['Hours_Worked'].mean()
latencies_count = df[df['Status'] == 'Late'].groupby('Department').size()

print("--- საშუალო სამუშაო საათები ---")
print(avg_hours_dept)
print("\n--- დაგვიანებების რაოდენობა ---")
print(latencies_count)

# სვეტოვანი დიაგრამა: საშუალო სამუშაო საათები
plt.figure(figsize=(10, 6))
avg_hours_dept.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('დეპარტამენტების მიხედვით საშუალო სამუშაო საათები')
plt.xlabel('დეპარტამენტი')
plt.ylabel('საათების საშუალო რაოდენობა')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# წრიული დიაგრამა: სტატუსების განაწილება
plt.figure(figsize=(8, 8))
df['Status'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['#ff9999', '#66b3ff', '#99ff99'])
plt.title('თანამშრომელთა სტატუსების განაწილება')
plt.show()

