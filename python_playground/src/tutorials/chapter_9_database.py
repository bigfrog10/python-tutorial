import sqlite3
import pyodbc


# https://db-engines.com/en/ranking
# There are 2 ways to get database connections:
#     vendor specific API
#     ODBC interface
# ODBC is a universal interface, easy to switch different databases. Vendor API
# could be faster and with more features.
def get_conn(db_file):
    # conn = sqlite3.connect(db_file)

    # to use odbc, download sqlite 3 odbc driver from http://www.ch-werner.de/sqliteodbc/.
    # windows version is: http://www.ch-werner.de/sqliteodbc/sqliteodbc_w64.exe
    # mac version is: http://www.ch-werner.de/sqliteodbc/sqliteodbc-0.9993.dmg
    driver = '{SQLite3 ODBC Driver}'
    server = 'localhost'
    database = db_file
    conn = pyodbc.connect(f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_connection=yes")
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
    conn.commit()

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
    conn.commit()

    cursor.execute('SELECT * FROM tasks')


def drop_table(conn):
    sql = '''DROP TABLE IF EXISTS projects'''
    cursor = conn.cursor()
    cursor.execute(sql)

    sql = '''DROP TABLE IF EXISTS tasks'''
    cursor = conn.cursor()
    cursor.execute(sql)

    conn.commit()


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

    # update

    # delete


if __name__ == '__main__':
    conn = get_conn('test1.db')
    try:
        # drop_table(conn)
        # create_table(conn)
        crud(conn)
    finally:
        conn.close()
