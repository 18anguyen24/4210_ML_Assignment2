#-------------------------------------------------------------------------
# AUTHOR: Andrew Nguyen
# FILENAME: knn.py
# SPECIFICATION: calculate LOO-CV error rate for 1NN using binary_points
# FOR: CS 4210- Assignment #2
# TIME SPENT: 4 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

data_array = []
correct = 0
incorrect = 0

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         data_array.append (row)


#loop your data to allow each instance to be your test set
for i, instance in enumerate(data_array):

    #add the training features to the 2D array X and remove the instance that will be used for testing in this iteration.
    #For instance, X = [[1, 3], [2, 1,], ...]]. Convert values to float to avoid warning messages
    X = []

    for j, row in enumerate(data_array):
        if i != j:
            hold = []
            for n in row[:-1]:
                hold.append(int(n))
            X.append(hold)

    #transform the original training classes to numbers and add them to the vector Y. Do not forget to remove the instance that will be used for testing in this iteration.
    #For instance, Y = [1, 2, ,...]. Convert values to float to avoid warning messages
    Y = []

    for z, row in enumerate(data_array):
        if i != z:
            if row[-1] == "-":
                Y.append(2)
            else:
                Y.append(1)
    #--> add your Python code here
    X_ins = int(instance[0])
    Y_ins = int(instance[1])
    testSample = [X_ins, Y_ins]

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict([testSample])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here

    test = 0
    if instance[2] == "-":
        test = 2
    else:
        test = 1

    if class_predicted == test:
        correct += 1
    else:
        incorrect += 1


#print the error rate
#--> add your Python code here
error_rate = incorrect / (correct + incorrect)
print("Error rate: " + str(error_rate))






