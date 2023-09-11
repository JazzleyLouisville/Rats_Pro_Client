from data_processing import merge_csv


def main():
    merged_data = merge_csv("../client_data/dataset_one.csv","../client_data/dataset_two.csv")
    # print(merged_data.head(2))


if __name__ == '__main__':
    main()