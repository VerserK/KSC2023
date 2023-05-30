import pymssql


def conn():
    try :
        conn = pymssql.connect('skcdwhprdmi.siamkubota.co.th', 'DWH_CS', 'Skc@cs60281', "Service Data", 'utf8')
            
        return conn
    except Exception as error:
        print(error)
        return 'ER'