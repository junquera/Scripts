#!/usr/bin/python
# -*- coding: utf-8

from socket import *
import sys

def main():

	if len(sys.argv) >=2:
		serverName = sys.argv[1]
	else:
		serverName = raw_input("Introduzca la dirección a escanear: ")
	
	for i in range(99999):
		try:
			serverPort = i
			clientSocket = socket(AF_INET, SOCK_STREAM)
			clientSocket.connect((serverName, serverPort))
			print i
			clientSocket.close()
		except:
			continue

if __name__ == "__main__":
	main()
