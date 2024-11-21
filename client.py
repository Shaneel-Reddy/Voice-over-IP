import pyaudio
import socket
import threading
from tkinter import *


chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 10240

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=chunk)

host = '192.168.179.207'  
port = 1234
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((host, port))  

class VOIP_FRAME(Frame):
    def speakStart(self):
        self.mute = False
        t = threading.Thread(target=self.speak)
        t.start()

    def muteSpeak(self):
        self.mute = True
        print("You are now muted")

    def speak(self):
        while not self.mute:
            data = stream.read(chunk)
            s.send(data)  

    def createWidgets(self):
        self.speakb = Button(self, text="Speak", command=self.speakStart)
        self.speakb.pack(side="left")
        self.muteb = Button(self, text="Mute", command=self.muteSpeak)
        self.muteb.pack(side="left")

    def __init__(self, master=None):
        self.mute = True 
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = VOIP_FRAME(master=root)
app.mainloop()
root.destroy()
s.close()
stream.close()
p.terminate()
