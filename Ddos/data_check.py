mydb
def start_Connection():
    import mysql.connector
    global mydb 
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )

def insert_user(username , password):
    mycursor = mydb.cursor()
    mycursor.execute("use Users ")
    sql = "INSERT INTO person (name, password) VALUES (%s, %s)"
    val = (username , password )
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.rowcount

def get_user(username , password):
        mycursor = mydb.cursor()
        mycursor.execute("use Users")
        sql = " select * from person where name =%s  and password = %s"
        val = (username , password )
        mycursor.execute(sql, val)
        return len(mycursor.fetchall())














# connection_info = mydb.__dict__
# for data in connection_info:
#     print(data ," => ",connection_info[data])
    
# print(connection_info['_socket'].__dict__)


