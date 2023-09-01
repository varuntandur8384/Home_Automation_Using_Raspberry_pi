from tkinter import *
from tkinter import messagebox
import RPi.GPIO as GPIO
 
import speech_recognition as sr   #This library is used to recognize the speech or command
import pyttsx3
import datetime
import time
import pyaudio
#import rfid
#import warnings
from mfrc522 import SimpleMFRC522

bedroom = 21
door = 16
tv = 26
fan = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(bedroom,GPIO.OUT)
GPIO.setup(fan,GPIO.OUT)
GPIO.setup(tv,GPIO.OUT)
GPIO.setup(door,GPIO.OUT)
GPIO.setwarnings(False)
#filterwarnings()
#voice code

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
 
def reset():
    GPIO.cleanup()
    
#Bedroom code    
def bedroom_light_ON():
    GPIO.output(bedroom,GPIO.LOW)

def bedroom_light_OFF():
    GPIO.output(bedroom,GPIO.HIGH)
    
#Fan code 
def fan_ON():
    GPIO.output(fan,GPIO.LOW)

def fan_OFF():
    GPIO.output(fan,GPIO.HIGH)
    
#TV code
def tv_ON():
    GPIO.output(tv,GPIO.LOW)

def tv_OFF():
    GPIO.output(tv,GPIO.HIGH)
    
#Door code
def door_Open():        
    GPIO.output(door,GPIO.LOW)
    talk("opening the door")
    print("opening the door")

def door_Close():
    GPIO.output(door,GPIO.HIGH)
    talk("closing the door")
    print("closing the door")
    
def turn_on_all():
    bedroom_light_ON()
    fan_ON()
    tv_ON()
    door_Open()
    
def turn_off_all():
    bedroom_light_OFF()
    fan_OFF()
    tv_OFF()
    door_Close()

def rfid(id):
    if id==1079478412837:
        print("User: Varun Tandur")
        talk("Welcome to Home")
        door_Open()
        time.sleep(5)
        door_Close()
        
    elif id == 1013610997406:
        print("User: Udayashankar Koulapur")
        talk("Welcome to Home")
        door_Open()
        time.sleep(5)
        door_Close()
    
    elif id==116752410287:
        print("User: Vaishnavi C")
        talk("Welcome to Home")
        door_Open()
        time.sleep(5)
        door_Close()
        
    elif id==255700198974:
        print("User: Nida M")
        talk("Welcome to Home")
        door_Open()
        time.sleep(5)
        door_Close()
        
#GUI code
def main_screen():
    screen = Tk()
    screen.title("Home Automation")
    screen.geometry("400x500")
    
    Label(text = "Home Control Button",fg="black",font=("arial",13) ).place(x=105,y=10)
    
    #Bedroom Buttons
    Button(text = "Bedroom Light ON",height = 2,width=20,bg="#00bd56",fg="black",command = bedroom_light_ON).place(x=10,y=50)
    Button(text = "Bedroom Light OFF",height = 2,width=20,bg="#ed3833",fg="black",command = bedroom_light_OFF).place(x=205,y=50)
    
    #Fans Buttons
    Button(text = "Fan ON",height = 2,width=20,bg="#00bd56",fg="black",command = fan_ON ).place(x=10,y=125)
    Button(text = "Fan OFF",height = 2,width=20,bg="#ed3833",fg="black",command = fan_OFF).place(x=205,y=125)
    
    #TV Buttons
    Button(text = "TV ON",height = 2,width=20,bg="#00bd56",fg="black",command = tv_ON).place(x=10,y=200)
    Button(text = "TV OFF",height = 2,width=20,bg="#ed3833",fg="black",command = tv_OFF).place(x=205,y=200)
    
    #Door Buttons
    Button(text = "Door OPEN",height = 2,width=20,bg="#00bd56",fg="black",command = door_Open).place(x=10,y=275)
    Button(text = "Door Close",height = 2,width=20,bg="#ed3833",fg="black",command = door_Close).place(x=205,y=275)
    
    #All appliances
    Button(text = "Turn ON all",height = 2,width=20,bg="#00bd56",fg="black",command = turn_on_all).place(x=10,y=350)
    Button(text = "Turn OFF all",height = 2,width=20,bg="#ed3833",fg="black",command = turn_off_all).place(x=205,y=350)
    
    #Reset Button
    Button(text = "RESET",height = 2,width=20,bg="#1089ff",fg="white",command=reset).place(x=105,y=425)
    
    screen.mainloop()
    


#Recognizing input commands
def take_command():
    try:
        print(" ")
        
        time.sleep(1)
        with sr.Microphone() as source:
            talk("listening")
            print("listening...")
            listener.pause_threshold = 1
            listener.energy_threshold = 300
            voice = listener.listen(source,timeout=10,phrase_time_limit=13)
            print("understanding...")
            command = listener.recognize_google(voice)
            command = command.lower()
            #command = command.replace("angel"," ")            
            print("user said:" + command)

            
                
            
    except:
        return 'None'
    
        #pass
    return command

#Voice assistant 
def run_angel():
    while True:
        command = take_command()
        
        #bedroom code
        if 'turn on bedroom light' in command or 'on bedroom light' in command:
            bedroom_light_ON()
            talk("turning on bedroom light")
            print("turning on bedroom light")
                
        elif 'turn off bedroom light' in command or 'off bedroom light' in command:
            bedroom_light_OFF()
            talk("turning off bedroom light")
            print("turning off bedroom light")
                    
        #fan code
        elif 'turn on fan' in command or 'on pan' in command:
            fan_ON()
            talk("turning on fan")
            print("turning on fan")
                
        elif 'turn off fan' in command or 'off pan' in command:
            fan_OFF()
            talk("turning off fan")
            print("turning off fan")
                    
        #TV code
        elif 'turn on tv' in command or 'on the tv' in command:
            tv_ON()
            talk("turning on tv")
            print("turning on tv")
                
        elif 'turn off tv' in command or 'off the tv' in command:
            tv_OFF()
            talk("turning off tv")
            print("turning off tv")
                
        #Door code
        elif 'open door' in command or 'open the door' in command:
            print("Place Card on Reader: ")
            reader = SimpleMFRC522()
            id, text = reader.read()
            print("ID: ",id)
            print("Text: ",text)
            time.sleep(1)
            rfid(id)
            
                
        elif 'close door' in command or 'close the door' in command:
            door_Close()
                    
        #GUI
        elif 'open' in command:
            talk("G U I is open, you can now control manually")
            print("G U I is open, you can now control manually")
            main_screen()
                 
        #turning off all the appliances
        elif 'turn off all the appliances' in command:
            turn_off_all()
            talk("turning off all the appliances")
            print("turning off all the appliances")
                    
        #turning on all the appliances
        elif 'turn on all the appliances' in command:
            turn_on_all()
            talk("turning on all the appliances")
            print("turning on all the appliances")
                    
        #Reset
        elif 'remove supply' in command:
            talk('Power off')
            print('Power off')
            reset()
                
        elif 'exit' in command:
            print('...')
            time.sleep(1)
            print('...')
            time.sleep(1)
            print('...')
            time.sleep(1)
            turn_off_all()
            talk('Good Bye')
            print('Good Bye')
            break   
        
        else:
            print("No commands given")
            talk("No commands given")

run_angel()
#main_screen()
#while True:
    #main_screen()
    
    
