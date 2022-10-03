#-------------------------------------------------------------------------
# AUTHOR: Andrew Nguyen
# FILENAME: naive_bayes.py
# SPECIFICATION: predict weather class using gaussiannb model
# FOR: CS 4210- Assignment #2
# TIME SPENT: 5 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#reading the training data in a csv file
#--> add your Python code here

weather_classifier_confidence = []
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:
            weather_classifier_confidence.append(row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
X = []
for row in weather_classifier_confidence:
    hold = []
    for i in range(1, 5):
        if  row[i] == "High" or row[i] == "Weak" or row[i] == "Sunny" or row[i] == "Hot":
            hold.append(1)
        elif row[i] == "String" or row[i] == "Normal" or row[i] == "Mild" or row[i] == "Overcast":
            hold.append(2)
        else:
            hold.append(3)

    X.append(hold)

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y = []

for row in weather_classifier_confidence:
    if row[5] == "Yes":
        Y.append(1)
    else:
        Y.append(2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here
weather_predictions = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: # skipping the header
            weather_predictions.append(row)
X_test = []
for row in weather_predictions:
    hold = []
    for i in range(1, 5):
        if row[i] == "High" or row[i] == "Weak" or row[i] == "Sunny" or row[i] == "Hot":
            hold.append(1)
        elif row[i] == "String" or row[i] == "Normal" or row[i] == "Mild" or row[i] == "Overcast":
            hold.append(2)
        else:
            hold.append(3)
    X_test.append(hold)

#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) +
       "PlayTennis".ljust(15) + "Confidence".ljust(15))


############check#####################

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here

predictions = clf.predict(X_test)
for i, row in enumerate(X_test):
    confidence = clf.predict_proba([row])[0]
    if confidence[0] >= 0.75:
        num = round(confidence[0], 2)
        print(weather_predictions[i][0].ljust(15) + weather_predictions[i][1].ljust(15) + weather_predictions[i][2].ljust(15) +
              weather_predictions[i][3].ljust(15) + weather_predictions[i][4].ljust(15) + "Yes".ljust(15) +  str(num).ljust(15))

