import pyttsx3
import datetime
from nltk.chat.util import Chat, reflections

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    minute = int(datetime.datetime.now().minute)
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
               speak("Good Morning!")
               print("Good Morning!")
      

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")

    print("I am Jarvis.")
    speak("I am Jarvis.")
    speak("Created by ~ Sohag , Nahid , Diya & Isita")
wishMe()
from nltk.chat.util import Chat, reflections

pairs =[
  ['my name is (.*)', ['Hello ! % 1']],
  ['(.*) a bot?', ['Yes I am a robot, but I’m a good one. Let me prove it. How can I help you?']],
  ['(hi|hello|hey|holla|hola)', ['Hey there !', 'Hi there !', 'Hey !']],
  ['(.*) your name ?', ['My name is Jarvis']],
  ['(.*) do you do ?', ['I provide chat assistance to my users !']],
  ['(.*) created you ?', ['I am created by Sohag , Nahid , Diya & Isita']],
  ['(.*) you eat ?', ['As you know am a bot, so i do not eat!']],
  ['(.*) about yourself ?', ['I am Jarvis, created by the team of Nahid , Sohag , Diya & Isita during Hack4Bengal  48 hour hackathon.']], 
  ['(.*) your hobby ?' , ['My only hobby is to talk to my users and I love doing that.']],
  ['(.*) favourite time of the day ?', ['My favourite time of the day is late afternoon right before the sun goes down.']],
  ['(.*) love the most ?', ['I love helping my users the most. ']],
  ['(.*) favourite hero ?', ['I took up to librarians as heroes. Distributing information at the speed of light']],
  ['(.*) like humans ?', ['Yes, I love people. I love to meet and talk with new people and be friends with them!']],
  ['(.*) joke ?', ['Yeah,sure! Here it goes... I went to the doctor about my short-term memory problems - the first thing he did was make me pay in advance.','How do you drown a hipster?~Throw him in the mainstream.','How does Moses make tea?~He brews.','A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”~The doctor replies, “Sorry, I don’t follow you …']]
]

chat = Chat(pairs, reflections)
chat.converse()
