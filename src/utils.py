import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            model_name = list(models.keys())[i]
            para = params[list(models.keys())[i]]
            if len(para) > 0:
                gs = GridSearchCV(model, para, cv=3)
                gs.fit(X_train, y_train)
                model.set_params(**gs.best_params_)

            logging.info(f'Training the model: {model_name}')
            model.fit(X_train, y_train)
            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)
            report[model_name] = test_model_score
            logging.info(f'{model_name} model score: {test_model_score}')
        return report
    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)