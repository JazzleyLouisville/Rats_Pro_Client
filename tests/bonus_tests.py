import unittest
from src.utils import read_csv
from src.data_processing import clean_df , merge_df_id
import pandas as pd


class Test(unittest.TestCase):
    def setUp(self):
        self.countries = ['United Kingdom','Germany']
        data_1 = {'id': [1, 2, 3], 
                  'country': ['Netherlands', 'United Kingdom', 'Germany'], 
                  'first_name': ['Alice', 'Bob', 'Charlie'], 
                  'last_name': ['Doe', 'Smith', 'Johnson'],
                  'email':['random1@gmail.com', 'user123@yahoo.com', 'test_email@hotmail.com']
                }
        data_2 = {'id': [3, 4, 5], 
                  'cc_n': ['123', '456', '789'],
                  'btc_a': ['123456789', '987654321', '246813579'],
                  'cc_t':['1','2','3']
                }
        self.df_1 = pd.DataFrame(data_1)
        self.df_2 = pd.DataFrame(data_2)

    def test_merge(self):
        merged_df = merge_df_id(self.df_1,self.df_2)
        # Check if the result is a DataFrame
        self.assertIsInstance(merged_df, pd.DataFrame)
        
        # Checking whether the new df contains 8 cols
        self.assertEqual(merged_df.shape[1],8)

        # Checking whether the df contains an ID column
        self.assertTrue('id' in merged_df)

    def test_clean_df(self):
        cleaned_df = clean_df(self.df_1,self.df_2,self.countries)
        expected_cols = ['client_identifier','bitcoin_address','credit_card_type']
        
        # Check if the result is a DataFrame
        self.assertIsInstance(cleaned_df, pd.DataFrame)
        # Check if the columns exist in the dataframe
        self.assertTrue(all(col in cleaned_df for col in expected_cols))


        


if __name__ == '__main__':
    unittest.main()

