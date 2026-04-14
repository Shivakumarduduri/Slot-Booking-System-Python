# Appointment Slot Booking System (Python)

## Description
This is a console-based Appointment Slot Booking System developed using Python. 
It allows users to book time slots for today or tomorrow. Each slot has limited capacity, 
and once full, users are suggested alternative options.

##  Technologies Used
- Python

## Features
- Book appointment slots for today or tomorrow
- Display available slots with capacity
- Prevent overbooking of slots
- Suggest same slot for next day if current day is full
- Store and display all user bookings

##  How to Run
1. Open terminal
2. Run the program:
   python main.py
3. Enter user details and follow instructions

##  Project Structure
- main.py

## 📷 Sample Output

Enter number of users: 1

Enter details of user 1
Enter name: Shiva
Enter age: 23
Select day (today/tomorrow): today

Available slots:
10 AM -> 0/2
12 PM -> 0/2
1 PM -> 0/2

Select a slot: 10 AM
Booking Confirmed

 All Appointments:
Name: Shiva, Age: 23, Day: today, Slot: 10 AM
