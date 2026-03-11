import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

# 1. მონაცემების ჩატვირთვა
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target
feature_names = diabetes.feature_names

# 2. მრავალჯერადი რეგრესიის აგება
model_diabetes = LinearRegression()
model_diabetes.fit(X, y)

# 3. კოეფიციენტების ამოღება და ცხრილში განლაგება
# კოეფიციენტი გვიჩვენებს, რამდენად ძლიერია კავშირი feature-სა და მიზნობრივ ცვლადს შორის
df_importance = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': model_diabetes.coef_
})

# დავალაგოთ აბსოლუტური მნიშვნელობით, რომ დავინახოთ ყველაზე დიდი გავლენა
df_importance['Abs_Coefficient'] = df_importance['Coefficient'].abs()
df_importance = df_importance.sort_values(by='Abs_Coefficient', ascending=False)

print("ფაქტორების გავლენა დიაბეტზე:")
print(df_importance[['Feature', 'Coefficient']])