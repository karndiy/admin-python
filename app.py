import sqlite3
from c_crud import SqliteDB
db = SqliteDB('customer.db')

# perform database operations using the methods of the class
#data = {'name': 'John Doe', 'email': 'johndoe@example.com', 'phone': '1234567890'}
#db.insert('customers', data)

rows = db.select('SELECT * FROM customers')
for row in rows:
    print(row)

print('#'*10)

db.update('customers', {'name': 'Jane Doe', 'phone': '555-6666'}, 'id = 1')

rows = db.select('SELECT * FROM customers')
for row in rows:
    print(row)
print('#'*10)

#db.delete('customers', 'id = 2')

# don't forget to close the database connection when you're done
del db
