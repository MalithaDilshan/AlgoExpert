import cx_Oracle as Oracle


try:
    con: object = Oracle.connect('###/&&&')
except Oracle.DatabaseError as error:
    print('Error occurred when connecting into the database: ', str(error.args[0]))
else:
    try:
        cursor = con.cursor()
        cursor.execute('select * from emp')
        rows = cursor.fetchall()
        for row in rows:
            print(str(row) + '\n')
    except Oracle.DatabaseError as error:
        print('Error occurred', error)
    except Exception as error:
        print('Error occurred: ' + str(error))
    finally:
        if cursor:
            cursor.close()
finally:
    if con:
        con.close()
