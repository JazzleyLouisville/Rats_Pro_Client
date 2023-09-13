# RATS PRO CLient Data Collation

## Overview
Rats pro client data collation is a data processing and filtering tool desgigned to help RATS PRO, ineteract more effectively with its clients. This application contains two seperate datasets
- Dataset 1: Information about clients.
- Dataset 2: Financial details clients.

#### Key objectives
- Combine client information and financial details into a single dataset.
- Filter and select client from specific countries(Limited to 4 countries: Netherlands, France, United Kingdom, United States)
- Ensure client privacy by removing personal identifiable information from the client dataset.
- Remove sensitive credit card numbers from the financial dataset.

This project showcases data processing, data manipulation, and basic data privacy practices in a Python environment, with an option to extend it into a more advanced framework with additional bonus features.

## Getting Started
#### Prerequisites
- Python 3.x, Pandas, Flask, Logging

Run the requirements.txt file to install all dependencies at once using:
```
pip install -r requirements.txt
```

#### Installation
- Clone Repository
- create virtual environment(Optional)
- Install requirements from requirements.txt file

# Running Application
The application can be ran with the following command:

```
python main.py --name_set_1 dataset_one.csv --name_set_1 dataset_two.csv --countries "UK,Netherlands"
```

As an added bonus, if you navigate towards the src/flask folder you can start up a flask server.

- Supported routes as of now are:
    - '/generate_client_data':
        - This route issue a POST request to the server, requesting the creation of data filtered on chosen countries.
    - '/download_filtered_data'
        - This route issue a GET request, requesting the resources in our case a 'csv' file that was just generated to be sent back to the user.

The flask server can be started through the following command:
```
flask --app api --debug run
```

Note: The convention that needs to be followed for succesful CSV parsing is the following(Comma seperated values):

| id       |first_name |last_name|email|country
| -------- | ------- | ------- | ------- | -------
| 0  | Feliza    | Eusden | feusden0@ameblo.jp|France

##### All result_data will be stored in the client_data directory.