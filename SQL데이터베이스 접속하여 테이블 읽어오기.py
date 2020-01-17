import sqlalchemy as sqla
import cx_Oracle
import pandas as pd


db = sqla.create_engine('oracle+cx_oracle://scott:oracle@127.0.0.1:1521/orcl')

result = pd.read_sql('select * from dept', db)

print(result)
