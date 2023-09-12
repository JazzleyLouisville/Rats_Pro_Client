import pandas as pd
import logging as log

def read_csv(file_path_1,file_path_2):
    return (pd.read_csv(file_path_1),pd.read_csv(file_path_2))

def log_info(info):
    log.basicConfig(level=log.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")
    log.info(info)

def save_csv(dataframe,path):
    """
    This function saves a dataframe to a csv file.

    Args:
        dataframe (pandas dataframe): pandas dataframe variable.
            
    Returns:
        void.
    """
    # log_info("Errors before save")
    if path == "main":
        dataframe.to_csv(r'client_data/filtered_client_data.csv')
    else:
        log_info("IN else")
        dataframe.to_csv(r'../../client_data/test_filtered_client_data.csv')

    log_info("Errors after save")