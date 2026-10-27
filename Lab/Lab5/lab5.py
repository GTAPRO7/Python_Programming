import numpy as np

def main():
    # ==========================================
    # TASK 1: Array Creation and Dataset Preparation
    # ==========================================
    # Using np.array() as shown in the cheatsheet Section 1[cite: 1]
    patients = np.array([
        [101, 45, 37.2,  82, 97, 125,  82, 20,  4],
        [102, 62, 38.1,  96, 94, 145,  90, 30,  7],
        [103, 35, 36.8,  72, 99, 118,  76, 10,  3],
        [104, 71, 39.0, 105, 91, 160,  95, 40, 12],
        [105, 54, 37.5,  88, 96, 135,  85, 25,  6],
        [106, 29, 36.6,  68, 98, 110,  72, 10,  2],
        [107, 66, 38.5, 101, 93, 150,  92, 35,  9],
        [108, 48, 37.0,  78, 97, 128,  80,  5,  5],
        [109, 76, 39.2, 110, 89, 170, 100, 50, 15],
        [110, 41, 36.9,  75, 98, 120,  78, 15,  4]
    ], dtype=np.float64) 

    while True:
        print("\n" + "=" * 60)
        print("HOSPITAL PATIENT MONITORING ANALYTICS SYSTEM")
        print("=" * 60)
        print("1. Display Dataset & Array Attributes")
        print("2. Indexing, Slicing & Data Extraction")
        print("3. Patient Risk Identification")
        print("4. Element-wise Medical Calculations")
        print("5. Reshaping & Array Manipulation")
        print("6. Statistical Patient Analysis")
        print("7. Identify Extreme/High-Risk Patients")
        print("8. Sort & Rank Patients")
        print("9. Generate Integrated Dashboard")
        print("10. Exit")
        
        choice = input("Select an option (1-10): ")
        
        if choice == '1':
            # TASK 2: Array Attributes
            print("\n--- Array Attributes ---")
            print("Shape (rows, cols): {}".format(patients.shape))
            print("Number of Dimensions: {}".format(patients.ndim))
            print("Total Elements: {}".format(patients.size))
            print("Data Type: {}".format(patients.dtype))
            print("Bytes per Element: {}".format(patients.itemsize))
            print("Total Memory Occupied: {} bytes".format(patients.nbytes))
            
        elif choice == '2':
            # TASK 3: Indexing and Slicing
            print("\n--- Indexing and Slicing ---")
            patient_ids = patients[:, 0]
            vital_signs = patients[:, 2:7] # Temp, HR, SpO2, SysBP, DiaBP
            first_five_patients = patients[:5, :]
            
            print("Extracted Patient IDs: {}".format(patient_ids))
            print("Vital Signs (First Patient): {}".format(vital_signs[0]))
            print("First 5 Patients Data:\n{}".format(first_five_patients))
            
        elif choice == '3':
            # TASK 4: Patient Risk Identification
            print("\n--- Risk Identification ---")
            high_temp = patients[:, 2] > 38.0
            low_spo2 = patients[:, 4] < 95.0
            high_hr = patients[:, 3] > 100.0
            high_sys_bp = patients[:, 5] > 140.0
            
            at_risk_mask = high_temp | low_spo2 | high_hr | high_sys_bp
            at_risk_patients = patients[at_risk_mask]
            
            print("Patient IDs requiring medical attention: {}".format(at_risk_patients[:, 0].astype(int)))
            
        elif choice == '4':
            # TASK 5: Element-wise Calculations
            print("\n--- Element-wise Operations ---")
            pulse_pressure = patients[:, 5] - patients[:, 6]
            medication_squared = patients[:, 7] ** 2
            temp_sqrt = np.sqrt(patients[:, 2])
            log_medication = np.log(patients[:, 7]) 
            
            print("Calculated Pulse Pressures: {}".format(pulse_pressure))
            print("Logarithmic Medication Dosages: {}".format(np.round(log_medication, 2)))
            print("Square Root of Temperatures: {}".format(np.round(temp_sqrt, 2)))
            
        elif choice == '5':
            # TASK 6: Reshaping and Manipulation
            print("\n--- Reshaping and Manipulation ---")
            ward_split = patients.reshape(2, 5, 9)
            transposed_data = patients.T
            group_a, group_b = np.split(patients, 2)
            
            print("Reshaped array shape (2 wards): {}".format(ward_split.shape))
            print("Transposed array shape (Features x Patients): {}".format(transposed_data.shape))
            print("Group A shape after split: {}".format(group_a.shape))
            
        elif choice == '6':
            # TASK 7: Statistical Analysis
            print("\n--- Statistical Analysis ---")
            mean_temp = np.mean(patients[:, 2])
            std_hr = np.std(patients[:, 3])
            var_sys_bp = np.var(patients[:, 5])
            median_spo2 = np.median(patients[:, 4])
            
            cum_med_dose = np.cumsum(patients[:, 7])
            cum_hosp_stay = np.cumsum(patients[:, 8])
            
            print("Mean Temperature: {:.2f} °C".format(mean_temp))
            print("Standard Deviation of Heart Rate: {:.2f} bpm".format(std_hr))
            print("Median SpO2: {}%".format(median_spo2))
            print("Cumulative Hospital Days progression: {}".format(cum_hosp_stay))
            
        elif choice == '7':
            # TASK 8: High-Risk and Best-Condition Patients
            print("\n--- Min/Max Indexing ---")
            lowest_spo2_id = patients[np.argmin(patients[:, 4]), 0]
            highest_temp_id = patients[np.argmax(patients[:, 2]), 0]
            highest_hr_id = patients[np.argmax(patients[:, 3]), 0]
            longest_stay_id = patients[np.argmax(patients[:, 8]), 0]
            
            print("Patient with Lowest SpO2: ID {}".format(int(lowest_spo2_id)))
            print("Patient with Highest Temp: ID {}".format(int(highest_temp_id)))
            print("Patient with Highest Heart Rate: ID {}".format(int(highest_hr_id)))
            print("Patient with Longest Stay: ID {}".format(int(longest_stay_id)))
            
        elif choice == '8':
            # TASK 9: Sorting and Searching
            print("\n--- Sorting and Ranking ---")
            stay_indices = np.argsort(patients[:, 8])[::-1]
            sorted_by_stay = patients[stay_indices]
            
            print("Patient IDs ranked by longest hospital stay: {}".format(
                sorted_by_stay[:, 0].astype(int)
            ))
            
        elif choice == '9':
            # TASK 10: Integrated Dashboard
            print("\n" + "=" * 60)
            print("INTEGRATED HOSPITAL DASHBOARD REPORT")
            print("=" * 60)
            at_risk_mask = (patients[:, 2] > 38.0) | (patients[:, 4] < 95.0) | (patients[:, 3] > 100.0) | (patients[:, 5] > 140.0)
            
            print("Total Patients Admitted: {}".format(patients.shape[0]))
            print("Patients Requiring Immediate Attention: {}".format(np.sum(at_risk_mask)))
            print("--- Fleet Averages ---")
            print("Average Age: {:.1f} years".format(np.mean(patients[:, 1])))
            print("Average SpO2: {:.1f} %".format(np.mean(patients[:, 4])))
            print("Average Heart Rate: {:.1f} bpm".format(np.mean(patients[:, 3])))
            print("--- Resource Utilization ---")
            print("Total Medication Dispensed: {} mg".format(np.sum(patients[:, 7])))
            print("Total Hospital Bed-Days: {} days".format(np.sum(patients[:, 8])))
            print("=" * 60)
            
        elif choice == '10':
            print("\nExiting the Hospital Analytics System. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main()