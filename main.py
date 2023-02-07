import time
from datetime import datetime
from plyer import notification

def main():
    first_time_running = True
    tme = datetime.now().strftime("%H:%M:%S %d-%m-%y")
    while True:
        if first_time_running == True:
            print("First time: {}".format(tme))
            first_time_running = False
        else:
            print("Stand up: Notification - {}".format(tme))
            notification.notify(
                #title of the notification,
                title = "Stand up: {}".format(tme),
                #the body of the notification
                message = "Half hour has passed",  
                #creating icon for the notification
                #we need to download a icon of ico file format
                app_icon = "chair-stand.ico",
                # the notification stays for 50sec
                timeout  = 50
            )
        time.sleep(1800)

if __name__ == "__main__":
    main()
