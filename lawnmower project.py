import math

def calculate_power_intensity(SPL, Original_distance, absorption_coefficient, is_inside, is_shifted):
    if is_inside:
        if is_shifted:
            reference_distance = float(input("Enter the current distance from the lawnmower: "))
            distance_ratio = reference_distance / Original_distance
            absorption = absorption_coefficient * (Original_distance - reference_distance)
        else:
            distance_ratio = 1  # No change in distance ratio
            absorption = absorption_coefficient * Original_distance
    else:
        distance_ratio = Original_distance
        absorption = 0  # No absorption coefficient outside


    intensity_ratio = distance_ratio * 2
    power_intensity = 10,  ((SPL - absorption) / 10) / intensity_ratio
    return power_intensity

def calculate_sound_level(SPL, Original_distance, absorption_coefficient, is_inside, is_shifted):
    power_intensity = calculate_power_intensity(SPL, Original_distance, absorption_coefficient, is_inside, is_shifted)
    sound_level = 10 * math.log10(float(power_intensity))
    return sound_level

print("\n----- Material -----")
print("1. Brick")
print("2. Plastic")
print("3. Glass")

option = input("Select the material (1-3): ")

if option == "1":
    material = "Brick"
    absorption_coefficient = 0.1
elif option == "2":
    material = "Plastic"
    absorption_coefficient = 0.2
elif option == "3":
    material = "Glass"
    absorption_coefficient = 0.05
else:
    print("Invalid choice. Exiting the program.")
    exit()

SPL = float(input("What is the reference sound pressure level in dB? "))
Original_distance = float(input("Enter the original distance from the lawnmower: "))
is_inside = input("Is the person inside? (Type 'yes' or 'no'): ").lower() == 'yes'
is_shifted = input("Has the lawnmower shifted from the original spot? (Type 'yes' or 'no'): ").lower() == 'yes'

sound_level = calculate_sound_level(SPL, Original_distance, absorption_coefficient, is_inside, is_shifted)

print("Material:", material)
print("Sound pressure level is", sound_level, "dB")





