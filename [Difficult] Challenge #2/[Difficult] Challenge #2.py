# Your mission is to create a stopwatch program. This program should have start,
# stop, and lap options, and it should write out to a file to be viewed later.

#shoutout to https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python for timer tools
# and https://learnpythonthehardway.org/book/ex16.html for file manipulation

import time


class stopwatch:

    def __init__(self):
        self.starttime = 0
        self.currtime = 0
        self.laptime = 0


    # start off by keeping the time. We can make time difference through subtracting the current
    # time with the start time
    def start(self):
        self.starttime = time.time()

    def stop(self):
        self.currtime = time.time() - self.starttime + self.currtime

    def lap(self):
        self.laptime = time.time() - self.starttime + self.currtime

if __name__ == '__main__':
    watch = stopwatch()
    response = ""
    script = open("watch_test", 'w')
    while response != "q":
        print "Type (start), (stop), or (lap). Type (quit) to stop"
        response = str(raw_input())
        if response == "s":
            watch.start()
            script.write("Starting the stopwatch...\n")
        elif response == "t":
            watch.stop()
            script.write("Stopping the watch! The current time is: " + str(watch.currtime) + "\n")
        elif response == "l":
            watch.lap()
            script.write("That's a lap! The time is: " + str(watch.laptime) + "\n")
    script.close()
