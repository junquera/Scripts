import random
ppt = ['piedra', 'papel', 'tijera']
gM = 0
uGanadas = 0
mGanadas = 0

def result(uC, mC):
	global gM
	global uGanadas
	global mGanadas
	if(uC == mC):
		print "Empate"
		return
	else:
	 if(uC == ppt[0]):
		if(mC == ppt[1]):
			print "Gana la maquina"
			gM = 1
		else:
			print "Gana el usuario"
			gM = 0
	 else:
	  if(uC == ppt[1]):
		if(mC == ppt[0]):
			print "Gana el usuario"
			gM = 0
		else:
			print "Gana la maquina"
			gM = 1
	  else:
	   if(uC == ppt[2]):
		if(mC == ppt[0]):
			print "Gana la maquina"
			gM = 1
		else:
			print "Gana el usuario"
			gM = 0
	if(gM):
		mGanadas+=1
	else:
		uGanadas+=1
def main():	
	while(1):
		if(gM):
			if(uC== ppt[0]):
				mC = ppt[2]
			else:
			 if(uC == ppt[1]):
				mC = ppt[0]
			 else:
				mC = ppt[1]
		else:
			mC = ppt[random.randint(0,2)]

		uC = raw_input("Selecciona piedra, papel o tijera (o fin, para terminar juego): ");
		if(uC == "fin"):
			break
		else:
			result(uC, mC)

	print "Partidas ganadas por el usuario:", uGanadas,"\nPartidas ganadas por la maquina:", mGanadas

main()
