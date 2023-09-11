from data_processing import filter_client_details
from utils import log_info
from utils import save_csv


def main():
    filtered_data = filter_client_details("../client_data/dataset_one.csv","../client_data/dataset_two.csv",["Netherlands","United Kingdom"])
    save_csv(filtered_data)



if __name__ == '__main__':
    main()