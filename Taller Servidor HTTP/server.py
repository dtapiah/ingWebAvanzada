##  ISMAEL ALVAREZ Q.
##  DANILO TAPIA H.

import socket
import os.path 

#creo socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.bind(('127.0.0.1', 9100))
s.listen()   #comienzo a escuchar

while True:
	#acepto conexion
	c, addr = s.accept()

	#recibo request    
	request = c.recv(1024)   

	line = request.split('\r\n'.encode())
	filePath = line[0].split(' '.encode())

	#depuración
	try: 
		#se le da formato a la ruta del archivo
		filePath[1] = str(filePath[1]).replace("b", "")
		filePath[1] = str(filePath[1]).replace("'", "")
		filePathDepuration = filePath[1].split("/")

		#se le da formato al metodo del request
		filePath[0] = str(filePath[0]).replace("b", "")
		filePath[0] = str(filePath[0]).replace("'", "")

		#se le da formato al protocolo del request
		filePath[2] = str(filePath[2]).replace("b", "")
		filePath[2] = str(filePath[2]).replace("'", "")

		#busco la dirección del archivo entregada por el response en mi directorio
		archivo = str(filePathDepuration[1]+"/"+filePathDepuration[2])

		#se verifica que exista el archivo
		if os.path.exists(archivo): 
		    file = open(archivo, "r") 
		    readline = file.read()

		    protocolo = "HTTP/1.1 200 Ok"

		    #envio la respuesta 200
		    c.sendall((protocolo+"\n").encode())

		    #variables estaticas: path, protocol, method
		    path = '"path"' + ':' + ' "' + filePath[1] + '"' + ', '	
		    protocol = '"protocol"' + ':' + ' "' + filePath[2] + '"' + ', ' 
		    method = '"method"' + ':' +  ' "' + filePath[0] + '"' + ', '
		    headers = '"headers"' + ': '


		    echo = path + protocol + method + headers
		    headerConcatenado = ""
		    for p in line[1:]:   #recorro la lista con el request spliteado
		        cabeceras = str(p).replace("b","")
		        unHeader = cabeceras.replace("'","") + "\n"
		        cadena = (cabeceras.replace("'","")).split(':', 1)
		        
		        try:
		            headerConcatenado += '"' + cadena[0] + '": ' + '"' + cadena[1].replace(" ","") + '"' + ' /// '		            
		        except:
		        	print("")

		        #se envian los headers uno por uno
		        c.sendall(unHeader.encode())
		    
		    headerOrdenado = sorted(headerConcatenado.split('///'))

		    var = ""

		    #dandole formato a la seccion headers del RequestEcho
		    for i in headerOrdenado[1:]:
		    	var += i + ","
		    casiF = "{" + var + "}"
		    casiF = casiF.replace("{ ", "{")
		    casiF = casiF.replace(" ,}", "}")
		    casiF = casiF.replace(' ,"', ' , "')
		    casiF = casiF.replace(' , ', ', ')

		    #se concatenan los strings solicitados
		    echoHeader = echo + casiF
		    XRequestEcho = "X-RequestEcho: " + "{" + echoHeader + "}"

		    #se imprime por consola lo solicitado
		    print(protocolo)
		    print(XRequestEcho+"\n") 
		    print(readline)

		    #se envia el html
		    c.sendall(readline.encode())

		    #cierro la conexion
		    c.close()         
		else:
		    protocolo = "HTTP/1.1 404 Not Found\r\n"
		    headerVacio = "\n"

		    #se envia la respuesta 404
		    c.sendall(protocolo.encode())
		    c.sendall(headerVacio.encode())

		    #cierro la conexion
		    c.close()

		    #se imprime por consola que no se encuetra el archivo
		    print("No existe el archivo")
	except:
		continue 

#dejo de escuchar
s.close()