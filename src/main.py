from utils import read_csv


def main():
    dataFrame_1,dataFrame_2 = read_csv("../client_data/dataset_one.csv","../client_data/dataset_two.csv")
    print(dataFrame_1.head(2))
    print("space\n")
    print(dataFrame_2.head(2))


if __name__ == '__main__':
    main()