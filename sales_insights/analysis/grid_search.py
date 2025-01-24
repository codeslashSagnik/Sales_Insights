

import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from params import models, params

def tune_models(X_train, y_train):
    results = []

    for model_name, model in models.items():
        grid_search = GridSearchCV(estimator=model, param_grid=params[model_name], cv=5, n_jobs=-1, scoring='neg_mean_squared_error')
        grid_search.fit(X_train, y_train)
        best_params = grid_search.best_params_
        best_score = grid_search.best_score_

        results.append({
            'Model': model_name,
            'Best Parameters': best_params,
            'Best Score (MSE)': best_score
        })

    return pd.DataFrame(results)

