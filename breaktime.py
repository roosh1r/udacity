import time
import webbrowser
total_breaks = 3
break_count = 0
print("Program has started on " + time.ctime())
while( break_count < total_breaks) :
    time.sleep(5)
    #webbrowser.open("http://news.ycombinator.com")
    print("Break number: " + str(break_count))
    break_count = break_count + 1
