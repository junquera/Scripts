#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def formateaFirmas(entrada):

  aux = entrada.split(",")

  salida=aux[0] + "," + aux[1] + "," + aux[2] + "," + aux[3] + ","
  aux=aux[4:]

  grupos= "* My Contacts ::: TODOS"

  for i in aux:
    grupos+=" ::: " + i

  salida+=grupos

  return salida

def main():
  
  if len(sys.argv) <3:
    print "Introduzca como parámetro la ubicación del archivo y la ubicacion de salida:"
    print "\t"+ sys.argv[0] +" UBICACION_ORIGEN UBICACION_SALIDA"
    return

  # Archivo con los datos
  archivo_i = open(sys.argv[1])
  # Archivo a crear
  archivo_o = open(sys.argv[2], "w")
  # Escribimos las cabeceras para el formato de contactos de Google
  archivo_o.write("Given Name,Additional Name,Phone 1 - Value,E-mail 1 - Value,Group Membership\n")
  # Leemos la primera linea de cabeceras (que no nos sirven)
  archivo_i.readline()

  linea = archivo_i.readline()
  
  while(linea!=""):
    archivo_o.write(formateaFirmas(linea))
    linea = archivo_i.readline()

if __name__ == "__main__":
  main()
