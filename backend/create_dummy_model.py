"""Create a small dummy regression model and save to model.pkl
This script matches the expected input schema in app.py:
- Present_Price (float)
- Kms_Driven (int)
- Fuel_Type (str)
- Seller_Type (str)
- Transmission (str)
- Owner (int)
- Car_Age (int)

Run with the project's virtualenv: .venv\Scripts\python create_dummy_model.py
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
import os

np.random.seed(42)

n = 1000
Present_Price = np.round(np.random.uniform(0.5, 20.0, n), 2)
Kms_Driven = np.random.randint(1000, 200000, n)
Fuel_Type = np.random.choice(['Petrol', 'Diesel', 'CNG'], n, p=[0.6, 0.3, 0.1])
Seller_Type = np.random.choice(['Dealer', 'Individual'], n, p=[0.7, 0.3])
Transmission = np.random.choice(['Manual', 'Automatic'], n, p=[0.75, 0.25])
Owner = np.random.choice([0, 1, 3], n, p=[0.8, 0.18, 0.02])
Car_Age = np.random.randint(0, 15, n)

# create a sensible target using a simple formula + noise
price = (
    Present_Price * (0.9 + np.random.normal(0, 0.05, n))
    - (Kms_Driven / 100000.0) * 2.0
    - Car_Age * 0.3
    + (Fuel_Type == 'Diesel') * 0.4
    + (Transmission == 'Automatic') * 0.5
    + np.random.normal(0, 0.5, n)
)
# ensure positive
price = np.clip(price, 0.1, None)

X = pd.DataFrame({
    'Present_Price': Present_Price,
    'Kms_Driven': Kms_Driven,
    'Fuel_Type': Fuel_Type,
    'Seller_Type': Seller_Type,
    'Transmission': Transmission,
    'Owner': Owner,
    'Car_Age': Car_Age,
})

y = price

numeric_features = ['Present_Price', 'Kms_Driven', 'Owner', 'Car_Age']
cat_features = ['Fuel_Type', 'Seller_Type', 'Transmission']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features),
    ]
)

pipeline = Pipeline([
    ('pre', preprocessor),
    ('model', RandomForestRegressor(n_estimators=50, random_state=42)),
])

print('Training dummy model...')
pipeline.fit(X, y)

out_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
joblib.dump(pipeline, out_path)
print(f'Saved dummy model to: {out_path}')
print('Done.')
