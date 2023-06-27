# Extended Volumetric Analysis Tool

def convert_units():
    # Get input from user
    value = float(input("Value: "))

    # Define conversion units and factors
    conversion_units = [
        "ppm",
        "ppb",
        "ug/L",
        "mg/L",
        "g/L",
        "%w/v"
    ]
    conversion_factors = {
        "ppm_to_ppb": 1e3,
        "ppb_to_ppm": 1e-3,
        "ug/L_to_mg/L": 1e-3,
        "mg/L_to_ug/L": 1e3,
        "g/L_to_mg/L": 1e3,
        "mg/L_to_g/L": 1e-3,
        "g/L_to_ug/L": 1e6,
        "ug/L_to_g/L": 1e-6,
        "%w/v_to_g/L": 10,
        "g/L_to_%w/v": 0.1
    }

    # Display options and get user selection
    for i in range(len(conversion_units)):
        print(str(i + 1) + ". " + conversion_units[i])
    from_unit = conversion_units[int(input("From (#): ")) - 1]
    to_unit = conversion_units[int(input("To (#): ")) - 1]

    # Determine conversion factor
    conversion_key = from_unit + "_to_" + to_unit
    if conversion_key in conversion_factors:
        # Calculate and print result
        result = value * conversion_factors[conversion_key]
        print(str(value) + ' ' + from_unit + ' = ' + str(result) + ' ' + to_unit)
    else:
        print("Invalid conversion")
    
    input("Press Enter to continue...")

def calculate_molarity():
    # Molarity = moles of solute / liters of solution
    moles = float(input("Moles: "))
    liters = float(input("Liters: "))
    molarity = moles / liters
    print("Molarity: " + str(molarity) + " mol/L")
    
    input("Press Enter to continue...")

def calculate_dilution():
    # M1V1 = M2V2
    m1 = float(input("M1: "))
    v1 = float(input("V1: "))
    v2 = float(input("V2: "))
    m2 = (m1 * v1) / v2
    print("M2: " + str(m2) + " mol/L")
    
    input("Press Enter to continue...")

def calculate_weight_volume_percent():
    # %w/v = (mass of solute / volume of solution) * 100
    mass = float(input("Mass (g): "))
    volume = float(input("Vol (L): "))
    wv_percent = (mass / volume) * 100
    print("W/V%: " + str(wv_percent) + " %w/v")
    
    input("Press Enter to continue...")

def main():
    # Run the program
    while True:
        print("\n1. Conv Units")
        print("2. Calc Molarity")
        print("3. Calc Dilution")
        print("4. Calc W/V%")
        print("5. Quit")
        
        option = int(input("Option: "))
        
        if option == 1:
            convert_units()
        elif option == 2:
            calculate_molarity()
        elif option == 3:
            calculate_dilution()
        elif option == 4:
            calculate_weight_volume_percent()
        elif option == 5:
            break
        else:
            print("Invalid option")

main()
