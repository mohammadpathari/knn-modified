# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:33:52 2021

@author: DANILO
"""

import numpy as np
from pl_nn.pl_nn_original import PlNearestNeighbors
from pl_nn.pl_nn_modified import PlNearestNeighborsModified


def calculate_accuracy(y_true, y_pred):
    return sum(y_pred == y_true) / len(y_true)


###############################################################################
# Loading the data
data = np.loadtxt('data/wine.txt', delimiter=',', dtype=float)
X = data[:, 1:].astype(float)
y = data[:, 0].astype(int)
###############################################################################

###############################################################################
# Split the data into train (80%) and test (20%)
random_list = list(range(X.shape[0]))
np.random.seed(5)  # Using a fixed seed value to make the test reproducible
np.random.shuffle(random_list)

train_idx = random_list[0:round(len(random_list) * 0.75)]
test_idx = random_list[0:round(len(random_list) * 0.25)]

X_train, y_train = X[train_idx, :], y[train_idx]
X_test, y_test = X[test_idx, :], y[test_idx]
###############################################################################

###############################################################################
# Scaling the data according to a normal distribution
X_train_sc = (X_train - np.mean(X_train, axis=0)) / np.std(X_train, axis=0)
X_test_sc = (X_test - np.mean(X_test, axis=0)) / np.std(X_test, axis=0)
###############################################################################

angle_thresholds = [30, 45, 60, 75, 105, 120, 135, 150]

print('')

for angle in angle_thresholds:
    ###############################################################################
    # Training
    plnn = PlNearestNeighbors()
    plnn_test = PlNearestNeighborsModified(
        angle_threshold=angle  # Setting different angle thresholds
    )

    plnn.fit(X_train_sc, y_train)
    plnn_test.fit(X_train_sc, y_train)
    ###############################################################################

    ###############################################################################
    # Performing predictions
    y_pred = plnn.predict(X_test_sc)
    y_pred_test = plnn_test.predict(X_test_sc)
    ###############################################################################

    ###############################################################################
    # Computing accuracies
    y_test = y_test.reshape(-1, 1)
    print(f'Angle -> 90 | Accuracy PL-NN: {calculate_accuracy(y_test, y_pred)}')
    print(f'Angle -> {angle} | Accuracy PL-NN-Modified: {calculate_accuracy(y_test, y_pred_test)}')
    print('')
    ###############################################################################
