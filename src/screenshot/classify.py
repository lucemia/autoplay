from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

import Image
import numpy as np


def load_image(infilename):
    img = Image.open(infilename)
    img.load()
    data = np.asarray(img, dtype="int32")
    return data

clf = DecisionTreeClassifier()

print cross_val_score(clf, data, target)
