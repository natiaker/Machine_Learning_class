import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# 1. მონაცემების მომზადება (ვიღებთ მხოლოდ 2 კლასს და 2 feature-ს)
iris = datasets.load_iris()
X = iris.data[iris.target < 2][:, :2] # მხოლოდ Setosa და Versicolor, მხოლოდ Sepal length/width
y = iris.target[iris.target < 2]

# 2. მოდელის გაწვრთნა
model = LogisticRegression()
model.fit(X, y)

# 3. Decision Boundary-სთვის "ბადის" შექმნა
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

# 4. პროგნოზი ბადის ყოველი წერტილისთვის
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 5. ვიზუალიზაცია
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu, alpha=0.3) # ფონური ფერები
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.RdYlBu) # თავად ყვავილები
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Logistic Regression: Decision Boundary')
plt.show()

print(f"Accuracy: {model.score(X, y):.4f}")
