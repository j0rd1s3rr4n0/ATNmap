 #!/usr/bin/env python
# encoding: utf-8
import os
# replace in conditionals 'si' & 'no' for in list
si_list = ['si','yes','s','y']
no_list = ['no','n']


#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                               MENU PRINCIPAL
print(chr(27)+"[3;32m"'''
                  BIENVENIDO A LA PRIMERA VERSION DE ATNmap (Asistente de Trabajo de Nmap)

                    por: OjeadorParker/malajunta/\n                                    ''')+chr(27)
while True:
    print(chr(27)+"[3;32m"'''                            [1] Escaner de Puertos\t

                            [2] Escaner Avanzado\t

                            [3] Salir
            ORGIEN                                                  DESTINO

                    |                                           |
    SINCRONIZACION  |  >·                                       |
                    |       ·                                   |
                    |           ·      SYN                      |
                    |               ·   >                       |
                    |                   ·                       |
                    |                       ·                   |
                    |                           ·               |
                    |                               ·           |
                    |                                   ·       |
                    |                                       >   |   SINCRONIZACION-ACEPTADA
                    |                                       <   |
                    |                SYN-ACK             ·      |
                    |                   <           ·           |
                    |                           ·               |
                    |                       ·                   |
                    |                   ·                       |
                    |               ·                           |
                    |           ·                               |
                    |       ·                                   |
                    |   ·                                       |
        ACEPATADA   |·                                          |
                    |   ·             ACK                       |
                    |       ·          >                        |
                    |           ·                               |
                    |               ·                           |
                    |                   ·                       |
                    |                       ·                   |
                    |                           ·               |
                    |                               ·           |
                    |                                   ·       |
                    |                                      ·    |   CONECTADO''')+chr(27)+"[0m"





    selectorMenu = raw_input('Seleccione una opcion > ')
    selectorMenu = selectorMenu.lower()
#............................................................................................................................................
#                                    OPCION 1, MENU ESCANER DE PUERTOS

    if selectorMenu == '1':
        print('''
                                            SELECCIONE EL TIPO DE ESCANEO DE PUERTOS A REALIZAR\n
            N  NOMBRE           OPCION EN NMAP       FUNCIONAMIENTO                                                    TIPO

            1- Connect ---------[-sT]----------[Envia un SYN,luego un RST para cerrar conexion,detecta los protocolos]-[TCP]

            2. SYN Stealth -----[-sS]----------[Envia un SYN,sigilosa ya que no llega a completar la conexion]---------[TCP]

            3. UDP Scan --------[-sU]----------[Envia un UDP vacio, mas lento que el sonde a TCP]----------------------[UDP]

            4. TCP ACK ---------[-sA]----------[Envia un ACK vacio, determina cerrado o abierto]-----------------------[TCP]

            5. TCP NULL --------[-sN]----------[Envia TCP con todos los flags a 0]-------------------------------------[TCP]

            6. TCP FIN ---------[-sF]----------[Envia un TCP con el flag FIN a 1]--------------------------------------[TCP]

            7. XMas SCan -------[-sX]----------[Envia TCP con los flags FIB, PSH y URG a 1]----------------------------[TCP]

            8. TCP Maimon ------[-sM]----------[Envia ACK con el flag FIN a 1]-----------------------------------------[TCP]

            9. TCP Window ------[-sW]----------[Envia ACK vacio, muy parecido ACK Stealth, no siempre fiable]----------[TCP]

            10. IP Protocolo ---[-sO]----------[Envia paquetes IP con cabeceras vacias except(TCP,UDP, e ICMP)]

            11. SCTP INIT ------[-sY]----------[Envia paquetes SCTP INIT(inicio de conexion) equivalente TCP SYN]------[TCP]

            12. SCTP Cookie Echo [-sZ]---------[Envia paquetes SCTP Cookie Echo(3er fase conexion)util cortafuegos sin estado]


        ''')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                               FORMULARIO COMANDOS ESCANER PUERTOS

        while True:
            selectorPuerto = raw_input('Seleccione un opcion > ')
            selectorPuerto = selectorPuerto.lower()


            versionSistema = raw_input('Teclee SI, para saber la version del sistema [-sV] enter para NO > ')
            versionSistema = versionSistema.lower()

            if versionSistema == 'si':
                versionSistema = '-sV '
            else:
                versionSistema = ''

            puerto = raw_input('ingrese -F para los 100 puertos mas comunes, -p para un rango de puertos y -p- para todos los puertos > ')
            puerto = puerto.lower()
            noPing = raw_input('Quiere hacer ping en el objetivo? SI o enter para NO > ')
            noPing = noPing.lower()

            if noPing == 'si':
                noPing = '-Pn '
            else:
                noPing = ''

            host = raw_input('ingrese el host > ')
            host = host.lower()
            vervosidad = raw_input('Quiere vervosidad? -v normal -vv mucha, enter ninguna > ')
            vervosidad = vervosidad.lower()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                               CONSTRUCTORES Y EJECUCION



            if selectorPuerto == '1':

                class ComandosPuertos1:
                    def __init__(self,c2,c3,c4,c5,c6):
                        self.versionSistema = c2
                        self.puerto = c3
                        self.noPing = c4
                        self.host = c5
                        self.vervosidad = c6
                        self.final = 'nmap -sT '+c2+' '+c3+' '+c4+' '+c5+' '+c6

                comando1 = ComandosPuertos1(versionSistema,puerto,noPing,host,vervosidad)
                print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comando1.final)+chr(27)+"[0m"
                os.system(comando1.final)
                print(chr(27)+"[3;32m"'''
                         CERRADO: recibimos paquete RST
                         ABIERTO: recibimos paquete SYN/ACK
                         FILTRADO: recibimos paquete ICMP inalcanzable o expiracion del TIMEOUT''')+chr(27)+"[0m"


            if selectorPuerto == '2':
                class ComandosPuertos1:
                    def __init__(self,c2,c3,c4,c5,c6):

                        self.versionSistema = c2
                        self.puerto = c3
                        self.noPing = c4
                        self.host = c5
                        self.vervosidad = c6
                        self.final = 'nmap -sS '+c2+' '+c3+' '+c4+' '+c5+' '+c6

                comando1 = ComandosPuertos1(versionSistema,puerto,noPing,host,vervosidad)
                print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comando1.final)+chr(27)+"[0m"
                os.system(comando1.final)
                print(chr(27)+"[3;32m"'''
                        CERRADO: recibimos RST
                        ABIERTO: recibimos SYN/ACK
                        FILTRADO: ICMP inalcanzable o expiracion del TIMEOUT''')+chr(27)+"[0m"

            if selectorPuerto == '3':

                class ComandosPuertos1:
                    def __init__(self,c2,c3,c4,c5,c6):
                        self.versionSistema = c2
                        self.puerto = c3
                        self.noPing = c4
                        self.host = c5
                        self.vervosidad = c6
                        self.final = 'nmap -sU '+c2+' '+c3+' '+c4+' '+c5+' '+c6

                comando1 = ComandosPuertos1(versionSistema,puerto,noPing,host,vervosidad)
                print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comando1.final)+chr(27)+"[0m"
                os.system(comando1.final)
                print(chr(27)+"[3;32m"'''
                        CERRADO: recibimos ICMP puerto inalcanzable
                        ABIERTO: Ha habido una respuesta
                        ABIERTO/FILTRADO: Expira el TIMEOUT
                        FILTRADO: Recibe otros ICMP inalcanzable''')+chr(27)+"[0m"

            if selectorPuerto == '4':

                class ComandosPuertos1:
                    def __init__(self,c2,c3,c4,c5,c6):
                        self.versionSistema = c2
                        self.puerto = c3
                        self.noPing = c4
                        self.host = c5
                        self.vervosidad = c6
                        self.final = 'nmap -sA '+c2+' '+c3+' '+c4+' '+c5+' '+c6

                comando1 = ComandosPuertos1(versionSistema,puerto,noPing,host,vervosidad)
                print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comando1.final)+chr(27)+"[0m"
                os.system(comando1.final)
                print(chr(27)+"[3;32m"'''
                        NO FILTRADO: recibimos RST
                        FILTRADO: recibimos ICMP error; expira el TIMEOUT
                        ''')+chr(27)+"[0m"


            if selectorPuerto == '5':

                class ComandosPuertos1:
                    def __init__(self,c2,c3,c4,c5,c6):
                        self.versionSistema = c2
                        self.puerto = c3
                        self.noPing = c4
                        self.host = c5
                        self.vervosidad = c6
                        self.final = 'nmap -sN '+c2+' '+c3+' '+c4+' '+c5+' '+c6

                comando1 = ComandosPuertos1(versionSistema,puerto,noPing,host,vervosidad)
                print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comando1.final)+chr(27)+"[0m"
                os.system(comando1.final)
                print(chr(27)+"[3;32m"'''
                        CERRADO: recibimos RST
                        ABIERTO/FILTRADO: expira el TIMEOUT
                        FILTRADO: ICMP inalcanzable''')+chr(27)+"[0m"


            if selectorPuerto == '6':

                class ComandosPuertos1:
                    def __init__(self,c2,c3,c4,c5,c6):
                        self.versionSistema = c2
                        self.puerto = c3
                        self.noPing = c4
                        self.host = c5
                        self.vervosidad = c6
                        self.final = 'nmap -sF '+c2+' '+c3+' '+c4+' '+c5+' '+c6

                comando1 = ComandosPuertos1(versionSistema,puerto,noPing,host,vervosidad)
                print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comando1.final)+chr(27)+"[0m"
                os.system(comando1.final)
                print(chr(27)+"[3;32m"'''
                        CERRADO: recibimos RST
                        ABIERTO/FILTRADO: expira el TIMEOUT
                        FILTRADO: ICMP inalcanzable''')+chr(27)+"[0m"

            if selectorPuerto == '7':

                class ComandosPuertos1:
                    def __init__(self,c2,c3,c4,c5,c6):
                        self.versionSistema = c2
                        self.puerto = c3
                        self.noPing = c4
                        self.host = c5
                        self.vervosidad = c6
                        self.final = 'nmap -sX '+c2+' '+c3+' '+c4+' '+c5+' '+c6

                comando1 = ComandosPuertos1(versionSistema,puerto,noPing,host,vervosidad)
                print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comando1.final)+chr(27)+"[0m"
                os.system(comando1.final)
                print(chr(27)+"[3;32m"'''
                        CERRADO: recibimos RST
                        ABIERTO/FILTRADO: expira el TIMEOUT
                        FILTRADO: ICMP inalcanzable''')+chr(27)+"[0m"

            if selectorPuerto == '8':

                class ComandosPuertos1:
                    def __init__(self,c2,c3,c4,c5,c6):
                        self.versionSistema = c2
                        self.puerto = c3
                        self.noPing = c4
                        self.host = c5
                        self.vervosidad = c6
                        self.final = 'nmap -sM '+c2+' '+c3+' '+c4+' '+c5+' '+c6

                comando1 = ComandosPuertos1(versionSistema,puerto,noPing,host,vervosidad)
                print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comando1.final)+chr(27)+"[0m"
                os.system(comando1.final)
                print(chr(27)+"[3;32m"'''
                        CERRADO: recibimos RST
                        ABIERTO/FILTRADO: expira el TIMEOUT
                        FILTRADO: ICMP inalcanzable''')+chr(27)+"[0m"

            if selectorPuerto == '9':

                class ComandosPuertos1:
                    def __init__(self,c2,c3,c4,c5,c6):
                        self.versionSistema = c2
                        self.puerto = c3
                        self.noPing = c4
                        self.host = c5
                        self.vervosidad = c6
                        self.final = 'nmap -sW '+c2+' '+c3+' '+c4+' '+c5+' '+c6

                comando1 = ComandosPuertos1(versionSistema,puerto,noPing,host,vervosidad)
                print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comando1.final)+chr(27)+"[0m"
                os.system(comando1.final)
                print(chr(27)+"[3;32m"'''
                        CERRADO: recibimos RST con window size CERO
                        ABIERTO: Recibe un RST con window size POSITIVO
                        FILTRADO: ICMP error; expira el TIMEOUT''')+chr(27)+"[0m"

            if selectorPuerto == '10':

                class ComandosPuertos1:
                    def __init__(self,c2,c3,c4,c5,c6):
                        self.versionSistema = c2
                        self.puerto = c3
                        self.noPing = c4
                        self.host = c5
                        self.vervosidad = c6
                        self.final = 'nmap -sO '+c2+' '+c3+' '+c4+' '+c5+' '+c6

                comando1 = ComandosPuertos1(versionSistema,puerto,noPing,host,vervosidad)
                print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comando1.final)+chr(27)+"[0m"
                os.system(comando1.final)
                print(chr(27)+"[3;32m"'''
                        CERRADO: recibimos ICMP protocolo inalcanzable
                        ABIERTO: Recibe cualquier respuesta, NO HAY ERROR
                        ABIERTO/FILTRADO:expira en TIMEOUT
                        FILTRADO: otros ICMP inalcanzable''')+chr(27)+"[0m"

            if selectorPuerto == '11':

                class ComandosPuertos1:
                    def __init__(self,c2,c3,c4,c5,c6):
                        self.versionSistema = c2
                        self.puerto = c3
                        self.noPing = c4
                        self.host = c5
                        self.vervosidad = c6
                        self.final = 'nmap -sY '+c2+' '+c3+' '+c4+' '+c5+' '+c6

                comando1 = ComandosPuertos1(versionSistema,puerto,noPing,host,vervosidad)
                print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comando1.final)+chr(27)+"[0m"
                os.system(comando1.final)
                print(chr(27)+"[3;32m"'''
                        CERRADO: Recibimos SCTP ABORT
                        ABIERTO: recibimos SCTP INIT-ACK
                        FILTRADO: ICMP error; Recibimos ICMP inalcanzable o expira el TIMEOUT''')+chr(27)+"[0m"

            if selectorPuerto == '12':

                class ComandosPuertos1:
                    def __init__(self,c2,c3,c4,c5,c6):
                        self.versionSistema = c2
                        self.puerto = c3
                        self.noPing = c4
                        self.host = c5
                        self.vervosidad = c6
                        self.final = 'nmap -sZ '+c2+' '+c3+' '+c4+' '+c5+' '+c6

                comando1 = ComandosPuertos1(versionSistema,puerto,noPing,host,vervosidad)
                print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comando1.final)+chr(27)+"[0m"
                os.system(comando1.final)
                print(chr(27)+"[3;32m"'''
                        CERRADO: recibimos SCTP ABORT
                        ABIERTO/FILTRADO: Expira TIMEOUT
                        FILTRADO: recibimos ICMP inalcanzable''')+chr(27)+"[0m"



#...........................................................................................................................................
#                       OPCION 2, MENU ESCANER CON SCRIPT

    if selectorMenu == '2':
        print('''\nSELECCIONE EL SCRIPT\n

        N  NOMBRE                   OPCION EN NMAP                      FUNCIONAMIENTO

        1. Analisis agresivo -----------[-A]---------------[Es un conjunto de -O -sV -sC --traceroute]

        2 Vulnerabilidades -------------[Vuln]-------------[deteccion de Vulnerabilidades]

        3. Autenticacion ---------------[Auth]-------------[Script de autenticacion]

        4. Default ---------------------[Default]----------[ejecuta script basicos por defecto de la herramienta]

        5. Intrusivo -------------------[Intrusive]--------[Ejecuta script que para el objetivo son intrusivos]

        6. Malware ---------------------[Malware]----------[Revisa si existes conexiones abiertas por codigo malicioso o backdoors en el objetivo]

        7. Segura ----------------------[Safe]-------------[Ejecuta script que no son intrusivos]

        8. ID de WAF --------------------------------------[Identificacion del Web Aplication Firewall del objetivo,puerto 80 y 443]

        9. Fuerza Bruta -----------------------------------[Fuerza Bruta a los directorios, mas de 2000 directorios]

        10. Fuerza Bruta ----------------------------------[Fuerza Bruta a Subdirectorios]

        11. Todos -----------------------[All]--------------[Ejecuta absolutamente todos los script con extenciones NSE]


        ''')

        selectorScript = raw_input('Seleccione una opcion > ')
        selectorScript = selectorScript.lower()

        host = raw_input('ingrese el host > ')
        host = host.lower()

        vervosidad = raw_input('Quiere vervosidad? -v normal -vv mucha, enter ninguna > ')
        vervosidad = vervosidad.lower()


        if selectorScript == '1':
            class ComandoScript:
                def __init__(self,host,vervosidad):

                    self.host = host
                    self.vervosidad = vervosidad
                    self.final = 'nmap -A ' + self.host +' '+ self.vervosidad
            comandoscript = ComandoScript(host,vervosidad)
            print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comandoscript.final)+chr(27)+"[0m"
            os.system(comandoscript.final)

        if selectorScript == '2':
            class ComandoScript:
                def __init__(self,host,vervosidad):

                    self.host = host
                    self.vervosidad = vervosidad
                    self.final = 'nmap --script Vuln ' + self.host +' '+ self.vervosidad
            comandoscript = ComandoScript(host,vervosidad)
            print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comandoscript.final)+chr(27)+"[0m"
            os.system(comandoscript.final)

        if selectorScript == '3':
            class ComandoScript:
                def __init__(self,host,vervosidad):

                    self.host = host
                    self.vervosidad = vervosidad
                    self.final = 'nmap --script Auth ' + self.host +' '+ self.vervosidad
            comandoscript = ComandoScript(host,vervosidad)
            print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comandoscript.final)+chr(27)+"[0m"
            os.system(comandoscript.final)

        if selectorScript == '4':
            class ComandoScript:
                def __init__(self,host,vervosidad):

                    self.host = host
                    self.vervosidad = vervosidad
                    self.final = 'nmap --script Default ' + self.host +' '+ self.vervosidad
            comandoscript = ComandoScript(host,vervosidad)
            print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comandoscript.final)+chr(27)+"[0m"
            os.system(comandoscript.final)

        if selectorScript == '5':
            class ComandoScript:
                def __init__(self,host,vervosidad):

                    self.host = host
                    self.vervosidad = vervosidad
                    self.final = 'nmap --script Intrusive ' + self.host +' '+ self.vervosidad
            comandoscript = ComandoScript(host,vervosidad)
            print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comandoscript.final)+chr(27)+"[0m"
            os.system(comandoscript.final)

        if selectorScript == '6':
            class ComandoScript:
                def __init__(self,host,vervosidad):

                    self.host = host
                    self.vervosidad = vervosidad
                    self.final = 'nmap --script Malware ' + self.host +' '+ self.vervosidad
            comandoscript = ComandoScript(host,vervosidad)
            print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comandoscript.final)+chr(27)+"[0m"
            os.system(comandoscript.final)

        if selectorScript == '7':
            class ComandoScript:
                def __init__(self,host,vervosidad):

                    self.host = host
                    self.vervosidad = vervosidad
                    self.final = 'nmap --script Safe ' + self.host +' '+ self.vervosidad
            comandoscript = ComandoScript(host,vervosidad)
            print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comandoscript.final)+chr(27)+"[0m"
            os.system(comandoscript.final)

        if selectorScript == '8':
            class ComandoScript:
                def __init__(self,host,vervosidad):

                    self.host = host
                    self.vervosidad = vervosidad
                    self.final = 'nmap --script http-waf-fingerprint ' + self.host +' '+ self.vervosidad
            comandoscript = ComandoScript(host,vervosidad)
            print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comandoscript.final)+chr(27)+"[0m"
            os.system(comandoscript.final)

        if selectorScript == '9':
            class ComandoScript:
                def __init__(self,host,vervosidad):

                    self.host = host
                    self.vervosidad = vervosidad
                    self.final = 'nmap --script http-enum ' + self.host +' '+ self.vervosidad
            comandoscript = ComandoScript(host,vervosidad)
            print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comandoscript.final)+chr(27)+"[0m"
            os.system(comandoscript.final)

        if selectorScript == '10':
            class ComandoScript:
                def __init__(self,host,vervosidad):

                    self.host = host
                    self.vervosidad = vervosidad
                    self.final = 'nmap --script dns-brute ' + self.host +' '+ self.vervosidad
            comandoscript = ComandoScript(host,vervosidad)
            print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comandoscript.final)+chr(27)+"[0m"
            os.system(comandoscript.final)

        if selectorScript == '11':
            class ComandoScript:
                def __init__(self,host,vervosidad):

                    self.host = host
                    self.vervosidad = vervosidad
                    self.final = 'nmap --script All ' + self.host +' '+ self.vervosidad
            comandoscript = ComandoScript(host,vervosidad)
            print(chr(27)+"[3;32m"'EJECUTANDO COMANDO =========> '+ comandoscript.final)+chr(27)+"[0m"
            os.system(comandoscript.final)


#----------------------------------------------------------------------------------------------------------------------------------------------
#                                           SALIDA

    if selectorMenu == '3':
        break
