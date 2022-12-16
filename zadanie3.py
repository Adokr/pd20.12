import numpy as np
#Load data from data/ex3_data.npy and filter out rows with nan values.
#Report how many rows are dropped during filtration, globally and how many nan are in each column.

with open ("data/ex3_data.npy", "r") as f:
    y = np.load("data/ex3_data.npy")

def func1(x):
    filtered_x = x[~np.isnan(x).any(axis=1)]
    dropped_rows_count = x[np.isnan(x).any(axis=1)].shape[0]
    column_nans_count = np.isnan(x).sum(axis=0)
    nan_count = np.isnan(x).sum()

    print(f"liczba odrzuconych wierszy: {dropped_rows_count}")
    print("liczba nan w kolejnych kolumnach: ", end='')
    print(*column_nans_count, sep=' ')
    print(f"Liczba nan w całej tabeli: {nan_count}")

func1(y)

