import sqlite3

URL_DATABASE = 'models/db_matcon.db'

def connect_db():
    # cria a conexão
    conn = sqlite3.connect(URL_DATABASE)
    return conn
