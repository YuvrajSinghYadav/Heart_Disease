import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
#from sklearn.metrics import accuracy_score


def disease_prediction(inputs):
    data = pd.read_csv('heart.csv')

    scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
    X = scaler.fit_transform(data.drop('target', axis=1))
    Y = data['target']


    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)


    model = LogisticRegression()


    model.fit(x_train, y_train)

    input_numpy_array = np.asarray(inputs)

    input_reshaped = input_numpy_array.reshape(1, -1)

    return model.predict(input_reshaped)
