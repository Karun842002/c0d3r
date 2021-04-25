import cx_Oracle
import os
from dotenv import load_dotenv
load_dotenv()

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DSN = os.getenv('DSN')
connection = cx_Oracle.connect(
    user=USER,
    password=PASSWORD,
    dsn=DSN)

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

cursor.execute("""
    begin
        execute immediate 'drop table tutorial';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")

cursor.execute('''create table tutorial(
    id int,
    name varchar(40)
    )''')

rows = [ ("Task 1", 1 ),
         ("Task 2", 2 ),
         ("Task 3", 3 ),
         ("Task 4", 4 ),
         ("Task 5", 5 ) ]

cursor.executemany("insert into tutorial (name,id) values(:1, :2)", rows)
print(cursor.rowcount, "Rows Inserted")

for row in cursor.execute('select id,name from tutorial'):
    print(row[0], row[1])