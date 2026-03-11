from sklearn.linear_model import Ridge, Lasso, LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error

# 1. მონაცემების მომზადება
housing = fetch_california_housing()
X, y = housing.data, housing.target

# 2. სამივე მოდელის შექმნა
lin_reg = LinearRegression()
ridge_reg = Ridge(alpha=1.0) # alpha არის "ჯარიმის" სიმძლავრე
lasso_reg = Lasso(alpha=1.0)

# 3. გაწვრთნა
lin_reg.fit(X, y)
ridge_reg.fit(X, y)
lasso_reg.fit(X, y)

# 4. შედეგების შედარება
print(f"Linear MSE: {mean_squared_error(y, lin_reg.predict(X)):.4f}")
print(f"Ridge MSE:  {mean_squared_error(y, ridge_reg.predict(X)):.4f}")
print(f"Lasso MSE:  {mean_squared_error(y, lasso_reg.predict(X)):.4f}")

# 5. ვნახოთ Lasso-ს კოეფიციენტები (რამდენი "გაანულა")
print("\nLasso-ს კოეფიციენტები:")
for name, coef in zip(housing.feature_names, lasso_reg.coef_):
    print(f"{name}: {coef:.4f}")
