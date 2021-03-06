#!/usr/bin/python

import wx
import time
import threading

import pyaudio

from log import log

import wave
#import codecs

# TODO:
# - Get rid of wx in this file
# - Play / transmit: roger beep, connect and disconnect sounds
# - Mix sounds together, adjust volume, detect volume (for VU etc.)

'''

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
	print p.get_device_info_by_index(i)

WAVE_OUTPUT_FILENAME = "test.wav"
# Save to file:
#waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#waveFile.setnchannels(CHANNELS)
#waveFile.setsampwidth(self.audio.get_sample_size(FORMAT))
#waveFile.setframerate(RATE)
#waveFile.writeframes(b''.join(frames))
#waveFile.close()

'''

audio = pyaudio.PyAudio()

def get_audiodevices():
	info = audio.get_host_api_info_by_index(0)
	numdevices = info.get('deviceCount')
	result = ""
	for i in range(0, numdevices):
		if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
			result += "Input Device id " + str(i) + " - " + audio.get_device_info_by_host_api_device_index(0, i).get('name') + "\n"
	return result

def play_sound(filename):
	CHUNK = 1024
	wave_test = wave.open(filename, 'rb')
	stream_test = audio.open(format=audio.get_format_from_width(wave_test.getsampwidth()), channels=wave_test.getnchannels(), rate=wave_test.getframerate(), output=True)
	data_test = wave_test.readframes(CHUNK)
	while data_test != '':
		stream_test.write(data_test)
		data_test = wave_test.readframes(CHUNK)
	stream_test.stop_stream()
	stream_test.close()
	#audio.terminate()

class Recorder(threading.Thread):
	def __init__(self, parent):
		threading.Thread.__init__(self)
		self.parent = parent
		self.__running = False

	def isrunning(self):
		return self.__running

	def run(self):
		self.__running = True
		FORMAT = pyaudio.paInt16
		CHANNELS = 2
		RATE = 44100
		CHUNK = 1024
		RECORD_SECONDS = 0.1

		# Start recording
		#audio = pyaudio.PyAudio()
		stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

		frames = []

		while self.__running:
			for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
				data = stream.read(CHUNK)
				frames.append(data)
				#log("Recorded: " + data)
			log("Recorded " + str(len(frames)) + " Kbytes.")
			# TODO: Return/Send/Stream recorded audio chunk
		
		# Stop recording
		stream.stop_stream()
		stream.close()
		#audio.terminate()

	def stop(self):
		self.__running = False

class EventAudiostreamerError(wx.PyCommandEvent):
	def __init__(self, etype, eid, value=None):
		wx.PyCommandEvent.__init__(self, etype, eid)
		self._value = value	# value = error

Event_ErrorAudiostreamer = wx.NewEventType()
EVT_ErrorAudiostreamer = wx.PyEventBinder(Event_ErrorAudiostreamer, 1)

class Audiostreamer(threading.Thread):
	def __init__(self, parent):
		"""
		@param parent: The gui object that should recieve the value
		@param value: value to 'calculate' to
		"""
		threading.Thread.__init__(self)
		self._parent = parent
		self.__running = False
		self.buffer = []

	def isrunning(self):
		return self.__running

	def run(self):
		self.__running = True
		# Overrides Thread.run. Don't call this directly its called internally when you call Thread.start().

		# If error:
		#evt = EventAudiostreamerError(Event_ErrorAudiostreamer, -1)
		#wx.PostEvent(self._parent, evt)

		timecounter = 0
		while self.__running:
			time.sleep(1)
			log("Streamed.")

			# TODO: Stream audio to server
			# frn.send(buffer[])

			# TODO: Roger beep (optional)

	def stop(self):
		self.__running = False
