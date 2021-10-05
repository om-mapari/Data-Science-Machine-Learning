import pandas as pd
import numpy as np

dataset = pd.read_csv("heart.csv")
dataset

# a) Find shape of data

print(dataset.shape)

# b) Find missing values
print(dataset.isnull().sum())
dataset.info

# c) find data type of each column

print("Data types of each column:")
dataset.dtypes

# d) Finding out Zero's

(dataset==0).sum(axis = 0)

# e) Find Mean age of patients

mean_age = dataset["Age"].mean()
print("Mean age of all the patients: ", mean_age)

# f) extract only Age, Sex, ChestPain, RestBP, Chol and  dividing dataset in training (75%) and testing (25%).
from sklearn.model_selection import train_test_split

train, test = train_test_split(dataset[["Age", "Sex", "ChestPain", "RestBP", "Chol"]], test_size = 0.25, train_size=0.75)
print
print(train)
print(test)

# Find Mean of all data set
# EXTRA
mean = np.mean(dataset)
print("Mean of all data sets:\n",mean)

# EXTRA
duplicate = dataset[dataset.duplicated()]
duplicate

#EXTRA: minimum and maximum age of patients having AHD

list_ages_HD = []
count = 0
for j in  dataset["AHD"]:
    if j == "Yes":
        list_ages_HD.append(dataset["Age"][count])
    count += 1

print(min(list_ages_HD), max(list_ages_HD))

'''
Through the diagnosis test I predicted 100 report as COVID positive, 
but only 45 of those were actually positive. Total 50 people in my sample were actually COVID positive.
I have total 500 samples.       
Create confusion matrix based on above data and find  I. Accuracy II. Precision III. Recall IV. F-1  score
'''

total_samples = 500
tested_positive = 100
actual_positive_cases = 45+5

from sklearn.metrics import accuracy_score

predicted_positive = []
actual_positive = []

for i in range(100):
    predicted_positive.append(1)

    
for i in range(45):
    actual_positive.append(1)
for i in range(55):
    actual_positive.append(0)
    
for i in range(400):
    predicted_positive.append(0)
    
for i in range(5):
    actual_positive.append(1)
for i in range(395):
    actual_positive.append(0)
    
accuracy_score(actual_positive, predicted_positive)

import numpy as np
from sklearn.metrics import precision_score

print(precision_score(actual_positive, predicted_positive))
#print(precision_score(actual_positive, predicted_positive, average='macro'))
#print(precision_score(actual_positive, predicted_positive, average='micro'))
#print(precision_score(actual_positive, predicted_positive, average='weighted'))

from sklearn.metrics import recall_score

recall_score(actual_positive, predicted_positive)

from sklearn.metrics import f1_score

f1_score(actual_positive, predicted_positive)

from sklearn import metrics


print(metrics.confusion_matrix(actual_positive, predicted_positive))

print(metrics.classification_report(actual_positive, predicted_positive))

