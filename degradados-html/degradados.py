def degradadoGris():
	texto = '<head><style type="text/css">body{margin:0;}</style></head><body>'
	for i in range(256):
		texto += '<div style="height: 4px; width: 100%; background: #'+ format(i,'02x')*3+';display: block;"></div>'
	texto += '</body>'
	escribir(texto)

def degradadoRojo():
	texto = '<head><style type="text/css">body{margin:0;}</style></head><body>'
	for i in range(256):
		texto += '<div style="height: 4px; width: 100%; background: #'+ format(i,'02x') +'0000;display: block;"></div>'
	texto += '</body>'
	escribir(texto)

def degradadoVerde():
	texto = '<head><style type="text/css">body{margin:0;}</style></head><body>'
	for i in range(256):
		texto += '<div style="height: 4px; width: 100%; background: #00'+ format(i,'02x')+'00;display: block;"></div>'
	texto += '</body>'
	escribir(texto)

def degradadoAzul():
	texto = '<head><style type="text/css">body{margin:0;}</style></head><body>'
	for i in range(256):
		texto += '<div style="height: 4px; width: 100%; background: #0000'+ format(i,'02x')+';display: block;"></div>'
	texto += '</body>'
	escribir(texto)

def escribir(texto):
	f = open ("degradado.html", "w")
	f.write(texto)
	f.close()
