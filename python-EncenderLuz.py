import serial
import time
import speech_recognition as sr

r=sr.Recognizer()
ser=serial.Serial("com5",9600)
while True:
    
    with sr.Microphone() as source:
        print("listening...")
        audio=r.listen(source,phrase_time_limit=5)
        try:
            text=r.recognize_google(audio)
            print(format(text))
        except:
            print("uncomprehensive")
            text="nothing"
    if ("lights" in text):
        try:
            ser.open()
            time.sleep(2.5)
        except:
            pass
        ser.write(b"1")
        ser.close()
        

