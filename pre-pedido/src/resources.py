import cx_Oracle as ora

def devolverConnOracle():
    try:
      cifra = ora.makedsn(
              "opclnxdbprod01.subnet150.gesvcn.oraclevcn.com", "1521",
              service_name="cifrapdb.subnet150.gesvcn.oraclevcn.com")
      cifra_con = 'gestion/manager@'+cifra
      connOra = ora.connect(cifra_con)
      return connOra
    except: 
      raise

def ejecutarSelect(cur, select, records='ALL'):
    cur.execute(select)
    if records == 'ALL':
        return cur.fetchall()
    else:
        return cur.fetchone()