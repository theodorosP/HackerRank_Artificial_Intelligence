import numpy as np

#this function gets the F, N, T integers specified by the problem
#choice is an integer, 1 or 2 specifying the number of integers the user wants to read
def get_integers(choice):
	if choice  == 2:
		try:
			F, N = map(int, input().split()[: 2] )
		except ValueError:
			print("Give an integer number")
			return None
		print("F = ", F, "N = ", N)
		return F, N
	elif choice == 1:
		try:
			T = int(input())
		except ValueError:
			print("Give an integer")
			return None
		print("T = ", T)
		return T
	else:
		print("Please use 1 or 2 as inputs")
		return None

#This function gets the data and stores them in a matrix with F rows and N columns
def get_big_data(columns, rows):
	big_data = list()
	for i in range(0, rows):
		try:
			data = list(map(float, input().split()[:columns] ) )
			big_data.append(data)
		except VallueError:
			print("Give a float")
	print("Big Data = ", big_data)
	return big_data


#This function wraps everything up and gets all the data required by the problem
def get_data():
	F, N = get_integers(2)
	training_data = get_big_data(F + 1 , N)
	T = get_integers(1)
	predicting_data = get_big_data(F, T)
	X_data = [ i[: -1] for i in training_data]
	Y_data = [ i[-1] for i in training_data ]
	X_data_array = np.array(X_data)
	Y_data_array = np.array(Y_data)
	print("X_data = ", X_data_array)
	print("Y_data = ", Y_data_array)
	predicting_data_array = np.array(predicting_data)
	print("Predicting_data = ", predicting_data_array)
	return X_data_array, Y_data, predicting_data_array
	

def train_model(x, y, to_pred):
	from sklearn import linear_model
	from sklearn.preprocessing import PolynomialFeatures
	model = linear_model.LinearRegression()
	polynomial = PolynomialFeatures(degree = 3)
	X_transformed = polynomial.fit_transform(x)
	print(X_transformed)
	model.fit(X_transformed, Y)
	to_pred_transformed = polynomial.fit_transform(to_pred)
	print(to_pred_transformed)
	predictions = model.predict(to_pred_transformed)
	for i in predictions:
		print( round(i, 2) )

X, Y, P = get_data()
train_model(X, Y, P)
