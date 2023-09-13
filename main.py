# from data_processing import filter_client_details
# from utils import log_info
# from utils import save_csv
import argparse
from src.data_processing import filter_client_details
from src.utils import log_info, save_csv



def main(name_set_1,name_set_2,countries):
    # name_set_1 = dataset_one.csv
    # name_set_2 = dataset_two.csv
    countries_list = countries.split(',')
    filtered_data = filter_client_details("client_data/"+name_set_1,"client_data/"+name_set_2,countries_list)
    save_csv(filtered_data,"main")



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name_set_1', required=True, help='Name of the first dataset')
    parser.add_argument('--name_set_2', required=True, help='Name of the second dataset')
    parser.add_argument('--countries', required=True, help='List of countries to filter (comma-separated)')

    args = parser.parse_args()
    main(args.name_set_1, args.name_set_2, args.countries)