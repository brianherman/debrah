"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""
import logging
logging.basicConfig(filename='debra.log',level=logging.INFO)

import pyaudio
import wave
import os

from alexa_client import AlexaClient

from pygame import mixer # Load the required library
import speech_recognition as sr
from os import path
current_dir = path.dirname(path.realpath(__file__))
def start_recording(CHUNK = 1024, FORMAT = pyaudio.paInt16, CHANNELS = 1, RATE = 16000, RECORD_SECONDS = 5, WAVE_OUTPUT_FILENAME = "C:\\tmp\\recording.wav"):
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    logging.info("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    logging.info("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
def play_wav(filename=None,CHUNK=1024):
    CHUNK = 1024

    # if len(sys.argv) < 2:
    #     print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    #     sys.exit(-1)

    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()
def play_mp3(data=None):
    mixer.init()
    mixer.music.load(data)
    mixer.music.play()
def throw_to_alexa_voice_service(rec="C:\\tmp\\recording.wav", save_to = "test_ask.mp3"):
    alexa = AlexaClient()
    with open("test.mp3", 'wb') as f:
        response = alexa.ask(rec)
        if not response:
            logging.info("Response Empty")

        if response:
            f.write(response)
        else:
            print("please try again!")
            return
    play_mp3("test.mp3")
def shove_to_Sphinx():
    AUDIO_FILE = path.join(current_dir, "recording.wav")
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source) # read the entire audio file
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
def throw_to_google():
    AUDIO_FILE = path.join(current_dir, "recording.wav")
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source) # read the entire audio file
    
if __name__ == '__main__':
    print("Start talkin...")
    start_recording()
    print("Stop!")
    shove_to_sphinx()
    throw_to_alexa_voice_service()
