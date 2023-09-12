import pandas as pd
import logging as log
from logging.handlers import RotatingFileHandler

def read_csv(file_path_1,file_path_2):
    return (pd.read_csv(file_path_1),pd.read_csv(file_path_2))

def log_info(log_type,message):
    # log.basicConfig(level=log.INFO,
    #                 format="%(asctime)s [%(levelname)s] %(message)s")
    # log.info(info)
    logger = log.getLogger('my_logs')
    logger.setLevel(log.DEBUG)

    log_file = 'user.log'
    max_log_size = 512 * 512
    num_backups = 3
    file_handler = RotatingFileHandler(log_file,maxBytes=max_log_size,backupCount=num_backups)
    

    formatter = log.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    match log_type:
        case "Warning":
            logger.warning(f'Warning:{message}')
        case "Info":
            logger.info(f'Info: {message}')
        case "Error":
            logger.error(f'{message}')




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
        # log_info("IN else")
        dataframe.to_csv(r'../../client_data/filtered_client_data.csv')

    # log_info("Errors after save")