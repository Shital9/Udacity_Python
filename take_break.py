#Open your favourite song on youtube, after every 2 hours and have a break from your work.

import webbrowser
import time
import datetime

total_breaks = 3
break_count = 0

print("The program has started on : "+time.ctime())
while(break_count<total_breaks):
    time.sleep(7200) #interval is of 2 hrs = 7200 seconds
    webbrowser.open('https://www.youtube.com/watch?v=rtOvBOTyX00')
    break_count = break_count + 1
    
