import pandas as pd

def read_csv(file_path_1,file_path_2):
    return (pd.read_csv(file_path_1),pd.read_csv(file_path_2))

