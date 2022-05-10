# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import requests
import matplotlib.pyplot as plt
import codecs
from contextlib import closing
import Estacion as est
import Gas as g
import Captar as cap
import pyodbc
import MySQLdb


DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = '22161327'
DB_NAME = 'a'

def run_query(query=' '):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
    conn = MySQLdb.connect(*datos)
    cursor = conn.cursor()
    cursor.execute(query)

query = 'INSERT INTO ESTACIONES (NOMBRE_ESTACION,TIPO,DIRECCION) VALUES ("%s","%s")'
val = [('Plaza España', 'Plaza España', 'Urbana Tráfico'),
       ('Escuelas Aguirre', 'Entre C/ Alcalá y C/ O´Donell', 'Urbana Tráfico'),
       ('Ramón y Cajal', 'Avenida.Ramón y Cajal esq. C/ Principe de Vergara', 'Urbana Tráfico'),
       ('Plaza del Carmen', 'Plaza del Carmen esq. Tres Cruces', 'Urbana Fondo'),
       ('Cuatro Caminos', 'Avda. Pablo Iglesias esq. C/ Marqués de Lema', 'Urbana Tráfico'),
       ('Barrio del Pilar', 'Avenida de Betanzos esq. C/Monforte de Lemos', 'Urbana Tráfico'),
       ('Méndez Álvaro', 'C/ Juan de Mariana / Plaza Amanecer Méndez Álvaro', 'Urbana Fondo'),
       ('Castellana', 'C/ José Gutiérrez Abascal', 'Urbana Tráfico'),
       ('Parque del Retiro', 'Paseo Venezuela- Casa de Vacas', 'Urbana Fondo'),
       ('Plaza Castilla', 'Plaza Castilla (Canal)', 'Urbana Tráfico')]

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

connection = pyodbc.connect
url = "https://datos.madrid.es/datosabiertos/MEDIOAMBIENTE/CALIDAD_DEL_AIRE/2021/12/datos202112.txt"
with closing(requests.get(url, stream=True)) as r:
    reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',')
    print('AÑO 2021')
    for colum in reader:
        est.id_estacion = (colum[0] + colum[1] + colum[2])
        print(est.id_estacion)
        est.puntoMuestreo = (colum[4])
        print(est.puntoMuestreo)
        g.id_gas = (colum[3])
        print(g.id_gas)
        cap.fecha = (colum[7] + '/' + colum[6])
        print(cap.fecha)
        n = 0
        for n in range(n + 2):
            cap.cantidad = (colum[8 + n])
            print(cap.cantidad)

url = "https://datos.madrid.es/datosabiertos/MEDIOAMBIENTE/CALIDAD_DEL_AIRE/2020/12/datos202012.txt"
with closing(requests.get(url, stream=True)) as r:
    reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',')
    print('AÑO 2020')
    for colum in reader:
        est.id_estacion = (colum[0] + colum[1] + colum[2])
        print(est.id_estacion)
        est.puntoMuestreo = (colum[4])
        print(est.puntoMuestreo)
        g.id_gas = (colum[3])
        print(g.id_gas)
        cap.fecha = (colum[7] + '/' + colum[6])
        print(cap.fecha)
        n = 0
        for n in range(n + 2):
            cap.cantidad = (colum[8 + n])
            print(cap.cantidad)

url = "https://datos.madrid.es/datosabiertos/MEDIOAMBIENTE/CALIDAD_DEL_AIRE/2019/12/datos201912.txt"
with closing(requests.get(url, stream=True)) as r:
    reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',')
    print('AÑO 2019')
    for colum in reader:
        est.id_estacion = (colum[0] + colum[1] + colum[2])
        print(est.id_estacion)
        est.puntoMuestreo = (colum[4])
        print(est.puntoMuestreo)
        g.id_gas = (colum[3])
        print(g.id_gas)
        cap.fecha = (colum[7] + '/' + colum[6])
        print(cap.fecha)
        n = 0
        for n in range(n + 2):
            cap.cantidad = (colum[8 + n])
            print(cap.cantidad)

url= "https://datos.madrid.es/datosabiertos/MEDIOAMBIENTE/CALIDAD_DEL_AIRE/2022/03/datos202203.txt"
with closing(requests.get(url, stream=True)) as r:
    reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',')
    print('AÑO 2022')
    for colum in reader:

        est.id_estacion = (colum[0] + colum[1] + colum[2])
        print(est.id_estacion)
        est.puntoMuestreo = (colum[4])
        print(est.puntoMuestreo)
        g.id_gas = (colum[3])
        print(g.id_gas)
        cap.fecha = (colum[7] + '/' + colum[6])
        print(cap.fecha)
        n = 0
        for n in range(n + 2):
            cap.cantidad = (colum[8 + n])
            print(cap.cantidad)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
