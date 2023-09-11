import pandas as pd
from utils import read_csv
from utils import log_info

def merge_csv(file_path_1,file_path_2):
    dataFrame_1,dataFrame_2 = read_csv(file_path_1,file_path_2)
    dataFrame_1.drop(["first_name","last_name"],axis=1,inplace=True)
    # log_info(dataFrame_1.keys())
    print(dataFrame_1.head(2))