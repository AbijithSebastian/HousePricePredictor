import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("house_data.csv")

features = ['Area', 'Bedrooms', 'Age', 'Location']
X = df[features]
y = df['Price']

ct = ColumnTransformer(
    [('encode', OneHotEncoder(drop='first'), ['Location'])],
    remainder='passthrough'
)
X_transformed = ct.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_transformed, y, test_size=0.3, random_state=42
)

poly = PolynomialFeatures(degree=2)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

model = LinearRegression()
model.fit(X_poly_train, y_train)
y_pred = model.predict(X_poly_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R²:", r2_score(y_test, y_pred))

pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(ct, open('preprocessor.pkl', 'wb'))
pickle.dump(poly, open('poly.pkl', 'wb'))

print("Model Trained & Saved ✅")
