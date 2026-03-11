from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1.მონაცემების შემოტანა
housing = fetch_california_housing()
X_multi = housing.data
y = housing.target

# 2. მოდელის შექმნა
model = LinearRegression()
model.fit(X_multi, y)

# 3. პროგნოზირება და მეტრიკები
y_pred_multi = model.predict(X_multi)

mse_multi = mean_squared_error(y, y_pred_multi)
r2_multi = r2_score(y, y_pred_multi)

print(f"MSE: {mse_multi:.4f}")
print(f"R²: {r2_multi:.4f}")

# წინა შემთხვევაში R² იყო 0.4734, ახლა 0.6062 გადასცდა. ეს ნიშნავს, რომ დამატებითმა
# ინფორმაციამ (ოთახების რაოდენობა, მდებარეობა) მოდელი საგრძნობლად გააუმჯობესა!
# MSE შემცირდა ანუ შემცირდა შეცდომებიც და მოდელი უფრო ზუსტია.