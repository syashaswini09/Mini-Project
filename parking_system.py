def allocate_slots(vehicles, slots):
    print("Parking Allocation Results\n")

    for i in range(min(len(vehicles), len(slots))):
        print(f"{vehicles[i]} -> {slots[i]}")

    if len(vehicles) > len(slots):
        print("\nNo parking slots available for remaining vehicles.")