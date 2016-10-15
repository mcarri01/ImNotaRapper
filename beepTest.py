import math
import pyaudio
from time import sleep

#sudo apt-get install python-pyaudio
PyAudio = pyaudio.PyAudio

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 16000 #number of frames per second/frameset.      

#See http://www.phy.mtu.edu/~suits/notefreqs.html
FREQUENCY = 261.63 #Hz, waves per second, 261.63=C4-note.
LENGTH = 1.2232 #seconds to play sound


NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''    
for x in xrange(NUMBEROFFRAMES):
	WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))


counter = 0

while(counter < 10):
	print(counter)
 	p = PyAudio()
	stream = p.open(format = p.get_format_from_width(1), 
	                channels = 1, 
	                rate = BITRATE, 
	                output = True)
	stream.write(WAVEDATA)
	stream.stop_stream()
	stream.close()
	p.terminate()
 	counter = counter+1
 	sleep(1)



