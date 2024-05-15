import sqlite3
import psycopg2
from utils import dict_factory
import os
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

conn = psycopg2.connect(
    database = os.getenv('DB'),
    user = os.getenv('USER_DB'),
    password = os.getenv('PASS_DB'),
    host = os.getenv('HOST_DB'),

)

def init_tables():
    cur = conn.cursor()
    cur.execute(
        '''CREATE TABLE 
            IF NOT EXISTS Users(
                id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
                name VARCHAR NOT NULL,
                age INTEGER NOT NULL,
                gender VARCHAR NOT NULL,
                password varchar NOT NULL
            );
            CREATE TABLE 
                IF NOT EXISTS Goals(
                    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
                    user_id uuid NOT NULL,
                    goals_type VARCHAR(50) NOT NULL,
                    target_value DECIMAL(8) NOT NULL,
                    deadline DATE,
                    FOREIGN KEY (user_id)
                        REFERENCES users (id) 
                );
            CREATE TABLE 
                IF NOT EXISTS Activity(
                    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
                    user_id uuid NOT NULL,
                    steps INTEGER NOT NULL,
                    dist DECIMAL(8,2) NOT NULL,
                    speed DECIMAL(8,1) NOT NULL,
                    cal DECIMAL(8) NOT NULL,
                    time TIME NOT NULL ,
                    FOREIGN KEY (user_id)
                        REFERENCES users (id) 
                );
        '''
    )
    conn.commit()

def new_user(conn):
    cur = conn.cursor()


def valedate_user(name,password):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT * FROM Users where name='{name}' """)
    user = cur.fetchone()
    print(user['password'])
    if user and user['password'] == password:
        return {'id': user['id'], 'name':user['name'], 'success':True}
    else:
        return {'success':False}


def get_user_info ():
    cur = conn.cursor()
    # Select all products from the table
    cur.execute('''SELECT * FROM Users ''')

    # Fetch the data
    info = cur.fetchall()

    cur.close()
    conn.close()

    return info

if __name__ == "__main__":
    init_tables()
    print(get_user_info())