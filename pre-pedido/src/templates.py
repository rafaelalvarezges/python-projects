template_soap = '''
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:elec="http://Electronet.B2B.Schemas.Fabricante.Consultas">
   <soap:Header/>
   <soap:Body>
      <elec:documento_ptl version="?">
         <info_control>
            <transaccion id="1" test="1">
               <fecha_creacion>
                  <anyo>{anyo}</anyo>
                  <mes>{mes}</mes>
                  <dia>{dia}</dia>
                  <hora>{hora}</hora>
                  <minuto>{min}</minuto>
                  <segundo>{seg}</segundo>
                  <msegundo></msegundo>
               </fecha_creacion>
               <fecha_modificacion>
                  <anyo>{anyo}</anyo>
                  <mes>{mes}</mes>
                  <dia>{dia}</dia>
                  <hora>{hora}</hora>
                  <minuto>{min}</minuto>
                  <segundo>{seg}</segundo>
                  <msegundo></msegundo>
               </fecha_modificacion>
               <estado></estado>
            </transaccion>
            <info_tipo url_xsd="?" version="0.6">?</info_tipo>
            <interlocutores>
               <origen>
                  <tipo id_usuario="143_GRUPO_ELECTRO_STOCKS" id_grupo=""/>
               </origen>
               <destino>
                  <tipo id_usuario="" id_grupo=""/>
               </destino>
            </interlocutores>
         </info_control>
         <datos_doc>
          <consulta_materiales version="?">
               <solicitante>GES{codemp}</solicitante>
               <destinatario></destinatario>
               {referencia}
          </consulta_materiales>
         </datos_doc>
         <!--Optional:-->
         <mensajes>
            <severidad></severidad>
            <msg_ptl id="1">1</msg_ptl>
            <msg_funcional id="1"></msg_funcional>
         </mensajes>
      </elec:documento_ptl>
   </soap:Body>
</soap:Envelope>
'''

referencia = '''
   <referencias id="{id_ref}">   
            <referencia>{codart}</referencia>
               <fecha>
                  <anyo>{anyo}</anyo>
                  <mes>{mes}</mes>
                  <dia>{dia}</dia>
                  <hora>{hora}</hora>
                  <minuto>{min}</minuto>
                  <segundo>{segundo}</segundo>
                  <msegundo></msegundo>
               </fecha>
               <cantidad>{cantidad}</cantidad>
               <!--Optional:-->
               {campanya}
               <!--Optional:-->
               {oferta}
               <extra></extra>
</referencias>
'''

campanya = '''<campanya>{campanya}</campanya>'''
oferta = '''<oferta>{oferta}</oferta>'''