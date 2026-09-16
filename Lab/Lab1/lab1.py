print("TUPLE..........")
# Creation
vehicle_types = ("Sedan", "SUV", "Hatchback", "Truck")
print("Original Tuple: ", vehicle_types)

# Access
print("Accessed 2nd element: ", vehicle_types[1])

# Update/Add/Delete: Tuples are immutable. To modify, we must convert to a list.
temp_list = list(vehicle_types)
temp_list.append("Coupe")      # Add
temp_list[0] = "Luxury Sedan"  # Update
temp_list.remove("Truck")      # Delete
vehicle_types = tuple(temp_list)
print("Modified Tuple (via list conversion): ", vehicle_types)
print()

print("LIST..........")
# Creation
inventory = ["Toyota Camry", "Honda CR-V", "Ford F-150"]
print("Original List: ", inventory)

# Add
inventory.append("Tesla Model 3")
# Update
inventory[1] = "Honda Pilot"
# Delete
inventory.remove("Ford F-150") # or inventory.pop()
# Access
print("Accessed 1st element: ", inventory[0])
print("Final List: ", inventory)
print()

print("SET..........")
# Creation
features = {"Bluetooth", "Backup Camera", "Lane Assist"}
print("Original Set: ", features)

# Add
features.add("Sunroof")
# Update
features.remove("Lane Assist") # Delete
features.add("Adaptive Cruise") # Add
# Access: Check for membership
has_bluetooth = "Bluetooth" in features
print("Contains Bluetooth? ", has_bluetooth)
print("Final Set: ", features)
print()

print("DICTIONARY..........")
# Creation
car_specs = {"make": "Toyota", "model": "Camry", "kmpl": 15.2}
print("Original Dictionary: ", car_specs)

# Add
car_specs["year"] = 2023
# Update
car_specs["kmpl"] = 16.0
# Access
print("Accessed Make: ", car_specs['make'])
# Delete
del car_specs["year"] 
print("Final Dictionary: ", car_specs)
print()

print("Menu Driven Data Management System..........")

def add_vehicle(db):
    vin = input("Enter 6-digit VIN(Eg: VINXXX): ")
    
    # Data Validation
    if len(vin) != 6 or not vin.isalnum():
        print("Error: VIN must be exactly 6 alphanumeric characters.")
        return
        
    make = input("Enter Make: ")
    model = input("Enter Model: ")
    body = input("Enter Body Style: ")
    
    # Data Validation
    try:
        kmpl = float(input("Enter KMPL (Kilometers per Liter): "))
        if kmpl <= 0:
            raise ValueError
    except ValueError:
        print("Error: KMPL must be a positive number.")
        return
        
    features_input = input("Enter features separated by commas: ")
    
    # Set Comprehension
    features_set = {feat.strip() for feat in features_input.split(",")}
    
    # Dictionary Operations
    db[vin] = {"make": make, "model": model, "kmpl": kmpl, "features": features_set, "body_style": body}
    print("Vehicle", vin, "added successfully!")

def list_all_vehicles(db):
    if not db:
        print("Fleet is empty.")
        return
        
    print("\nComplete Fleet Directory..........")
    for vin, details in db.items():
        print("VIN:", vin)
        print("  Make:", details['make'])
        print("  Model:", details['model'])
        print("  Body Style:", details['body_style'])
        print("  KMPL:", details['kmpl'])
        print("  Features:", details['features'])
        print("-" * 30)

def search_vehicle(db):
    search_vin = input("Enter VIN to search: ")
    # Searching
    if search_vin in db:
        print("Found: ", db[search_vin])
    else:
        print("Vehicle not found.")

def sort_fleet(db):
    # Sorting
    sorted_fleet = sorted(db.items(), key=lambda item: item[1]['kmpl'], reverse=True)
    print("\nFleet sorted by KMPL (Highest to Lowest):")
    for vin, details in sorted_fleet:
        print(vin, ":", details['make'], details['model'], "-", details['kmpl'], "KMPL")

def compare_features(db):
    vin1 = input("Enter first VIN: ")
    vin2 = input("Enter second VIN: ")
    
    if vin1 in db and vin2 in db:
        features1 = db[vin1]['features']
        features2 = db[vin2]['features']
        
        # Set Operations
        print("\nFeatures in both cars (Intersection):", features1.intersection(features2))
        print("Features unique to", vin1, "(Difference):", features1.difference(features2))
        print("All features combined (Union):", features1.union(features2))
    else:
        print("One or both VINs not found.")

def view_analytics(db):
    if not db:
        print("Fleet is empty.")
        return
        
    # List Comprehension
    kmpl_list = [car["kmpl"] for car in db.values()]
    
    # Aggregation
    avg_kmpl = sum(kmpl_list) / len(kmpl_list)
    
    # Dictionary Comprehension
    vin_to_car = {vin: details['make'] + " " + details['model'] for vin, details in db.items()}
    
    # Set Comprehension 
    all_unique_features = {feature for car in db.values() for feature in car["features"]}    
    print("\nFleet Analytics..........")
    print("Total Vehicles:", len(db))
    print("Average Fleet KMPL:", round(avg_kmpl, 2))
    print("Highest KMPL:", max(kmpl_list))
    print("All Unique Features in Fleet:", all_unique_features)
    print("Quick Lookup Directory:", vin_to_car)

def run_fleet_system(db):
    while True:
        print("\nFleet Data Management System..........")
        print("1. Add a New Vehicle")
        print("2. List All Vehicles")
        print("3. Search Vehicle by VIN (Searching)")
        print("4. Sort Fleet by Fuel Efficiency (Sorting)")
        print("5. Compare Vehicle Features (Set Operations)")
        print("6. View Fleet Analytics (Aggregations & Comprehensions)")
        print("7. Exit")
        
        choice = input("Select an option (1-7): ")

        if choice == '1':
            add_vehicle(db)
        elif choice == '2':
            list_all_vehicles(db)
        elif choice == '3':
            search_vehicle(db)
        elif choice == '4':
            sort_fleet(db)
        elif choice == '5':
            compare_features(db)
        elif choice == '6':
            view_analytics(db)
        elif choice == '7':
            print("Exiting..........")
            break
        else:
            print("Invalid selection. Please try again.")


starting_fleet_db = {
    "VIN001": {
        "make": car_specs["make"], 
        "model": car_specs["model"], 
        "kmpl": car_specs["kmpl"], 
        "features": features, 
        "body_style": vehicle_types[0]
    },
    "VIN002": {
        "make": "Hyundai", 
        "model": "i20", 
        "kmpl": 10.56, 
        "features": {"Bluetooth", "Backup Camera"},
        "body_style": vehicle_types[2]
    }
}

# Run the menu system
run_fleet_system(starting_fleet_db)