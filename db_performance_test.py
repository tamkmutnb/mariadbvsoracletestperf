import mariadb
import sys
import time

# Instantiate Connection
"""
import cx_Oracle
import  time
dsn_tns = cx_Oracle.makedsn('127.0.0.1', '1521', service_name='ORCL') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user=r'c##tamtong007', password='o87525o135', dsn=dsn_tns)"""

try:
   conn = mariadb.connect(
      user="root",              # root
      password="o87525o135",     # fill your password
      host="localhost",
      port=3306,
      autocommit=False)
except mariadb.Error as e:
   print(f"Error connecting to MariaDB Platform: {e}")
   sys.exit(1)
print("database connected")


# Instantiate Cursor
cur = conn.cursor()
#conn.autocommit = False
def insert_row(counter):
   cur.execute(f"INSERT INTO car_db.MANUFACTURER(MANAME) VALUES ('Wasawat')")

def update_row(counter):
   """Adds the given contact to the contacts table"""
   cur.execute(f"UPDATE car_db.PART SET PPRICE = '696969' WHERE PID = {counter}")

def delete_row(counter):
   cur.execute(f"DELETE FROM car_db.part WHERE Pid = {counter} ")

start_time = time.perf_counter_ns()
stop_time = start_time + (60 * 1000000000)
prev_time = time.perf_counter_ns()
count = 1
while(time.perf_counter_ns() < stop_time):
    try:
        #insert_row(count)
        #update_row(count)
        delete_row(count)
        count += 1
        prev_time = time.perf_counter_ns()
    except:
        break
print("=============== TIME OUT ===============")
print("Row Deleted : "+str(count)+"(per 60 second)")
print(f"total time {time.perf_counter_ns() - start_time} ns")