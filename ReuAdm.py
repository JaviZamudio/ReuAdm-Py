from time import localtime, sleep
from os import system
import keyboard
from lib import *

#name,wday,h_init,h_end,urlFirst,urlEver

#function to restart the actual class
restart = False
def restartClass():
    global restart
    restart = True

def main():
    #keyboard event listener
    keyboard.add_hotkey("ctrl+alt+r", restartClass)

    #setup
    # system("start brave")
    f = open("classes.txt", "r")
    fContent = f.read()
    f.close()
    global restart

    lines = fContent.split("\n")[:-1]
    day = localtime().tm_wday

    meetings = []
    for meeting in lines:
        meeting = meeting.split("|")
        meeting = Meeting(meeting[0],meeting[1],meeting[2],meeting[3],meeting[4],meeting[5])
        #add a meeting to meetings if it's the meeting's day
        if(meeting.day == str(day)):
            meetings.append(meeting)

    lines = open("conferences.txt", "r").read().split("\n")[:-1]
    for line in lines:
        line = line.split("|")
        meeting = Meeting(line[0],line[1],line[2],line[3],line[4],line[5])
        if(meeting.day.split(",")[0] == str(localtime().tm_mday) and meeting.day.split(",")[1] == str(localtime().tm_mon)):
            meetings.append(meeting)

    #Sort the meetings by starting hour
    meetings.sort(key = lambda meeting: meeting.start)

    #main execution loop
    dayOver = False
    while(not dayOver):
        #seting up the restart

        #update date and time
        hour = localtime().tm_hour
        mins = localtime().tm_min

        #restarting class indicator

        #find current meeting we should be or will be
        actualMeeting = Meeting()
        for meeting in meetings:
            #if we are before the ending hour, we are still in the meeting
            if(hour <= int(meeting.end.split(":")[0]) and mins < int(meeting.end.split(":")[1])):
                actualMeeting = meeting
                break
        
        #remove the meetings before the actual meeting
        try:
            meetings = meetings[meetings.index(actualMeeting):]
        except:
            #if we arent in a meeting, exit
            break
        
        #if it's time for the meeting, start it
        if(hour == int(actualMeeting.start.split(":")[0]) and mins == int(actualMeeting.start.split(":")[1])):
            print(f"[{hour}:{mins}] Starting {actualMeeting.name}")
            if actualMeeting.first != "0":
                system("start " + actualMeeting.first)
            system("start " + actualMeeting.always)
            sleep(50)

        #checking if we need to restart
        if(restart):
            print(f"[{hour}:{mins}] Restarting {actualMeeting.name}")
            system("start " + actualMeeting.always)
            restart = False
        
        sleep(10)

    #ending
    # input()
    print("bye bye!")

main()