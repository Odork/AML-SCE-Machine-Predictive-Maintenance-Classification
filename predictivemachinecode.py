# -*- coding: utf-8 -*-
"""cspro.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bsgZSltV6n0I0CujmD4jxSUxo1-2cE55
"""

!pip install scikit-learn==1.3.0

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/csv files/predictive_maintenance.csv")

df.head()

df.info()

df['Type'].nunique()

df.isnull().sum()

df[df['Target']==1]

X = df.iloc[:,2:8]
y = df.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)
y_train.shape

from sklearn.preprocessing import OrdinalEncoder
oe = OrdinalEncoder(categories=[['L', 'M', 'H']])
oe.fit(X_train[['Type']])
X_train['Type'] = oe.transform(X_train[['Type']]).astype(int)
X_test['Type'] = oe.transform(X_test[['Type']]).astype(int)

X_train.head()

from sklearn.preprocessing import LabelEncoder
categories = ['No Failure', 'Heat Dissipation Failure', 'Power Failure', 'Overstrain Failure', 'Tool Wear Failure', 'Random Failures']
custom_encoder = {cat: i for i, cat in enumerate(categories)}
y_train_encoded = [custom_encoder.get(cat, len(categories)) for cat in y_train]
y_test_encoded = [custom_encoder.get(cat, len(categories)) for cat in y_test]
le = LabelEncoder()
le.fit(list(custom_encoder.values()))
y_train = le.transform(y_train_encoded)
y_test = le.transform(y_test_encoded)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

clf = LogisticRegression(solver='lbfgs', max_iter=10000)
clf.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = clf.predict(X_test)

log_train = round(clf.score(X_train, y_train) * 100, 2)
log_accuracy = round(accuracy_score(y_pred, y_test) * 100, 2)


print("Training Accuracy    :",log_train ,"%")
print("Model Accuracy Score :",log_accuracy ,"%")
print("\033[1m--------------------------------------------------------\033[0m")
print("Classification_Report: \n",classification_report(y_test,y_pred))
print("\033[1m--------------------------------------------------------\033[0m")

# Decision Tree
from sklearn.tree import DecisionTreeClassifier
decision = DecisionTreeClassifier()
decision.fit(X_train, y_train)
y_pred_dec = decision.predict(X_test)

decision_train = round(decision.score(X_train, y_train) * 100, 2)
decision_accuracy = round(accuracy_score(y_pred_dec, y_test) * 100, 2)

print("Training Accuracy    :",decision_train ,"%")
print("Model Accuracy Score :",decision_accuracy ,"%")
print("\033[1m--------------------------------------------------------\033[0m")
print("Classification_Report: \n",classification_report(y_test,y_pred_dec))
print("\033[1m--------------------------------------------------------\033[0m")

# Random Forest
from sklearn.ensemble import RandomForestClassifier
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, y_train)
y_pred_rf = random_forest.predict(X_test)
random_forest.score(X_train, y_train)

random_forest_train = round(random_forest.score(X_train, y_train) * 100, 2)
random_forest_accuracy = round(accuracy_score(y_pred_rf, y_test) * 100, 2)

print("Training Accuracy    :",random_forest_train ,"%")
print("Model Accuracy Score :",random_forest_accuracy ,"%")
print("\033[1m--------------------------------------------------------\033[0m")
print("Classification_Report: \n",classification_report(y_test,y_pred_rf))
print("\033[1m--------------------------------------------------------\033[0m")

# Support Vector Machines
from sklearn.svm import SVC
svc = SVC()
svc.fit(X_train, y_train)
y_pred_svc = svc.predict(X_test)

svc_train = round(svc.score(X_train, y_train) * 100, 2)
svc_accuracy = round(accuracy_score(y_pred_svc, y_test) * 100, 2)

print("Training Accuracy    :",svc_train ,"%")
print("Model Accuracy Score :",svc_accuracy ,"%")
print("\033[1m--------------------------------------------------------\033[0m")
print("Classification_Report: \n",classification_report(y_test,y_pred_svc))
print("\033[1m--------------------------------------------------------\033[0m")

import pickle
pickle.dump(random_forest,open('model2.pkl','wb'))

import joblib

# Assuming you have 'random_forest' as your trained model
joblib.dump(random_forest, 'model2.joblib')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data
csv_file = "/content/drive/MyDrive/csv files/predictive_maintenance.csv"  # Replace with the path to your CSV file
data = pd.read_csv(csv_file)

# Assuming the failure categories are in the 'Failure Type' column
failure_categories = ['No Failure', 'Heat Dissipation Failure', 'Power Failure', 'Overstrain Failure', 'Tool Wear Failure', 'Random Failures']

# Create a pie chart
fig, ax = plt.subplots(figsize=(8, 6))

# Count the occurrences of each failure category
failure_counts = data['Failure Type'].value_counts()

# Set custom colors for the pie chart slices
colors = sns.color_palette('pastel')

# Explode the 'No Failure' slice to emphasize it
explode = [0.1 if category == 'No Failure' else 0 for category in failure_categories]

# Create the pie chart
ax.pie(failure_counts, labels=failure_categories, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, wedgeprops={'edgecolor': 'black'})
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Set the title for the chart
ax.set_title('Failure Categories Distribution', fontsize=16, fontweight='bold')

# Add legend with category names and their corresponding counts
ax.legend(failure_counts.index, title='Failure Category', loc='best')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('/content/drive/MyDrive/csv files/predictive_maintenance.csv')

# Histograms for each feature
df.hist(figsize=(10,10))
plt.tight_layout()
plt.show()

# Box plots for each feature
df.plot(kind='box', subplots=True, layout=(4,3), sharex=False, sharey=False, figsize=(10,10))
plt.tight_layout()
plt.show()

# Scatter plot matrix
pd.plotting.scatter_matrix(df, alpha=0.2, figsize=(10, 10))
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve

def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None, n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.legend(loc="best")
    return plt

# Replace 'random_clf' with your model
title = "Learning Curves (Random Forest)"
plot_learning_curve(random_forest, title, X_train, y_train, cv=5)
plt.show()