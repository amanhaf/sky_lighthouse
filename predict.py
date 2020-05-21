import pandas as pd
import os, pickle


def predict(name):
    
    test = pd.read_csv(name)
    pkl_filename = "pickle_model.pkl"

    features = [i for i in test.columns]
    X_test = test[features]

    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)

    #predictions using our Logisitic Regression model
    predictions_final = pickle_model.predict(X_test)
    str = ''.join(predictions_final)
    return str
