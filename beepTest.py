import os
import math
import pyaudio
from time import sleep
import thread
import threading
from tweet import get_sentiment


def speak(value):
	os.system("say -v Bad News 'Now this is a story all about how My life got flipped-turned upside down And I'd like to take a minute Just sit right there I'll tell you how I became the prince of a town called Bel-Air'")


def beep(value):
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


	while( speak_t.is_alive() ):
	 	p = PyAudio()
		stream = p.open(format = p.get_format_from_width(1), 
		                channels = 1, 
		                rate = BITRATE, 
		                output = True)
		stream.write(WAVEDATA)
		stream.stop_stream()
		stream.close()
		p.terminate()
	 	sleep(1)

beep_t = threading.Thread(target=beep, args=())
speak_t = threading.Thread(target=speak, args=())

def init_threads(value):
	
	try:
		speak_t.start(value)
		beep_t.start(value)
		# wait for threads
		speak_t.join(value)
		beep_t.join(value)

	except:
		print("Error")

if __name__ == "__main__":
	print("please enter input")
	search = raw_input()
	value = get_sentiment(search)
	init_threads(value)
	

