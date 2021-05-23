# -*- coding: utf-8 -*-
"""targil4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ttF4DQHP1gr6v_-yGhu0sOv9An1trMcn

In this homework, we will learn about SKLEARN and a little about how Python deals with files (using Dataframes) and arrays (numpy) and its graphing library, matplot.
"""

import numpy as np
import pandas as pd
from sklearn import tree #For decision trees
from sklearn.datasets import load_digits
from sklearn.model_selection import cross_val_score #For cross validation
import matplotlib.pyplot as plt #for plotting graphs
from sklearn import datasets #for datasets
from sklearn.metrics import plot_confusion_matrix, recall_score

url = 'https://github.com/rosenfa/nn/blob/master/pima-indians-diabetes.csv?raw=true'
iris = datasets.load_iris()
wine = datasets.load_wine()
digits = load_digits()
df=pd.read_csv(url,  header=0, error_bad_lines=False) 
X = np.asarray(df.drop('Outcome',1))#feature
y = np.asarray(df['Outcome'])#label

listDA = []
listDP = []

listIA = []
listIP = []

listWA = []
listWP = []

listNA = []
listNP = []

maxD = 0
DD = 0
maxI = 0
DI = 0
maxW = 0
DW = 0
maxN = 0
DN = 0

for i in range(1,11):
    clf = tree.DecisionTreeClassifier(max_depth=i)
    accuracyD = cross_val_score(clf, X, y, scoring='accuracy', cv=10)
    listDA.append(accuracyD.mean())
    # y_true = df[:-1]
    # X = df.data
    # y = df.target
    # clf.fit(X,y)
    # y_pred = clf.predict(df.to_numpy().data[:-1])
    # recall_score(y_true,y_pred)
    precisionD = cross_val_score(clf, X,y, scoring='precision_weighted', cv=10)
    score = precisionD.mean()
    if score > maxD:
        maxD = score
        DD = i
    listDP.append(score)

    clf = tree.DecisionTreeClassifier(max_depth = i,criterion = 'entropy')
    accuracyI = cross_val_score(clf, iris.data, iris.target, scoring='accuracy', cv=10)
    listIA.append(accuracyI.mean())
    precisionI = cross_val_score(clf, iris.data, iris.target, scoring='precision_weighted', cv=10)
    # X = iris.data
    # y = iris.target
    # clf.fit(X,y)
    # y_pred = clf.predict(iris.data[:-1])
    # recall_score(y,y_pred)
    score = precisionI.mean()
    if score > maxI:
        maxI = score
        DI = i
    listIP.append(score)

    clf = tree.DecisionTreeClassifier(max_depth=i, criterion='entropy')
    accuracyI = cross_val_score(clf, wine.data, wine.target, scoring='accuracy', cv=10)
    listWA.append(accuracyI.mean())
    precisionW = cross_val_score(clf, wine.data, wine.target, scoring='precision_weighted', cv=10)
    score = precisionW.mean()
    if score > maxW:
        maxW = score
        DW = i
    listWP.append(score)

    clf = tree.DecisionTreeClassifier(max_depth=i, criterion='entropy')
    accuracyI = cross_val_score(clf, digits.data, digits.target, scoring='accuracy', cv=10)
    listNA.append(accuracyI.mean())
    precisionN = cross_val_score(clf, digits.data, digits.target, scoring='precision_weighted', cv=10)
    score = precisionN.mean()
    if score > maxN:
        maxN = score
        DN = i
    listNP.append(score)


X = range(1, 11)
plt.plot(X, listDA,label = 'acc')
plt.plot(X, listDP,label = 'pre')
plt.title("diabetes")
plt.xlabel("Depth")
plt.ylabel("Score pre/acc")
plt.legend()
plt.show()

X = range(1, 11)
plt.plot(X, listIA,label = 'acc')
plt.plot(X, listIP,label = 'pre')
plt.title("iris")
plt.xlabel("Depth")
plt.ylabel("Score pre/acc")
plt.legend()
plt.show()


X = range(1, 11)
plt.plot(X, listWA,label = 'acc')
plt.plot(X, listWP,label = 'pre')
plt.title("wine")
plt.xlabel("Depth")
plt.ylabel("Score pre/acc")
plt.legend()
plt.show()

X = range(1, 11)
plt.plot(X, listNA,label = 'acc')
plt.plot(X, listNP,label = 'pre')
plt.title("digits")
plt.xlabel("Depth")
plt.ylabel("Score pre/acc")
plt.legend()
plt.show()


print("diabetes: \nmax value:", maxD,"\ndepth:" ,DD)
print("Iris: \nmax value:", maxI,"\ndepth:" ,DI)
print("Wine: \nmax value:", maxW,"\ndepth:" ,DW)
print("Digits: \nmax value:", maxN,"\ndepth:" ,DN)



# X = range(10)
# plt.plot(X, [x * x for x in X])
# plt.xlabel("This is the X axis")
# plt.ylabel("This is the Y axis")
# plt.show()


"""A confusion matrix for the data..."""

class_names = iris.target_names
clf.max_depth = 2
clf = clf.fit(iris.data, iris.target)
titles_options = [("Confusion matrix")]
for title in titles_options:
    disp = plot_confusion_matrix(clf, iris.data, iris.target,
                                 display_labels=class_names,
                                 cmap=plt.cm.Blues)
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)

plt.show()

"""Hint for how to plot the results:"""

# elyasaf


