def vacuum_cleaner(location, status):
    print(f"\nInitial State: Location = {location}, Status = {status}")

    if status[location] == 'Dirty':
        print(f"Cleaning location {location}...")
        status[location] = 'Clean'
    else:
        print(f"Location {location} is already clean.")

    if location == 'A':
        print("Moving to location B...")
        location = 'B'
    else:
        print("Moving to location A...")
        location = 'A'

    if status[location] == 'Dirty':
        print(f"Cleaning location {location}...")
        status[location] = 'Clean'
    else:
        print(f"Location {location} is already clean.")

    print(f"Final State: Location = {location}, Status = {status}")



status = {'A': 'Dirty', 'B': 'Dirty'}
vacuum_cleaner('A', status)