# -*- coding: cp1252 -*-
import serial
import csv
import time
import struct

ser = serial.Serial("COM4" ,9600, timeout = 1)
velocidades = []
desplazamientos = []
i = 0
escala=0

##Leer Archivo CSV
with open('example.csv') as csvfile: ##Va el nombre del archivo que se quiere
    readCSV = csv.reader(csvfile, delimiter=';')
    for row in readCSV:
        velocidades = velocidades+[row[2]]
        desplazamientos = desplazamientos+[row[3]]   
    print("Se han cargado los datos")

while True:
    time.sleep(1)

    #Elimina los títulos
    velocidades = velocidades[1:]
    desplazamientos = desplazamientos[1:]
        
    
    if i==0:
        escala = int(input("Digite la escala deseada: "))
        escala=str(escala)
        ser.write(b';'+escala+ b';')
        ser.write(b';'+ min(velocidades)+ b';')
        ser.write(b';'+ max(velocidades)+ b';')
        

    numberRead = ser.readline()
    velocidad = velocidades[i]
    velocidad = velocidad.encode()
    desplazamiento = desplazamientos[i]
    desplazamiento = desplazamiento.encode()
      
    print(numberRead.decode('utf-8'))
    ser.write(b';' +velocidad+ b';')
    ser.write(b';' +desplazamiento+ b';')
    i = i+1
        
