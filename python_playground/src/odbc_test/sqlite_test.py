import sqlite3
import pyodbc


# https://db-engines.com/en/ranking
def get_conn(db_file):
    conn = sqlite3.connect(db_file)
    # conn = pyodbc.connect("DRIVER={SQLite3 ODBC Driver};SERVER=localhost;DATABASE=test1.db;Trusted_connection=yes")
    return conn


def create_table(conn):
    sql = '''
    CREATE TABLE IF NOT EXISTS projects (
        proj_id INTEGER PRIMARY KEY, 
        proj_name TEXT NOT NULL, 
        begin_date TEXT, 
        end_date TEXT
    );
    '''

    cursor = conn.cursor()
    cursor.execute(sql)

    cursor.execute('SELECT * FROM projects')

    sql = '''
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY, 
        task_name TEXT NOT NULL,
        priority INTEGER,
        proj_id INTEGER NOT NULL,
        status_id INTEGER NOT NULL,
        begin_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        FOREIGN KEY (proj_id) REFERENCES project(id)
    );
    '''

    cursor = conn.cursor()
    cursor.execute(sql)

    cursor.execute('SELECT * FROM tasks')


def drop_table(conn):
    sql = '''
    DROP TABLE IF EXISTS projects
    '''

    cursor = conn.cursor()
    cursor.execute(sql)

    sql = '''
    DROP TABLE IF EXISTS tasks
    '''

    cursor = conn.cursor()
    cursor.execute(sql)


def crud(conn):
    sql = ''' INSERT INTO projects(proj_name, begin_date, end_date)
              VALUES(?, ?, ?) '''

    cursor = conn.cursor()
    cursor.execute(sql, ('p1', '2015-01-01', '2015-01-31'))

    sql = ''' INSERT INTO tasks(task_name, priority, status_id, proj_id, begin_date, end_date)
              VALUES(?, ?, ?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, ('t1', 0, 0, 1, '2015-01-01', '2015-01-31'))

    conn.commit()


if __name__ == '__main__':
    conn = get_conn('test1.db')
    try:
        # drop_table(conn)
        # create_table(conn)
        crud(conn)
    finally:
        conn.close()