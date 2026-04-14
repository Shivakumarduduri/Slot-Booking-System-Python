in = int(input("Enter number of users: "))

users = []


today_slots = {'10 AM': 0, '12 PM': 0, '1 PM': 0}
tomorrow_slots = {'10 AM': 0, '12 PM': 0, '1 PM': 0}

capacity = 2  

for i in range(n):
    print(f"\nEnter details of user {i+1}")
    
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    
    while True:
        day = input("Select day (today/tomorrow): ").lower()
        
        if day == "today":
            current_slots = today_slots
        elif day == "tomorrow":
            current_slots = tomorrow_slots
        else:
            print("Invalid day. Try again.")
            continue

        print("\nAvailable slots:")
        for s in current_slots:
            print(f"{s} -> {current_slots[s]}/{capacity}")
        
        slot = input("Select a slot: ")

        if slot not in current_slots:
            print("invalid slot. Try again.")
        
        elif current_slots[slot] >= capacity:
            print("slot full.")
            
            if day == "today":
                if tomorrow_slots[slot] < capacity:
                    choice = input("Do you want same slot tomorrow? (yes/no): ")
                    
                    if choice.lower() == "yes":
                        tomorrow_slots[slot] += 1
                        print("✅ Booked for tomorrow")
                        users.append({
                            "name": name,
                            "age": age,
                            "day": "tomorrow",
                            "slot": slot
                        })
                        break
                print("Please select another slot.")
        
        else:
            current_slots[slot] += 1
            print("✅ Booking Confirmed")
            users.append({
                "name": name,
                "age": age,
                "day": day,
                "slot": slot
            })
            break

print("\n📋 All Appointments:")
for u in users:
    print(f"Name: {u['name']}, Age: {u['age']}, Day: {u['day']}, Slot: {u['slot']}")
