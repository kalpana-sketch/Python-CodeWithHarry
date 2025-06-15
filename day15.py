import time
timestamp = time.strftime('%H')
hr = int(timestamp)

if(hr > 0 and hr < 12):
    print("Good Morning")
elif(hr > 12 and hr < 15):
    print("Good Afternoon")
else:
    print("Good Evening")