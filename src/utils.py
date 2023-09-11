import pandas as pd
import logging as log

def read_csv(file_path_1,file_path_2):
    return (pd.read_csv(file_path_1),pd.read_csv(file_path_2))

def log_info(info):
    log.basicConfig(level=log.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")
    log.info(info)