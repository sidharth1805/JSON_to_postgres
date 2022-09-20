import pandas as pd
import os

BASE_DIR = 'C:/work_dir/data_copier_data/retail_db_json'
table_name = 'orders'

file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
fp = f'{BASE_DIR}/{table_name}/{file_name}'

def main():
    json_reader = pd.read_json(fp, lines=True, chunksize=1000)
    conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
    for df in json_reader:
        min_key = df['order_id'].min()
        max_key = df['order_id'].max()
        df.to_sql(table_name, conn, if_exists='append', index=False)
        print(f'Processed {table_name} with in the range of {min_key} and {max_key}')



if __name__ == "__main__":
    main()