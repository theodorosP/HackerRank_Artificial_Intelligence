from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

class PredictValues:
    #define the constructor
    def __init__(self, dataset_file, cols):
        self.data = self.read_file_to_dataframe(dataset_file, cols)

    def get_data(self):
        try:
            num = float(input())
            return num
        except ValueError:
            print("Please give a float number")

    def read_file_to_dataframe(self, file_to_read, cols):
        try:
            dataframe = pd.read_csv(file_to_read,  sep = ",", skiprows = 0, header = None, skipinitialspace = True, skipfooter=0, engine = "python")
            dataframe.columns = cols
            return dataframe
        except ValueError:
            print("Give correct number of row names")

    #break_point = the number where data start changing trend
    #choice = 1 for < break_point, 2 > break_point
    def split_data(self, break_point, choice):
        try: 
            if choice == 1:
                data_splitted = self.data[ self.data[ self.data.columns[0] ] < break_point ]
                #print(len(data_splitted))
            elif choice == 2:
                data_splitted = self.data[ self.data[ self.data.columns[0] ] > break_point ]
                #print(data_splitted)
            return data_splitted
        except UnboundLocalError:
            print("Choice number should either be 1 or 2. Give correct choice number.")
    
    #data_before = dataframe with charging_time < 4
    #data_after = dataframe with charging_time > 4
    def train_model(self, data_before, data_after):
        X_data_before = data_before[data_before.columns[0]].values.reshape(-1, 1)
        Y_data_before = data_before[data_before.columns[1]].values.reshape(-1, 1)

        X_data_after = data_after[data_after.columns[0]].values.reshape(-1, 1)
        Y_data_after = data_after[data_after.columns[1]].values.reshape(-1, 1)

        model_before = LinearRegression()
        model_after = LinearRegression()
        model_before.fit(X_data_before, Y_data_before)
        model_after.fit(X_data_after, Y_data_after)
        return model_before, model_after
    
    def make_prediction(self, model1, model2, number):
        if number < 4:
            prediction = model1.predict(np.array([self.num]).reshape(-1, 1))
        elif number > 4:
            prediction = model2.predict(np.array([self.num]).reshape(-1, 1))
        print(round(prediction[0][0], 2))

object = PredictValues("trainingdata.txt", ["charging_time", "battery_life"])
object.num = object.get_data()
a = object.split_data(4, 1)
b = object.split_data(4, 2)
before, after = object.train_model(a, b)
object.make_prediction(before, after, object.num)
