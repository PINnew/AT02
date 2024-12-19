import sqlite3

def init_db():
   conn = sqlite3.connect(':memory:')  # сохраняем в оперативной памяти
   cursor = conn.cursor()
   cursor.execute('''
   CREATE TABLE IF NOT EXISTS users (
   id INTEGER PRIMARY KEY,
   name TEXT,
   age INTEGER)
   ''')
   return conn

def add_user(conn, name, age):   # будем добавлять пользователей
   cursor = conn.cursor()
   cursor.execute('''
   INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
   conn.commit()

def get_user(conn, name):  # будем извлекать информацию из нашей базы данных
   cursor = conn.cursor()
   cursor.execute('''SELECT * FROM users WHERE name=?''', (name,))
   return cursor.fetchone()
