import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

class DataSplitter:
    
    def __init__(self, df, target_column, test_size):
        self.df = df
        self.target_column = target_column
        self.test_size = test_size
        self.scaler = MinMaxScaler()
    
    def split(self):

        # X = macierz danych wejściowych (features)
        # y = wektor docelowego wyniku (target)
        X = self.df.drop(columns=[self.target_column])
        y = self.df[self.target_column]

        # dzielenie na zbiór treningowy i testowy
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=self.test_size
        )

        # skalowanie / normalizacja do przedziału [0, 1]
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        return X_train_scaled, X_test_scaled, y_train, y_test
