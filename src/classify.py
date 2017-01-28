import cv2
from sklearn import svm
import os
import scipy
import numpy as np
from sklearn import tree
from sklearn.model_selection import cross_val_score

features = None
targets = None

for label in os.listdir('./classify'):
    if not os.path.isdir('./classify/%s' % label):
        continue

    files = os.listdir('./classify/%s' % label)

    for f in files:
        if not f.endswith('.png'):
            continue

        img = cv2.imread('./classify/%s/%s' % (label, f))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        resize = cv2.resize(img, (75, 128))
        feature = resize.ravel()
        feature = feature[..., np.newaxis]
        target = [label]

        if targets is None:
            targets = target
        else:
            targets = np.hstack((targets, target))

        if features is None:
            features = feature

        else:
            features = np.hstack((features, feature))
        print features.shape

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features.T, targets)
# print cross_val_score(clf, features.T, targets, cv=10)

P = clf.predict(features.T)

for a, b in zip(P, targets):
    print a, b
