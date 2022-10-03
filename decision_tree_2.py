#-------------------------------------------------------------------------
# AUTHOR: Andrew Nguyen
# FILENAME: decision_tree_2.py
# SPECIFICATION: create decision tree and find performance of each training set
# FOR: CS 4210- Assignment #2
# TIME SPENT: 5 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

classifier_accuracy = []
for ds in dataSets:
    dbTraining = []
    X = []
    Y = []

    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0: # skipping the header
                dbTraining.append(row)

    # transform the original categorical training features to numbers and add to the 4D array X.For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # --> add your Python code here
    # X =
    for row in dbTraining:
        hold = []
        for i in range(4):
            if row[i] == "Young" or row[i] == "Myope" or row[i] == "Yes" or row[i] == "Reduced":
                hold.append(1)
            elif row[i] == "Prepresbyopic" or row[i] == "Hypermetrope" or row[i] == "No" or row[i] == "Normal":
                hold.append(2)
            else:
                hold.append(3)
        X.append(hold)

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> addd your Python code here
    # Y =
    for row in dbTraining:
        if row[4] == "No":
            Y.append(2)
        else:
            Y.append(1)

    lowestAccuracy = 1
    # loop your training and test tasks 10 times here
    for i in range(10):

        # fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
        clf = clf.fit(X, Y)

        # read the test data and add this data to dbTest
        # --> add your Python code here
        dbTest = []
        with open("contact_lens_test.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            for b, row in enumerate(reader):
                if b > 0:
                    dbTest.append(row)

        correct = 0
        incorrect = 0
        for data in dbTest:
            #transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here
            transform_data = []

            for j in range(5):
                if data[j] == "Myope" or data[j] == "Young" or data[j] == "Yes" or data[j] == "Reduced":
                    transform_data.append(1)
                elif data[j] == "Hypermetrope" or data[j] == "Prepresbyopic" or data[j] == "No" or data[j] == "Normal":
                    transform_data.append(2)
                else:
                    transform_data.append(3)

            class_predicted = clf.predict([transform_data[:-1]])[0]

            # compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            # --> add your Python code here
            if transform_data[4] == class_predicted:
                correct += 1
            else:
                incorrect += 1

        # find the lowest accuracy of this model during the 10 runs (training and test set)
        # --> add your Python code here
        accuracy = correct / (correct + incorrect)
        if lowestAccuracy > accuracy:
            lowestAccuracy = accuracy
    classifier_accuracy.append(lowestAccuracy)
 #print the lowest accuracy of this model during the 10 runs (training and test set).
 #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
print("final accuracy when training on contact_lens_training_1.csv: ", classifier_accuracy[0])
print("final accuracy when training on contact_lens_training_2.csv: ", classifier_accuracy[1])
print("final accuracy when training on contact_lens_training_3.csv: ", classifier_accuracy[2])