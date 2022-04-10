import psutil
import wmi
from plyer import notification
import time
import tkinter as tk
import Config


statement = True
poststate = False

while True:

    def checkIfProcessRunning(processName):
        '''
        Check if there is any running process that contains the given name processName.
        '''
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if processName.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False;

    if checkIfProcessRunning(Config.true1):
        print('Yes a FILE2N process was running.')
        statement = True

    else:
        print('No FILE2N process was running.')


    if checkIfProcessRunning(Config.true2):
            statement = True

    else:
        print('No FILE2N process was running')

    if checkIfProcessRunning(Config.false1):
        statement = False

    else:
        print('No FILE3P process was running')

    if checkIfProcessRunning(Config.false2):
        print('Yes a FILE4P process was running')
        statement = False

    else:
        print('No FILE4P process was running')

    if statement == poststate:
        print("no change")

    elif statement == False:
        print("change detected")
        notification.notify(
            title='We recommended you detach your wrist wrest',
            message='Precision application detected.',
            app_icon="switch_off.ico",
            timeout=10,
        )
        poststate = False

    elif statement == True:
        print("change detected")
        notification.notify(
            title='We recommended you attach your wrist wrest',
            message='Precision application not detected.',
            app_icon="switch_on.ico",
            timeout=10,

        )
        poststate = True

