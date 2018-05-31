import winspeech
import sys

winspeech.initialize_recognizer(winspeech.INPROC_RECOGNIZER)

def speechRecognized(result, listener):
	print("You said: %s" % result)
	if result == 'stop':
		winspeech.stop_listening()
		sys.exit(0)

listener = winspeech.listen_for_anything(speechRecognized)

while listener.is_listening():
	continue