#fortune cookie bot
#before we start the programme, we ask python to get all the packages we need
#random allows us to pick a random fortune later
#time allows us to pause between outputs
#pyttsx3 is the package that does speech for us. We will ask it to start up and will close it down later
import random
import time
import pyttsx3
engine = pyttsx3.init()

#first, find out the user's name, then store the name in the variable "name"
#we tell the computer what to say aloud by using engine.say, then we tell it to go ahead and say it with engine.runAndWait()
engine.say("Hello! What is your name?")
print("Hello, what is your name?")
engine.runAndWait()
name = input()

#tell the user how many letters are in their name
print("Hello, " + name)
engine.say("Hello, " + name)
time.sleep(1)
print("Did you know you have " +str(len(name)) +" letters in your name?")
engine.say("Did you know you have " +str(len(name)) +" letters in your name?")
engine.runAndWait()
time.sleep(1)
print("...")
time.sleep(1)
print("Oh, you did, huh?")
engine.say("Oh, you did, huh?")
engine.runAndWait()
time.sleep(1)

#creates a variable based on input and checks to see if it's yes or no
#then introduces the fortune with varying degrees of snark

engine.say("Ok, then. Do you want me to give you a lyric?")
engine.runAndWait()
fortune = input("Ok, then. Do you want me to give you a lyric?")

if fortune == "yes":
    print("FANTASTIC, I love reading lyrics to people!!!!")
    engine.say("fantastic, I love reading lyrics to people!")
    engine.runAndWait()
    time.sleep(1)
elif fortune == "no":
    print("Listen here, bucko. I came here to chew gum and read lyrics. And I'm fresh out of gum. So why don't you sit down and listen to your lyric, before I knock you down?")
    engine.say("Listen here, bucko. I came here to chew gum and read lyrics from popular songs. And I'm fresh out of gum. So why don't you sit down and listen to your song lyric, before I knock you down?")
    engine.runAndWait()
    time.sleep(1)
while fortune not in ("yes", "no"):
    engine.say("Answer yes or no, please, using only lower case letters. I'm not that smart a programme.")
    engine.runAndWait()

    fortune = input("Answer yes or no, please")
    
    if fortune == "yes":
        print("I'm so happy. I'm glad I understand you now.")
        engine.say("I'm so happy. I'm glad I understand you now.")
        engine.runAndWait()
        time.sleep(1)
    elif fortune == "no":
        print("Right, you little squirt. You'll get your lyrics whether you like it or not.")
        engine.say("Right, you little squirt. You'll get your lyrics whether you like it or not.")
        engine.runAndWait()
        time.sleep(1)
          
#looks for a fortune from a txt file called lines.txt and prints it out
#lines.txt needs to be in the same place this programme is stored
print("Ok, " + name)
engine.say("Ok, " + name)
engine.runAndWait()
print("I'm computing your lyrics now.")
engine.say("I'm computing your lyrics now.")
engine.runAndWait()
time.sleep(1)
print("(please imagine musical noises)")
engine.say("(please imagine musical noises)")
engine.runAndWait()
time.sleep(1)
#this is where the programme reads the file and picks a random line
fileobj = open('lines.txt','r')
line = random.choice(fileobj.readlines())
fileobj.close()
print (line)
engine.say(line)
engine.runAndWait()
time.sleep(1)

#good manners
engine.say("Thanks for playing with me. It's someone else's turn now.")
engine.runAndWait()
print ("Thanks for playing with me. It's someone else's turn now.")

#we stop the speech package and exit the programme.
engine.stop()

time.sleep(5)

exit



