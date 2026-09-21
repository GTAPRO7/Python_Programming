# automotive_module.py

def add_vehicle(db, vin, make, model, kmpl, body_style):
    """1. Adds a new vehicle record to the database."""
    db[vin] = {
        "make": make,
        "model": model,
        "kmpl": kmpl,
        "body_style": body_style
    }
    print("Success: Vehicle {} added to the inventory.".format(vin))

def search_vehicle(db, vin):
    """2. Searches for a specific vehicle by VIN."""
    if vin in db:
        print("Vehicle Found: {} {} ({} KMPL)".format(
            db[vin]["make"], db[vin]["model"], db[vin]["kmpl"]
        ))
        return db[vin]
    else:
        print("Notice: Vehicle {} not found in inventory.".format(vin))
        return None

def display_inventory(db):
    """3. Displays all records in a tabular format."""
    if not db:
        print("The inventory is currently empty.")
        return
        
    print("VIN".ljust(15) + "| Make".ljust(15) + "| Model".ljust(15) + "| KMPL")
    print("-" * 55)
    for vin, details in db.items():
        print("{:<14} | {:<13} | {:<13} | {}".format(
            vin, details["make"], details["model"], details["kmpl"]
        ))

def calculate_average_kmpl(db):
    """4. Calculates the average fuel efficiency across the fleet."""
    if not db:
        return 0.0
    total_kmpl = sum(car["kmpl"] for car in db.values())
    return total_kmpl / len(db)

def evaluate_efficiency_rating(kmpl):
    """5. Business Logic: Evaluates a KMPL score and returns a category."""
    if kmpl >= 20.0:
        return "Excellent (Eco-Friendly)"
    elif kmpl >= 14.0:
        return "Good (Standard Efficiency)"
    else:
        return "Poor (High Fuel Consumption)"

def calculate_trip_cost(kmpl, distance_km, fuel_price_per_liter):
    """6. Calculates the estimated fuel cost for a road trip."""
    if kmpl <= 0:
        return 0.0
    liters_needed = distance_km / kmpl
    total_cost = liters_needed * fuel_price_per_liter
    return total_cost

def find_most_efficient_vehicle(db):
    """7. Finds the vehicle with the highest KMPL in the inventory."""
    if not db:
        print("Inventory is empty.")
        return None
        
    best_vin = ""
    best_kmpl = 0.0
    
    for vin, details in db.items():
        if details["kmpl"] > best_kmpl:
            best_kmpl = details["kmpl"]
            best_vin = vin
            
    print("Most Efficient: {} {} with {} KMPL".format(
        db[best_vin]["make"], db[best_vin]["model"], best_kmpl
    ))
    return db[best_vin]

def filter_by_body_style(db, desired_style):
    """8. Displays all vehicles matching a specific body style (e.g., SUV)."""
    print("\n--- {} VEHICLES ---".format(desired_style.upper()))
    found = False
    
    for vin, details in db.items():
        if details["body_style"].lower() == desired_style.lower():
            print("- {} {} ({} KMPL)".format(
                details["make"], details["model"], details["kmpl"]
            ))
            found = True
            
    if not found:
        print("No vehicles found for this body style.")