from datetime import datetime


current_datetime = datetime.now()
current_date = current_datetime.strftime("%Y-%m-%d")
current_time = current_datetime.strftime("%H:%M:%S")
current_day = current_datetime.strftime("%A")

print("Current Date:", current_date)
print("Current Time:", current_time)
print("Day:", current_day)