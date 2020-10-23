import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
import tempfile

def text_to_speak(text, language = "es"):
    try:
        gttsObj = gTTS(text=text, lang=language)
        tempWavFile = tempfile.mktemp('.wav')
        gttsObj.save(tempWavFile)
        playsound.playsound(tempWavFile)
        if os.path.isfile(tempWavFile):
            os.remove(tempWavFile)
        return True
    except ValueError:
        print("UPS, EXPLOTO EN TEXT_TO_SPEAK")
        print(ValueError)
        return False

def save_text_mp3(text, language = "es", fileName = "audio"):
    gttsObj = gTTS(text=text, lang=language)
    filename = fileName + '.mp3'
    gttsObj.save(filename)
    return filename

def text_to_speak_and_save(text, language = "es", fileName = "audio"):
    filename = save_text_mp3(text, fileName, language)
    playsound.playsound(filename)
    return filename