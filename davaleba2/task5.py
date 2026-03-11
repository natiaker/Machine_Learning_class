import matplotlib
matplotlib.use('TkAgg')
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# 1. მონაცემების ჩატვირთვა
cancer = load_breast_cancer()
X, y = cancer.data, cancer.target

# 2. მოდელის შექმნა (max_iter ვზრდით, რომ მოდელმა მოასწროს "ფიქრი")
model = LogisticRegression(max_iter=10000)
model.fit(X, y)

# 3. პროგნოზი
y_pred = model.predict(X)

# 4. მეტრიკები
acc = accuracy_score(y, y_pred)
prec = precision_score(y, y_pred)
rec = recall_score(y, y_pred)
cm = confusion_matrix(y, y_pred)

print(f"Accuracy: {acc:.4f}")
print(f"Precision: {prec:.4f}")
print(f"Recall: {rec:.4f}")

# 5. Confusion Matrix-ის ვიზუალიზაცია
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('პროგნოზი')
plt.ylabel('რეალობა')
plt.title('Confusion Matrix')
plt.show()
