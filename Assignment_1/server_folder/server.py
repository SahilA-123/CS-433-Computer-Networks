# first of all import the socket library
import socket  
import os   
import os.path 
import crypto2      
 
s = socket.socket()        
print ("Socket successfully created")

port = 4040             

s.bind(('10.7.56.201', port))        
print ("socket binded to %s" %(port))
 
s.listen(5)    
print ("socket is listening")  

c, addr = s.accept()
print ('Got connection from', addr )

curr_dir = os.getcwd()

while (True):
    msg = c.recv(1024).decode()
    if (msg == 'CMD'):
        c.send(curr_dir.encode())
    elif (msg == 'LS'):
        str = ""
        dir_list = os.listdir(curr_dir)
        for file in dir_list:
            str += file
            str += "$"
        str = str[:-1]
        c.send(str.encode())
    elif (msg == 'CD'):
        path = c.recv(1024).decode()
        try:
            os.chdir(path)
            curr_dir = os.getcwd()
            c.send('OK'.encode())
        except:
            c.send('NOK'.encode())
    elif (msg == "DWD"):
        reqFile = c.recv(1024).decode()
        file_exists = os.path.exists(reqFile)
        if (file_exists == False):
            c.send('NOK'.encode())
            continue
        else:
            c.send('OK'. encode())
        crypto2.substitute_encode(reqFile)
        with open(reqFile, 'rb') as file_to_send:
            for data in file_to_send:
                c.sendall(data)
        crypto2.substitute_decode(reqFile)    
    elif (msg == "UPD"):
        downloadDir = os.getcwd()
        filename = c.recv(1024).decode()
        with open(os.path.join(downloadDir, filename), 'wb') as file_to_write:
            data = c.recv(1024)
            if not data:
                break
            file_to_write.write(data)
        file_to_write.close()
        crypto2.substitute_decode(filename)
    else:
        c.send('error'.encode())
        c.close()


