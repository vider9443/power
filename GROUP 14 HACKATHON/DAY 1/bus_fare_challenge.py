#bus fare challenge
import datetime

date = datetime.datetime.today()
day_name = date.strftime("%A")

if day_name == "Monday":
    day = "Mon"
elif day_name == "Tuesday":
    day = "Tue"
elif day_name == "Wednesday":
    day = "Wed"
elif day_name == "Thursday":
    day = "Thu"
elif day_name == "Friday":
    day = "Fri"
elif day_name == "Saturday":
    day = "Sat"
elif day_name == "Sunday":
    day = "Sun"
else:
    print("Invalid date.")

# Comparison of fare according to day of the week.
if day_name == "Monday":
    fare = 100
elif day_name == "Tuesday":
    fare = 100
elif day_name == "Wednesday":
    fare = 100
elif day_name == "Thursday":
    fare = 100
elif day_name == "Friday":
    fare = 100
elif day_name == "Saturday":
    fare = 60
elif day_name == "Sunday":
    fare = 80

print("Date: ", date.date())
print("Day: ", day)
print("Fare: ", fare)
