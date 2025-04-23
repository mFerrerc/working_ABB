import socket
import select
import time

# Crear dos sockets para conectarse a los dos robots
socket1 = socket.socket()
socket2 = socket.socket()

# Definir las direcciones IP de cada robot
ip1 = "127.0.0.1"
ip2 = "127.0.0.2"

# Conectar el primer socket al robot
socket1.connect((ip1, 8000))
# Conectar el segundo socket al robot
socket2.connect((ip2, 8000))

# Recibir los mensajes iniciales de conexión que envían los robots
# Se decodifican los bytes a cadena usando utf-8
respuesta1 = socket1.recv(1024).decode('utf-8')
respuesta2 = socket2.recv(1024).decode('utf-8')

# Imprimir en consola las respuestas de conexión para verificar la comunicación
print("Conexión ABB 1:", respuesta1)
print("Conexión ABB 2:", respuesta2)

# Preparar los datos a enviar a cada robot (comandos de control)
# Convertir la cadena a bytes con codificación utf-8
datos1 = "1".encode('utf-8')
datos2 = "2".encode('utf-8')

# Bucle principal que mantiene la comunicación entre ambos robots
while True:
    # Usamos select para esperar que alguno de los sockets tenga datos disponibles sin bloquear el programa
    readable, _, _ = select.select([socket1, socket2], [], [])
    # Iteramos sobre los sockets que tienen datos listos para leer
    for s in readable:
        # Recibir el mensaje (hasta 1024 bytes) y decodificarlo a cadena
        data = s.recv(1024).decode('utf-8')
        print("Recibido:", data)
        # Si el mensaje viene del primer socket y es "1", se envía "2" al segundo robot
        if s == socket1 and data == "1":
            socket2.send(datos2)
        # Si el mensaje viene del segundo socket y es "2", se envía "1" al primer robot
        elif s == socket2 and data == "2":
            socket1.send(datos1)

        time.sleep(1)

    
