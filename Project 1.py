import time
import random
CO_LIMIT = 100
CO2_LIMIT = 1200
def read_emission_sensors():
    co = random.randint(60, 150)     
    co2 = random.randint(800, 1600)  
    return co, co2
def control_engine():
    print(">> Engine parameters optimized (Air–Fuel ratio adjusted)")
print("Carbon Emission Monitoring & Control System")
print("-------------------------------------------")

while True:
    co, co2 = read_emission_sensors()

    print(f"\nCO Level  : {co} ppm")
    print(f"CO2 Level : {co2} ppm")

    if co > CO_LIMIT or co2 > CO2_LIMIT:
        print("⚠ ALERT: High Emission Detected!")
        control_engine()
    else:
        print("✅ Emission Levels Normal")

    time.sleep(3)
