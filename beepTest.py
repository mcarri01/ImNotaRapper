import os
import math
import pyaudio
from time import sleep
import threading
import pyttsx
from gtts import gTTS

def beep(num):
	print("in beep")
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

	while(counter < num):
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

def speak(engine):
	print('in sleep')
	engine.connect('finished-utterance', finish)
	engine.say("Now")
	engine.runAndWait()
	#os.system("say 'Now this is a story all about how My life got flipped-turned upside down And I would d like to take a minuteJust sit right there I will tell you how I became the prince of a town called Bel-Air'")
def finish():
	exit()

def init_threads():
	num = 5
	engine = pyttsx.init()
	try:
		beep_t = threading.Thread(target=beep, args=(num,))
		speak_t = threading.Thread(target=speak, args=(engine,))
		beep_t.start()
		speak_t.start()
		# wait for threads
		speak_t.join()
		beep_t.join()
	except:
		print("Error")

if __name__ == "__main__":
	init_threads()
	

