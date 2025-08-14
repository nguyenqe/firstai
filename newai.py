import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)

    print("Robot: ...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)

    if you == "": 
        robot = "I can't hear you ,try again "
    elif "hello" in you or "hi" in you:
        robot = "Hello Q"

    elif "today" in you:
        today = date.today()
        robot = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot = now.strftime("%H hours %M minutes %S seconds")
    elif "president" in you:
        robot = "Donald Trump"
    elif "bye" in you:
        robot = "Bye Q"
        print("Robot: " + robot)
        robot_mouth.say(robot)
        robot_mouth.runAndWait()
        break
    else:
        robot = "I'm fine thank you and you"
    print("Robot: " + robot)
    robot_mouth.say(robot)
    robot_mouth.runAndWait()
    