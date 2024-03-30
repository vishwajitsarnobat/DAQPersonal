from datetime import datetime
import sqlite3

def database_connect():
    global database, cursor, table
    try:
        database = sqlite3.connect('daq.db')
        print("Connected to database 'daq' successfully")
        cursor = database.cursor()

        table = """ CREATE TABLE PINDATA (
            TIMESTAMP TEXT,
            PIN1 INTEGER,
            PIN2 INTEGER,
            PIN3 INTEGER,
            PIN4 INTEGER,
            PIN5 INTEGER,
            PIN6 INTEGER,
            PIN7 INTEGER,
            PIN8 INTEGER,
            PIN9 INTEGER
        ); """

        cursor.execute(table)
        print("Created table 'PINDATA' successfully")
    
    except:
        print("Connected to table 'PINDATA' successfully")

def database_store():
    result_list = ["Hello", 1, 3, 4, 5, 6, 7, 4, 8, 7]
    # current_time = datetime.now()
    # formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")
    # result_list.append(formatted_time)
    # line = ser.readline()
    # for byte in line:
    #     if byte == ord('0'): # this checks if byte(which is converted to ASCII automatically) matches with 0s ASCII.
    #         result_list.append(0) # byte will print ASCII value of 0, hence this is needed.
    #     elif byte == ord('1'):
    #         result_list.append(1)
        
    cursor.execute('''INSERT INTO PINDATA VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', tuple(result_list))
    

def database_disconnect():
    if database:
        database.commit()
        database.close()
        print('SQLite Connection closed')