# # #Create a Calendar Booking System.
# # in which user select Date and time slout
# # If the Date and time slout is already Booked
# # then Dispaly a message that Given Time is already Booked Please choose an other time.
# # Then Enter Name, email and phone number.

import datetime
from datetime import date
from datetime import date, timedelta

today = datetime.date.today()
dates_list = []
for i in range(1, 6):
    next_date = today + datetime.timedelta(days=i)
    dates_list.append(next_date)

default_slots = ["06:00 PM", "06:30 PM", "07:00 PM", "07:30 PM", "08:00 PM", "08:30 PM", "09:00 PM"]

available_slots = {}
for d in dates_list:
    date_str = d.strftime("%Y-%m-%d")
    available_slots[date_str] = default_slots.copy()

booked_slots = []
selected_date = input("Please select a date (YYYY-MM-DD): ")
selected_time = input("Please select a time slot (e.g., 07:00 PM): ")

if selected_date in available_slots:
    if selected_time in available_slots[selected_date]:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        available_slots[selected_date].remove(selected_time)
        booked_slots.append({
            "date": selected_date,
            "time": selected_time,
            "name": name,
            "email": email,
            "phone": phone
        })
        print(f"✅ Slot booked for {name} on {selected_date} at {selected_time}")
    else:
        print("❌ Time slot not available or already booked.")
else:
    print("❌ Invalid date selected.")

