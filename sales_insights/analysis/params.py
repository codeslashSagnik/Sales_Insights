

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(),
    'Lasso Regression': Lasso(),
    'Random Forest': RandomForestRegressor(),
    
    'Support Vector Regression': SVR()
}

params = {
    'Linear Regression': {},
    'Ridge Regression': {'alpha': [0.1, 1, 10, 100]},
    
    'Lasso Regression': {'alpha': [0.1, 1, 10, 100]},
    'Random Forest': {'n_estimators': [100, 200], 'max_depth': [None, 10, 20]},
    
    'Support Vector Regression': {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
}
