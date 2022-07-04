# -*- coding: utf-8 -*-
"""KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ag6GGZ7WNVc236sl-MVDT9tfK6Vb8iRs
"""

#lib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

# dataset
from google.colab import files
upload=files.upload()

#dataset
iris=pd.read_csv("Iris.csv")
iris.head(5)

iris.columns

x_variables=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
y_variables=['Species']
x=np.array(iris[x_variables]).reshape(-1,4) #first value is -1 and the next value is the length of x_variable
y=np.array(iris[y_variables]).reshape(-1,1)
print(x.shape)
print(y.shape)

# split the dataset
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)
print(x_train.shape)
print(x_test.shape)

#if you want to use differen distand like manhaltan so p=1 and euclidean so p=2
knn_model=KNeighborsClassifier(n_neighbors=5, n_jobs=-1).fit(x_train,y_train)

y_predict=knn_model.predict(x_test)
print(y_predict)

"""1. lib
2. Dataset
3. Preprocessing ,3.1 X_variablles , 3.2 y_variables
4. Model buil
5. predict the result
6. probability
7. Ealution metrics (Accuracy ) -Accuracy score

task
1. create a table between actual and predict
2. Check the formula of accuracy score
3. find the procedure to get  the opimal k-value
"""

#create a table between actual and predict
table_iris_dataset = pd.DataFrame({"y_predict": y_predict, "y_test": list(y_test)})
print(table_iris_dataset )

"""#Check the formula of accuracy score
accuracy score = Number of correct predictions / total number of prediction

#find the procedure to get the opimal k-value
For determine the K values :
1. step 1: we need to choose value for K that must be least number and greater then 2
2. step 2: Take k from step 1 put into KNN algorithm to predict the classes

3. step 3: determine the percentage of accuracy error prediction
4. setp 4: Try to determine increase k by s(s>=1) repeat it again and again as posible with the limitation of resource
5. setp 5: choose k value with the result that contain the least accuracy error percentage
"""