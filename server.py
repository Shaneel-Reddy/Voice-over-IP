import pyaudio
import socket


chunk = 1024
pa = pyaudio.PyAudio()


stream = pa.open(format=pyaudio.paInt16,
                 channels=1,
                 rate=10240,
                 output=True)


host = ''
port = 1234
size = 4096 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((host, port))  

print("Server is now running\n=======================")

while True:
    data, addr = sock.recvfrom(size)
    print(f"{addr}")
    if data:
        stream.write(data) 
sock.close()
stream.close()
pa.terminate()
print("Server has stopped running")
