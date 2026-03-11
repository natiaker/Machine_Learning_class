import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

# 1. სინთეტიკური მონაცემების შექმნა
np.random.seed(42)
X = 6 * np.random.rand(100, 1) - 3  # X არის [-3, 3] დიაპაზონში
noise = np.random.randn(100, 1)    # შემთხვევითი "ხმაური"
y = 0.5 * X**2 - 2 * X + 3 + noise

# 2. Linear Regression (წრფივი)
lin_reg = LinearRegression()
lin_reg.fit(X, y)
y_pred_lin = lin_reg.predict(X)

# 3. Polynomial Regression (პოლინომიური, degree=2)
# ჯერ გარდავქმნით X-ს: ვამატებთ X^2 სვეტს
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)

poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)
y_pred_poly = poly_reg.predict(X_poly)

# 4. შედეგების შედარება (MSE)
mse_lin = mean_squared_error(y, y_pred_lin)
mse_poly = mean_squared_error(y, y_pred_poly)

print(f"Linear Regression MSE: {mse_lin:.4f}")
print(f"Polynomial Regression MSE: {mse_poly:.4f}")

# 5. ვიზუალიზაცია
plt.scatter(X, y, color='blue', alpha=0.5, label='მონაცემები')

X_new = np.linspace(-3, 3, 100).reshape(-1, 1)
X_new_poly = poly_features.transform(X_new)
y_new_poly = poly_reg.predict(X_new_poly)

plt.plot(X, y_pred_lin, color='red', label='Linear (წრფე)')
plt.plot(X_new, y_new_poly, color='green', linewidth=3, label='Polynomial (მრუდი)')

plt.legend()
plt.title("Linear vs Polynomial Regression")
plt.show()
