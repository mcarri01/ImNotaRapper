import os
import math
import pyaudio
from time import sleep
import thread
import threading
from tweet import get_sentiment
from pysynth_b import make_wav
import wave



def speak(tweet_data):
	text = tweet_data['tweet']
	print(text)
	rate = 0
	if tweet_data['sentiment'] == 0:
		rate = 300
	elif tweet_data['sentiment'] == 1:
		rate = 100
	else:
		rate = 200
	print(rate)
	final_rate = str(rate) + ' '

	print "say -r " + final_rate + "'" + text.encode('utf-8') + "'"
	os.system("say -r " + final_rate + "'" + text.encode('utf-8') + "'")


def start_beat(tweet_data):
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
	
	speak_t = threading.Thread(target=speak, args=(tweet_data,))
	speak_t.start()

	#paly stream  
	while data != '':  
	    stream.write(data)  
	    data = f.readframes(chunk)  

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate() 




if __name__ == "__main__":
	print("please enter input")
	search = raw_input()
	tweet_data = get_sentiment(search)
	start_beat(tweet_data)
	

