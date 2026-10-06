from abc import ABC, abstractmethod

class Engine:
    def __init__(self, horsepower, type_name):
        self.horsepower = horsepower
        self.type_name = type_name

    def __str__(self):
        return "{} ({} HP)".format(self.type_name, self.horsepower)


class Vehicle(ABC):
    total_vehicles = 0

    def __init__(self, vin, make, model, base_price, horsepower, engine_type):
        self.__vin = vin
        self.make = make
        self.model = model
        self.__base_price = base_price
        
        self.engine = Engine(horsepower, engine_type)
        
        Vehicle.total_vehicles += 1

    def get_vin(self):
        return self.__vin

    def get_base_price(self):
        return self.__base_price

    def set_base_price(self, new_price):
        if new_price > 0:
            self.__base_price = new_price
        else:
            print("Error: Price must be positive.")

    @staticmethod
    def validate_vin(vin):
        return len(vin) == 6 and vin.isalnum()

    @classmethod
    def get_total_count(cls):
        return cls.total_vehicles

    @abstractmethod
    def calculate_range(self):
        pass

    def update_details(self, price=None, horsepower=None):
        if price is not None:
            self.set_base_price(price)
        if horsepower is not None:
            self.engine.horsepower = horsepower

    def __str__(self):
        return "{} {} [VIN: {}] - Rs {} | Engine: {}".format(
            self.make, self.model, self.__vin, self.__base_price, self.engine
        )

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.__vin == other.get_vin()
        return False


class CombustionVehicle(Vehicle):
    def __init__(self, vin, make, model, base_price, horsepower, kmpl, fuel_capacity):
        super().__init__(vin, make, model, base_price, horsepower, "Internal Combustion")
        self.kmpl = kmpl
        self.fuel_capacity = fuel_capacity

    def calculate_range(self):
        return self.kmpl * self.fuel_capacity

    def __str__(self):
        base_str = super().__str__()
        return "{} | Range: {} km ({} KMPL)".format(base_str, self.calculate_range(), self.kmpl)


class ElectricVehicle(Vehicle):
    def __init__(self, vin, make, model, base_price, horsepower, km_per_kwh, battery_capacity):
        super().__init__(vin, make, model, base_price, horsepower, "Electric Motor")
        self.km_per_kwh = km_per_kwh
        self.battery_capacity = battery_capacity

    def calculate_range(self):
        return self.km_per_kwh * self.battery_capacity

    def __str__(self):
        base_str = super().__str__()
        return "{} | Range: {} km ({} km/kWh)".format(base_str, self.calculate_range(), self.km_per_kwh)


class FleetManager:
    def __init__(self):
        self.fleet = []

    def add_vehicle(self, vehicle):
        if vehicle in self.fleet:
            print("Error: Vehicle with this VIN already exists.")
        else:
            self.fleet.append(vehicle)
            print("Successfully added {} {}.".format(vehicle.make, vehicle.model))

    def display_fleet(self):
        print("\n--- Current Fleet Directory ---")
        if not self.fleet:
            print("Fleet is empty.")
        for vehicle in self.fleet:
            print(vehicle)
        print("Total Vehicles Created: {}".format(Vehicle.get_total_count()))

    def search_vehicle(self, vin):
        for vehicle in self.fleet:
            if vehicle.get_vin() == vin:
                return vehicle
        return None


def main():
    manager = FleetManager()
    
    car1 = CombustionVehicle("VIN111", "Toyota", "Camry", 25000, 200, 15.2, 50)
    car2 = ElectricVehicle("VIN222", "Tesla", "Model 3", 40000, 280, 6.5, 75)
    manager.add_vehicle(car1)
    manager.add_vehicle(car2)

    while True:
        print("\n=== Automotive OOP Management System ===")
        print("1. Add Combustion Vehicle")
        print("2. Add Electric Vehicle")
        print("3. Display Fleet")
        print("4. Search Vehicle")
        print("5. Update Vehicle Price")
        print("6. Exit")
        
        choice = input("Select option (1-6): ")

        if choice in ['1', '2']:
            vin = input("Enter 6-digit VIN (Eg. VINXXX): ").upper()
            
            if not Vehicle.validate_vin(vin):
                print("Error: VIN must be exactly 6 alphanumeric characters.")
                continue
                
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            try:
                price = float(input("Enter Base Price: "))
                hp = int(input("Enter Horsepower: "))
                
                if choice == '1':
                    kmpl = float(input("Enter KMPL: "))
                    cap = float(input("Enter Fuel Capacity (Liters): "))
                    new_car = CombustionVehicle(vin, make, model, price, hp, kmpl, cap)
                else:
                    efficiency = float(input("Enter km per kWh: "))
                    batt = float(input("Enter Battery Capacity (kWh): "))
                    new_car = ElectricVehicle(vin, make, model, price, hp, efficiency, batt)
                    
                manager.add_vehicle(new_car)
                
            except ValueError:
                print("Error: Invalid number format. Operation cancelled.")

        elif choice == '3':
            manager.display_fleet()

        elif choice == '4':
            vin = input("Enter 6-digit VIN to search (Eg. VINXXX): ").upper()
            vehicle = manager.search_vehicle(vin)
            
            if vehicle:
                print("\n--- Vehicle Found ---")
                print(vehicle)
            else:
                print("Notice: Vehicle with VIN {} not found.".format(vin))

        elif choice == '5':
            vin = input("Enter 6-digit VIN to update (Eg. VINXXX): ").upper()
            vehicle = manager.search_vehicle(vin)
            
            if vehicle:
                print("Current Price: {}".format(vehicle.get_base_price()))
                try:
                    new_price = float(input("Enter new price (or 0 to skip): "))
                    new_hp = int(input("Enter new horsepower (or 0 to skip): "))
                    
                    if new_price > 0 and new_hp > 0:
                        vehicle.update_details(price=new_price, horsepower=new_hp)
                    elif new_price > 0:
                        vehicle.update_details(price=new_price)
                    elif new_hp > 0:
                        vehicle.update_details(horsepower=new_hp)
                        
                    print("Vehicle details updated successfully.")
                except ValueError:
                    print("Error: Invalid input.")
            else:
                print("Error: Vehicle not found.")

        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()