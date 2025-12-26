import os
import time
import psycopg

host = os.getenv("POSTGRES_HOST", "db")
port = int(os.getenv("POSTGRES_PORT", 5432))

while True:
    try:
        conn = psycopg.connect(
            host=host,
            port=port,
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", ""),
            dbname=os.getenv("POSTGRES_DB", "linkupdb"),
        )
        conn.close()
        print("postgres is ready")
        break
    except psycopg.OperationalError:
        print("waiting for postgress")
        time.sleep(1)
