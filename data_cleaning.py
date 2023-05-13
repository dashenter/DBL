import pandas as pd
import os
import sqlite3

client = 'American Air'
client_nr = 22536055

competitor = 'AirFrance'
competitor_nr = 106062176


def get_json_files(directory):
    """
    Get a list of JSON files in a directory.
    """
    json_files = []
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            if name.endswith('.json'):
                json_files.append(str(os.path.join(root, name)))
    return json_files


def drop_columns(df):
    """
    Drop unnecessary columns from the dataframe.
    """
    columns_to_drop = ['id_str', 'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'quoted_status_id_str',
                       'favorited', 'retweeted', 'filter_level', 'timestamp_ms', 'retweeted_status', 'delete']
    df.drop(columns_to_drop, axis=1, inplace=True)
    return df


def separate_user_dataframe(df):
    """
    Create a separate dataframe for the 'user' column.
    """
    list_of_user_values = df['user'].tolist()
    list_of_user_names = [n for n in list_of_user_values[0]]
    df_user_separate = pd.DataFrame([list_of_user_values[0]])
    return df_user_separate


def create_sqlite_table(df, table_name, db_name):
    """
    Create a table in a SQLite database and insert data from a dataframe.
    """
    conn = sqlite3.connect(db_name)
    df.columns = df.columns.str.strip()
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

# Get the list of JSON files
json_files = get_json_files(".")

# Read the first JSON file into a dataframe and process it
df = pd.read_json(json_files[1], lines=True)
df = drop_columns(df)
df_user_separate_1 = separate_user_dataframe(df)

# Read the second JSON file into a dataframe and process it
df = pd.read_json(json_files[0], lines=True)
df = drop_columns(df)
df_user_separate_2 = separate_user_dataframe(df)

# Create SQLite tables for the separate 'user' dataframes
table_name_1 = 'Air_line_1'
table_name_2 = 'Air_line_2'
db_name = 'pythonsqlit3.db'

create_sqlite_table(df_user_separate_1, table_name_1, db_name)
create_sqlite_table(df_user_separate_2, table_name_2, db_name)
