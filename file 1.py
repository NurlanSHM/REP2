# Here i used AI for it to explain to me how i could optimize the code more, surprised i got quite close to the optimized one. 
# NOTE: This is NOT AI, but is optimized by AI, which didnt change much. I created these files to test and improve my Python knowledge outside of YT Courses
# Note again that I am currently 14 yo at the time of creation of this file. Having foreshadowed this will be shown to a university/in a job application.
# If this did get to a university/job, this me would be very happy and grateful for creating this, especially posting it on GitHub. As expanding is
# the only reason im doing this. Thank you.

import time

malw = range(1, 100000) 
current_dir = None 

print("---------------------------")
print("You're at dir... well, none")
print("---------------------------")

while True:  
    current_dir = input("Select your next directory (/home, /sys32, /TOP SECRET): ").lower()

    if current_dir not in ["/home", "/sys32", "/top secret"]:
        print("Please enter a valid directory.")
        time.sleep(1)
        continue 

    elif current_dir == "/home":
        time.sleep(0.75)
        print("The current directory is now /home")
        time.sleep(1)
        print("This directory has 2 files:")
        time.sleep(0.5)
        print("python code.exe")
        time.sleep(0.3)
        print("virus.py")

        choice = input("Please enter which file you want to choose, or enter 'cd ..' if you want to quit: ").lower()

        if choice == "cd ..":
            print("Returning to main menu...")
            time.sleep(1.5)
            continue  

        elif choice == "python code.exe":
            print("Since when are Python codes an EXE file? Good luck dealing with your malware now.")
            time.sleep(4)
            for x in malw:
                print("THIS IS A VIRUS!!!!")
                print("GET COOKED!!!!!!!!!")

        elif choice == "virus.py":
            print("You probably restarted and came back, didn't you? Either way, a .py file can be a virus too. Deal with this now.")
            time.sleep(5.5)
            for x in malw:
                print("GOTCHA AGAIN, HAHA")

        else:
            print("PLEASE CHOOSE A VALID FILE.")

    elif current_dir == "/sys32":
        choice2 = input("You can delete this directory. If so, enter 'DEL'. If you want to head back, enter 'cd ..': ").lower()
        if choice2 == "del":
            time.sleep(1)
            print("bye bye")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            break
        elif choice2 == "cd ..":
            continue
        else:
            print("Please enter a valid choice")

    elif current_dir == "/top secret":
        print("ACCESS DENIED: You don’t have permission to enter this directory.")
        time.sleep(1)
        guess = input("Enter a password for permission: ").lower()

        if guess == "there is a password?":
            print("ACCESS GRANTED")
            time.sleep(1)
            print("There is 1 file in this directory")
            time.sleep(0.5)
            print("nice pic.png")
            inp = input("Enter 'Y' if you want to open the file, if not, enter 'cd ..': ").lower()

            if inp == "y":
                print("bro wat is wrong wit u")
                continue
            elif inp == "cd ..":
                continue

            else:
                print("Please enter a valid choice")
    