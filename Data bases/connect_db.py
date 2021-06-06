import cx_Oracle as Oracle
from read_db_config import read_db_con

db_conf = read_db_con()
connection_pool = Oracle.SessionPool(db_conf.get('user'), db_conf.get('password'),
                                     min=2, max=5, increment=1, threaded=True, getmode=Oracle.SPOOL_ATTRVAL_WAIT)
# mode = SPOOL_ATTRVAL_WAIT means that waiting time for a get session before giving a error

try:
    # con: object = Oracle.connect(db_conf.get('user') + "/" + db_conf.get('password'))
    con = connection_pool.acquire()
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

# References : https://cx-oracle.readthedocs.io/en/latest/api_manual/module.html
