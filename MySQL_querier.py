# SQL Query executer from Python. This uses the MySQLdb module


import MySQLdb

QUIT = "Q"

def connect_to_database():
    connect_to = input("Host server (e.g. localhost): ")
    dbase_name = input("Name of Database to connect to: ")
    user_name = input("User Id: ")
    pw = input("Password: ")

    try:
        db = MySQLdb.connect(connect_to,user_name,pw,dbase_name)
    except:
        print("Unable to make a connection to the database. Check input parameters")
    else:
        print("Successful connection to:", dbase_name)
        return db.cursor()
    return


def accept_sql(cursor):
    sql_command = ""
    while str.upper(sql_command) != QUIT:
        sql_command = input("provide a SQL statement or Q to quit:")
        if str.upper(sql_command) == QUIT: break # Exit Condition
        execute_sql(cursor, sql_command)
    return


def execute_sql(cursor, sql_command):
    if cursor is None:
        print("No database connection has been made")
    else:
        try:
            cursor.execute(sql_command)
        except:
            print("Error in execution of SQL. No data returned")
        else:
            num_rows = cursor.rowcount
            print("Execution successful", num_rows, "returned")
            command = ""
            while str.upper(command) != QUIT:
                command = str.upper(input("Y to see next record, 1 for first record, L for last, Q for new SQL statement: "))
                if command == QUIT:
                    print("Query results abandoned")
                    break
                if command == "1":
                    print("feature not yet implemented")
                elif command != "Y":
                    print("Unrecognised input")
                else:
                    data = cursor.fetchone()
                    print(data)
    return

cursor = connect_to_database()
accept_sql(cursor)


            
            

            

                
            
                
        
