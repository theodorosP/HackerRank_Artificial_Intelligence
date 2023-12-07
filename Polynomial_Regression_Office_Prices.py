import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

#This function collects the data. Table has f_ columns and n_ rows
def collect_data(f_, n_):
    data_ = list()
    for i in range(0, n_):
        try:
            values_ = list( map(float, input().split()[:f_] ) ) 
            data_.append(values_)
        except ValueError:
            print("Give float")
    return data_


def get_data():
    try:
        f, n = map(int, input().split()[:2])
    except ValueError:
        print("Give an integer")
    data = collect_data(f + 1, n)
    try:
        t = int(input())
    except ValueError:
        print("Give an integer")
    to_predict_ = collect_data(f, t)
    X_ = [i[: -1] for i in data]
    Y_ = [i[-1] for i in data]
    return X_, Y_, to_predict_

X, Y, new_X = get_data()
model = linear_model.LinearRegression()
polynomial = PolynomialFeatures(degree = 3)
X_transformed = polynomial.fit_transform(X)
model.fit(np.array(X_transformed), Y)
new_X_transformed = polynomial.fit_transform(new_X)
predictions = model.predict(np.array(new_X_transformed))
for i in predictions:
    print(round(i, 2))

