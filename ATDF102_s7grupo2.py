#-----------------------------
#Avance 3
#-----------------------------


# Variables iniciales
oficina1 = "Dirección: Estación Central\nGerente: Carlos Pachenco\nAgente de venta: Fernando Lopez"
oficina2 = "Dirección: El bosque\nGerente: Nicolas Andaluz\nAgente de venta: Roberto Paredes"
oficina3 = "" #Espacio vacío para nueva oficina
total_oficinas = 2

inmueble1 = "Tipo: vivienda usada (departamento)\nDirección: Avenida Vitacura 4380, Vitacura\nSuperficie: 120 m^2\nTasa de tasación: 540 UF\nNúmero de habitaciones: 4\nNúmero de baños: 1\nNúmero de cocinas: 1\nCaracterísticas específicas: ||"
inmueble2 = "Tipo: bodega\nDirección: Calle Alonso de Córdova 5870, Las Condes\nSuperficie: 95 m^2\nTasa de tasación: 1770 UF\nNúmero de puertas de acceso: 2\n¿Tiene ventanas?: Si\nEstructura: acondicionado"
inmueble3 = "" #Espacio vacío para agregar nuevo inmueble
total_inmueble = 2

contrato1 = "Nombre del propietario: Sebastián Ignacio Valdés Rojas\nRut: 14903221K\nNúmero de teléfono: |+56223456789|+56221454508|\nFecha del contrato: 15 01 2026\nPlazo del contrato: 12 meses"
contrato2 = "Nombre del propietario: Rodrigo Esteban Castillo Navarro\nRut: 108563415\nNúmero de teléfono: |+56227119034|\nFecha del contrato: 23 02 2025\nPlazo del contrato: indefinido"
contrato3 = "" #Espacio vacío para agregar nuevo contrato del propietario
total_contratos = 2

cliente1 = "Nombre del cliente: Benjamin Nicolas Castro Rojas\nNúmero de oficina: 1\nNúmero de inmueble: 2\nTipo de contrato: Exclusividad\nMonto 0.5%: 8.85 UF\nTipo de operación: Arriendo\nFecha de visita: 13 02 2025\nComentario: ||"
cliente2 = "Nombre del cliente: Sarah Fernanda Flores Valdez\nNúmero de oficina: 2\nNúmero de inmueble: 1\nTipo de contrato: Sin exclusividad\nTipo de operación: Venta\nFecha de visita: 15 11 2025\nComentario: |La casa debe ser amarilla|"
cliente3 = "" #Espacio vacío para agregar nuevo cliente
total_visitas = 2


# --- Acumuladores financieros precargados (en pesos) ---
total_ventas_casas = 300000000
total_arriendos_casa = 100000000

total_ventas_depto = 200000000
total_arriendos_depto = 60000000

total_ventas_bodega = 500000000
total_arriendos_bodega = 0

total_ventas_local = 0
total_arriendos_local = 600000000

comisión_gerente = 0.1
comisión_agente = 0.3
comisión_venta = 0.3


#-----------------------------
#Menú principal
#-----------------------------
while True:
    print("====================================================")
    print("Bienvenidos al menú de la mejor inmobiliaria de Chile")
    print("=====================================================")
    print("A continuación se mostrarán las alternativas de navegación: ")
    print("1. Solicitar datos")
    print("2. Registrar nuevos datos")
    print("3. Solicitar reporte de venta o arriendo")
    print("0. Salir del sistema")
    print("=====================================================")
    opcion_principal = int(input("Seleccione la alternativa que desea: "))
    print("************************************************")


    #consulta de datos
    if opcion_principal == 1:

        while True:
            print("......................................................")
            print("Menú de consulta de datos:")
            print("......................................................")
            print("Escoja una de las siguientes opciones:")
            print("1. Consultar oficinas registradas")
            print("2. Consultar inmuebles registrados")
            print("3. Consultar contratos de propietarios registrados")
            print("4. Consultar las visitas de clientes registrados")
            print("0. Volver al menú principal")

            llave_secundaria_consulta = int(input("Seleccione la opción que desea: "))

            if llave_secundaria_consulta == 1:
            #Consultar la oficina
                ox = 0
                while ox <= total_oficinas:
                    if ox == 1:
                        print("1:\n",oficina1)
                    elif ox == 2:
                        print("2:\n",oficina2)
                    elif ox == 3:
                        print("3:\n", oficina3)
                    ox = ox + 1

            elif llave_secundaria_consulta == 2:
            #Consultar inmueble
                ix = 0
                while ix <= total_inmueble:
                    if ix == 1:
                        print("1:\n",inmueble1)
                    elif ix == 2:
                        print("2:\n",inmueble2)
                    elif ix == 3:
                        print("3:\n", inmueble3)
                    ix = ix + 1

            elif llave_secundaria_consulta == 3:
            #Consultar contrato del propietario del inmueble
                cx = 0
                while cx <= total_contratos:
                    if cx == 1:
                        print("1:\n",contrato1)
                    elif cx == 2:
                        print("2:\n",contrato2)
                    elif cx == 3:
                        print("3:\n", contrato3)
                    cx = cx + 1

            elif llave_secundaria_consulta == 4:
            #Consultar la visita del cliente
                vx = 0
                while vx <= total_visitas:
                    if vx == 1:
                        print("1:\n",cliente1)
                    elif vx == 2:
                        print("2:\n",cliente2)
                    elif vx == 3:
                        print("3:\n", cliente3)
                    vx = vx + 1

            elif llave_secundaria_consulta == 0:
            #Volver al menú principal
                break
            else:
                print("Opción de consulta no válida.")


    #registrar nuevos datos
    elif opcion_principal == 2:
        while True:
            print("......................................................")
            print("Menú para registrar datos nuevos:")
            print("......................................................")
            print("Escoja una de las siguientes opciones:")
            print("1. Nueva oficina")
            print("2. Nuevo inmueble")
            print("3. Nuevo contrato")
            print("4. Nueva visita")
            print("0. Volver al menú principal")

            llave_secundaria_registrar = int(input("Seleccione la opción que desea (para volver al menú ingrese '0'): "))


            if llave_secundaria_registrar == 1:
                #Nueva oficina
                if total_oficinas < 3:
                    numero_o = 0
                    while numero_o <=total_oficinas:
                        numero_o = numero_o + 1

                    print("Registro de información de la oficina")
                    print("")
                    oficina = input("Introduzca la dirección de la sucursal de la oficina: ")
                    gerente_oficina = input("Introduzca el nombre del gerente de oficina: ")
                    agente_venta =input("Introduzca el nombre del agente de venta: ")
                    print("===============================================")
                    print("Datos registrados: ")
                    print("===============================================")
                    print()

                    print("Oficina registrada")
                    print("Oficina: ", oficina)
                    print("Gerente de oficina: ", gerente_oficina)
                    print("Agente de venta: ", agente_venta)

                    oficina3 = "Dirección: " + oficina + "\n" + "Gerente: " +  gerente_oficina + "\n" + "Agente de venta: " + agente_venta

                    print("Se ha registrado con éxito la oficina " + str(numero_o))
                    total_oficinas = total_oficinas +1
                else:
                    print("Se alcanzó la máxima capacidad de oficinas (3). No se puede agregar más.")


            elif llave_secundaria_registrar == 2:
                #Nuevo inmueble
                if total_inmueble < 3:
                    numero_i = 0
                    while numero_i <=total_inmueble:
                        numero_i = numero_i + 1

                    print("Registro de la información general del inmueble")
                    print("")
                    
                    calle = input("Introduzca la calle del inmueble: ")
                    numero = int(input("Introduzca el número del inmueble: "))
                    comuna = input("Introduzca la comuna del inmueble: ")
                    superficie_m2 = int(input("Introduzca la superficie del inmueble (m^2): "))
                    valor_tasación = float(input("Introduzca el valor de tasación del inmueble (UF): "))

                    print("")
                    print("Registro de la información específica del inmueble")
                    print("")
                    print("Indica la opción del tipo de inmueble a registrar: ")
                    print("0: Vivienda")
                    print("1: Local comercial")
                    print("2: Bodega")
                    tipo_inmueble = int(input("El tipo de inmueble es: "))

                    if tipo_inmueble == 0:
                        estado_vivienda = input("Indica si la vivienda es 'nueva' o 'usada': ")
                        tipo_vivienda = input("Indica si la vivienda es 'casa' o 'departamento': ")
                        n_habitaciones = int(input("Indica el número de habitaciones: "))
                        n_baños = int(input("Indica el número de baños: "))
                        n_cocinas = int(input("Indica el número de cocinas: "))

                        caract_fica = "|"
                        while True:
                            nueva_características = input("Opcionalmente, introduzca al menos 1 característica específica del inmueble, en caso contrario o ya introdujo suficientes características, no escriba nada: ")
                            caract_fica = caract_fica + nueva_características + "|"
                            if nueva_características == "":
                                break
                        inmueble3 = "Tipo: " + "vivienda " + estado_vivienda + " (" + tipo_vivienda + ")" + "\n" + "Dirección: " + calle + " " + str(numero) + ", " + comuna + "\n" + "Superficie: " + str(superficie_m2) + " m^2" + "\n" + "Tasa de tasación: " + str(valor_tasación) + " UF" + "\n" + "Número de habitaciones: " + str(n_habitaciones) + "\n" + "Número de baños: " + str(n_baños) + "\n" + "Número de cocinas: " + str(n_cocinas) + "\n" + "Características específicas: " + caract_fica

                    elif tipo_inmueble == 1 or tipo_inmueble == 2:
                        if tipo_inmueble == 1:
                            local_o_comercio = "Local comercial"
                        elif tipo_inmueble == 2:
                            local_o_comercio = "Bodega"
                        numero_puertas =  int(input("Indica el número de puertas de acceso: "))
                        ventanas = input("Indica la presencia de ventanas (Si/No): ")
                        estructura = input("Indica si el inmueble está 'acondicionado' o es 'planta libre': ")

                        inmueble3 = "Tipo: " + local_o_comercio + "\n" + "Dirección: " + calle + " " + str(numero) + ", " + comuna + "\n" + "Superficie: " + str(superficie_m2) + " m^2" + "\n" + "Tasa de tasación: " + str(valor_tasación) + " UF" + "\n" + "Número de puertas de acceso: " + str(numero_puertas) + "\n" + "¿Tiene ventanas?: " + ventanas + "\n" + "Estructura: " + estructura
                    
                    print("Se ha registrado con éxito el inmueble " + str(numero_i))
                    total_inmueble = total_inmueble +1
                else:
                    print("Se alcanzó la máxima capacidad de inmuebles (3). No se puede agregar más.")


            elif llave_secundaria_registrar == 3:
                #Nuevo contrato
                if total_contratos < 3:
                    numero_c = 0
                    while numero_c <=total_contratos:
                        numero_c = numero_c + 1
                    #Información del propietario que ofrecerá el inmueble
                    print("===============================================")
                    print("Registro de información del propietario y de su contrato en el que ingresó su inmueble")
                    print("===============================================")
                    print()
                    nombre_propietario = input("Introduzca el nombre completo: ")
                    rut_propietario = input("Introduzca el RUT: ")

                    cantidad_telefono = 1
                    telefono = "|" + input("Introduzca el número de contacto: ") + "|"
                    while cantidad_telefono <= 3:
                        respuesta_telefono = int(input("Opcionalmente introduzca otro número (máximo 3), use una de las siguientes opciones: "))
                        print ("1. Introducir otro número")
                        print ("0. No introducir más")

                        if respuesta_telefono == 1:
                            teléfono_adicional = input("Introduzca el número de contacto adicional: ")
                            telefono = telefono + teléfono_adicional + "|"
                            
                            cantidad_telefono = cantidad_telefono + 1
                        elif respuesta_telefono == 0:

                            cantidad_telefono = cantidad_telefono + 3

                        else:
                            print("Opción inválida, solo se acepta 1 o 0.")

                    fecha_contrato = input("Introduzca la fecha en que se firmó el contrato, siguiendo el formato 'día-mes-año' (ejemplo: 12 05 2024): ")

                    plazo_contrato = input("Introduzca el plazo del contrato, indicando las unidades de tiempo (meses) o, si el plazo no está fijado, escriba 'indefinido': ")

                    contrato3 = "Nombre del propietario: " + nombre_propietario + "\n" + "Rut: " + str(rut_propietario) + "\n" + "Número de teléfono: " + telefono + "\n" + "Fecha del contrato: " + fecha_contrato + "\n" + "Plazo del contrato: " + plazo_contrato

                    print("Se ha registrado con éxito el contrato " + str(numero_c))
                    total_contratos = total_contratos +1
                else:
                    print("Se alcanzó la máxima capacidad de contratos de propietario (3). No se puede agregar más.")


            elif llave_secundaria_registrar == 4:
                #Nueva visita del cliente
                if total_visitas < 3:
                    numero_v = 0
                    while numero_v <= total_visitas:
                        numero_v = numero_v + 1
                    print("===============================================")
                    print("Registro de información de visita")
                    print("===============================================")
                    print()

                    nombre_cliente = input("Ingrese nombre completo del cliente: ")

                    while True:
                        oficina_visitar = int(input("Ingrese el número de la oficina a visitar: "))
                        if oficina_visitar > total_oficinas:
                            print("No hay una oficina registrada con ese número, ingrese otro")
                        else:
                            break

                    while True:
                        inmueble_interes = int(input("Ingrese el número del inmueble para comprar o arrendar: "))
                        if inmueble_interes > total_inmueble:
                            print("No hay un inmueble registrado con ese número, ingrese otro")
                        else:
                            break

                    fecha = input("Ingrese fecha de visita, siguiendo el formato 'día-mes-año' (ejemplo: 12 05 2024): ")

                    while True:
                        print("Escoja la opción para indicar el tipo de operación: ")
                        print("1. Venta")
                        print("2. Arriendo")
                        opcion_operación = int(input())

                        if opcion_operación != 1 and opcion_operación != 2:
                            print("Opción inválida, solo se acepta 1 o 2.")
                        else:
                            break

                    tipo_operación = ""
                    
                    if opcion_operación == 1:
                        tipo_operación = "Venta"
                    elif opcion_operación == 2:
                        tipo_operación = "Arriendo"

                    comentario = "|"

                    while True:
                        print("Escoja una opción para la sección de comentarios del cliente: ")
                        print("1. Agregar comentario.")
                        print("0. Dejar de poner comentarios.")
                        hacer_comentarios = int(input())

                        if hacer_comentarios == 1:
                            comentario_nuevo = input("Ingrese el comentario del cliente: ")
                            comentario = comentario + comentario_nuevo + "|"

                        elif hacer_comentarios == 0:
                            break

                        else:
                            print("Opción inválida, solo se acepta 1 o 0.")


                    #Información del cliente y su visita que comprará o arrendará el inmueble
                    print("Antes de terminar, escoja la opción del tipo de contrato comercial a realizar:")
                    print("0. Exclusividad (Escoger esta opción hará que el cliente deba cancelar un monto del 0.5 % del valor de tasación del inmueble)")
                    print("1. Sin exclusividad")

                    opcion_tcontrato = int(input())

                    if opcion_tcontrato == 0:
                        while True:
                            tasación = float(input("Valor de tasación del inmueble escogido por el cliente: "))
                            if tasación <= 0:
                                print("El valor debe ser mayor que cero.")                    
                            else:
                                tipo_contrato = "Exclusividad"                
                                monto = tasación * 0.5 / 100
                                break

                        cliente3= "Nombre del cliente: " + nombre_cliente + "\n" + "Número de oficina: " + str(oficina_visitar) + "\n" + "Número de inmueble: "+ str(inmueble_interes) + "\n" + "Tipo de contrato: " + tipo_contrato + "\n" + "Monto 0.5%: " + str(monto) + " UF" + "\n" + "Tipo de operación: " + tipo_operación + "\n" + "Fecha de visita: " + fecha + "\n" + "Comentario: " + comentario

                    elif opcion_tcontrato == 1:
                        tipo_contrato = "Sin exclusividad"                
                        cliente3= "Nombre del cliente: " + nombre_cliente + "\n" + "Número de oficina: " + str(oficina_visitar) + "\n" + "Número de inmueble: "+ str(inmueble_interes) + "\n" + "Tipo de contrato: " + tipo_contrato + "\n" +"Tipo de operación: " + tipo_operación + "\n" + "Fecha de visita: " + fecha + "\n" + "Comentario: " + comentario
                    
                    print("Se ha registrado con éxito la visita del cliente " + str(numero_v))
                    total_visitas = total_visitas +1
                else:
                    print("Se alcanzó la máxima capacidad de visitas (3). No se puede agregar más.")


            elif llave_secundaria_registrar == 0:
                print("Volviendo al menú principal")
                break


    #Solicitar reporte de ventas o arriendos
    elif opcion_principal == 3:

        ingreso = total_ventas_casas + total_arriendos_casa + total_ventas_depto + total_arriendos_depto + total_ventas_bodega + total_arriendos_bodega + total_ventas_local + total_arriendos_local
        fuente_ingresos = "todos los inmuebles"

        while True:

            total_casa = total_ventas_casas + total_arriendos_casa
            
            total_depto = total_ventas_depto + total_arriendos_depto
            
            total_bodega = total_ventas_bodega + total_arriendos_bodega
            
            total_local = total_ventas_local + total_arriendos_local
            
            print("Solicitud de reportabilidad")
            print("")

            print("Seleccione el reporte que desea visualizar: ")
            print("")
            
            print("1. Total de ingresos: ")
            print("2. Total de ingresos por ventas: ")
            print("3. Total de ingresos por arriendo: ")
            print("4. Ingresos de la oficina: ")
            print("0. Volver al menú principal.")
            print("")
            opcion_reporte = int(input("Alternativa seleccionada: "))
            print("")
            
            if opcion_reporte == 1:
                ingreso = total_casa + total_depto + total_bodega + total_local
                fuente_ingresos = "todos los inmuebles"
                print("Los ingresos totales son: ",ingreso)

            elif opcion_reporte == 2:
                print("Seleccione el reporte a visualizar: ")
                print("")
                print("1. Total de ventas globales")
                print("2. Total de ventas en casas")
                print("3. Total de ventas en departamentos")
                print("4. Total de ventas en bodegas")
                print("5. Total de ventas en locales comerciales")
                alternativa_reporte = int(input("Alternativa seleccionada: "))
                
                if alternativa_reporte == 1:
                    ingreso = total_ventas_casas + total_ventas_depto + total_ventas_bodega + total_ventas_local
                    fuente_ingresos = "todos los inmuebles vendidos"

                    print("Ingresos totales en ventas: ",ingreso)

                elif alternativa_reporte == 2:
                    ingreso = total_ventas_casas
                    fuente_ingresos = "las ventas de casas"
                    print("Ingresos totales en ventas de casas: ",ingreso)

                elif alternativa_reporte == 3:
                    ingreso = total_ventas_depto
                    fuente_ingresos = "las ventas de departamentos"
                    print("Ingresos totales en ventas de departamentos: ",ingreso)

                elif alternativa_reporte == 4:
                    ingreso = total_ventas_bodega
                    fuente_ingresos = "las ventas de bodegas"
                    print("Ingresos totales en ventas de bodegas: ",ingreso)

                elif alternativa_reporte == 5:
                    ingreso = total_ventas_local
                    fuente_ingresos = "las ventas de locales comerciales"
                    print("Ingresos totales en ventas de locales comerciales: ",ingreso)
            
            elif opcion_reporte == 3:
                print("Seleccione el reporte a visualizar: ")
                print("")
                print("1. Total de arriendos globales")
                print("2. Total de arriendo en casas")
                print("3. Total de arriendo en departamentos")
                print("4. Total de arriendo en bodegas")
                print("5. Total de arriendo en locales comerciales")
                alternativa_reporte = int(input("Alternativa seleccionada: "))
                
                if alternativa_reporte == 1:
                    ingreso = total_arriendos_casa + total_arriendos_depto + total_arriendos_bodega + total_arriendos_local
                    fuente_ingresos = "los arriendos de todos los inmuebles"
                    print("Ingresos totales en arriendos: ",ingreso)
                elif alternativa_reporte == 2:
                    ingreso = total_arriendos_casa
                    fuente_ingresos = "los arriendos de casas"
                    print("Ingresos totales en arriendos de casas: ",ingreso)
                elif alternativa_reporte == 3:
                    ingreso = total_arriendos_depto
                    fuente_ingresos = "los arriendos de departamentos"
                    print("Ingresos totales en arriendos de departamentos: ",ingreso)
                elif alternativa_reporte == 4:
                    ingreso = total_arriendos_bodega
                    fuente_ingresos = "los arriendos de las bodegas"
                    print("Ingresos totales en arriendos de bodegas: ",ingreso)
                elif alternativa_reporte == 5:
                    ingreso = total_arriendos_local
                    fuente_ingresos = "los arriendos de los locales comerciales"
                    print("Ingresos totales en arriendos de locales comerciales: ",ingreso)

            elif opcion_reporte == 4:
                ingreso_gerente = comisión_gerente * ingreso
                ingreso_agente = comisión_agente * ingreso
                ingreso_comisión = comisión_venta * ingreso
            
                print("Los ingresos de la oficina, según los ingresos de " + fuente_ingresos + " son: ")
                print("Ingresos totales: ", ingreso)
                print("Ingresos por comisión de gerente: ", ingreso_gerente)
                print("Ingreso por comisión de agente: ", ingreso_agente)
                print("Ingreso por comisión: ", ingreso_comisión)

            elif opcion_reporte == 0:
                print("Volviendo al menú principal")
                break
            
            else:
                print("La opción que ha ingresado no es válida")


    #apagar
    elif opcion_principal ==0:
        print("Adiós")
        break


    else:
        print("La opción ingresada es inválida, inténtelo de nuevo")
