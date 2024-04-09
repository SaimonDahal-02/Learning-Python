import time

from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Get off your computer moron!",
            timeout = 10
        )
        time.sleep(3600)