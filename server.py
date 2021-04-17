import socket 
import time
ip = 'localhost'
port = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, port))

sock.listen(1)

connection, address = sock.accept()

print("[+] A connection was made:", address)
print("\n")

while True:
	message = input("Enter command: ")
	connection.send(message.encode('utf8'))

	time.sleep(1)


	recv = connection.recv(10240)
	print(recv.decode('utf8'))
