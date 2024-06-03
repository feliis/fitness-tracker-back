import os

import psycopg2
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
                username VARCHAR NOT NULL,
                password VARCHAR NOT NULL,
                birthday DATE NOT NULL,
                sex BOOLEAN NOT NULL,
                height REAL NOT NULL,
                weight REAL NOT NULL
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
                IF NOT EXISTS Workout(
                    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
                    user_id uuid NOT NULL,
                    steps INTEGER NOT NULL,
                    distance REAL NOT NULL,
                    speed REAL NOT NULL,
                    pace REAL NOT NULL,
                    calories INTEGER NOT NULL,
                    duration VARCHAR NOT NULL ,
                    FOREIGN KEY (user_id)
                        REFERENCES users (id) 
                );
        '''
    )
    conn.commit()

def new_user(conn):
    cur = conn.cursor()


def valedate_user(name, password):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT * FROM Users where name='{name}' """)
    user = cur.fetchone()
    if user and user['password'] == password:
        return {'id': user['id'], 'name':user['name'], 'success':True}
    else:
        return {'success':False}

def create_user(name, sex, birthday, password):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT * FROM Users where name='{name}' """)
    user = cur.fetchone()
    if user:
        return {'success':False}
    else :
        cur.execute(
            f"""INSERT into Users (name, sex, birthday, password) VALUES ('{name}', '{sex}', '{birthday}', '{password}')""")
        conn.commit()

        cur.execute(f"""SELECT * FROM users where name='{name}' """)
        user = cur.fetchone()
        return {'id': user['id'], 'name': user['name'], 'success': True}


def get_user_info (id):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT * FROM users where id = '{id}' """)
    info = cur.fetchone()
    print(info)
    cur.close()
    return info

def create_workout(user_id, steps, distance, speed, pace, calories, duration):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
            f"""INSERT into Workout (user_id, steps, distance, speed, pace, calories, duration) VALUES 
            ('{user_id}', '{steps}', '{distance}', '{speed}', '{pace}', '{calories}', '{duration}')""")
    conn.commit()
    
    # cur.execute(f"""SELECT * FROM workout where user_id='{user_id}' """)
    # workout = cur.fetchall()
    # return [{'user_id': workout['user_id'], 'steps': workout['steps'], 'distance': workout['distance'], 'speed': workout['speed'], 'pace': workout['pace'],
    #         'calories': workout['calories'], 'duration': workout['duration']}]

def get_workout_info(id):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT * FROM workout where user_id = '{id}' """)
    workout = cur.fetchall()
    print(workout)
    cur.close()
    return {"rows": workout}

if __name__ == "__main__":
    init_tables()
    #print(get_user_info())