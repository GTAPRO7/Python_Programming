import re

class InvalidPipelineRecord(Exception):
    pass

class VehicleDataPipeline:
    def __init__(self):
        self.valid_records = []
        
        self.patterns = {
            "vin": r"^[A-Z0-9]{6}$",
            "date": r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$",
            "time": r"^([01]\d|2[0-3]):([0-5]\d)$",
            "email": r"^[\w\.-]+@[\w\.-]+\.\w{2,}$",
            "phone": r"^[6-9]\d{9}$",
            "pincode": r"^\d{6}$",
            "engine": r"^[A-Z]{3}-\d{4}$",
            "url": r"^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$",
            "distance": r"^\d+$",
            "fuel": r"^\d+\.\d+$"
        }

    def process_record(self, raw_data):
        try:
            if raw_data is None:
                raw_data.split(',')
                
            assert str(raw_data).strip() != "", "Record cannot be completely empty."

            if isinstance(raw_data, list):
                raise TypeError("Pipeline expects a comma-separated string, not a list.")

            if "TRIGGER_NAME_ERROR" in raw_data:
                print(undeclared_variable)

            fields = [f.strip() for f in raw_data.split(',')]

            field_mapping = {
                "vin": fields[0],
                "date": fields[1],
                "time": fields[2],
                "email": fields[3],
                "phone": fields[4],
                "pincode": fields[5],
                "engine": fields[6],
                "url": fields[7],
                "distance": fields[8],
                "fuel": fields[9]
            }

            if "TRIGGER_KEY_ERROR" in raw_data:
                bad_lookup = self.patterns["invalid_regex_key"]

            for key, value in field_mapping.items():
                if not re.match(self.patterns[key], value):
                    raise InvalidPipelineRecord("Validation failed for '{}'. Value '{}' does not match required format.".format(key, value))

            distance = int(field_mapping["distance"])
            fuel_used = float(field_mapping["fuel"])

            kmpl = distance / fuel_used

            if "TRIGGER_GENERIC_ERROR" in raw_data:
                raise Exception("A generic system fault occurred during processing.")

            field_mapping["calculated_kmpl"] = round(kmpl, 2)
            self.valid_records.append(field_mapping)
            print("[SUCCESS] Record for VIN {} processed safely.".format(field_mapping["vin"]))

        except InvalidPipelineRecord as e:
            print("[ERROR - Custom] Domain Validation: {}".format(e))
        except AttributeError:
            print("[ERROR - AttributeError] Invalid data type passed (NoneType). Cannot process.")
        except AssertionError as e:
            print("[ERROR - AssertionError] Data missing: {}".format(e))
        except TypeError as e:
            print("[ERROR - TypeError] Incorrect data structure: {}".format(e))
        except NameError:
            print("[ERROR - NameError] Code referenced an undefined variable.")
        except IndexError:
            print("[ERROR - IndexError] Record is missing required columns. Expected 10 fields.")
        except KeyError:
            print("[ERROR - KeyError] Attempted to use an unregistered Regex pattern key.")
        except ValueError:
            print("[ERROR - ValueError] Numeric conversion failed (likely text in a number field).")
        except ZeroDivisionError:
            print("[ERROR - ZeroDivisionError] Cannot calculate efficiency: Fuel used is 0.0 liters.")
        except Exception as e:
            print("[ERROR - Generic Exception] An unexpected error occurred: {}".format(e))


def main():
    pipeline = VehicleDataPipeline()
    
    print("=" * 60)
    print("AUTOMOTIVE DATA PIPELINE - REGEX & EXCEPTION TESTING")
    print("=" * 60)
    
    while True:
        print("\nEnter a comma-separated record (10 fields).")
        print("Triggers: NONE, LIST, TRIGGER_NAME_ERROR, TRIGGER_KEY_ERROR, TRIGGER_GENERIC_ERROR")
        user_input = input("Record (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            break
        elif user_input == "NONE":
            pipeline.process_record(None)
        elif user_input == "LIST":
            pipeline.process_record(["VIN123", "15-08-2026"])
        else:
            pipeline.process_record(user_input)

    print("\n" + "=" * 60)
    print("PIPELINE SUMMARY: Successfully Stored Valid Records")
    print("=" * 60)
    for valid in pipeline.valid_records:
        print("VIN: {} | Extracted KMPL: {} | Manager Email: {}".format(
            valid['vin'], valid['calculated_kmpl'], valid['email']
        ))

if __name__ == "__main__":
    main()