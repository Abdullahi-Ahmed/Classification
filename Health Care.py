import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv(r"C:\Users\mourinho\Downloads\Project_2\Project 2\Healthcare - Diabetes\health care diabetes.csv")


Target = data['Outcome']
features = x = data.drop(['Outcome'], axis=1)

for col in features.columns:
    val = features[col].mean()
    features[col] = features[col].replace(0, val)

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import time
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

x_train, x_test, y_train, y_test = train_test_split(features,Target, test_size = 0.2, random_state = 42)

estimators = {
    "DecisionTreeRegressor": DecisionTreeRegressor(),
    "SVR": SVC(),
    'KNN':KNeighborsClassifier(n_neighbors=3),
    "LogisticRegressor": LogisticRegression(),
}

data_models = pd.DataFrame(columns=['model', 'run_time', 'roc_auc_score', 'Accuracy'])

for key in estimators:
    print('*', key)

    start_time = time.time()

    estimator = estimators[key]
    model = estimator.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    scores = cross_val_score(model,
                             x_train,
                             y_train,
                             scoring="neg_mean_squared_error",
                             cv=10)

    row = {'model': key,
           'run_time': format(round((time.time() - start_time) / 60, 2)),
           'roc_auc_score': round(metrics.roc_auc_score(y_test, y_pred)),
           'Accuracy': (metrics.accuracy_score(y_test, y_pred))

           }

    data_models = data_models.append(row, ignore_index=True)

data_models.head(20).sort_values(by='Accuracy', ascending=False)


hyperparameters = dict(leaf_size=list(range(1,50)),
                       n_neighbors=list(range(1,30)),
                       p=[1,2])
KNN = KNeighborsClassifier()

clf = GridSearchCV(KNN, hyperparameters, cv=5)

best_model = clf.fit(features,Target)


print('Best leaf_size:', best_model.best_estimator_.get_params()['leaf_size'])
print('Best p:', best_model.best_estimator_.get_params()['p'])
print('Best n_neighbors:', best_model.best_estimator_.get_params()['n_neighbors'])
