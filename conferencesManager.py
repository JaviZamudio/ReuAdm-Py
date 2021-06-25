from lib import *

#setup
print("\n\n\t\t - - - Meetings Modifier - - -\n")

while(True):
    name = input("Tell me the name of the meeting: ")
    always = input("Tell me a link to open when you start the session: ")
    days = input("Give me the days of the sessions: ")
    month = input("Tell me the month of the sessions: ")
    start = input("Give me the starting hour(0-23hrs): ")
    end = input("Tell me the ending hour(0-23hrs): ")

    if(len(start.split(":")) == 1):
        start += ":00"
    if(len(end.split(":")) == 1):
        end += ":00"
    

    f = open("conferences.txt", "a")
    for day in days.split(","):
        f.write(Meeting(name,day + f",{month}",start,end,"0",always).toRegister() + "\n")
    f.close()

    if(input("\nDo you wish to add another conference? (Y/N): ").upper() != "Y"):
        break

print("\n\nbye bye!")
input()