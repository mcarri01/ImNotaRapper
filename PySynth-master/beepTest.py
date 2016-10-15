import os
import math
import pyaudio
from time import sleep
import thread
import threading
import pyaudio  
import wave  
from pysynth_b import make_wav


def speak():
	sleep(3)
	os.system("say So I ball so hard mothafuckas wanna fine me First niggas gotta find me What's 50 grand to a mothafucka like me? Can you please remind me?'")


def beep():
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

beep_t = threading.Thread(target=beep, args=())
speak_t = threading.Thread(target=speak, args=())

def init_threads():
	try:
		speak_t.start()
		beep_t.start()
		# wait for threads
		speak_t.join()
		beep_t.join()

	except:
		print("Error")

if __name__ == "__main__":
	init_threads()
	

