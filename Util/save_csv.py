import pandas as pd
def save_csv(x, y, file_path):
    df = pd.DataFrame({'x': x, 'y': y})
    df.to_csv(file_path, index=False)