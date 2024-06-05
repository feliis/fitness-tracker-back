import os
import json
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
                name VARCHAR NOT NULL,
                lastname VARCHAR NOT NULL,
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
                    duration TIME WITH TIME ZONE NOT NULL ,
                    date_start DATETIME NOT NULL,
                    date_stop DATETIME NOT NULL,
                    FOREIGN KEY (user_id)
                        REFERENCES users (id) 
                );
        '''
    )
    conn.commit()

def new_user(conn):
    cur = conn.cursor()


def valedate_user(username, password):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT * FROM Users where username='{username}' """)
    user = cur.fetchone()
    if user and user['password'] == password:
        return {'id': user['id'], 'username':user['username'], 'success':True}
    else:
        return {'success':False}

def create_user(name, lastname, username, sex, birthday, height, weight, password):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT * FROM Users where username='{username}' """)
    user = cur.fetchone()
    if user:
        return {'success':False}
    else :
        cur.execute(
            f"""INSERT into Users (name, lastname, username, sex, birthday, height, weight, password) 
                VALUES ('{name}','{lastname}','{username}', '{sex}', '{birthday}','{height}','{weight}', '{password}')""")
        conn.commit()

        cur.execute(f"""SELECT * FROM users where username='{username}' """)
        user = cur.fetchone()
        return {'id': user['id'], 'username': user['username'], 'success': True}


def get_user_info (id):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT * FROM users where id = '{id}' """)
    info = cur.fetchone()
    print(info)
    cur.close()
    return info

def create_workout(user_id, steps, distance, speed, pace, calories, duration, date_start, date_stop):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
            f"""INSERT into Workout (user_id, steps, distance, speed, pace, calories, duration, date_start, date_stop) VALUES 
            ('{user_id}', '{steps}', '{distance}', '{speed}', '{pace}', '{calories}', '{duration}','{date_start}','{date_stop}')""")
    conn.commit()
    

def get_workouts(id):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT * FROM workout where user_id = '{id}' """)
    workouts = cur.fetchall()
    print(workouts)
    cur.close()
    workouts = [dict(w) for w in workouts ]
    j = {"rows": workouts }
    print(j)
    return json.dumps(j, indent=4, sort_keys=True, default=str)

def get_workout_info(id):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f"""SELECT * FROM workout where id = '{id}' """)
    workout = cur.fetchone()
    print(workout)
    cur.close()
    return json.dumps(workout, indent=4, sort_keys=True, default=str)

if __name__ == "__main__":
    init_tables()
    #print(get_user_info())