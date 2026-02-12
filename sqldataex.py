import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="SUDIPTA",
    user="23051792",
    password="sudipta",
    database="employees"
)

query = "SELECT * FROM emp_table"
df = pd.read_sql(query, conn)
print(df.head())