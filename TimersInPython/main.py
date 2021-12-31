import signal
import time
from multiprocessing import Process

class TimeOut(Exception):
  pass

def signalHandler(sign, frame):
  raise TimeOut("Sorry, time is out.")

processArray = []

def clearTimers():
  global processArray
  signal.alarm(0)
  
  for i in range(len(processArray)):
    processArray[i].kill()
    processArray.pop(i)

def resetTimer(timeEnd):
    global processArray
    #Clear existing timers
    clearTimers()

    #Starting a new signal
    signal.signal(signal.SIGALRM, signalHandler)
    signal.alarm(timeEnd)

    #Starting another process too
    p2 = Process(target=timer, args=(timeEnd, ))
    p2.start()
    processArray.append(p2)

def timer(t, timer_res=1):
    org = t
    while (t > 0):
        comp_t = int(timer_res * (t // timer_res))
        if (comp_t == int(org / 2)):
            print(RED_BOLD + "\nHalf Time Left!" + RESET)
        if (comp_t == int(org / 4)):
            print(RED_BOLD + "\nAlmost up!" + RESET)
        time.sleep(timer_res)
        t -= timer_res

resetTimer(10)
input("input a number: ")