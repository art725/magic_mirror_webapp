import mariadb
import pandas as pd

conn = mariadb.connect(
    user="paul",
    password="lubu",
    host="localhost",
    database="familydb"
)
df = pd.read_sql('SELECT * FROM pi_stats', con=conn)

print(df)