__author__ = 'Adam C'

import time
import sys

hometown = (" ")    #default hometown
playername = (" ")  #default playername
leavehome = (" ")   #default leavehome

def displayIntro():
    print "The time is " +time.strftime("%H" ":" "%M%p")
    #time.sleep(3)
    print "You wake up in your small one room home, "\
    "You have no memory of what took place earlier in your life."
    #time.sleep(3)
    print "You hear a booming voice coming from every direction"
    #time.sleep(3)
    print "Hello there hero, you are about to start your journey"
    #time.sleep(4)

def hometown():
    global hometown
    print "From where do you hale?"
    hometown = raw_input()
    #time.sleep(3)
    print ("I see, you are from " +hometown)
    #time.sleep(5)
    #return hometown

def playername():
    global playername
    print ("I almost forgot, what is your name?")
    playername = str(raw_input())
    print ("It is nice to meet you " + playername)
    #time.sleep(4)
    #return playername

def leavehome():
    global leavehome
    while leavehome != "yes" and leavehome != "y":
        print ("Are you ready to leave your home?")
        leavehome = raw_input()
        #return leavehome

def outsideofhome():
    #time.sleep(5)
    print "You step outside of your home, you see the similar dirt road off of your property."
    #time.sleep(2)
    print
    print ("Your task, {} " + playername) ,
    print " is to save the king"
    return outsideofhome





displayIntro()
hometown()
playername()
leavehome()
outsideofhome()

"""
print "Welcome to the world of no idea"
print "You are on a journey of acid"
print "Tell me your name!"
name = raw_input()
print ("Okay, " +name),
"""
