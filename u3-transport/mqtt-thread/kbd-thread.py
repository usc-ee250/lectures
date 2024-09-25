import threading
import time

# parallel task/thread to read keyboard input
def kbd_thread():
        while True:
                # must hit enter to complete the input
                k = input("")
                if(k == 'a'):
                        print("Got an a")
                        # do other tasks
                elif(k == 'w'):
                        print("Got an w")
                        # do other tasks

# Main script

# spawn a thread to read keyboard input, specifying the function to run
thread = threading.Thread(target=kbd_thread)
#thread.daemon = True
# start the thread executing
thread.start()

# main task - Replace with whatever useful work you want to do
# or just have it sleep 
# Press Ctrl-C to stop the program
while True:
        print("Sleeping for 5")
        time.sleep(5)