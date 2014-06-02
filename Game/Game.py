__author__ = 'Adam'

import time
import sys



def displayIntro():
    print "The time is " +time.strftime("%H" ":" "%M%p")
    time.sleep(3)
    print "You wake up in your small one room home,",
    print "You have no memory of what took place earlier in your life."
    time.sleep(3)
    print "You hear a booming voice coming from every direction"
    time.sleep(3)
    print "Hello there hero, you are about to start your journey"
    time.sleep(4)

def hometown():
    hometown = (" ")
    print "From where do you hale?"
    hometown = raw_input()
    time.sleep(3)
    print ("I see, you are from " +hometown)
    time.sleep(5)
    return hometown

def playername():
    playername = (" ")
    print ("I almost forgot, what is your name?")
    playername = raw_input()
    print ("It is nice to meet you " +playername)
    time.sleep(4)


def leavehome():
    leavehome = ""
    while leavehome != "yes" and leavehome != "y":
        print ("Are you ready to leave your home?")
        leavehome = raw_input()
        return leavehome

def OutsideofHome():
    playername = playername()
    time.sleep(5)
    print ("You step outside of your home, you see the similar dirt road off of your property.")
    time.sleep(2)
    print
    print ("Your task" +playername)
    print ("is to save the kings balls")


#This is a test update


displayIntro()
hometown()
playername()
leavehome()
OutsideofHome()
