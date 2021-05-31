# Netanel Bashan, 323056077, netanebashan12@gmail.com
# Elyasaf Dimant, 204006415, elyasafdi@gmail.com
# -*- coding: utf-8 -*-
"""targil4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ttF4DQHP1gr6v_-yGhu0sOv9An1trMcn

In this homework, we will learn about SKLEARN and a little about how Python deals with files (using Dataframes)
and arrays (numpy) and its graphing library, matplot.
"""

import numpy as np
import pandas as pd
from sklearn import tree  # For decision trees
from sklearn.datasets import load_digits
from sklearn.model_selection import cross_val_score  # For cross validation
import matplotlib.pyplot as plt  # for plotting graphs
from sklearn import datasets  # for datasets
from sklearn.metrics import plot_confusion_matrix
import warnings
warnings.filterwarnings('ignore')

url = 'https://github.com/rosenfa/nn/blob/master/pima-indians-diabetes.csv?raw=true'
iris = datasets.load_iris()
wine = datasets.load_wine()
digits = load_digits()
df = pd.read_csv(url,  header=0, error_bad_lines=False)
X = np.asarray(df.drop('Outcome', 1))  # feature
y = np.asarray(df['Outcome'])  # label

listDA = []
listDP = []
listDR = []
listDF = []

listIA = []
listIP = []
listIR = []
listIF = []

listWA = []
listWP = []
listWR = []
listWF = []

listNA = []
listNP = []
listNR = []
listNF = []

maxD = 0
DD = 0

maxI = 0
DI = 0

maxW = 0
DW = 0

maxN = 0
DN = 0

for i in range(1, 11):
    clf = tree.DecisionTreeClassifier(max_depth=i, criterion='entropy')
    accuracyD = cross_val_score(clf, X, y, scoring='accuracy', cv=10)
    listDA.append(accuracyD.mean())
    precisionD = cross_val_score(clf, X, y, scoring='precision_weighted', cv=10)
    score = precisionD.mean()
    if score > maxD:
        maxD = score
        DD = i
    listDP.append(score)
    recallD = cross_val_score(clf, X, y, scoring='recall_weighted', cv=10)
    listDR.append(recallD.mean())
    f1scoreD = cross_val_score(clf, X, y, scoring='f1_weighted', cv=10)
    listDF.append(f1scoreD.mean())
    print('depth', i,
          'acc', round(accuracyD.mean(), 3),
          'pre', round(precisionD.mean(), 3),
          'f1', round(f1scoreD.mean(), 3),
          'recall', round(recallD.mean(), 3), 'diabetes')

    clf = tree.DecisionTreeClassifier(max_depth=i, criterion='entropy')
    accuracyI = cross_val_score(clf, iris.data, iris.target, scoring='accuracy', cv=10)
    listIA.append(accuracyI.mean())
    precisionI = cross_val_score(clf, iris.data, iris.target, scoring='precision_weighted', cv=10)
    score = precisionI.mean()
    if score > maxI:
        maxI = score
        DI = i
    listIP.append(score)
    recallI = cross_val_score(clf, iris.data, iris.target, scoring='recall_weighted', cv=10)
    listIR.append(recallI.mean())
    f1scoreI = cross_val_score(clf, iris.data, iris.target, scoring='f1_weighted', cv=10)
    listIF.append(f1scoreI.mean())
    print('depth', i,
          'acc', round(accuracyI.mean(), 3),
          'pre', round(precisionI.mean(), 3),
          'f1', round(f1scoreI.mean(), 3),
          'recall', round(recallI.mean(), 3), 'iris')

    clf = tree.DecisionTreeClassifier(max_depth=i, criterion='entropy')
    accuracyW = cross_val_score(clf, wine.data, wine.target, scoring='accuracy', cv=10)
    listWA.append(accuracyI.mean())
    precisionW = cross_val_score(clf, wine.data, wine.target, scoring='precision_weighted', cv=10)
    score = precisionW.mean()
    if score > maxW:
        maxW = score
        DW = i
    listWP.append(score)
    recallW = cross_val_score(clf, wine.data, wine.target, scoring='recall_weighted', cv=10)
    listWR.append(recallW.mean())
    f1scoreW = cross_val_score(clf, wine.data, wine.target, scoring='f1_weighted', cv=10)
    listWF.append(f1scoreW.mean())

    clf = tree.DecisionTreeClassifier(max_depth=i, criterion='entropy')
    accuracyN = cross_val_score(clf, digits.data, digits.target, scoring='accuracy', cv=10)
    listNA.append(accuracyN.mean())
    precisionN = cross_val_score(clf, digits.data, digits.target, scoring='precision_weighted', cv=10)
    score = precisionN.mean()
    if score > maxN:
        maxN = score
        DN = i
    listNP.append(score)
    recallN = cross_val_score(clf, digits.data, digits.target, scoring='recall_weighted', cv=10)
    listNR.append(recallN.mean())
    f1scoreN = cross_val_score(clf, digits.data, digits.target, scoring='f1_weighted', cv=10)
    listNF.append(f1scoreN.mean())


X = range(1, 11)
plt.plot(X, listDA, label='acc')
plt.plot(X, listDP, label='pre')
plt.plot(X, listDR, label='rec')
plt.plot(X, listDF, label='f1')
plt.title("diabetes")
plt.xlabel("Depth")
plt.ylabel("Score pre/acc/rec/f1")
plt.legend()
plt.show()

X = range(1, 11)
plt.plot(X, listIA, label='acc')
plt.plot(X, listIP, label='pre')
plt.plot(X, listIR, label='rec')
plt.plot(X, listIF, label='f1')
plt.title("iris")
plt.xlabel("Depth")
plt.ylabel("Score pre/acc/rec/f1")
plt.legend()
plt.show()


X = range(1, 11)
plt.plot(X, listWA, label='acc')
plt.plot(X, listWP, label='pre')
plt.plot(X, listWR, label='rec')
plt.plot(X, listWF, label='f1')
plt.title("wine")
plt.xlabel("Depth")
plt.ylabel("Score pre/acc/rec/f1")
plt.legend()
plt.show()

X = range(1, 11)
plt.plot(X, listNA, label='acc')
plt.plot(X, listNP, label='pre')
plt.plot(X, listNR, label='rec')
plt.plot(X, listNF, label='f1')
plt.title("digits")
plt.xlabel("Depth")
plt.ylabel("Score pre/acc/rec/f1")
plt.legend()
plt.show()


print("diabetes: \nmax value:", round(maxD, 3), "\ndepth:", round(DD, 3))
print("Iris: \nmax value:", round(maxI, 3), "\ndepth:", round(DI, 3))
print("Wine: \nmax value:", round(maxW, 3), "\ndepth:", round(DW, 3))
print("Digits: \nmax value:", round(maxN, 3), "\ndepth:", round(DN, 3))


"""A confusion matrix for the data..."""

class_names = iris.target_names
clf.max_depth = 2
clf = clf.fit(iris.data, iris.target)
titles_options = ["Confusion matrix"]
for title in titles_options:
    disp = plot_confusion_matrix(clf, iris.data, iris.target,
                                 display_labels=class_names,
                                 cmap=plt.cm.Blues)
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)

plt.show()
