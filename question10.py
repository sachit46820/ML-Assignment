import numpy as np #imported numy as np
import pandas as pd #imported pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) # here for training i took train and test for testing
#k=3  I develop two classifiers with k value of 3 to demonstrate the relevance of the k value
from sklearn.metrics import accuracy_score
knn3 = KNeighborsClassifier(n_neighbors = 3)
knn3.fit(X_train, y_train)
y_pred_3 = knn3.predict(X_test)
print("Accuracy with k=3", accuracy_score(y_test, y_pred_3)*100)
