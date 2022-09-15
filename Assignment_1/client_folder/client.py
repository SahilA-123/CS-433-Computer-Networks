# Import socket module
import socket 
import os  
import sys 
import os.path
import crypto1
     

s = socket.socket()        
port = 4040               
s.connect(('10.7.56.201', port)) 

 
while (True):
    x = input().split(' ')
    if (x[0] == "CMD"):
        s.send(x[0].encode())
        print(s.recv(1024).decode())
    elif (x[0] == "LS"):
        s.send(x[0].encode())
        dir_list = s.recv(1024).decode().split("$")
        print(dir_list)
    elif (x[0] == "CD"):
        s.send(x[0].encode())
        s.send(x[1].encode())
        print(s.recv(1024).decode())
    elif (x[0] == "DWD"):
        downloadDir = "/IIT GN Sem 5/CN/CN_assignments/client_folder"
        filename = x[1]
        s.send(x[0].encode())
        s.send(filename.encode())
        z = s.recv(1024).decode()
        if (z == 'NOK'):
            print('NOK')
            continue
        elif (z == 'OK'):
            with open(os.path.join(downloadDir, filename), 'wb') as file_to_write:
                data = s.recv(1024)
                if not data:
                    break
                file_to_write.write(data)
            file_to_write.close()
            crypto1.substitute_decode(filename)
            print('OK')
    elif (x[0] == "UPD"):
        filename = x[1]
        file_exists = os.path.exists(filename)
        if (file_exists == False):
            print('NOK')
            continue
        crypto1.substitute_encode(filename)
        s.send(x[0].encode())
        s.send(filename.encode())
        with open(filename, 'rb') as file_to_send:
            for data in file_to_send:
                s.sendall(data)
        print('OK')
    else:
        print('error')
        break

s.close() 