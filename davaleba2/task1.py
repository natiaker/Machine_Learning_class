import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. მონაცემების ჩატვირთვა
housing = fetch_california_housing()
X = housing.data[:, [0]]  # მხოლოდ MedInc (მედიანური შემოსავალი)
y = housing.target      # სახლების ფასები

# 2. მოდელის შექმნა და გაწვრთნა
model = LinearRegression()
model.fit(X, y)

# 3. პროგნოზირება
y_pred = model.predict(X)

# 4. მეტრიკების გამოთვლა
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"MSE: {mse:.4f}")
print(f"R²: {r2:.4f}")

# 5. ვიზუალიზაცია
plt.scatter(X[:500], y[:500], color='blue', alpha=0.5, label='რეალური')  # პირველი 500 წერტილი
plt.plot(X[:500], y_pred[:500], color='red', linewidth=2, label='პროგნოზი')
plt.xlabel('მედიანური შემოსავალი (MedInc)')
plt.ylabel('სახლის ფასი')
plt.legend()
plt.show()
