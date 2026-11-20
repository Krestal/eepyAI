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
        print(f"---------------------------------------------------------------\nThere are {len(columns)} non-numerical columns:")
        for column in columns:
            unique_values = self.df[column].unique()
            print(f"\t{column} - {len(unique_values)} values:")
            for value in unique_values:
                print(f"\t\t{value}")
        print("---------------------------------------------------------------")
        
    # histogram jednej kolumny
    def histogram(self, column):
        counts, edges, patches = plt.hist(self.df[column], bins=10, color='turquoise')  # turkusowy kolor

        # dodanie wartości nad każdym słupkiem
        for count, patch in zip(counts, patches):
            height = patch.get_height()
            if height > 0:
                plt.text(patch.get_x() + patch.get_width()/2, height, 
                         str(int(height)), ha='center', va='bottom')

        plt.xlabel(column)
        plt.ylabel("count")
        plt.title(f"Histogram of {column}")
        plt.show()


    # wszystkie histogramy
    def histogram_all_columns(self):
        num_cols = self.df.select_dtypes(include=['float64','int64']).columns
        self.df[num_cols].hist(bins=10, figsize=(23,14), color='turquoise')
        plt.tight_layout(h_pad=1, w_pad=1)
        plt.show()

    # mapa korelacji cech
    def correlation_heatmap(self):
        plt.figure(figsize=(23,10))
        correlation_coefficients = self.df.corr()
        # maska dla górnej trójkątnej części (nie chcę jej oglądać)
            # np.ones_like() tworzy macierz o wymiarach jak correlation_coefficients i wypełnia ją wartościami True
            # np.triu zamienia wszystko poniżej głównej przekątnej na False
        mask = np.triu(np.ones_like(correlation_coefficients, dtype=bool)) 
            # sns.heatmap() ukrywa wszystkie pola które w masce mają True
        sns.heatmap(correlation_coefficients, mask=mask, annot=True, fmt=".2f", cmap=sns.color_palette("BrBG", 10))
        plt.show()
