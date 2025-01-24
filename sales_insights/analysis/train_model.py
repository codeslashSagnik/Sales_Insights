import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_squared_error

import pickle

data = pd.read_csv('./csv_data/modelling_ready_sales_data.csv')

X = data[['price_per_unit', 'units_sold', 'month']]
y = data['total_revenue']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(max_depth=20, n_estimators=200, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Model MSE: {mse}")



with open('./models/random_forest_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved successfully!")
