
import pyaudio  
import wave  
from pysynth_b import make_wav



song2 = (
  ('f4*', 16), ('c4', 16), ('r', 8),
  ('ab4*', 16), ('c4', 16), ('r', 8),
  ('g4*', 16), ('c4', 16), ('r', 8),
  ('f4*', 16), ('c4', 16), ('c5', 16),
  ('r', 16)
)

make_wav(song2, bpm=80, repeat=3)



#define stream chunk   
chunk = 1024  

#open a wav format music  
f = wave.open(r"out.wav","rb")  
#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
data = f.readframes(chunk)  

#paly stream  
while data != '':  
    stream.write(data)  
    data = f.readframes(chunk)  

#stop stream  
stream.stop_stream()  
stream.close()  

#close PyAudio  
p.terminate() 