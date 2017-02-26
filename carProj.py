from flask import Flask
import time, http.client, sys, json, urllib.request
import numpy as np

leftSpeed = 1.0
rightSpeed = 1.0

DELAY = .25

client = http.client.HTTPConnection('localhost', 3000)
client.connect()

pyClient = http.client.HTTPConnection('localhost', 1024)
pyClient.connect()


class Stack(list):
    def push(self, element):
        self.append(element)
    def isEmpty(self):
        return not self

class Direction():
    FORWARD = 1
    RIGHT = 2
    BACKWARDS = 4
    LEFT = 0
    

def main():
    

    
    finished = False

    DEFAULT_DELTA = 5.0
    delta = DEFAULT_DELTA

    foundIntersection = False

    nextDir = Direction.FORWARD

    while not finished:
        intersection = checkForIntersection()
        if foundIntersection:
            handleIntersection(intersection)
            delta = DEFAULT_DELTA
                
        else:
            if checkFinished():
                finished = True
            else:
                goForward(delta)
                delta = getNextDelta(delta)
                time.sleep(DELAY)
                
def handleIntersection(direction):
    INTERSECTION_HANDLER_TIMER = .5
    start = time.time()
    end = start + INTERSECTION_HANDLER_TIMER
    while start < end:
        goForward()
    if direction == Direction.RIGHT:
        turnRight()
    elif direction == Direction.LEFT:
        turnLeft()
    else:
        goForward()
        
def getNextDelta(delta):
    return delta - delta / 5.0
            
def goForward(delta = 0):
    if delta:
        deviance = getDeviance()
        if deviance = Direction.LEFT:
            leftSpeed -= delta
            rightSpeed += delta
        elif deviance = Direction.RIGHT:
            rightSpeed -= delta
            leftSpeed += delta
    client.request('', 'w')
    client.request('', str(delta))
    
    #More code here

def go():
    client.request('', 'w')

def stop():
    client.request('', 's')
            
def turnRightInPlace():
    stop()
    client.request('', 'r')
    time.delay(.3)
    stop()
    go()
    
    #more code here

def turnLeftInPlace():
    stop()
    client.request('', 'l')
    time.delay(.3)
    stop()
    go()
    #more code here

def turnRight(intensity = 0.0):
    client.request('', str(int(intensity)))

def turnLeft(intensity = 0.0):
    client.request('', str(int(-intensity)))

#def turnAround():
    #pass

#def goBack():
    #pass

def checkFinished():
    data = not scan()[3]
    return data

def checkForIntersection():
    data = scan()
    dataLeft = data[0]
    dataRight = data[2]

    if dataLeft:
        return Direction.LEFT
    elif dataRight:
        return Direction.RIGHT
    else:
        return Direction.FORWARD
    

def getDeviance():
    data = scan()[4]
    if data < 0:
        return Direction.LEFT
    elif data > 0:
        return Direction.RIGHT
    else:
        return Direction.FORWARD
    

def scan():
    request = urllib.request.urlopen("http://localhost:1024")
    reader = codecs.getreader('utf-8')
    data = json.load(reader(request))
    scan_list = [data['left']]
    scan_list += [data['top']]
    scan_list += [data['right']]
    scan_list += [data['bottom']]
    scan_list += [data['headingBottomRel']]
    return scan_list
    
