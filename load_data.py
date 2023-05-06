# Imports
import os
import dask.dataframe as dd
import pandas as pd

client = 'American Air'
client_nr = 22536055
competitor = 'AirFrance'
competitor_nr = 106062176


# Read data form a selected file
def read_single_file(file_path):
    with open(file_path, 'r') as f:
        data = f.readlines()
    return data

# Read the data using OS
def read_all_files(dir_path):
    tweets = []
    for filename in os.listdir(dir_path):
        if filename.endswith('.json'):
            with open(os.path.join(dir_path, filename), 'r', encoding='utf-8') as f:
                tweets.extend(f.readlines())
    return tweets

# Read the data using PANDAS
def read_data_pandas(file_path):
    df = pd.read_json(file_path, lines=True)
    return df
# Read the data using DASK
def read_data_dask(dir_path):
    df = dd.read_json(os.path.join(dir_path, '*.json'), lines=True)
    return df.compute()

# Prints last tweet of a file
def print_last_tweet(tweets):
    print(tweets[-1])


def print_column_names(df):
    for col in df.columns:
        print(col)
def print_first_two_rows(df):
    print(df.head(2))


if __name__ == '__main__':
    # Read data from a single file
    file_path = 'data/airlines-1558527599826.json'
    data_single = read_single_file(file_path)

    # Read data from all JSON files using OS
    dir_path = 'data/'
    data_all = read_all_files(dir_path)
    # Print the first line of the data from the last file processed
    print_last_tweet(data_all)

    # Read the data using dask
    df_dask = read_data_dask(dir_path)

    # Read the data using pandas
    df_pandas = read_data_pandas(file_path)

    # Print the column names
    print_column_names(df_dask)
    # Print the first two rows of the data
    print_first_two_rows(df_dask)
    # Print the first two rows of the data
    print_first_two_rows(df_pandas)