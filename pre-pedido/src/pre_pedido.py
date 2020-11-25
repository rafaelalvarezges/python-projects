import resources as res
import datetime
from templates import template_soap, referencia, campanya, oferta
import requests
import re
import lxml.etree as ET


conn = res.devolverConnOracle()
csr = conn.cursor()

dict_selects = {
        #Select para pruebas. Para ponerlo en marcha, habrá que sustituir la select de pedidos_proveedor_head por
        #select codemp, numped from pedidos_proveedor where estado = 'P' and estptl = 'V'.
        #disponibildad, precio unitario efectivo
        #pedidos schneider con estado ptl V o e, no se pueden enviar por ptl. "para garantizar que el pedido ha sido adpatado a las especificaciones de schneider"        
        
        'pedidos_proveedor_head':'''select codemp, numped, idzoe, idzcam
                                      from pedidos_proveedor
                                      where codemp = '065'
                                        and numped = 245123 ''',
        'pedidos_proveedor_det':'''Select codmar, artpro, unidad
                                      from detalle_pedidos_proveedor
                                      where codemp = '{CODEMP}'
                                        and numped = {NUMPED}'''

}


def enviar_soap(str_soap):
  url = 'https://servicios.schneiderelectric.es/electro/getMultiDataWSDL.php'
  headers = {
    'Content-Type':'application/soap+xml'
  }

  str_soap = re.sub(r'\n','',str_soap)
  str_soap = re.sub(r'\s+',' ', str_soap)
  req = requests.post(url,headers= headers,data=str_soap)
  parser = ET.XMLParser(recover=True)
  tree = ET.ElementTree(ET.fromstring(str.encode(req.text), parser=parser))
  tree_to_print = (ET.tostring(tree, pretty_print=True)).decode('utf-8')
  with open('prueba.xml','wt') as xml_file:
    xml_file.write(tree_to_print)
    xml_file.close
  

def consultar_datos_pedido():

    hoy = datetime.datetime.now()
    dia = hoy.day
    mes = hoy.month
    anio = hoy.year
    hora = hoy.hour
    minut = hoy.minute
    sec = hoy.second

    str_refs = ''
    num_ref = 1
    # Empezamos trayendonos de base de datos los pedidos que están pendientes de tratar
    rdo = res.ejecutarSelect(csr, dict_selects['pedidos_proveedor_head'])
    for r in rdo:
        codemp, numped = (r[0], r[1])        
        idzoe, idzcam = (r[2], r[3])
        str_select = dict_selects['pedidos_proveedor_det'].format(CODEMP=codemp, NUMPED=numped)
        rdo_ped_prov_det = res.ejecutarSelect(csr, str_select)        
        str_ofe = ''
        if idzoe != None:
          str_ofe = oferta.format(oferta=idzoe)
        str_camp = ''
        if idzcam != None:
          str_camp = campanya.format(campanya=idzcam)
        for rppd in rdo_ped_prov_det:
          str_ref = referencia.format(id_ref=num_ref,codart=rppd[1],cantidad=rppd[2],dia=dia, mes=mes, anyo=anio, hora=hora, min=minut,segundo=sec,campanya=str_camp,oferta=str_ofe)
          str_refs+=str_ref
          num_ref+=1
        str_soap = template_soap.format(anyo=anio, mes=mes,dia=dia,hora=hora,min=minut, seg=sec, referencia=str_ref,codemp=codemp)
        enviar_soap(str_soap)

        


if __name__ == "__main__":
    consultar_datos_pedido()