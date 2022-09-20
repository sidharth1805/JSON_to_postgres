import pandas as pd

def main():
    fp = 'C:/work_dir/data_copier_data/retail_db_json/order_items/part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e'
    json_reader = pd.read_json(fp, lines=True, chunksize=500)
    for idx, df in enumerate(json_reader):
        print(f'Number of records in chunk with index {idx} is {df.shape[0]}')



if __name__ == "__main__":
    main()