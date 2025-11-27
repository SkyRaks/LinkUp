import psycopg2

conn = psycopg2.connect(
    database = 'postgres',
    user = 'postgres',
    password = 'password',
    host = 'localhost',
    port = '5432'
)

conn.autocommit = True
cur = conn.cursor()

cur.execute("CREATE DATABASE linkupdb;")

print("db created!")
# DON'T USE