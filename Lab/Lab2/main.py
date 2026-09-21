# main.py

# Importing our custom modules
import utility_module as utils
import automotive_module as auto

def run_application():
    # Pre-loading some data so you don't have to type it every time you test
    fleet_db = {
        "VIN001": {"make": "Toyota", "model": "Camry", "kmpl": 15.2, "body_style": "Sedan"},
        "VIN002": {"make": "Hyundai", "model": "i20", "kmpl": 10.5, "body_style": "Hatchback"},
        "VIN003": {"make": "Tata", "model": "Nexon", "kmpl": 17.5, "body_style": "Hatchback"}
    }
    
    utils.print_header("AUTOMOTIVE DATA MANAGEMENT SYSTEM")
    
    while True:
        print("\n1. Add New Vehicle")
        print("2. Search Vehicle")
        print("3. Display Full Inventory")
        print("4. View Fleet Averages & Ratings")
        print("5. Find Most Efficient Vehicle")
        print("6. Filter by Body Style")
        print("7. Calculate Trip Cost")
        print("8. Exit")
        
        choice = input("Select an option (1-8): ")
        
        if choice == '1':
            utils.print_header("ADD VEHICLE", 30)
            vin = utils.get_unique_alphanumeric("Enter 6-digit VIN(Eg VINXXX): ", 6, fleet_db.keys())
            make = utils.get_valid_string("Enter Make: ")
            model = utils.get_valid_string("Enter Model: ")
            body = utils.get_valid_string("Enter Body Style: ")
            kmpl = utils.get_valid_float("Enter KMPL: ", 0.0)
            
            auto.add_vehicle(fleet_db, vin, make, model, kmpl, body)
            
        elif choice == '2':
            utils.print_header("SEARCH VEHICLE", 30)
            vin = utils.get_alphanumeric_string("Enter 6-digit VIN to search(Eg VINXXX): ", 6)
            auto.search_vehicle(fleet_db, vin)
            
        elif choice == '3':
            utils.print_header("FLEET INVENTORY", 55)
            auto.display_inventory(fleet_db)
            
        elif choice == '4':
            utils.print_header("FLEET ANALYTICS", 40)
            avg = auto.calculate_average_kmpl(fleet_db)
            print("Average Fleet KMPL: {:.2f}".format(avg))
            
            rating = auto.evaluate_efficiency_rating(avg)
            print("Overall Fleet Rating: {}".format(rating))
            
        elif choice == '5':
            utils.print_header("TOP PERFORMER", 40)
            auto.find_most_efficient_vehicle(fleet_db)
            
        elif choice == '6':
            utils.print_header("FILTER INVENTORY", 40)
            style = utils.get_valid_string("Enter Body Style (e.g., SUV, Sedan): ")
            auto.filter_by_body_style(fleet_db, style)
            
        elif choice == '7':
            utils.print_header("TRIP CALCULATOR", 40)
            vin = utils.get_alphanumeric_string("Enter the 6-digit VIN for the trip: ", 6)
            
            if vin in fleet_db:
                distance = utils.get_valid_float("Enter trip distance in Kilometers: ", 0.0)
                price = utils.get_valid_float("Enter fuel price per liter (e.g. 100.5): ", 0.0)
                
                car_kmpl = fleet_db[vin]["kmpl"]
                cost = auto.calculate_trip_cost(car_kmpl, distance, price)
                
                print("\nEstimated Fuel Cost: ₹{:.2f}".format(cost))
            else:
                print("Error: Vehicle not found in the database.")
            
        elif choice == '8':
            print("Exiting system...........")
            break
            
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    run_application()