import pymssql


def conn():
    try :
        conn = pymssql.connect('localhost', 'sa', '702481007zz', "mtokm", 'utf8')
            
        return conn
    except Exception as error:
        print(error)
        return 'ER'