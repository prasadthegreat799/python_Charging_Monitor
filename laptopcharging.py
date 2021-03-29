from plyer import notification
import psutil
import time
import pyttsx3

engine = pyttsx3.init()



while (True):
    battery = psutil.sensors_battery()
    percent = battery.percent

    if(percent>=45):
        notification.notify(
            title="Battery Percentage",
            message=str(percent) + "% Battery remaining",
            timeout=10
        )
        engine.say("Please,Remove Charging")
        engine.runAndWait()


    time.sleep(60 * 60)
    continue
