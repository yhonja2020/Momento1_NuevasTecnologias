"""
Una institución educativa se encuentra en proceso de finalizar semestre y en proceso de admisión para el próximo semestre. 
La institución requiere un software que le permita solucionar estas dos problemáticas con las siguientes restricciones. 
Para finalización de semestre: 
Se desean subir las notas de los alumnos al sistema de los programas de Desarrollo de software y Telecomunicaciones, 
para ello, se le pide al docente el número de alumnos, nombre de cada alumno, programa académico, si es hombre, mujer, 
no binario, además, las 5 notas obtenidas durante el curso. El software calcula el promedio de las 5 notas. Al finalizar 
la ejecución debe mostrar cuántos hombres, mujeres y no bonarios hay en cada programa académico, el promedio de notas por 
cada programa y el listado de alumnos con el respectivo promedio de cada uno.
Para el proceso de admisión 
La institución requiere que se le muestre cuántos estudiantes en total se matricularon y el promedio de edad de los 
matriculados, además, requiere saber cuántos hombres y mujeres se matricularon.
El proceso de admisión termina hasta que el usuario decida que ya no se van a matricular más personas.
"""

def averageStudent():
    average = 0
    for j in range(1,6):
        average = average + float(input(f"Ingrese nota {j}: "))
    if average > 0:
        average = average / 5
    else:
        average = 0
    print(f"Nota Promedio: {round(average, 2)}")
    return average

def main():
    while(True):
        option = str(input("Ingrese Opcion Semestre(S), Admision(A), Otro para salir: ")) 
        if option.upper() == 'S':
            semestre()
        elif option.upper() == 'A':
            admision()     
        else:
            break  

def semestre():
    programa = {
        'Software': ['S','',0,0,0,0],
        'Telecomunicaciones' : ['T','',0,0,0,0]
        }
    
    
    #countWomenSoftware = 0
    #countMenSoftware = 0
    #countNotBinarySoftware = 0
    #countWomenTelecomunications = 0
    #countMenTelecomunications = 0
    #countNotBinaryTelecomunications = 0
    students = []
    averageSoftware = 0
    #averageTelecomunications = 0 
    listProgramas = []
    listSiglas = []
    printProgramas = ""
    academicKey = ""
    #dictPrograma = {}
    

    while(True):   
        listUpdate = ['','',0,0,0,0] #Sigla, Nombre,M,H,NB,AV
        nombrePrograma = ""
        siglaPrograma = ""
        print("Programas por defecto Software(S) - Telecomunicaciones(T)")
        addProgram = str(input("Desea Agregar programa: (S), (N): ")) 
        if addProgram.upper() == 'S':
            print("Digite nombre programa y sigla: \n")
            nombrePrograma = str(input("Nombre Programa: ")) 
            siglaPrograma = str(input("Sigla Programa: "))
            listUpdate[0] = siglaPrograma
            programa[nombrePrograma] = listUpdate
        elif addProgram.upper() == 'N':
            break
        else:
            print("Digite Opcion Valida")
            pass

    print(programa)
    listUpdate = ['','',0,0,0,0] #Sigla, Nombre,M,H,NB,AV
    numAlumnos = int(input("Ingrese número de alumnos: "))
    for i in range(numAlumnos):
        
        name = str(input(f"Ingrese nombre {i +  1}: "))
        printProgramas= ""
        for key, value in programa.items():
            listProgramas.append(key)
            listSiglas.append(value)
            printProgramas += key + "(" + value[0] + "), "
            
        
        #print(listProgramas)
        academicKey = ""
        while(True):
            academicProgram = str(input(f"Ingrese programa académico, {printProgramas}: "))
            for key, value in programa.items():
                if academicProgram.upper() == value[0]:
                    print("Exist")
                    academicKey = key
            if academicKey != '':
                break
        
        print(academicKey)
        listUpdate = programa[academicKey]
        listUpdate[1] = listUpdate[1] + name + ", "

        sex = str(input("Ingrese sexo: Mujer(M), Hombre(H), No Binario(NB): "))
        if sex.upper() == "M":
            print("women")
            listUpdate[2] = listUpdate[2] + 1
        elif sex.upper() == "H":
            print("Men")
            listUpdate[3] = listUpdate[3] + 1
        elif sex.upper() == "NB":
            print("BN")
            listUpdate[4] = listUpdate[4] + 1
        average = averageStudent()
        students.append({"name": name, "average": average})
        #averageSoftware+=average
        listUpdate[5] = listUpdate[5] + average
        programa[academicKey] = listUpdate
        print(programa)
        #listUpdate = ['','',0,0,0,0]
                    
                #else:
                #    print("Programa Invalido")
        
            
        # elif academicProgram.upper() == 'T':
        #     sex = input("Ingrese sexo: Mujer(M), Hombre(H), No Binario(NB): ")
        #     if sex.upper() == "M":
        #         countWomenTelecomunications+=1
        #     elif sex.upper() == "H":
        #         countMenTelecomunications+=1
        #     elif sex.upper() == "NB":
        #         countNotBinarycomunications+=1
        #     average = averageStudent()
        #     students.append({"name": name, "average": average})
        #     averageTelecomunications += average
        
    print(programa)
    for key, value in programa.items():
        if (value[2] + value[3] + value[4]) > 0:
            print(f"Promedio  {key}: {value[5] / (value[2] + value[3] + value[4])}")
            print(f"Número de mujeres en {key}: {value[2]}")
            print(f"Número de hombres en {key}: {value[3]}")
            print(f"Número de No Binarios en {key}: {value[4]}")
    #print(f"Promedio Software: {averageSoftware}")
    #print(f"Número de mujeres en Software: {countWomenSoftware}")
    #print(f"Número de Hombre en Software: {countMenSoftware}")
    #print(f"Número de no binarios en Software: {countNotBinarySoftware}")
    #print(f"Promedio Telecomunicaciones: {averageTelecomunications}")
    #print(f"Número de mujeres en Telecomunicaciones: {countWomenTelecomunications}")
    #print(f"Número de Hombre en Telecomunicaciones: {countMenTelecomunications}")
    #print(f"Número de no binarios en Telecomunicaciones: {countNotBinaryTelecomunications}")
    for i in students: # for i in range(len(students))
        print(f"Nombre: {i['name']} - Nota final: {i['average']}")
    return 1

def admision():
    average = 0
    countMen = 0
    countWomen = 0
    countStudents = 0
    averageAge = 0
    while(True):
        numAlumnos = int(input("Ingrese número de alumnos: "))
        for x in range(numAlumnos):
            average+=int(input(f"Ingrese edad {x + 1}: "))
            sex = str(input(f"Ingrese sexo {x + 1}: "))
            if sex.upper() == "M":
                countWomen+=1
            elif sex.upper() == "H":
                countMen+=1
            countStudents += 1
        
        

        averageAge = average/countStudents
        print(f"Número de estudiantes matriculados: {countStudents}")
        print(f"Promedio de edad de matriculados: {round(averageAge,2)}")
        print(f"Número de mujeres matriculadas: {countWomen}")
        print(f"Número de hombre matriculados: {countMen}")
        
        stopAdmission = int(input("si desea parar de matricular ingrese 0, de lo contrario cualquier tecla para continuar: "))
        if stopAdmission == 0:
                break
    return 1

if __name__ == '__main__':
    main()

    
    
    