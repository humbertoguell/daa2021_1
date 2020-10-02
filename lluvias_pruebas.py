from lluvias import lluviasADT
from Nodo_Doble import *

def main():

    ruta_archivo = "2017-2018/2017Precip.txt"
    ruta_archivo = "2017-2018/2018Precip.txt"
    ll = ListaDobleLigada()
    archivo = open(ruta_archivo,'rt')
    datos_crudos = archivo.readlines()
    for index in range(len(datos_crudos)):
        datos_crudos[index] = datos_crudos[index].strip().split(',')
        #print(datos_crudos[index])


    for renglon in range(0,len(datos_crudos),1):
        for columna in range(1,1,1):
            datos_crudos[renglon][columna] = int(datos_crudos[renglon][columna])
            l = lluviasADT(datos_crudos[0][0],datos_crudos[0][0],datos_crudos[0][0], datos_crudos[0][0])

    #IMPRIME TODO EL CONTENIDO DEL DOCUMENTO .txt
    #print(datos_crudos)
     
    #IMPRIME TODO EL DOCUMENTO DEL DOCUMENTO .txt PERO EN UNA ListaDobleLigada
    """for r in range(1,len(datos_crudos)-1,1):
        for c in range(0,14,1):
            ll.append(datos_crudos[r][c])   
    ll.transversal()
"""



    #MENU CONSULTAR
    a = lluviasADT(datos_crudos[0][0],datos_crudos[0][0],datos_crudos[0][0], datos_crudos[0][0])
    opcion = int(input("\nPresione 1 para ingresar: "))
    while opcion != 0:
        print("\n")
        print("\t\tMenu")
        print("1 Cual año deseas ver")
        print("1) Consultar Promedio Por Mes")
        print("2) Consultar Promedio por Entidad Federativa")
        print("3) Imprimir el documento")
        print("0) Salir")
        opcion = int(input("\nElige una opcion: "))

        if opcion ==1:
            if 
            
        if opcion == 2:
                print("\t\nPROMEDIO MENSUAL\n")
                mes = int(input("Dame un Mes(1-12):"))
                mes2 = datos_crudos[1][a.set_mes(mes)]
                prom = 0
                for i in range(len(datos_crudos)-4):
                    prom += (float(datos_crudos[i+2][a.set_mes(mes)]))/32
                print(f"El Promedio Para el Mes de {mes2} es : {prom}")
        if opcion == 3:
            ef2 =0
            print("\t\nPROMEDIO POR ENTIDAD FEDERATIVA\n")
            ef = int(input("Dame una Entidad Federativa(1-32):"))
            #for i in range(len(datos_crudos)):
             #   ef1 = (datos_crudos[ef+1][0])
            for i in range(3,15,1):
                ef1 = (datos_crudos[ef+1][0])
                ef2 += float(datos_crudos[a.set_entidad(ef)+2][i-2])
            print(f"El Promedio Para la Entidad Federativa {ef1} es {ef2}\n")

        if opcion == 4:
            for r in range(1,len(datos_crudos)-1,1):
                for c in range(0,14,1):
                    ll.append(datos_crudos[r][c])   
            ll.transversal()
            

    
main()

