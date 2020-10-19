import mysql.connector
from mysql.connector import Error

try:
    cnx = mysql.connector.connect(host='127.0.0.1',
                                  database='python',
                                  user='adrigo',
                                  password='1234')
    sql_select_Query = "select * from alumnos"
    cursor = cnx.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in alumnos is: ", cursor.rowcount)
    print("\nAlumnos:")
    for row in records:
        print("  Id = ", row[0], )
        print("  nombre = ", row[1])
        print("  edad  = ", row[2])
        print()

except Error as e:
    print("Error reading data from MySQL table", e)

finally:
    if (cnx.is_connected()):
        cnx.close()
        cursor.close()
        print("Cerrada conexion de mysql")
