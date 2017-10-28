import speech_recognition
import pyttsx3
import os
import time
import cv2
import numpy as np

speech_engine = pyttsx3.init() # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)

def speak(text):
	speech_engine.say(text)
	speech_engine.runAndWait()

recognizer = speech_recognition.Recognizer()

def calendar():
	b=os.system("espeak 'Here your calendar'")
	
	c=os.system("cal")

def face():

        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

        cap = cv2.VideoCapture(0)

        while 1:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
        
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            cv2.imshow('img',img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

        
def hello():
	b=os.system("espeak 'Hello, sir, good, morning '")
	c=os.system("espeak 'how, can, i, help, you '")		
	print("Hello, sir good morning")
	print("how can i help you")		

def shutdown():
	os.system("poweroff")
	
def search(q):

	os.system("firefox http://www.google.com/search?q=%s" %q)
		
def listen():
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
		print (audio)

	try:
		#return recognizer.recognize_sphinx(audio)
		return recognizer.recognize_google(audio)
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))

	return ""

#speak("Say something!")
#a=listen()
#speak("I heard you say " + a)
#import re
#print (a)
#wordList = re.sub("[^\w]", " ",  a).split()
#print(wordList)
speech = ['Jarvis','hi','hello']
while True:
	
	time.sleep(2)
	speak("Say something!")
	a=listen()
	if a == "":
		speak("I am sorry, sir")
	else:
		speak("I heard you say " + a)
	import re
	print (a)
	wordList = re.sub("[^\w]", " ",  a).split()
	print(wordList)
	
	if "Jarvis"in wordList or "hello"in wordList or "hi"in wordList or "hey"in wordList:
		hello()
	
		
	elif "calendar" in wordList:
		calendar()

	elif "stop" in wordList:
		break
	
	elif "search"  in wordList:
		
		wordList=wordList[1::]
		
		str1 = '+'.join(wordList)
		
		search(str1)
		
		
	elif "shutdown" in wordList:
                
		shutdown()
		
	elif "face" in wordList:
	    face()	
        		
#a=[]
#a.append(listen())
#print(a)



