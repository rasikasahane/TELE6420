from datetime import datetime


current_datetime = datetime.now()
current_date = current_datetime.strftime("%Y-%m-%d")
current_time = current_datetime.strftime("%H:%M:%S")

print("Current Date:", current_date)
print("Current Time:", current_time)