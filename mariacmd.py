import mariadb
import sys
import time

# Instantiate Connection
try:
   conn = mariadb.connect(
      user="root",              # root
      password="o87525o135",     # fill your password
      host="localhost",
      port=3306)
except mariadb.Error as e:
   print(f"Error connecting to MariaDB Platform: {e}")
   sys.exit(1)
print("database connected")


# Instantiate Cursor
cur = conn.cursor()


def terminate():
    conn.close()
    print("terminated mariadb")


# create database
def createdb(name):
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {name};")
    print(f"created database {name}")


# use DATABASE
def usedb(name):
    cur.execute(f"USE {name};")
    print(f"using database {name}")


# create table
def create_table(dbname, tname, col):
    cur.execute(f'CREATE TABLE IF NOT EXISTS {dbname}.{tname}({col});')
    print(f"table {tname} created")


# drop table
def drop_table(dbname, tname):
    cur.execute(f'DROP TABLE {dbname}.{tname};')
    print(f"droped table {tname}")


# Adds row
def add_row(dbname, tname, pname, ptype, pprice):
   """Adds the given contact to the contacts table"""

   cur.execute(f'INSERT INTO {dbname}.{tname}(Pname, Ptype, Pprice) VALUES ("{pname}", "{ptype}", {pprice});')
   conn.commit()
   print("row added")


 # Print List of Contacts
def show_table(col, dbname, tname):
   """Retrieves the list of contacts from the database and prints to stdout"""

   # Initialize Variables
   contacts = []

   # Retrieve Contacts
   cur.execute(f"SELECT {col} FROM {dbname}.{tname}")

   # Prepare Contacts
   for row in cur:
      contacts.append(str(row))

   # List Contacts
   print("\n".join(contacts))
   print(f"row count : {len(contacts)}")
'''
def update_row(counter):
   """Adds the given contact to the contacts table"""
   cur.execute(f"UPDATE car_db.part SET Pprice = '696969' WHERE Pid = {counter} ")
   conn.commit()
   print("row update")

start_time = time.perf_counter_ns()
stop_time = start_time + (60 * 1000000000)
prev_time = time.perf_counter_ns()
count = 1
while(time.perf_counter_ns() < stop_time):
    update_row(count)
    count += 1
    print(f"{time.perf_counter_ns() - prev_time} ns")
    prev_time = time.perf_counter_ns()
print("=============== TIME OUT ===============")
print("Row Updated:"+str(count-1)+"(in 60 second)")
print(f"total time {time.perf_counter_ns() - start_time} ns")
'''
'''
def update_row(counter):
   """Adds the given contact to the contacts table"""
   cur.execute(f"UPDATE car_db.part SET Pprice = '696969' WHERE Pid = {counter} ")
   conn.commit()
   print("row update")


def delete_row(counter):
   cur.execute(f"DELETE FROM car_db.part WHERE Pid = {counter} ")
   conn.commit()
   print("row delete")


start_time = time.perf_counter_ns()
stop_time = start_time + (60 * 1000000000)
prev_time = time.perf_counter_ns()
count = 1
while(time.perf_counter_ns() < stop_time):
    #update_row(count)
    delete_row(count)
    count += 1
    print(f"{time.perf_counter_ns() - prev_time} ns")
    prev_time = time.perf_counter_ns()
print("=============== TIME OUT ===============")
print("Row Deleted : "+str(count)+"(per 60 second)")
print(f"total time {time.perf_counter_ns() - start_time} ns")'''

def insert_row(counter):
   cur.execute(f"INSERT INTO car_db.manufacturer(MAname) VALUE ('Wasawat')")
   conn.commit()
   print("row delete")

def update_row(counter):
   """Adds the given contact to the contacts table"""
   cur.execute(f"UPDATE car_db.part SET Pprice = '696969' WHERE Pid = {counter} ")
   conn.commit()
   print("row update")


def delete_row(counter):
   cur.execute(f"DELETE FROM car_db.part WHERE Pid = {counter} ")
   conn.commit()
   print("row delete")

start_time = time.perf_counter_ns()
stop_time = start_time + (60 * 1000000000)
prev_time = time.perf_counter_ns()
count = 1
while(time.perf_counter_ns() < stop_time):
    #update_row(count)
    insert_row(count)
    count += 1
    print(f"{time.perf_counter_ns() - prev_time} ns")
    prev_time = time.perf_counter_ns()
print("=============== TIME OUT ===============")
print("Row Inserted : "+str(count)+"(per 60 second)")
print(f"total time {time.perf_counter_ns() - start_time} ns")