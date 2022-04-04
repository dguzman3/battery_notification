# This script checks the laptop's battery level and creates a desktop 
# notification when the battery level is 95% or higher. This allows the user
# to be aware of when to unplug their laptop to perserve battery health

# Import necessary packages to collect battery details, create notifications
# and identify important times
import psutil
from win10toast import ToastNotifier
from time import sleep, time
from datetime import datetime, date

# Create notification object and send initial notification
toaster = ToastNotifier()
toaster.show_toast("Battery Level Notifier", "Program has been initiated")

# Get current time and set end time to 9:00pm today
current_time = datetime.now().time()
today = date.today()
end_time = datetime(year=today.year,month=today.month,day=today.day,hour=21,
    minute=0,second=0).time()

# Loop through code until after 9:00pm today
while current_time <= end_time:
    # Create initial battery object
    battery = psutil.sensors_battery()

    # Check if computer is currently charging
    if battery.power_plugged:
        # Keep checking battery level while plugged in
        while battery.power_plugged:
            # Send notification if battery reaches 95% or higher
            if battery.percent >= 95:
                toaster.show_toast("Battery Level Notifier", 
                    f"Battery level has reached {battery.percent}%")

            # Delay code for 15 minutes, then update battery object
            sleep(900)
            battery = psutil.sensors_battery()

    # Check if computer battery is running low
    if battery.percent < 35:
        toaster.show_toast("Battery Level Notifier",
            f"Battery is at {battery.percent}% - Time to start charging")

    # Delay code for 30 minutes, then update time
    sleep(1800)
    current_time = datetime.now().time()
