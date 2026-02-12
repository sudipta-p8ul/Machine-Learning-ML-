import pandas
from sklearn import linear_model

df = pandas.read_csv("data1.csv")

X = df[['x1', 'x2']]
y = df['y']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predicted = regr.predict([[3,2]])
print(predicted)