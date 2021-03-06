# BLS demo

import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from broadLearning_oneShot import BroadNet

# Load and process dataset
mat = pd.read_csv('stock.csv')
X = mat.values[:, :-1]
y = mat.values[:, -1].reshape(-1, 1)
y[y=='P'] = 1
y[y=='N'] = 2
y = y.astype(int)

# split the dataset
x_train, x_test, y_train, y_test = train_test_split(X, y)

# train and test
C = 2**(-10)
bls = BroadNet(20, 20, 300, C)
init_time = time.time()
bls.make_model(x_train, y_train)
training_time = time.time()-init_time
y_pre = bls.forward(x_test)
accuracy = accuracy_score(y_pre, y_test)
print('The training time is {} s, and the test accuracy is {}'.format(training_time, accuracy))
