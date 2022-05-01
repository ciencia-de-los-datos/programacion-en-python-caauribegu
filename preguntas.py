"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open('data.csv', 'r') as file:  
        lines=file.readlines()

    final = sum([int(row[2]) for row in lines])

    return final


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    import operator

    with open('data.csv', 'r') as file:  
        lines=file.readlines()

    letras = [row[0] for row in lines]

    salida = {}
    for letra in letras:
        if letra in salida.keys():
            salida[letra] = salida[letra] + 1
        else:
            salida[letra] = 1
            
    tuplas = [(v, k) for v,k in salida.items()]
    tuplas = sorted(tuplas, key=operator.itemgetter(0), reverse=False)
    
    return tuplas


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    import operator

    with open('data.csv', 'r') as file:  
        lines=file.readlines()

    letras = [row[0] for row in lines]
    nums = [int(row[2]) for row in lines]


    pos=0

    salida = {}
    for letra in letras:
        
        if letra in salida.keys():
            salida[letra] = salida[letra] + nums[pos]
            
            
        else:
            salida[letra] = nums[pos]
        pos+=1
        


    tuplas = [(v, k) for v,k in salida.items()]
    tuplas = sorted(tuplas, key=operator.itemgetter(0), reverse=False)

    return tuplas


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),  
        ("11", 2),
        ("12", 3),
    ]

    """
    import operator

    with open('data.csv', 'r') as file:  
        lines=file.readlines()

    lines=[x.split('\t')for x in lines]

    fecha=[fechas[2].split('-')[1] for fechas in lines]

    num_mes={}
    for mes in fecha:
        if mes in num_mes.keys():
            num_mes[mes]=num_mes[mes] + 1
        else:
            num_mes[mes]=1



    tuplas = [(v, k) for v,k in num_mes.items()]
    tuplas = sorted(tuplas, key=operator.itemgetter(0), reverse=False)



    return tuplas


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    import operator

    with open('data.csv', 'r') as file:  
        lines=file.readlines()

    lines=[x.split('\t')for x in lines]

    letras=[ (x[0], x[1]) for x in lines]


    salida={}
    for letra,valor in letras:

        if letra in salida.keys():
            if salida[letra] < valor:
                salida[letra]=valor
        else:
                salida[letra]=valor

    salida_min={}
    for letra,valor in letras:

        if letra in salida_min.keys():
            if valor < salida_min[letra]:
                salida_min[letra]=valor
    
        else:
                salida_min[letra]=valor


    salida_final={}
    lista=[]
    for k,v in salida.items():
        for k2,v2 in salida_min.items():
            if k==k2:
                salida_final[k]=(k,int(v),int(v2))

    tuplas = [v for v in salida_final.values()]

    tuplas = sorted(tuplas, key=operator.itemgetter(0), reverse=False)

    print(tuplas)


    return tuplas


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    
    
    x = open('data.csv', 'r').readlines()
    x = [i.replace('\n', '') for i in x]
    x = [i.split('\t') for i in x]

    lista = []
    for a in [i[4].split(',') for i in x]:
        lista.extend(a)
    diccionario = {}
    for b in lista:
        clave = b.split(':')[0]
        valor = b.split(':')[1]
        if clave in diccionario.keys():
            diccionario[clave].append(int(valor))
        else:
            diccionario[clave] = [int(valor)]

    resultado = [(clave, min(diccionario[clave]), max(diccionario[clave])) for clave in diccionario.keys()]
    resultado=sorted(resultado, key=lambda tup: tup[0])
    resultado
    
    return resultado


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    x = open('data.csv', 'r').readlines()
    x = [i.replace('\n', '') for i in x]
    x = [i.split('\t') for i in x]


    diccionario = {}
    for i in x:
        clave = int(i[1]) 
        if clave in diccionario.keys():
            diccionario[clave].append(i[0])
        else:
            diccionario[clave] = [i[0]]
    lista = sorted(list(diccionario.items()))
    
    return lista 


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    x = open('data.csv', 'r').readlines()
    x = [i.replace('\n', '') for i in x]
    x = [i.split('\t') for i in x]

    diccionario = {}
    for i in x:
        clave = int(i[1])
        if clave in diccionario.keys():
            diccionario[clave].append(i[0])
        else: 
            diccionario[clave] = [i[0]]
        
    resultado = sorted(list(diccionario.items()))
    resultado = [(b[0], sorted(list(set(b[1])))) for b in resultado]
    

    return resultado


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
