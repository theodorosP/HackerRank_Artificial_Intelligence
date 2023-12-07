#This function converts a list containing lists with string elements into a list comprising lists with float elements
#list_of_lists has the format [['1', '2', '3'], ['4', '5', '6']...]
def to_float(list_of_lists):
    l_out = list()
    for i in list_of_lists:
        l = [float(j) for j in i]
        l_out.append(l)
    return l_out

# This function collects data.
# n represents the number of data lines.
# f represents the number of elements in each list.
# Both n and f are integers.
def collect_data(n, f):
    data = list()
    for i in range(0, n):
        data.append(input().split()[:f])
    data = to_float(data)
    return data

# This function combines the to_float() and collect_data() functions to return the training data ('my_data') and the data for prediction ('to_predict').
# X, Y: represent the training data.
# to_predict: represents the data for which we want to make a prediction.
def get_data():
    F, N = input().split()[:2]
    F = int(F)
    N = int(N)
    my_data = collect_data(N, F + 1)
    T = int(input())
    to_predict = collect_data(T, F)
    Y_ = [i[-1] for i in my_data]
    X_ = [i[:-1] for i in my_data]
    return X_, Y_, to_predict


from sklearn import linear_model
import numpy as np
X, Y, new_X  = get_data()
model = linear_model.LinearRegression()
model.fit(np.array(X), Y)
results = model.predict(np.array(new_X))
for i in results:
    print(round(i, 2))
