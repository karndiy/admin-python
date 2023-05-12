import sqlite3

class SqliteDB:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    
    def execute(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def select(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows
    
    def insert(self, table_name, data):
        fields = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        query = f"INSERT INTO {table_name} ({fields}) VALUES ({placeholders})"
        return self.execute(query, tuple(data.values()))
    
    def update(self, table_name, data, condition):
        fields = ', '.join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {table_name} SET {fields} WHERE {condition}"
        return self.execute(query, tuple(data.values()))
    
    def delete(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        return self.execute(query)
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()
