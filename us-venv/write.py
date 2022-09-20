import pandas as pd
query = 'SELECT * FROM users'
conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
df = pd.read_sql(
    query,
    conn
)

print(df)

print(df.count())