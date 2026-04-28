#2.	გამოიყენეთ student_performance_dirty.xlsx ფაილი. სტუდენტების მონაცემების ფაილში გაასუფთავეთ Hours_Study, Attendance,
# Assignments, Midterm, Final_Score და Passed სვეტები, გამოავლინეთ არასწორი მნიშვნელობები, მაგალითად ტექსტური ჩანაწერები
# რიცხვით სვეტებში, 100-ზე მეტი ან უარყოფითი ნიშნები, და გაასწორეთ ან გაფილტრეთ ისინი, შემდეგ pandas-ით გამოთვალეთ
# საშუალო ქულა, ჩაჭრილთა და გასულთა რაოდენობა, კორელაცია Hours_Study-სა და Final_Score-ს შორის, ხოლო matplotlib-ით
# ააგეთ გაფანტვის დიაგრამა Hours_Study და Final_Score სვეტებისთვის და ჰისტოგრამა საბოლოო ქულების განაწილებისთვის.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data/student_performance_dirty.xlsx', header=2)
print(df.to_string())


df['Passed'] = df['Passed'].astype(str).str.strip().str.lower()

num_cols = ['Hours_Study', 'Attendance', 'Assignments', 'Midterm', 'Final_Score']
for col in num_cols:
    df[col] = df[col].astype(str).str.replace(r'[^\d.]', '', regex=True)
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 100ზე მეტი ან უარყოფითი ნიშნები
for col in ['Attendance', 'Assignments', 'Midterm', 'Final_Score']:
    df.loc[(df[col] > 100) | (df[col] < 0), col] = None

# Hours_Study არ უნდა იყოს უარყოფითი
df.loc[df['Hours_Study'] < 0, 'Hours_Study'] = None

# დავამუშავოთ Noneები
df = df.dropna(subset=['Final_Score'])

print('\n', df.to_string())

# საშუალო ქულა
avg_score = df['Final_Score'].mean()

# Passed / Failed
passed_count = (df['Passed'] == 'yes').sum()
failed_count = (df['Passed'] == 'no').sum()

# კორელაცია
correlation = df['Hours_Study'].corr(df['Final_Score'])

print("\nAverage Final Score:", avg_score)
print("Passed:", passed_count)
print("Failed:", failed_count)
print("Correlation:", correlation)

# scatter
plt.figure()
plt.scatter(df['Hours_Study'], df['Final_Score'])
plt.xlabel("Hours Study")
plt.ylabel("Final Score")
plt.title("Hours Study vs Final Score")
plt.show()

# histogram
plt.figure()
plt.hist(df['Final_Score'], bins=10)
plt.xlabel("Final Score")
plt.ylabel("Frequency")
plt.title("Final Score Distribution")
plt.show()

