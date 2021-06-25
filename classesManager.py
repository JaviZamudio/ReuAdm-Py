#name,wday,h_init,h_end,urlFirst,urlEver

from lib import *

#setup
print("\n\n\t\t - - - Meetings Modifier - - -\n")

#asking for data
while(True):
    name = input("Give me the name of the class: ")
    print()
    first = input("Tell me a link to open ONLY when the session starts: ")
    always = input("Tell me a link to open when you start/restart the session: ")

    #if they have the class more than once in a week
    while(True):
        #ask for the single session info
        day = input("Give me the day of the Week(1-7): ")
        start = input("Tell me the starting hour(0-23hrs): ")
        end = input("Tell me the ending hour(0-23hrs): ")

        #format the input to make it correct for the register
        if(len(start.split(":")) == 1):
            start += ":00"
        if(len(end.split(":")) == 1):
            end += ":00"
        day = str(int(day) - 1)

        #prepare to write in the file
        file = open("classes.txt", "a")
        days = day.split(",")
        #check if the user put many days, so the info will be identical for all of them
        for day in days:
            #register every class sesion as a new meeting
            file.write(Meeting(name, day, start, end, first, always).toRegister() + "\n")
        file.close()

        #ask if we have another meeting of the class during the week
        if(input(f"\nDo you have \"{name}\" any other time in the week?(Y/N): ").upper() != "Y"):
            break
        
        print()
        #ask if we have another links of info for the next session of the class 
        if(input(f"\nDo you want to change the links for the next session of \"{name}\"?(Y/N): ").upper() == "Y"):
            #"first_aux" and "always_aux" are to check if each input is empty, if so, dont change "first" or "always" respectively
            first_aux = input("Tell me a link to open ONLY when the session starts: ")
            first = first_aux if first_aux != "" else first
            always_aux = input("Tell me a link to open when you start/restart the session: ")
            always = always_aux if always_aux != "" else always

    if(input("\nDo you wish to add another class? (Y/N): ").upper() != "Y"):
        break
print("\n\nbye bye!")
input()
