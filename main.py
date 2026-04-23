users = []

today_slots = {'10 AM': 0, '12 PM': 0, '1 PM': 0}
tomorrow_slots = {'10 AM': 0, '12 PM': 0, '1 PM': 0}

capacity = 2  

i = 1

while True:
    print(f"\nEnter details of user {i}")
    
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
            print("Invalid slot. Try again.")
        
        elif current_slots[slot] >= capacity:
            print("Slot full.")
            
            if day == "today":
                if tomorrow_slots[slot] < capacity:
                    choice = input("Do you want same slot tomorrow? (yes/no): ")
                    
                    if choice.lower() == "yes":
                        tomorrow_slots[slot] += 1
                        print("Booked for tomorrow")
                        users.append({
                            "name": name,
                            "age": age,
                            "day": "tomorrow",
                            "slot": slot
                        })
                        break
                print("Select another slot.")
        
        else:
            current_slots[slot] += 1
            print("Booking confirmed")
            users.append({
                "name": name,
                "age": age,
                "day": day,
                "slot": slot
            })
            break

    # 🔥 Ask to continue
    cont = input("\nDo you want to continue booking? (yes/no): ").lower()
    
    if cont != "yes":
        break

    i += 1


print("\nAll Appointments:")
for u in users:
    print(u["name"], u["age"], u["day"], u["slot"])

total_today = sum(today_slots.values())
total_tomorrow = sum(tomorrow_slots.values())

print("\nTotal bookings today:", total_today)
print("Total bookings tomorrow:", total_tomorrow)

max_slot = ""
max_value = 0

for s in today_slots:
    if today_slots[s] > max_value:
        max_value = today_slots[s]
        max_slot = s

print("Most booked slot today:", max_slot)

print("\nRemaining slots today:")
for s in today_slots:
    print(s, "->", capacity - today_slots[s])
