from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.datasets import fetch_california_housing

# 1. მონაცემების ჩატვირთვა
housing = fetch_california_housing()
X, y = housing.data, housing.target

# 2. მონაცემების გაყოფა (80% სასწავლო, 20% საგამოცდო)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. მოდელის გაწვრთნა მხოლოდ Train მონაცემებზე
model = LinearRegression()
model.fit(X_train, y_train)

# 4. პროგნოზი ორივე ჯგუფისთვის
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# 5. შეცდომების შედარება
print(f"Train MSE: {mean_squared_error(y_train, y_train_pred):.4f}")
print(f"Test MSE:  {mean_squared_error(y_test, y_test_pred):.4f}")
