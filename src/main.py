from data_processing import filter_client_details
from utils import log_info


def main():
    filtered_data = filter_client_details("../client_data/dataset_one.csv","../client_data/dataset_two.csv")
    log_info(filtered_data.head(6))



if __name__ == '__main__':
    main()