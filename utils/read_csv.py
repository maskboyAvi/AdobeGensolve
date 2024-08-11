import pandas as pd
def read_csv(file_path):
    data = pd.read_csv(file_path)
    x = data.iloc[:, -2].values
    y = data.iloc[:, -1].values
    return x, y