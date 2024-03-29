import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

# Load the passenger data
passengers = pd.read_csv('passengers.csv')
# Update sex column to numerical
encoder = LabelEncoder()
passengers['Sex'] = encoder.fit_transform(passengers['Sex'])
# Fill the nan values in the age column
passengers['Age'].fillna(value='30',inplace=True)
# Create a first class column
passengers['FirstClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 1 else 0)

# Create a second class column
passengers['SecondClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 2 else 0)
# print(passengers)
# Select the desired features
features = passengers[['Sex','Age','FirstClass','SecondClass']]
survival = passengers['Survived']
# Perform train, test, split
x_train,x_test,y_train,y_test = train_test_split(features,survival,train_size=0.8,test_size=0.2,random_state=100)

# Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
# Create and train the model
model = LogisticRegression()
model.fit(x_train,y_train)

# Score the model on the train data
print(model.score(x_train,y_train))

# Score the model on the test data
print(model.score(x_test,y_test))

# Analyze the coefficients
coeff = model.coef_
print(coeff)
# Sample passenger features
Jack = np.array([1.0,20.0,0.0,0.0])
Rose = np.array([0.0,17.0,1.0,0.0])
You = np.array([1.0,19,1.0,0.0])

# Combine passenger arrays
sample_passengers = np.array([Jack,Rose,You])

# Scale the sample passenger features
sample_passengers = scaler.transform(sample_passengers)

# Make survival predictions!
print(model.predict(sample_passengers))

