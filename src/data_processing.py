import pandas as pd
from utils import read_csv
from utils import log_info

def filter_client_details(file_path_1,file_path_2,countries=["Netherlands","United Kingdom"]):
    dataFrame_1,dataFrame_2 = read_csv(file_path_1,file_path_2)
    # dataFrame_1,dataFrame_2 = clean_df( dataFrame_1,dataFrame_2)
    filtered_df = clean_df(dataFrame_1,dataFrame_2,countries)
    return filtered_df

def merge_df_id(dataFrame_1,dataFrame_2):
    merged_df = pd.merge(dataFrame_1,dataFrame_2,left_on='id',right_on='id')
    # log_info(merged_df.head(3))
    return merged_df

def clean_df(dataFrame_1,dataFrame_2,countries):
    dataFrame_1.drop(["first_name","last_name"],axis=1,inplace=True)
    dataFrame_2.drop("cc_n",axis=1,inplace=True)
    merged_df = merge_df_id(dataFrame_1,dataFrame_2)
    # log_info(merged_df.loc[merged_df["country"].isin(["Netherlands","United Kingdom"])])
    merged_filtered = merged_df.loc[merged_df["country"].isin(countries)]
    return merged_filtered
    