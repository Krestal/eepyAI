import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class DataAnalyzer:

    # konstruktor (przyjmuje tylko dataframe)
    def __init__(self, df):
        self.df = df

    # podstawowe info o danych
    def basic_info(self):
        print(self.df.info())

    # statystyki opisowe
    def statistics(self):
        display(self.df.describe())

    # wszystkie wartości w nienumerycznych kolumnach
    def unique(self):
        columns = self.df.select_dtypes(include=['object']).columns
        print(f"There are {len(columns)} non-numerical columns:")
        for column in columns:
            unique_values = self.df[column].unique()
            print(f"\t{column} - {len(unique_values)} values:")
            for value in unique_values:
                print(f"\t\t{value}")